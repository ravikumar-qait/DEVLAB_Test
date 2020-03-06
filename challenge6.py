import requests
import json


username =  "ravikumar"
password =  "9909Rk##"

register_url = "https://code-riddler.herokuapp.com/api/v1/challenges/get_challenge/"

resp = requests.get(register_url, auth=('ravikumar', '9909Rk##') )

#print(resp.status_code)

check_id = resp.content
string_input = resp.json()

final_str = (string_input['test_input']['text'])
print(final_str)

count = 0
for i in range(len(final_str)):
    char = final_str[i]
    if char == ' ' and  final_str[i+1] != ' ':
        count+=1

ans = count+1

data1 = {
    "test_session": 13,
    "output": { "wordCount": ans }, 
    "challenge": 2
}

data2 = json.dumps(data1)

#print(data2)


headers = {'Content-type':'application/json', 'Accept':'application/json'}

url = "https://code-riddler.herokuapp.com/api/v1/testsessionchallenges/output/"

check = requests.post(url,data = data2 ,auth = (username,password),headers =headers)
#print(check.status_code)
print(check.content)

