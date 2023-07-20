```python
#왜 안돼??3번

for i in range(1,11):
    API_URL_1 = API_URL + str(i)
    response = requests.get(API_URL_1)
    parsed_data = response.json()
    name = {
        'company':parsed_data['company']['name'],
        'name':   parsed_data['name']
        }
    if float(parsed_data['address']['geo']['lat']) < 80 :
        {'lat':    parsed_data['address']['geo']['lat']}
    if float(parsed_data['address']['geo']['lng']) > -80 :
        {'lng':    parsed_data['address']['geo']['lng']}
    dummy_data.append(name)

print(dummy_data)
```

```python
#5번
def create_user(users):
    for user in users:



def is_validation(user):
    is_okay = True
    if user['blood_group'] not in blood_types:
        is_okay = False
        
    if user['company'] in black_list:
        is_okay = False
        return 'blocked'
        break
        
    if '@' not in user['mail']:
        is_okay = False
        
    if len(user['name']) < 1 or len(user['name']) > 30 :
        is_okay = False
        
    if len(user['website']) < 1 :
        is_okay = False
```

```python
#4번
company가 중복될 수 있으므로 append해야

```

