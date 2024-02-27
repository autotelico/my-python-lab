def online_count(dict):
    counter = 0
    for key, value in dict.items():
        print(key)
        if (value == 'online'):
            counter += 1
    return counter
    
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

r = online_count(statuses)
print(r)