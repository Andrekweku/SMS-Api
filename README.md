# SMS-Api

This is a simple SMS Api created with the help of BulkSms API to send SMS messages to any mobile number.

- To run this program, first clone this repo, cd into the folder and create a virtual environment

> python -m venv venv

Next to install all the packages used in this program, please run:

> pip install -r requirements.txt 

- Create a '.env' file and add your environment configs listed in the `config.py` to the '.env' file.

- Run `uvicorn app.main:app --reload` to start your program in localhost.

- Open the link '(CTRL + click)' provided in your terminal and add '/docs' to open the Swagger UI to test the `/send-sms` endpoint in this api.
