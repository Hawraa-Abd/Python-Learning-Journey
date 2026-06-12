def check_trip_ages(any_ages_list):
    print("---Trip Eligibility Results ---")
    for a in any_ages_list:
        if a >= 18:
            print(f"Age {a}: Allowed to enter! ✅")
        else:
            print(f"Age {a}: Underage - Needs Parents! 👪")
group_A = [20, 15, 35, 12]
group_B = [40, 17, 22]
check_trip_ages(group_A)
print("--------------------------")
check_trip_ages(group_B)
