def digitToStr(n, numberStr):
    if n < 10:  # the number has only one digit : base case
        return str(n) + numberStr

     
    aux = n%10 # to get the last digit from right to left
    numberStr = str(aux) + numberStr
    print(f"N {numberStr}")
    return digitToStr(int((n - aux)/10) , numberStr )




def run():
    n = digitToStr(12345, "")
    print(f"Result: {n} and its type is {type(n)}")
    



if __name__ == "__main__":
    run()
