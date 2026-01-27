#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["youtube-transcript-api"]
# ///
"""Fetch YouTube video transcript and metadata.

Usage: uv run fetch_transcript.py <youtube_url_or_id>
"""

import sys
import re
import json
from urllib.request import urlopen
from urllib.error import URLError

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


def extract_video_id(url: str) -> str | None:
    """Extract video ID from various YouTube URL formats."""
    patterns = [
        r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([a-zA-Z0-9_-]{11})',
        r'^([a-zA-Z0-9_-]{11})$'  # Just the ID
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def get_video_title(video_id: str) -> str:
    """Fetch video title from YouTube (basic method without API key)."""
    try:
        url = f"https://www.youtube.com/watch?v={video_id}"
        response = urlopen(url, timeout=10)
        html = response.read().decode('utf-8')
        # Extract title from HTML
        match = re.search(r'<title>(.+?)</title>', html)
        if match:
            title = match.group(1)
            # Clean up " - YouTube" suffix
            title = re.sub(r'\s*-\s*YouTube\s*$', '', title)
            return title
    except (URLError, Exception):
        pass
    return f"Video {video_id}"


def fetch_transcript(video_id: str) -> tuple[str, list[dict]]:
    """Fetch transcript, returns (formatted_text, raw_segments)."""
    ytt_api = YouTubeTranscriptApi()
    transcript_list = ytt_api.list(video_id)
    
    # Prefer manual transcripts, fall back to auto-generated
    try:
        transcript = transcript_list.find_manually_created_transcript(['en'])
    except:
        try:
            transcript = transcript_list.find_generated_transcript(['en'])
        except:
            # Get whatever is available
            transcript = next(iter(transcript_list))
            transcript = transcript.translate('en')
    
    fetched = transcript.fetch()
    formatter = TextFormatter()
    formatted = formatter.format_transcript(fetched)
    
    # Convert to list of dicts for duration calculation
    segments = [{'start': s.start, 'duration': s.duration, 'text': s.text} for s in fetched]
    
    return formatted, segments


def main():
    if len(sys.argv) < 2:
        print("Usage: fetch_transcript.py <youtube_url_or_id>", file=sys.stderr)
        sys.exit(1)
    
    url_or_id = sys.argv[1]
    video_id = extract_video_id(url_or_id)
    
    if not video_id:
        print(f"ERROR: Could not extract video ID from: {url_or_id}", file=sys.stderr)
        sys.exit(1)
    
    try:
        title = get_video_title(video_id)
        transcript_text, segments = fetch_transcript(video_id)
        
        output = {
            "video_id": video_id,
            "title": title,
            "url": f"https://www.youtube.com/watch?v={video_id}",
            "transcript": transcript_text,
            "duration_seconds": int(segments[-1]['start'] + segments[-1]['duration']) if segments else 0
        }
        
        print(json.dumps(output, indent=2))
        
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
