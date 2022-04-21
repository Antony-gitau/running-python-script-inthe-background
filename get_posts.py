import os
import json
import pandas as pd
import requests
from datetime import datetime

def fetch(url:str) -> list:
    results = requests.get(url)
    return json.loads(results.content)

def process(posts:list) -> pd.DataFrame:
    processed = []
    for post in posts:
        processed.append({
            'ID':post['id'],
            'UserID':post['userId'],
            'Title':post['title']
        })
    return pd.DataFrame(processed)

def save(posts:pd.DataFrame, path:str) -> None:
    posts.to_csv(path, index=False)

if __name__ == "__main__":
    posts = fetch(url='https://jsonplaceholder.typicode.com/posts')
    posts = process(posts=posts)
    current_timestamp = int(datetime.timestamp(datetime.now()))
    path = os.path.abspath(f'/home/antonym/running-python-script-inthe-background/get_posts_{current_timestamp}.csv')
    save(posts=posts, path=path)
