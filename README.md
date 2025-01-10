## Overview

This example program uses [torproxy](https://github.com/dperson/torproxy) and [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) to fetch transcripts from a cloud machine. It bypasses YouTube's IP blocking on cloud services by routing traffic through the Tor network. Sometimes, requests may fail if the exit node's IP is blocked by YouTube.

This was successfully tested on a GitHub codespace.

## Prerequisites

1. Docker
2. Python 3.12+
3. [uv](https://github.com/astral-sh/uv)

## Quickstart

1. Clone the repository

```bash
git clone https://github.com/rinvii/yt-transcript.git
cd yt-transcript
```

2. Set up tor proxy

```bash
docker compose up -d
```

3. Run script

```bash
uv run main.py
```