$ErrorActionPreference = 'Stop'

$global:GitHubSyncSkipEntrypoint = $true
$scriptPath = Join-Path $PSScriptRoot '..\scripts\sync_repos.ps1'
. $scriptPath

function Assert-Equal {
    param(
        [Parameter(Mandatory = $true)]
        $Actual,
        [Parameter(Mandatory = $true)]
        $Expected,
        [Parameter(Mandatory = $true)]
        [string]$Message
    )

    if ($Actual -ne $Expected) {
        throw "$Message`nExpected: $Expected`nActual: $Actual"
    }
}

function Assert-Contains {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Actual,
        [Parameter(Mandatory = $true)]
        [string]$ExpectedSubstring,
        [Parameter(Mandatory = $true)]
        [string]$Message
    )

    if ($Actual -notlike "*$ExpectedSubstring*") {
        throw "$Message`nExpected substring: $ExpectedSubstring`nActual: $Actual"
    }
}

$docSummary = [pscustomobject]@{
    TotalChangedFiles = 2
    PrimaryType = 'docs'
    PrimaryScope = 'documentation'
    HasBinaryFiles = $false
    HasLargeChangeSet = $false
}

$docMessage = New-CommitMessageFromSummary -Summary $docSummary
Assert-Equal -Actual $docMessage -Expected 'docs: update documentation' -Message 'Docs-only summary should produce a docs commit message.'

$singlePathList = @(Get-RelativePathsFromStatus -StatusLines @('?? report\sample.sql'))
Assert-Equal -Actual $singlePathList.Count -Expected 1 -Message 'Single status lines should still return an array-like path list.'
Assert-Equal -Actual $singlePathList[0] -Expected 'report\sample.sql' -Message 'Single status lines should preserve the relative path.'

$report = Format-SyncReport -Results @(
    [pscustomobject]@{
        RepoName = 'my-skills'
        Branch = 'main'
        Status = 'succeeded'
        CommitMessage = 'docs: update documentation'
        CommitHash = 'abc1234'
        Stage = ''
        Error = ''
    },
    [pscustomobject]@{
        RepoName = 'cf_quant'
        Branch = 'main'
        Status = 'failed'
        CommitMessage = ''
        CommitHash = ''
        Stage = 'push'
        Error = 'authentication error'
    },
    [pscustomobject]@{
        RepoName = 'iCloudNote'
        Branch = 'main'
        Status = 'skipped'
        CommitMessage = ''
        CommitHash = ''
        Stage = ''
        Error = ''
    }
)

Assert-Contains -Actual $report -ExpectedSubstring 'Summary' -Message 'Report should contain the Summary section.'
Assert-Contains -Actual $report -ExpectedSubstring '- total: 3' -Message 'Report should show the total repo count.'
Assert-Contains -Actual $report -ExpectedSubstring '- succeeded: 1' -Message 'Report should show succeeded count.'
Assert-Contains -Actual $report -ExpectedSubstring '- skipped: 1' -Message 'Report should show skipped count.'
Assert-Contains -Actual $report -ExpectedSubstring '- failed: 1' -Message 'Report should show failed count.'
Assert-Contains -Actual $report -ExpectedSubstring 'my-skills | main | docs: update documentation | abc1234' -Message 'Succeeded rows should be compact.'
Assert-Contains -Actual $report -ExpectedSubstring 'cf_quant | push | authentication error' -Message 'Failed rows should include stage and error.'

Write-Output 'PASS'
