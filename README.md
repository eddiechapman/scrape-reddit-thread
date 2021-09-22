# Scrape Reddit Thread

For thesis research

Eddie Chapman 

## Usage

clone repository

```
git clone https://www.github.com/eddiechapman/scrape-reddit-thread.git
```


make a virtual environment

```
python3 -m venv venv
```

activate the virtual environment and install dependencies

```
source venv/bin/activate 
pip install -r requirements.txt
```

Create a file named `.env` in the project directory and add the following fields. The values should be taken from your Reddit account.

```
client_id=adfgrefasifune
client_secret=ijdnroimsoeimf
```

You may also set these enviroment variables manually.

Run `reddit_scrape_comments.py` to produce a directory of JSON comment files.

Run `json2csv.py` to convert the JSON comment files directory into a CSV file.

Run `csv2txt.py` to produce a directory of txt files containing comment text

Run `sample_comments_txt.py` to produce a text file containing *n* random comments. Good for inspecting dataset. 



```
source .env
```
