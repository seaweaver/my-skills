$ErrorActionPreference = 'Stop'
Set-StrictMode -Version 2.0
if (Get-Variable -Name PSNativeCommandUseErrorActionPreference -ErrorAction SilentlyContinue) {
    $PSNativeCommandUseErrorActionPreference = $false
}

$script:GitHubSyncConfig = @{
    LargeFileThresholdBytes = 20MB
    Repositories = @(
        @{ Name = 'my-skills'; Path = 'D:\Dropbox\Project\my-skills' },
        @{ Name = 'iCloudNote'; Path = 'D:\iCloud\iCloudDrive\iCloud~md~obsidian\iCloudNote' },
        @{ Name = 'cf_quant'; Path = 'D:\Dropbox\Project\cf_quant' },
        @{ Name = 'cf_quant_web'; Path = 'D:\Dropbox\Project\cf_quant_web' },
        @{ Name = 'cf_quant_weixin'; Path = 'D:\Dropbox\Project\cf_quant_weixin' },
        @{ Name = 'data_project'; Path = 'D:\Dropbox\Project\data_project' }
    )
    BinaryExtensions = @(
        '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.pdf', '.zip', '.7z', '.rar',
        '.exe', '.dll', '.so', '.dylib', '.bin', '.db', '.sqlite', '.doc', '.docx',
        '.ppt', '.pptx', '.xls', '.xlsx', '.xlsm', '.mp3', '.wav', '.mp4', '.mov',
        '.avi', '.ttf', '.otf', '.woff', '.woff2'
    )
    DocsExtensions = @('.md', '.markdown', '.txt', '.rst')
    ScriptExtensions = @('.ps1', '.psm1', '.sh', '.bat', '.cmd')
    ConfigExtensions = @('.json', '.yaml', '.yml', '.toml', '.ini', '.cfg', '.conf', '.env')
    CodeExtensions = @('.py', '.js', '.ts', '.tsx', '.jsx', '.go', '.rs', '.java', '.cs', '.cpp', '.c', '.h', '.hpp', '.vue', '.sql')
}

function Get-ConfiguredRepositories {
    $repositories = @()
    foreach ($repo in $script:GitHubSyncConfig.Repositories) {
        $repositories += [pscustomobject]@{
            Name = $repo.Name
            Path = $repo.Path
        }
    }

    return $repositories
}

function Invoke-GitCommand {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RepoPath,
        [Parameter(Mandatory = $true)]
        [string[]]$Arguments,
        [switch]$AllowFailure
    )

    $previousErrorActionPreference = $ErrorActionPreference
    try {
        $ErrorActionPreference = 'Continue'
        $output = & git -C $RepoPath @Arguments 2>&1
    }
    finally {
        $ErrorActionPreference = $previousErrorActionPreference
    }
    $exitCode = $LASTEXITCODE
    $lines = @()
    foreach ($item in $output) {
        $lines += $item.ToString()
    }
    $text = ($lines -join [Environment]::NewLine).Trim()

    if (-not $AllowFailure -and $exitCode -ne 0) {
        throw "git $($Arguments -join ' ') failed: $text"
    }

    return [pscustomobject]@{
        ExitCode = $exitCode
        Lines = $lines
        Output = $text
    }
}

function Get-CurrentBranch {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RepoPath
    )

    $result = Invoke-GitCommand -RepoPath $RepoPath -Arguments @('rev-parse', '--abbrev-ref', 'HEAD')
    return $result.Output.Trim()
}

function Get-GitDirPath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RepoPath
    )

    $result = Invoke-GitCommand -RepoPath $RepoPath -Arguments @('rev-parse', '--git-dir')
    $gitDir = $result.Output.Trim()
    if ([System.IO.Path]::IsPathRooted($gitDir)) {
        return $gitDir
    }

    return [System.IO.Path]::GetFullPath((Join-Path $RepoPath $gitDir))
}

function Test-RepositorySafeState {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RepoPath
    )

    $issues = @()
    $branch = Get-CurrentBranch -RepoPath $RepoPath
    if ($branch -eq 'HEAD') {
        $issues += 'detached HEAD'
    }

    $gitDir = Get-GitDirPath -RepoPath $RepoPath
    $checks = @(
        @{ Path = 'MERGE_HEAD'; Label = 'merge in progress' },
        @{ Path = 'CHERRY_PICK_HEAD'; Label = 'cherry-pick in progress' },
        @{ Path = 'REVERT_HEAD'; Label = 'revert in progress' },
        @{ Path = 'rebase-merge'; Label = 'rebase in progress' },
        @{ Path = 'rebase-apply'; Label = 'rebase in progress' }
    )

    foreach ($check in $checks) {
        if (Test-Path -LiteralPath (Join-Path $gitDir $check.Path)) {
            $issues += $check.Label
        }
    }

    return [pscustomobject]@{
        IsSafe = ($issues.Count -eq 0)
        Issues = $issues
    }
}

function Get-StatusLines {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RepoPath
    )

    $result = Invoke-GitCommand -RepoPath $RepoPath -Arguments @('status', '--short', '--untracked-files=all')
    $lines = @()
    foreach ($line in $result.Lines) {
        if (-not [string]::IsNullOrWhiteSpace($line)) {
            $lines += $line
        }
    }

    return @($lines)
}

function Get-PathFromStatusLine {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Line
    )

    if ($Line.Length -lt 4) {
        return $null
    }

    $pathPart = $Line.Substring(3).Trim()
    if ($pathPart -like '* -> *') {
        $pathPart = ($pathPart -split ' -> ')[-1].Trim()
    }

    return $pathPart.Trim('"')
}

function Get-RelativePathsFromStatus {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$StatusLines
    )

    $paths = @()
    foreach ($line in $StatusLines) {
        $path = Get-PathFromStatusLine -Line $line
        if (-not [string]::IsNullOrWhiteSpace($path)) {
            $paths += ($path -replace '/', '\')
        }
    }

    return @($paths | Select-Object -Unique)
}

function Test-LargeFiles {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RepoPath,
        [Parameter(Mandatory = $true)]
        [string[]]$StatusLines
    )

    $largeFiles = @()
    $threshold = [int64]$script:GitHubSyncConfig.LargeFileThresholdBytes
    $paths = Get-RelativePathsFromStatus -StatusLines $StatusLines

    foreach ($relativePath in $paths) {
        $fullPath = Join-Path $RepoPath $relativePath
        if (-not (Test-Path -LiteralPath $fullPath -PathType Leaf)) {
            continue
        }

        $item = Get-Item -LiteralPath $fullPath
        if ([int64]$item.Length -gt $threshold) {
            $largeFiles += [pscustomobject]@{
                Path = $relativePath
                SizeBytes = [int64]$item.Length
                SizeMB = [math]::Round(($item.Length / 1MB), 2)
            }
        }
    }

    return [pscustomobject]@{
        HasLargeFiles = ($largeFiles.Count -gt 0)
        Files = $largeFiles
    }
}

function Get-NameStatusLines {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RepoPath
    )

    $result = Invoke-GitCommand -RepoPath $RepoPath -Arguments @('diff', '--cached', '--name-status')
    return @($result.Lines)
}

function Get-DiffStatLines {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RepoPath
    )

    $result = Invoke-GitCommand -RepoPath $RepoPath -Arguments @('diff', '--cached', '--stat', '--no-ext-diff')
    return @($result.Lines)
}

function Get-LeafName {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RelativePath
    )

    return [System.IO.Path]::GetFileName($RelativePath)
}

function Get-PathCategory {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RelativePath
    )

    $path = ($RelativePath -replace '/', '\').Trim()
    $leaf = Get-LeafName -RelativePath $path
    $extension = [System.IO.Path]::GetExtension($leaf).ToLowerInvariant()
    $segments = @($path -split '\\')
    $lowerSegments = @()
    foreach ($segment in $segments) {
        $lowerSegments += $segment.ToLowerInvariant()
    }

    if (($leaf -in @('README.md', 'AGENTS.md', 'CLAUDE.md', 'SKILL.md')) -or ($extension -in $script:GitHubSyncConfig.DocsExtensions) -or ($lowerSegments -contains 'docs') -or ($lowerSegments -contains 'references')) {
        return 'docs'
    }

    if (($extension -in $script:GitHubSyncConfig.ScriptExtensions) -or ($lowerSegments -contains 'scripts')) {
        return 'scripts'
    }

    if (($leaf -in @('.gitignore', '.gitattributes')) -or ($extension -in $script:GitHubSyncConfig.ConfigExtensions) -or ($lowerSegments -contains 'config') -or ($lowerSegments -contains 'configs') -or ($lowerSegments -contains '.github')) {
        return 'config'
    }

    if ($extension -in $script:GitHubSyncConfig.CodeExtensions) {
        return 'code'
    }

    return 'other'
}

function Test-BinaryPath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RelativePath
    )

    $extension = [System.IO.Path]::GetExtension($RelativePath).ToLowerInvariant()
    return ($extension -in $script:GitHubSyncConfig.BinaryExtensions)
}

function Get-PrimaryScope {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$RelativePaths,
        [Parameter(Mandatory = $true)]
        [string]$PrimaryType
    )

    if ($PrimaryType -eq 'docs') {
        return 'documentation'
    }

    if ($PrimaryType -eq 'scripts') {
        return 'scripts'
    }

    if ($PrimaryType -eq 'config') {
        return 'config'
    }

    $generic = @('docs', 'references', 'scripts', 'tests', 'assets', 'config', 'configs', '.github')
    $counts = @{}
    foreach ($relativePath in $RelativePaths) {
        $segments = @((($relativePath -replace '/', '\') -split '\\'))
        foreach ($segment in $segments) {
            if ([string]::IsNullOrWhiteSpace($segment)) {
                continue
            }

            $candidate = $segment.ToLowerInvariant()
            if ($candidate -in $generic) {
                continue
            }

            if ([System.IO.Path]::GetExtension($candidate)) {
                continue
            }

            if (-not $counts.ContainsKey($candidate)) {
                $counts[$candidate] = 0
            }
            $counts[$candidate] += 1
            break
        }
    }

    if ($counts.Count -eq 0) {
        return 'repository'
    }

    $top = $counts.GetEnumerator() | Sort-Object -Property Value -Descending | Select-Object -First 1
    return $top.Key
}

function Get-ChangeSummary {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$StatusLines,
        [Parameter(Mandatory = $true)]
        [string[]]$NameStatusLines,
        [Parameter(Mandatory = $true)]
        [string[]]$DiffStatLines
    )

    $paths = Get-RelativePathsFromStatus -StatusLines $StatusLines
    $categoryCounts = @{
        docs = 0
        scripts = 0
        config = 0
        code = 0
        other = 0
    }
    $categories = @()
    $hasBinaryFiles = $false

    foreach ($path in $paths) {
        $category = Get-PathCategory -RelativePath $path
        $categoryCounts[$category] += 1
        if ($category -notin $categories) {
            $categories += $category
        }
        if (Test-BinaryPath -RelativePath $path) {
            $hasBinaryFiles = $true
        }
    }

    $orderedCategories = $categoryCounts.GetEnumerator() | Sort-Object -Property Value -Descending
    $topCategory = ($orderedCategories | Select-Object -First 1).Key
    $topCount = ($orderedCategories | Select-Object -First 1).Value
    $secondCount = ($orderedCategories | Select-Object -Skip 1 -First 1).Value

    $realCategories = @()
    foreach ($category in $categories) {
        if ($category -ne 'other') {
            $realCategories += $category
        }
    }
    if ($realCategories.Count -eq 0 -and $paths.Count -gt 0) {
        $realCategories += 'other'
    }

    $primaryType = $topCategory
    if ($realCategories.Count -gt 1 -and $topCount -le ($secondCount + 1)) {
        $primaryType = 'mixed'
    }
    if ($topCategory -eq 'other') {
        $primaryType = 'mixed'
    }

    $addedCount = 0
    foreach ($line in $NameStatusLines) {
        if ($line -match '^(A|R)') {
            $addedCount += 1
        }
    }
    foreach ($line in $StatusLines) {
        if ($line -like '?? *') {
            $addedCount += 1
        }
    }

    $scope = Get-PrimaryScope -RelativePaths $paths -PrimaryType $primaryType
    $uniqueScopes = @()
    foreach ($path in $paths) {
        $segments = @((($path -replace '/', '\') -split '\\'))
        if ($segments.Count -gt 1) {
            $segment = $segments[0].ToLowerInvariant()
            if ($segment -notin $uniqueScopes) {
                $uniqueScopes += $segment
            }
        }
    }

    return [pscustomobject]@{
        TotalChangedFiles = $paths.Count
        PrimaryType = $primaryType
        PrimaryScope = $scope
        Categories = $realCategories
        AddedCount = $addedCount
        HasBinaryFiles = $hasBinaryFiles
        HasLargeChangeSet = (($paths.Count -gt 25) -or ($uniqueScopes.Count -gt 4))
        DiffStatLineCount = $DiffStatLines.Count
    }
}

function New-CommitMessageFromSummary {
    param(
        [Parameter(Mandatory = $true)]
        $Summary
    )

    if ($Summary.HasBinaryFiles -or $Summary.HasLargeChangeSet -or $Summary.TotalChangedFiles -le 0) {
        return 'chore: sync local changes'
    }

    switch ($Summary.PrimaryType) {
        'docs' {
            if ($Summary.PrimaryScope -and $Summary.PrimaryScope -ne 'documentation') {
                return "docs: update $($Summary.PrimaryScope) documentation"
            }
            return 'docs: update documentation'
        }
        'scripts' {
            if ($Summary.PrimaryScope -and $Summary.PrimaryScope -ne 'scripts' -and $Summary.PrimaryScope -ne 'repository') {
                return "chore: update $($Summary.PrimaryScope) scripts"
            }
            return 'chore: update scripts'
        }
        'config' {
            if ($Summary.PrimaryScope -and $Summary.PrimaryScope -ne 'config' -and $Summary.PrimaryScope -ne 'repository') {
                return "chore: update $($Summary.PrimaryScope) config"
            }
            return 'chore: update config'
        }
        'code' {
            if ($Summary.PrimaryScope -and $Summary.PrimaryScope -ne 'repository') {
                if ($Summary.AddedCount -gt 0) {
                    return "feat: update $($Summary.PrimaryScope) code"
                }
                return "chore: update $($Summary.PrimaryScope) code"
            }
            if ($Summary.AddedCount -gt 0) {
                return 'feat: update code'
            }
            return 'chore: update code'
        }
        'mixed' {
            $types = @()
            foreach ($category in $Summary.Categories) {
                if ($category -in @('docs', 'scripts', 'config', 'code')) {
                    $types += $category
                }
            }
            $types = $types | Select-Object -Unique
            if ($types.Count -ge 2) {
                return "chore: update $($types[0]) and $($types[1])"
            }
            return 'chore: sync local changes'
        }
        default {
            return 'chore: sync local changes'
        }
    }
}

function Get-PushArguments {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RepoPath,
        [Parameter(Mandatory = $true)]
        [string]$Branch
    )

    $upstream = Invoke-GitCommand -RepoPath $RepoPath -Arguments @('rev-parse', '--abbrev-ref', '--symbolic-full-name', '@{u}') -AllowFailure
    if ($upstream.ExitCode -eq 0 -and $upstream.Output -match '^([^/]+)/(.+)$') {
        return @('push', $matches[1], "HEAD:$($matches[2])")
    }

    $origin = Invoke-GitCommand -RepoPath $RepoPath -Arguments @('remote', 'get-url', 'origin') -AllowFailure
    if ($origin.ExitCode -ne 0) {
        throw 'origin remote not found and no upstream configured'
    }

    return @('push', 'origin', $Branch)
}

function Normalize-ErrorText {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Text
    )

    $normalized = ($Text -replace '\s+', ' ').Trim()
    if ($normalized.Length -gt 180) {
        return $normalized.Substring(0, 180).Trim() + '...'
    }

    return $normalized
}

function Invoke-RepositorySync {
    param(
        [Parameter(Mandatory = $true)]
        $Repository
    )

    $result = [ordered]@{
        RepoName = $Repository.Name
        RepoPath = $Repository.Path
        Branch = ''
        Status = 'failed'
        CommitMessage = ''
        CommitHash = ''
        Stage = 'init'
        Error = ''
    }

    try {
        $result.Stage = 'path'
        if (-not (Test-Path -LiteralPath $Repository.Path -PathType Container)) {
            throw "path not found: $($Repository.Path)"
        }

        $result.Stage = 'git'
        $gitCheck = Invoke-GitCommand -RepoPath $Repository.Path -Arguments @('rev-parse', '--is-inside-work-tree') -AllowFailure
        if ($gitCheck.ExitCode -ne 0 -or $gitCheck.Output -ne 'true') {
            throw 'not a git repository'
        }

        $result.Branch = Get-CurrentBranch -RepoPath $Repository.Path

        $result.Stage = 'state'
        $safeState = Test-RepositorySafeState -RepoPath $Repository.Path
        if (-not $safeState.IsSafe) {
            throw ($safeState.Issues -join '; ')
        }

        $result.Stage = 'status'
        $statusLines = @(Get-StatusLines -RepoPath $Repository.Path)
        if ($statusLines.Count -eq 0) {
            $result.Status = 'skipped'
            $result.Error = 'no changes'
            return [pscustomobject]$result
        }

        $result.Stage = 'large-file-check'
        $largeFileCheck = Test-LargeFiles -RepoPath $Repository.Path -StatusLines $statusLines
        if ($largeFileCheck.HasLargeFiles) {
            $descriptions = @()
            foreach ($file in $largeFileCheck.Files) {
                $descriptions += "$($file.Path) ($($file.SizeMB) MB)"
            }
            throw ('large file exceeds 20 MB: ' + ($descriptions -join ', '))
        }

        $result.Stage = 'stage'
        Invoke-GitCommand -RepoPath $Repository.Path -Arguments @('add', '--all') | Out-Null

        $hasStagedChanges = Invoke-GitCommand -RepoPath $Repository.Path -Arguments @('diff', '--cached', '--quiet') -AllowFailure
        if ($hasStagedChanges.ExitCode -eq 0) {
            $result.Status = 'skipped'
            $result.Error = 'nothing to commit'
            return [pscustomobject]$result
        }

        $nameStatusLines = @(Get-NameStatusLines -RepoPath $Repository.Path)
        $diffStatLines = @(Get-DiffStatLines -RepoPath $Repository.Path)
        $summary = Get-ChangeSummary -StatusLines $statusLines -NameStatusLines $nameStatusLines -DiffStatLines $diffStatLines
        $result.CommitMessage = New-CommitMessageFromSummary -Summary $summary

        $result.Stage = 'commit'
        $commitResult = Invoke-GitCommand -RepoPath $Repository.Path -Arguments @('commit', '-m', $result.CommitMessage) -AllowFailure
        if ($commitResult.ExitCode -ne 0) {
            if ($commitResult.Output -match 'nothing to commit') {
                $result.Status = 'skipped'
                $result.Error = 'nothing to commit'
                return [pscustomobject]$result
            }
            throw $commitResult.Output
        }

        $hashResult = Invoke-GitCommand -RepoPath $Repository.Path -Arguments @('rev-parse', '--short', 'HEAD')
        $result.CommitHash = $hashResult.Output.Trim()

        $result.Stage = 'push'
        $pushArguments = Get-PushArguments -RepoPath $Repository.Path -Branch $result.Branch
        $pushResult = Invoke-GitCommand -RepoPath $Repository.Path -Arguments $pushArguments -AllowFailure
        if ($pushResult.ExitCode -ne 0) {
            throw $pushResult.Output
        }

        $result.Status = 'succeeded'
        $result.Stage = 'done'
        return [pscustomobject]$result
    }
    catch {
        $message = $_.Exception.Message
        if ([string]::IsNullOrWhiteSpace($message)) {
            $message = $_.ToString()
        }
        $result.Error = Normalize-ErrorText -Text $message
        return [pscustomobject]$result
    }
}

function Format-SyncReport {
    param(
        [Parameter(Mandatory = $true)]
        [object[]]$Results,
        [int]$DurationSeconds = 0
    )

    $succeeded = @($Results | Where-Object { $_.Status -eq 'succeeded' })
    $skipped = @($Results | Where-Object { $_.Status -eq 'skipped' })
    $failed = @($Results | Where-Object { $_.Status -eq 'failed' })

    $lines = New-Object System.Collections.Generic.List[string]
    [void]$lines.Add('# GitHub Sync Report')
    [void]$lines.Add('')
    [void]$lines.Add('Summary')
    [void]$lines.Add("- total: $($Results.Count)")
    [void]$lines.Add("- succeeded: $($succeeded.Count)")
    [void]$lines.Add("- skipped: $($skipped.Count)")
    [void]$lines.Add("- failed: $($failed.Count)")
    if ($DurationSeconds -gt 0) {
        [void]$lines.Add("- duration_seconds: $DurationSeconds")
    }

    if ($succeeded.Count -gt 0) {
        [void]$lines.Add('')
        [void]$lines.Add('Succeeded')
        foreach ($item in $succeeded) {
            [void]$lines.Add("- $($item.RepoName) | $($item.Branch) | $($item.CommitMessage) | $($item.CommitHash)")
        }
    }

    if ($failed.Count -gt 0) {
        [void]$lines.Add('')
        [void]$lines.Add('Failed')
        foreach ($item in $failed) {
            [void]$lines.Add("- $($item.RepoName) | $($item.Stage) | $($item.Error)")
        }
    }

    if ($skipped.Count -gt 0) {
        [void]$lines.Add('')
        [void]$lines.Add('Skipped')
        [void]$lines.Add("- count: $($skipped.Count)")
    }

    return ($lines -join [Environment]::NewLine)
}

function Invoke-GitHubSync {
    param(
        [switch]$PassThru
    )

    $results = @()
    $start = Get-Date
    $repositories = Get-ConfiguredRepositories

    foreach ($repository in $repositories) {
        $results += Invoke-RepositorySync -Repository $repository
    }

    $duration = [int][math]::Round(((Get-Date) - $start).TotalSeconds, 0)
    $report = Format-SyncReport -Results $results -DurationSeconds $duration

    if ($PassThru) {
        return [pscustomobject]@{
            Results = $results
            Report = $report
        }
    }

    Write-Output $report
}

if (-not (Get-Variable -Name GitHubSyncSkipEntrypoint -Scope Global -ErrorAction SilentlyContinue)) {
    Invoke-GitHubSync
}
