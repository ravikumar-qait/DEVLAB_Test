import requests
import json
import urllib


my_dict = {
    "username": "ravikumar",
    "password": "9909Rk##",
    "first_name": "Ravi",
    "last_name": "Kumar ",
    "email": "ravikumar@qainfotech.com"
}



register_url = "https://code-riddler.herokuapp.com/api/v1/candidates/"
r = requests.post(url = register_url , data = my_dict)

check_id = r.content    
print(check_id)