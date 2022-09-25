print("TINH DIEM TRUNG BINH")

a = float(input("diem mon Anh : "))
if a < 0 :
    print("loi~")
    exit()
b = float(input("diem mon Van : "))
if b <0  :
    print("loi~")
    exit()
c = float(input("diem mon Toan : "))
if c <0 :
    print("loi~")
    exit()
dtb = (a+b+c)/3
print(dtb)
if dtb >= 8 :
    print("gioi !")
elif dtb < 8 and dtb >= 6.5:
    print("kha' !")
elif dtb < 6.5 and dtb >= 5:
    print("trung binh !")
else:
    print("cui` bap !")


