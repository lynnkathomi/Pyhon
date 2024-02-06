#program to calculate bonus
#prompt the user to enter salary and years
salary=int(input("Enter your salary:"))
years=int(input("Enter years of services:"))
if years>10:
    bonus=0.1*salary
    net_salary=bonus+salary
    print("Bonus:",bonus)
    print("net_salary",net_salary)
elif  years >=6 and years <=10:
    bonus=0.08*salary
    net_salary=bonus+salary
    print("Bonus:",bonus)
    print("net_salary",net_salary)
elif years <6:
    bonus=0.05*salary
    net_salary=bonus+salary
    print("Bonus:",bonus)
    print("net_salary",net_salary)






