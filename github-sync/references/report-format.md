# GitHub Sync Report Format

Return one concise report with these sections only:

## Summary

- `total`
- `succeeded`
- `skipped`
- `failed`
- `duration_seconds` when available

## Succeeded

List only repositories that produced a new commit:

```text
- repo | branch | message | hash
```

## Failed

List only failed repositories:

```text
- repo | stage | error
```

## Skipped

Keep this section compact:

```text
- count: N
```

## Example

```text
# GitHub Sync Report

Summary
- total: 6
- succeeded: 4
- skipped: 1
- failed: 1
- duration_seconds: 18

Succeeded
- my-skills | main | docs: update documentation | c0dd351
- cf_quant_web | main | chore: sync local changes | a13f920

Failed
- cf_quant | push | authentication error

Skipped
- count: 1
```
