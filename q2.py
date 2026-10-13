basic = float(input("Enter basic salary:"))
hra = basic * 0.20 
pf = basic * 0.12
gross = basic + hra
net = gross - pf

print("HRA:",hra)
print("PF:",pf)
print("Gross:",gross)
print("Net:",net)