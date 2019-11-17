
'''
BMI=weight*0.45259227/(hei*0.0254)**
'''
wht=2
if wht==0:
    print("wht is",wht)
else:
    print("whtsdsb")
#今天也完成了100波比跳
wei=float(input("wei="))
hei=float(input("hei="))
bmi=(wei*0.45259227)/((hei*0.0254)**2)
print("BMI=",bmi)
if bmi<18.5:
    print("too light")
elif bmi<25:
    print("normal")
elif bmi<30:
    print("over")
else:
    print("wanghantangshidssb")
