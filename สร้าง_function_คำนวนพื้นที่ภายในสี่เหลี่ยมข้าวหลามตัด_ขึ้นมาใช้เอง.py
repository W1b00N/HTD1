import random

def generate_random_characters(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    result = ""
    for _ in range(length):
        random_index = random.randint(0, len(characters) - 1)
        result += characters[random_index]
    return result

# เรียกใช้ฟังก์ชันเพื่อสร้างตัวอักษรที่สุ่มแล้วแสดงผล
random_characters = generate_random_characters(20)
print(random_characters)