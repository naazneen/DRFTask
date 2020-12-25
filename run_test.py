import requests
# register user
import json
"""
url = 'http://127.0.0.1:8000/register/'
data = {
    'username': 'foobarrr',
    'email': 'foobarrr@example.com',
    'password': 'somepassword',
    'user_type':'staff'
}
r = requests.post(url, data=data)
print(r.status_code)
print(r.text)
"""

# Get Token
"""
url = 'http://127.0.0.1:8000/api-token-auth/'
data = {'username':'foobarr','password':'somepassword'}
r = requests.post(url, data=data)
print(r.status_code)
print(r.text)
"""

# Visit Page
"""
url = 'http://127.0.0.1:8000/home/'
headers = {'Authorization': 'Token 365523cabaf0ec10c0535a1754de1e903f6708f'}
r = requests.get(url, headers=headers)
print(r.status_code)
print(r.text)
"""

"""
url = 'http://127.0.0.1:8000/Aadhar/'
headers = {'Authorization': 'Token 3365523cabaf0ec10c0535a1754de1e903f6708f'}
r = requests.get(url, headers=headers)
print(r.status_code)
print(r.text)

"""

#Add Aadhar
"""
url = 'http://127.0.0.1:8000/AddAadhar/'
headers = {'Authorization': 'Token 3365523cabaf0ec10c0535a1754de1e903f6708f','content-type': 'application/json'}
data = {'AadharNumber':'147852147852','is_Active':'True',
        }
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.status_code)
print(r.text)
"""

#Update Aadhar
"""
url = 'http://127.0.0.1:8000/UpdateAadhar/147852147852'
params = {'aadhar_number':'147852147852'}
headers = {'Authorization': 'Token 3365523cabaf0ec10c0535a1754de1e903f6708f','content-type': 'application/json'}
data = {'AadharNumber':'147852147852','is_Active':'False',
        }
r = requests.put(url, data=json.dumps(data), headers=headers)
print(r.status_code)
print(r.text)
"""

# Delete Aadhar
#"""
url = 'http://127.0.0.1:8000/DeleteAadhar/147852147852'
params = {'aadhar_number':'147852147852'}
headers = {'Authorization': 'Token 3365523cabaf0ec10c0535a1754de1e903f6708f','content-type': 'application/json'}

r = requests.delete(url,  headers=headers)
print(r.status_code)
print(r.text)
#"""
