# 1. قائمة فارغة لتخزين الموظفين المقبولين
employees_list = []

# 2. دالة التحقق وإضافة الموظف
def register_employee(name, age):
    if age >= 18:
        # نقوم بإنشاء قاموس (Dictionary) للموظف الجديد
        new_employee = {"name": name, "age": age}
        # نضيف الموظف إلى القائمة الكبيرة
        employees_list.append(new_employee)
        print(f"🎉 Done! {name} has been registered successfully.")
    else:
        print(f"💔 Sorry, {name} is under 18 and cannot be registered.")

# 3. دالة لعرض جميع الموظفين المقبولين في القائمة
def show_all_employees():
    if len(employees_list) == 0:
        print("📁 The list is empty. No employees registered yet.")
    else:
        print("\n📋 --- Registered Employees List ---")
        for emp in employees_list:
            print(f"- Employee: {emp['name']} | Age: {emp['age']}")

# 4. الحلقة التفاعلية للبرنامج (Menu Loop)
while True:
    print("\n🌟 --- Welcome to Employee Verification System ---")
    print("1. Register a new employee (تسجيل موظف جديد)")
    print("2. Show all employees (عرض جميع الموظفين)")
    print("3. Exit (خروج)")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        emp_name = input("Enter employee name: ")
        # نقوم بتحويل النص المدخل للعمر إلى رقم صحيح (int)
        emp_age = int(input("Enter employee age: "))
        register_employee(emp_name, emp_age)
        
    elif choice == "2":
        show_all_employees()
        
    elif choice == "3":
        print("Goodbye! Thank you for using the system. 👋")
        break # ينهي حلقة while ويغلق البرنامج
        
    else:
        print("⚠️ Invalid choice! Please enter 1, 2, or 3.")
