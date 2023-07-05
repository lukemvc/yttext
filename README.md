# YTTEXT 

## Overview
The YTTEXT package provides a convenient way to scrape subtitles from YouTube videos and save them to text files. It offers a simple interface for retrieving and processing subtitles, making it easy to extract text data for analysis or other purposes.
<br></br>

## Installation
```
pip install yttext
```
upgrade
```
pip install --upgrade yttext
```

## Usage

To scrape the subtitles from any youtube video, simply call the get_text function with the video_id, and the text will be saved to <video_id>.txt.
```python
import yttext

video_id = 'IflfP4XwzAI'
yttext.get_text(video_id)
```
Output printed to console:
```
48773 words successfully scraped.
```
Optionally, you can specify a folder name to write the file to as well.

```python
video_id = 'IflfP4XwzAI'
yttext.get_text(video_id, folder='subtitles')
```
<br>

## Multiple video usage

To use the get_text function for a list of videos, you can simply call the function in a loop or iterate over the video IDs, and they will all be saved to a txt file with the cooresponding video ID.

```python
video_ids = ['video_id1', 'video_id2', 'video_id3']

for video_id in video_ids:
    yttext.get_text(video_id)
    # Optional: Specify folder for saving the text file
    # yttext.get_text(video_id, folder='subtitles')
```
