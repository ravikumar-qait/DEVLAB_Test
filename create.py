import requests
import json
import urllib


# my_dict = {
#    "candidate": "9"
# }

username =  "ravikumar"
password =  "9909Rk##"

register_url = "https://code-riddler.herokuapp.com/api/v1/testsessions/"

resp = requests.post(register_url, data={ "candidate": "75" }, auth=('ravikumar', '9909Rk##')) 
#resp = requests.post(url = register_url ,  auth = (username,password) , data = my_dict)

check_id = resp.content
print(check_id)