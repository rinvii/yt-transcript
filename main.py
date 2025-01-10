from youtube_transcript_api import YouTubeTranscriptApi

def main():
    try:
        transcript = YouTubeTranscriptApi.get_transcript(
            "yE3kwHfeDaQ",
            proxies={
                "https": "socks5://localhost:9050",
                "http": "socks5://localhost:9050"
            }
        )
        
        for entry in transcript:
            start_time = entry['start']
            minutes = int(start_time // 60)
            seconds = int(start_time % 60)
            text = entry['text']

            print(f"{minutes:02}:{seconds:02} {text}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
