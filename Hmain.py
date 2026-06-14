staff_list = [
    {"name": "Hawraa", "role": "Developer", "clearance_level": 5},
    {"name": "Zahra", "role": "Assistant", "clearance_level": 2},
    {"name": "Adel", "role": "Manage", "clearance_level": 4}
]
print("--- 🔰 Staring Security Clearance Check 🔰 ---")
for employee in staff_list:
    if employee["clearance_level"] >= 4:
        secure_name = employee["name"]. upper()
        print(f"🟢 ACCESS GRANTED: {secure_name} ({employee['role']}) - Code: [SECURE-10x]")
    else:
        print(f"🔴 ACCESS DENIED: {employee['name']} ({employee['role']}) - Low Level!")
        print("------------------------------------------")