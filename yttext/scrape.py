import xml.etree.ElementTree as ET
import requests
import html
import json
import re
import os

def get_text(video_id: str, folder: str = None):
    try:
        timed_text_url = helper.get_timed_text_url(video_id)
        text_list = helper.get_text(video_id, timed_text_url)
        sanitized_text = helper.sanitize_text(text_list)
        helper.write_text(video_id, sanitized_text, folder)
        words = len(sanitized_text.split())
        print(f"{words} words successfully scraped.")
    except Exception as e:
        print(f"Error occurred while scraping text for video {video_id}: {str(e)}")

class helper:
    def get_timed_text_url(vid_id):
        resp = requests.get(f'https://www.youtube.com/watch?v={vid_id}')
        with open('test.txt', 'w') as f:
            f.write(resp.text)

        format = r'https://www.youtube.com/api/timedtext(.*?)"'
        match = re.search(format, resp.text)
        if match:
            text_url = match.group(1)
            print(text_url)
            u, _ = text_url.split('lang')
            full = 'https://www.youtube.com/api/timedtext' + u + 'lang=en-US'
            timed_url = json.loads('"' + full + '"')
            print(full)

            if 'Twitch+Chat' in timed_url:
                raise Exception("Failed to retrieve subtitles")
            return timed_url
        else:
            raise Exception("Failed to retrieve timed text URL")

    def get_text(vid_id, url):
        r = requests.get(url)
        if r.status_code == 200:
            xml_response = r.text
            root = ET.fromstring(xml_response)
            text_list = []
            for text in root.findall('text'):
                if text.text:
                    decoded_text = html.unescape(text.text)
                    cleaned_text = re.sub(r'\[.*?\]', '', decoded_text)
                    text_list.append(cleaned_text.strip())
            return text_list
        else:
            raise Exception("Failed to retrieve timed text")

    def sanitize_text(text_list):
        if text_list:
            content = " ".join(text_list)
            content_list = content.split()
            single_spaced_content = " ".join(content_list).strip()
            return single_spaced_content.lower()
        else:
            raise Exception("No text found in the timed text")

    def write_text(video_id, sanitized_text, folder=None):
        if folder:
            path = f"{folder}/{video_id}.txt"
            if not os.path.exists(folder):
                os.makedirs(folder)
        else:
            path = f"{video_id}.txt"
        try:
            with open(path, 'w') as f:
                f.write(sanitized_text)
        except Exception as e:
            raise Exception(f"Failed to write text to file: {str(e)}")
