---
name: duplicate-skill
description: First skill that deliberately claims the name "duplicate-skill" (collision case A).
---

# Duplicate Skill (A)

This file and `dup-b.md` both declare `name: duplicate-skill`. The importer must
keep the first as `duplicate-skill` and suffix the second (`duplicate-skill-2`),
surfacing a rename warning in the preview.
