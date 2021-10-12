# Scrape Reddit Thread

Download Reddit data for a single Reddit thread. 

Eddie Chapman 

## Installation

Clone this repository onto your machine

```
git clone https://www.github.com/eddiechapman/scrape-reddit-thread.git
```

Enter the directory of the new repository

```
cd scrape-reddit-thread
```

Make a Python virtual environment

```
python3 -m venv venv
```

Activate the virtual environment and install the required Python packages

```
source venv/bin/activate 
pip install -r requirements.txt
```

Create a file named `.env` in the project directory and add the following fields. 

The values should be taken from your Reddit account.

```
client_id=adfgrefasifune
client_secret=ijdnroimsoeimf
```

You may also set these enviroment variables manually.

## Usage

Run `reddit_scrape_comments.py` to download the comments of a Reddit thread.

Comments will be stored as JSON files in a `comments` folder in the project directory.

```
python reddit_scrape_comments.py
```

You can change the `URL` variable in `reddit_scrape_comments.py` on line 10 to 
choose a different Reddit thread.

Just click on a Reddit thread and copy and paste the URL at the top of the page. 

### Converting JSON comments into a CSV file

After you run `reddit_scrape_comments.py`, you'll have a bunch of JSON files in `scrape-reddit-thread/comments/`. 

You can merge these into a single CSV file with `json2csv.py`.

You'll need to provide the location of the comments folder and the name of the CSV file.

```
python3 json2csv.py comments comments.csv
```

Assuming you are already in `scrape-reddit-thread/`, the above command will collect JSON 
files from `scrape-reddit-thread/comments/` and create a new CSV file at 
`scrape-reddit-thread/comments.csv`.

### Converting the CSV file into text files

If you'd like to make a bunch of .txt files containing the comment text, run `csv2txt.py`.

You'll get a folder full of plain text files with the text from each comment. Each file will be named after the `ID` field
of the comment. Again, you'll need to provide the location of the CSV file and the intended location of the text files.

```
python3 csv2txt.py comments.csv comment_text
```

The above command will collect comment data from `scrape-reddit-thread/comments.csv` and create text files for each
comment in `scrape-reddit-thread/comment_text/`

### Sampling the comment text

The thread I scraped contained over 2,000 comments. I found it useful to make a single text file with 
a random sample of comments so that I could review them. 

You can run `sample_comments_txt.py` to produce a sample file for your inspection.

You'll need to provide the location of the text comments (created with `csv2txt.py`), the number of 
comments to sample, and the location of the output file.

```
python3 sample_comments_txt.py comments_text 25 sample_25.txt
```

This will look for comment .txt files in `scrape-reddit-thread/comments_text/` and sample 25 comments 
into `scrape-reddit-thread/sample_25.txt`.
