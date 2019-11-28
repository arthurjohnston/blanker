Rhyme group generator
=======

This code will generate all the rhymes in the English language using the cmudict. If the rhyme.py is directly run it will print out all the rhymes in the English language. A full writeup, including a strict definition of what consitutes a rhyme, can be found [here](https://medium.com/@the_ajohnston/how-many-rhymes-are-there-in-english-9ab81029ebdf)

Getting Started
=======

Clone this repository and change directory to the new folder that was created

Create a virtual environment and activate the environment
    virtualenv .venv
    source .venv/bin/activate

Install the required python packages
    pip install -r requirements.txt

Download the nltk data
    python -m nltk.downloader all

Execute rhyme.py
    python rhyme.py -h
