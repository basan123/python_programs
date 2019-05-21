def factorial(num):
    if num==1 or num==0:
        return 1

    result=1
    for i in range(num,1,-1):
        result=result*i

    return result

a=factorial(10)
print(a)
