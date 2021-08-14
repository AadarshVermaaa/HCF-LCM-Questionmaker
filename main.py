from random import randint
from math import gcd
"""
1.hcf calculator
2.lcm calculator
hcf maker
lcm maker
and print them 
in file and print answer in other file
"""
def lcm_calculator(x,y):
    """This will calculate lcm of two digits by using num1*num2==lcm*hcf"""
    lcm_ans= x*y//gcd(x,y)
    with open("Answers.txt", "a") as hcf_file:
        hcf_file.write(str(i) + f". x={x} y={y} =" + str(lcm_ans) +"--[LCM]\n")
    return x*y//gcd(x,y)
def HCF(x,y):
    gcdstr =str(gcd(x,y))
    with open("Answers.txt", "a") as hcf_file:
        hcf_file.write("\n"+ str(i) + f". x={x} y={y} =" + gcdstr + " --[HCF]\t")
    return gcdstr

    
for i in range(51):
    x = randint(1,1000)
    y = randint(1,1000)
    HCF(x,y)
    lcm_calculator(x,y)
    with open("Question_paper.txt", "a") as ques_paper:
        ques_paper.write("\n"+ str(i)+f". num1 = {x}\tnum2 = {y}\n")
    print(i, "num1 =", x)
    print(i, "num2 =",y)
    
print(HCF(x,y))