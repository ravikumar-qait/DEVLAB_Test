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

my_dict = {'a': 0,'e':0,'i':0,'o':0,'u':0}
count = 0

for i in range(len(final_str)):
    char = final_str[i]
    if char in ('a','e','i','o','u'):
        my_dict[char]  += 1
    
a = my_dict['a']
e = my_dict['e']
i = my_dict['i']
o =  my_dict['o']
u =  my_dict['u']

#print(my_dict['a'])
data1 = {
    "test_session": 13,
    "output": { 'a': a , 'e': e, 'i': i, 'o': o, 'u': u }, 
    "challenge": 4   
}

data2 = json.dumps(data1)

#print(data2)

headers = {'Content-type':'application/json', 'Accept':'application/json'}

url = "https://code-riddler.herokuapp.com/api/v1/testsessionchallenges/output/"

check = requests.post(url,data = data2 ,auth = (username,password),headers =headers)
#print(check.status_code)
print(check.content)
