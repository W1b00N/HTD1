polwa = int(input("ปริมาณน้ำเสีย: "))

littokg = polwa*1000
kgtog = littokg*1000
stream = kgtog -(167 /(143*60))
strtow = stream - (89 /(143*60))
oxahy = (strtow/2) / 143

print("ปริมาณออกซิเจน = ",'%.2f'%(oxahy) ,"กิโลกรัม")