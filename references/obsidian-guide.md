# Obsidian Categorization Guide

Use this guide when the user requests Obsidian output (e.g., "move to obsidian", "save to vault").

## Vault Location

Base path: `/mnt/c/Obsidian/Life_sync`

All files should be saved relative to this location.

## Categories (STRICT)

| Category | Subcategories                                      |
| -------- | -------------------------------------------------- |
| Football | Skills, Drills, Session_Plan, Tactics, Match_Notes |
| Tech     | AI, Web_Dev, Linux, Docker, Microsoft, Tools       |
| Business | Marketing, General, Finance, Legal                 |
| Health   | Workouts, Recipe, Nutrition, Recovery              |
| Journal  | (none - use date)                                  |

## File Path Format

```
/mnt/c/Obsidian/Life_sync/{Category}/Articles/{filename}.md
```

- Lowercase filenames with hyphens
- Example: `/mnt/c/Obsidian/Life_sync/Tech/Articles/react-hooks-tutorial.md`

## Required Frontmatter

```yaml
---
title: Full Title Here
date_created: YYYY-MM-DD
date_modified: YYYY-MM-DD
category: CategoryName
subcategory: SubcategoryName
tags: ["source/video", "status/inbox", "type/tutorial", "topic1", "topic2"]
status: inbox
source_url: https://youtube.com/watch?v=xxx
source_type: video
author: Channel Name
duration: 45min
summary: Brief 1-2 sentence summary
---
```

## Required Tag Prefixes

Always include:

- `source/video` (for YouTube)
- `status/inbox` (always for new notes)

Additional prefixes:

- `type/` - tutorial, reference, opinion, research, guide
- `action/` - review, implement, research, practice
- `cross/` - for multi-category content (cross/tech, cross/business, etc.)

Topic tags have no prefix: `react`, `coaching`, `nutrition`

## Categorization Logic

For YouTube learning notes, determine category by content:

| Content About                          | Category | Likely Subcategory            |
| -------------------------------------- | -------- | ----------------------------- |
| Coaching, drills, tactics, players     | Football | Skills, Drills, Tactics       |
| Programming, AI, tools, infrastructure | Tech     | AI, Web_Dev, Tools            |
| Entrepreneurship, marketing, finance   | Business | General, Marketing, Finance   |
| Fitness, nutrition, wellness, recipes  | Health   | Workouts, Nutrition, Recovery |
| Personal reflection                    | Journal  | (date)                        |

If content spans categories, pick PRIMARY and add `cross/{other}` tags.

## Example: YouTube Video Note

```markdown
---
title: Building Raising Cane's - Entrepreneurial Obsession
date_created: 2025-12-30
date_modified: 2025-12-30
category: Business
subcategory: General
tags:
  [
    "source/video",
    "status/inbox",
    "type/guide",
    "entrepreneurship",
    "focus",
    "quality",
    "founders-mindset",
  ]
status: inbox
source_url: https://www.youtube.com/watch?v=B5rRIdQKB0A
source_type: video
author: David Senra
duration: 2h15min
summary: Todd Graves on building Raising Cane's through fanatical focus on one product done excellently
---

# Building Raising Cane's - Entrepreneurial Obsession

**Source:** YouTube - David Senra Interview
**Author:** Todd Graves (Raising Cane's Founder) & David Senra
**Date Consumed:** 2025-12-30
**Link:** https://www.youtube.com/watch?v=B5rRIdQKB0A
**Type:** Video/Podcast

---

## Summary

[content]

## Key Takeaways

[content]

...
```

## Note Body Structure

After frontmatter, use the standard learning notes template from `output-template.md`.
The frontmatter is additional metadata for Obsidian, the body content stays the same.
