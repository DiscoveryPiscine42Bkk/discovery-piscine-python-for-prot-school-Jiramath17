
age = int(input("กรุณาบอกอายุของคุณ: "))

# ใช้ฟังก์ชันในการคำนวณอายุในอนาคต
def future_age(current_age, years):
    return current_age + years

# แสดงอายุปัจจุบันและอายุในอนาคต
print(f"ตอนนี้คุณอายุ {age} ปี.")
print(f"ในอีก 10 ปี คุณจะอายุ {future_age(age, 10)} ปี.")
print(f"ในอีก 20 ปี คุณจะอายุ {future_age(age, 20)} ปี.")
print(f"ในอีก 30 ปี คุณจะอายุ {future_age(age, 30)} ปี.")
