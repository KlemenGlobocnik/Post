def calculator(a,b,operator):
    if operator=="+":
        result=float(a)+float(b)
    elif operator=="-":
        result=float(a)-float(b)
    elif operator=="*":
        result=float(a)*float(b)
    elif operator=="/":
        result=float(a)/float(b)
    return result

def main():
    print calculator(5,1,"/")

if __name__=="__main__":
    main()
