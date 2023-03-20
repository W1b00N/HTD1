liter = float(input("ป้อนตัวเลขลิตร(l) :"))
gram = liter*0.001
print(f"{liter:.2f}ลิตร(l)มีค่าเท่ากับ {gram:.2f} กรัม(g)")


import datetime

s = 60
t = datetime.timedelta( seconds = s )
print( s, 'วินาที เท่ากับ', t )