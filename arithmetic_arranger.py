import re
def checkLength(num1,num2):
    return len(num1)<=4 and len(num2)<=4

def arithmetic_arranger(data,withResult=False):
    nums=[]
    if len(data)>5:
        return "Error: Too many problems."
    for expr in data:
        try:
            res=str(eval(expr))
                # print(res)
        except:
            return "Error: Numbers must only contain digits."
        if re.match('[0-9]+ [+-] [0-9]+', expr)!=None:


            if '+' in expr:
                numbers=expr.split(' + ')
                if not checkLength(str(numbers[0]),str(numbers[1])):
                    return "Error: Numbers cannot be more than four digits."
                numbers[0],numbers[1]=str(numbers[0]),'+ '+str(numbers[1])
                numbers.append("-"*len(numbers[-1]))
                numbers.append(res)
                nums.append(numbers)
            else:
                numbers=expr.split(' - ')
                if not checkLength(str(numbers[0]),str(numbers[1])):
                    return "Error: Numbers cannot be more than four digits."
                numbers[0],numbers[1]=str(numbers[0]),'- '+str(numbers[1])
                numbers.append("-"*len(numbers[-1]))
                numbers.append(res)
                nums.append(numbers)
        else:
            return "Error: Operator must be '+' or '-'."
    
    maxIndex=3
    if withResult==True:
        maxIndex=4
    for index in range(maxIndex):
        for values in nums:
            gap=""
            if index==0 or index==3:
                gap=" "*(len(values[1])-len(values[index]))
            print(gap+values[index],end="\t")
        print()



