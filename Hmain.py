project_list = [
    {"sender": "Hawraa", "text": "top secret data", "is_encrypted": True},
    {"sender": "Zahra", "text": "system firewalls are up", "is_encrypted": True},
    {"sender": "Fatima", "text": "database backup complete", "is_encrypted": False},
]
print("-------🔐 Secret Message Shield 🔐--------")
for message in project_list:
    if message["is_encrypted"] == True:
        print(f"🟢 [SAFE] Message from {message['sender']} is fully secured!")
else:
    secure_text = message["text"]. upper()
    print(f"🔴 [RAW] {message['sender']} -> {secure_text}")
    print("------------------------------------------")
