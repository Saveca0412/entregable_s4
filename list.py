from flask import Flask
import pandas as pd
import requests

app = Flask(__name__)

@app.route('/add_users')
def add_users():
    url = 'https://docs.google.com/spreadsheets/d/1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU/export?format=csv&id=1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU&gid=135007174'
    list_of_students = pd.read_csv(url)
    for i in range(len(list_of_students)):
        first_name = list_of_students.iloc[i]['first_name']
        email = list_of_students.iloc[i]['first_name'][0:4]
        email = f"{email}{i}@hotmail.com"
        email = email.lower()
        password = i
        # print(first_name, email)

        payload = {
            "name":first_name,
            "email":email,
            "password":password
        }

        API_ENDPOINT = 'http://127.0.0.1:8000/v1/register'
        response = requests.post(url = API_ENDPOINT, data=payload)
    return{'status':'user created successfully'}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)