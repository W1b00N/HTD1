import re

def special_char_check(input_string):
    # กำหนด pattern ในการตรวจสอบอักขระพิเศษ
    pattern = r"[^a-zA-Z0-9\s]"

    # ใช้ method findall เพื่อค้นหาอักขระพิเศษใน input_string
    special_chars = re.findall(pattern, input_string)

    # แสดงผลเฉพาะอักขระพิเศษที่พบ
    print("Special characters found:", ', '.join(special_chars))