---
name: youtube-learning-notes
description: Generate personalized learning notes from YouTube videos. Takes a YouTube URL and optionally uses user's TELOS context file from references/, then outputs a structured markdown document with summary, key takeaways, personalized insights, action items, and connections. Can also format for Obsidian vault when requested. Triggers on requests like "create notes from this video", "summarize this YouTube video for my learning", "make learning notes from [URL]", or "summarize this video and move it to obsidian".
---

# YouTube Learning Notes

Generate comprehensive, personalized learning notes from YouTube videos.

## Workflow

### 1. Fetch Transcript

Run the transcript fetcher script (dependencies auto-install via uv):

```bash
uv run scripts/fetch_transcript.py "<youtube_url>"
```

Returns JSON with: `video_id`, `title`, `url`, `transcript`, `duration_seconds`

### 2. Check for TELOS File

Look for `references/TELOS.md`. If it exists and contains real user content (not just the placeholder template), use it to personalize the output.

**TELOS sections to parse:**

- PROBLEMS, MISSION, GOALS, CHALLENGES, IDEAS, WISDOM, PROJECTS

**If TELOS exists:** Personalize insights, questions, and action items to user's context. Reference TELOS items by ID (G1, C2, etc.).

**If no TELOS (or placeholder only):** Generate general insights based on video content alone. Skip TELOS-specific references.

### 3. Analyze & Generate

Process the transcript to extract:

- Core message and thesis
- 3-5 main ideas with explanations
- 4-6 memorable direct quotes
- Actionable insights

See `references/output-template.md` for full template structure.

**Critical rules:**

- Only include sections relevant to the video content
- If video is purely technical tutorial → skip "business application" sections
- Always include: Summary, Key Takeaways, Tags, Personal Rating
- Quotes must be actual quotes from the video transcript
- Action items must be specific and actionable

### 4. Check for Obsidian Output

If the user requests Obsidian output (phrases like "move to obsidian", "save to vault", "add to obsidian"):

1. Read `references/obsidian-guide.md` for vault location and categorization rules
2. Determine the appropriate category and subcategory based on video content
3. Add Obsidian frontmatter (title, date_created, category, subcategory, tags, etc.)
4. Generate the correct file path using the vault base path from the guide: `{vault_path}/{Category}/Articles/{filename}.md`
5. Use lowercase hyphenated filename
6. Save the file directly to the vault location

The Obsidian frontmatter goes at the top, followed by the standard learning notes body.

### 5. File Output

**Standard output:** `[Video Title] - [Topic].md` (current directory)

**Obsidian output:** Full path from `references/obsidian-guide.md` + `{Category}/Articles/{lowercase-hyphenated-title}.md`

Clean titles for filesystem compatibility (remove special characters).
