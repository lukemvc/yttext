from setuptools import setup

setup(
    name='yttext',
    version='0.0.1',
    description='A Python package for scraping subtitles from youtube videos.',
    long_description='yttext is a Python package for automatically collecting subtitles from a youtube video, sanitizing the text to be lowercase and single spaced, and writing it to a .txt file.',
    url='https://github.com/lukemvc/yttext',
    packages=['yttext'],
    install_requires=['requests']
)
