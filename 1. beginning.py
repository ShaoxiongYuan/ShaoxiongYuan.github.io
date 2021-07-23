import time
from datetime import datetime
from github import Github
import os

ACCESS_TOKEN = open('token.txt').read()
g = Github(ACCESS_TOKEN)

end_time = time.time() - 86400 * 50
start_time = end_time - 86400 * 51
for i in range(3):
    start_time_str = datetime.utcfromtimestamp(start_time).strftime('%Y-%m-%d')
    end_time_str = datetime.utcfromtimestamp(end_time).strftime('%Y-%m-%d')
    start_time -= 86400
    end_time -= 86400
    query = f'language:python created:{start_time_str}..{end_time_str}'
    result = g.search_repositories(query)

    for repo in result:
        print(repo.clone_url)
        try:
            os.system(f'git clone {repo.clone_url} repos/{repo.owner.login}/{repo.name}')
        except Exception as e:
            continue
