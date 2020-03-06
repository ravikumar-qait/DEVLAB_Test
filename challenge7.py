import requests
import json
import ast


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
print(type(final_str))
my_list = list(final_str.split(" "))
#print(type(my_list))

#print(final_str)
for i in my_list:
    print(i)

data3 = final_str
data4 = ast.literal_eval(data3)  
data5 = data4.get('player1')

pot = 1000

list1 = []
for x in data5:
    if x[0] == 'SP':
        data1 = 100
    elif x[0] == 'CL':
        data1 = 50
    elif x[0] == 'HT':
        data1 = -100
    elif x[0] == 'DD':
        data1 = -50

    if x[1] == 'SP':
        data2 = 100
    elif x[1] == 'CL':
        data2 = 50
    elif x[1] == 'HT':
        data2 = -100
    elif x[1] == 'DD':
        data2 = -50
    final = data2+data1
    list1.append(final) 
total1 = 0
for x in range(0,len(list1)):
    total1 = total1 + list1[x]
total1 = total1 + pot

data6 = data4.get('player2')
l2 = []
for x in data6:
    if x[0] == 'SP':
        data1 = 100
    elif x[0] == 'CL':
        data1 = 50
    elif x[0] == 'HT':
        data1 = -100
    elif x[0] == 'DD':
        data1 = -50

    if x[1] == 'SP':
        data2 = 100
    elif x[1] == 'CL':
        data2 = 50
    elif x[1] == 'HT':
        data2 = -100
    elif x[1] == 'DD':
        data2 = -50
    final = data2+data1
    l2.append(final) 
total2 = 0
for x in range(0,len(l2)):
    total2 = total2 + l2[x]
total2 = total2 + pot

if total1 > total2:
    ans = 'player1'    
else:
    ans = 'player2'
    

#print(ans)
final_data = {
    "test_session":13,
    "output": {"winner":ans},
    "challenge": 7
}


data10 = json.dumps(final_data)

# print(data10)


headers = {'Content-type':'application/json', 'Accept':'application/json'}

url = "https://code-riddler.herokuapp.com/api/v1/testsessionchallenges/output/"

check = requests.post(url,data = data10 ,auth = (username,password),headers =headers)
print(check.status_code)
print(check.content)
