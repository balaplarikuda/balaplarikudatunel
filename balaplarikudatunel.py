import os
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

REPO_PATH = "."
DAYS_RANGE = 30
COMMITS_PER_RUN = 10

def random_date(start_date, days_range):
    return start_date + timedelta(days=random.randint(0, days_range - 1))

def make_commit(commit_date, message):
    with open("log.txt", "a") as f:
        f.write(f"[AUTO LOG] {commit_date.isoformat()} {random.randint(100000, 999999)}\n")

    os.system("git add .")
    os.environ["GIT_AUTHOR_DATE"] = commit_date.isoformat()
    os.environ["GIT_COMMITTER_DATE"] = commit_date.isoformat()
    os.system(f'git commit -m "{message}"')

if __name__ == "__main__":
    base_date = datetime(2024, 6, 1)
    for _ in range(COMMITS_PER_RUN):
        commit_date = random_date(base_date, DAYS_RANGE)
        commit_msg = fake.sentence(nb_words=4)
        make_commit(commit_date, commit_msg)
        os.system("git push origin main")
