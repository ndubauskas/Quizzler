
#API https://opentdb.com/api.php?amount=10
import requests
response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()

data = response.json()

question = data["results"][0]["question"]
answer = data["results"][0]["correct_answer"]

question_data = []
answer_data = []
for index in range(0, 10):
    question_data.append(data["results"][index]["question"])
    answer_data.append(data["results"][index]["correct_answer"])


