from youtube_dl import YoutubeDL

# Download audio
options = {
    # Tell the downloader to download only the best quality of audio
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=AAbokV76tkU'])

# Sample 5: Search and then download the first audio
options = {
    # tell downloader to search instead of directly downloading
    'default_search': 'ytsearch',
    # Tell downloader to download only the first entry (audio)
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Girls Like You (feat. Cardi B)'])
