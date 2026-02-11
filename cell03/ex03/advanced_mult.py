import sys
if len(sys.argv) > 1:
    print("none")
else:
    i = 0  # ตาราง
    while i <= 10:
        j = 0  # ตัวคูณ
        row = [] # เรียงต่อกันทีหลัง
        while j <= 10:
            row.append(str(i * j)) # เอาข้อความไปต่อท้ายในลิสต์ row |.join ใช้กับตัวเลขไม่ได้เลยเปลี่ยนเป็น str
            j += 1
        print(f"Table de {i}: {' '.join(row)}") # .join(row) เอาข้อมูลในลิสต์ row ทั้งหมดมาต่อกันแล้สคั่นด้วยช่องว่าง
        i += 1