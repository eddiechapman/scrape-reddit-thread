import json
import os
import pprint

import dotenv
import praw


URL = 'https://www.reddit.com/r/DataHoarder/comments/krx449/megathread_archiving_the_capitol_hill_riots/?utm_source=share&utm_medium=web2x&context=3'

COMMENT_FIELDS = [
    'body', 
    'body_html', 
    'created', 
    'created_utc',
    'controversiality',
    'depth',
    'downs',
    'edited',
    'id', 
    'is_submitter', 
    'name', 
    'parent_id', 
    'permalink',
    'score', 
    'subreddit_id', 
    'subreddit_name_prefixed',
    'ups'
]


def main():
    dotenv.load_dotenv()

    if not os.environ.get('client_id'):
        raise SystemExit('Please supply the `client_id` environment variable')
    if not os.environ.get('client_secret'):
        raise SystemExit('Please supply the `client_secret` environment variable')

    print('Authenticating')

    reddit = praw.Reddit(
        client_id=os.environ.get('client_id'),
        client_secret=os.environ.get('client_secret'),
        user_agent='Comment extraction (by u/eatenbytree)'
    )

    print('Fetching submission')

    submission = reddit.submission(url=URL)

    print(f'Fetched submission {submission.id}')

    print('Unpacking comment forest')

    submission.comments.replace_more(limit=None)
    for i, comment in enumerate(submission.comments.list()):
        filename = f'comments/{comment.id}.json'
        
        comment_data = {field: vars(comment).get(field) for field in COMMENT_FIELDS}
     
        if comment.author:
            comment_data['author'] = vars(comment.author).get('name')
        else:
            comment_data['author'] = None
        
        with open(filename, 'w') as f:
            json.dump(comment_data, f, sort_keys=True)

    return 0


if __name__ == '__main__':
    rv = main()
    print(rv)