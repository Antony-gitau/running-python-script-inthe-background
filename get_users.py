from importlib.resources import path
import os
import json
from unicodedata import name
import requests
import pandas as pd
from datetime import datetime 

def fetch(url:str ) -> list:
    results = requests.get(url)
    return json.loads(results.content)

def process(users: list) -> pd.DataFrame:
    processed = []
    for user in users:
        processed.append({"ID" :user['id'],
        "Name" :user['name'],
        'Username': user['username'],
        'Email':user['email'],
        'Phone':user['phone'],
        'Company': user['company']['name']})
    return pd.DataFrame(processed)    

def save(users:pd.DataFrame, path:str) -> None:
    users.to_csv(path, index=False)

if __name__ == "__main__":
    users = fetch(url= 'https://jsonplaceholder.typicode.com/users')
    users = process(users=users)
    current_timestamp = int(datetime.timestamp(datetime.now())) #ensure files are not overridden
    path = os.path.abspath(f'/home/antonym/running-python-script-inthe-background/get_users_{current_timestamp}.csv')
    save(users=users, path=path)