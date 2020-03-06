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
final_str1 = (string_input['test_input']['range'][1])
final_str2 = (string_input['test_input']['range'][4])
print(final_str1)
print(final_str2)

a = int(final_str1)
b = int(final_str2)

my_list = [True] * (b)

my_list[0] = False
my_list[1] = False
i = 2
for i in range(b):
    if my_list[i] == True:
        for j in range(2*i,b, i):
            my_list[j] = False

ans_list = []

for i in range(a+1,b):
    if my_list[i] == True:
        ans_list.append(i)

#print(ans_list)

#         count +=1
data1 = {
    "test_session": 13,
    "output": { "list": ans_list }, 
    "challenge": 6
}

data2 = json.dumps(data1)

#print(data2)

headers = {'Content-type':'application/json', 'Accept':'application/json'}

url = "https://code-riddler.herokuapp.com/api/v1/testsessionchallenges/output/"

check = requests.post(url,data = data2 ,auth = (username,password),headers =headers)
#print(check.status_code)
print(check.content)
