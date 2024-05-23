import json

user_ids = []
auth_keys = []
secret_keys = []
with open('fgop.txt','r') as f:
    for line in f.readlines():
        if not line:
            continue
        data = line[16:]
        data = json.loads(data)
        user_ids.append(data['userId'])
        auth_keys.append(data['authKey'])
        secret_keys.append(data['secretKey'])


print(','.join(user_ids))
print()
print()
print()
print(','.join(auth_keys))
print()
print()
print()
print(','.join(secret_keys))