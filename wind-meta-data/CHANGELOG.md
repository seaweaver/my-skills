# Changelog

## 1.1.0 - 2026-03-12

- Added `test-cases.md` with trigger, layer, fallback, and regression scenarios
- Linked testing guidance from `SKILL.md` and `reference.md`
- Bumped `skill_version` to `1.1.0`

Compatibility:

- Knowledge-base content unchanged
- L3 script interface unchanged

## 1.0.0 - 2026-03-12

- Initial packaged release of `wind-meta-data`
- Added project-local skill structure under `.claude/skills/wind-meta-data`
- Packaged 6 Wind metadata knowledge-base files into `data/`
- Added progressive lookup guidance for L1, L2, and L3
- Added `query_l3.py` for field-level lookup against full JSON metadata
- Added `VERSION.json` and `data/MANIFEST.json` for versioning and traceability

Compatibility:

- Queries target metadata lookup only
- No live Wind API or terminal extraction is performed by this skill
