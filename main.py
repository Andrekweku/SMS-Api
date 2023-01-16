
from fastapi import FastAPI
import config
import requests


app = FastAPI()
settings = config.Settings()


@app.post("/send-sms")
def send_sms(recipient: str, message: str, ): 
    api_url = "https://api.bulksms.com/v1/messages"
    data = {
        "to": recipient,
        "body": message
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Authorization: Basic {settings.basic_auth}"
    }
    response = requests.post(api_url, json=data, auth= (settings.token_id, settings.token_secret), headers=headers)
    return response.json()

