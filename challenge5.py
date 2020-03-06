import requests
import json


username =  "ravikumar"
password =  "9909Rk##"

register_url = "https://code-riddler.herokuapp.com/api/v1/challenges/get_challenge/"

resp = requests.get(register_url, auth=('ravikumar', '9909Rk##') )

print(resp.status_code)

check_id = resp.content
print(check_id)
#string_input = resp.json()
string_input = resp.json()
final_str = (string_input['test_input']['list'])
my_list = final_str.strip('][').split(', ') 
my_set = set()
ans_list = []

for i in my_list:
    if i not in my_set:
        ans_list.append(int(i))
    my_set.add(i)

print(ans_list)

data1 = {
    "test_session": 13,
    "output": { "list": ans_list }, 
    "challenge": 5
}

data2 = json.dumps(data1)

#print(data2)


headers = {'Content-type':'application/json', 'Accept':'application/json'}

url = "https://code-riddler.herokuapp.com/api/v1/testsessionchallenges/output/"

check = requests.post(url,data = data2 ,auth = (username,password),headers =headers)
#print(check.status_code)
print(check.content)
