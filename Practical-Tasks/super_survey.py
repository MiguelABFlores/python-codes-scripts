#!/usr/bin/env python3
import requests
import json

# Enter your survey details here
SURVEY_NAME = "Survey_Name"
PAGE_NAME = "Page_Name"
CLIENT_ID = "iQTOR-D0T8qiWOw6-BwDIQ"
CLIENT_SECRET = "159347523243266839229721365528588970719"
ACCESS_TOKEN = "cOmUpOXfevWx560egh1njpUlAK6xf-6f763CarupUdZrS5mSPbqqRycvTs8wJ8ImqNLCb6gpfMlSwRyyFD2oA154j1XWni5X.j5qkEpu9K2yiJ5Co4AjePKOo2lCC580"

# Load survey questions from JSON file
with open("survey_questions.json") as f:
    questions = json.load(f)[SURVEY_NAME][PAGE_NAME]

# Get survey details
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}
response = requests.get(
    f"https://api.surveymonkey.com/v3/surveys?title={SURVEY_NAME}", headers=headers
)
survey_id = response.json()["data"][0]["id"]

# Create collector
payload = {
    "type": "email",
    "name": "PythonCollector",
    "recipients": {"type": "all"},
    "send": False,
}
response = requests.post(
    f"https://api.surveymonkey.com/v3/surveys/{survey_id}/collectors",
    headers=headers,
    json=payload,
)
collector_id = response.json()["id"]

# Add message to collector
payload = {
    "type": "invite",
    "subject": "Survey Invitation",
    "body": {"text": "Please take this survey!"},
}
response = requests.post(
    f"https://api.surveymonkey.com/v3/collectors/{collector_id}/messages",
    headers=headers,
    json=payload,
)
message_id = response.json()["id"]

# Add recipients to collector
payload = {
    "email_message_id": message_id,
    "recipients": [
        {"email": "mbriseno@griddynamics.com"}
    ],
}
response = requests.post(
    f"https://api.surveymonkey.com/v3/collectors/{collector_id}/recipients/bulk",
    headers=headers,
    json=payload,
)

# Print survey questions and answers
print("Survey questions:")
for question_name, question in questions.items():
    print(f"{SURVEY_NAME}/{PAGE_NAME}/{question_name}: {question['Description']}")
    print(f"Possible answers: {', '.join(question['Answers'])}")
    print()

# Send survey invitation to recipients
payload = {
    "collector_id": collector_id,
    "type": "email",
    "recipients": [
        {"email": "mbriseno@griddynamics.com"}
    ],
    "send": True,
    "subject": "Survey Invitation",
    "body_text": f"Please take this survey: https://es.surveymonkey.com/r/WKK33ZK",
}
response = requests.post(
    f"https://api.surveymonkey.com/v3/collectors/{collector_id}/send",
    headers=headers,
    json=payload,
)

# Print response from sending survey invitations
print(response.json())


