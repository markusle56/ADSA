
def intAddition(X,Y, base):
    l1 = len(X)
    l2 = len(Y)
    result = ""
    carry = 0 

    while (l1 > 0 or l2 > 0):
        total = 0
        if (l1 > 0):
            l1 -=1
            total += int(X[l1])
        if (l2 > 0):
            l2 -= 1
            total += int(Y[l2])
        total += carry 
        carry = total // base
        result = str(total % base) + result
    if carry:
        result = str(carry) + result
    return result

def intSubstraction(X, Y, base):
    n = max(len(X), len(Y))
    if len(X) < n:
        X = "0"*(n-len(X)) + X
    else:
        Y = "0"*(n-len(Y)) + Y 
    
    carry = 0
    result = ""
    isneg = False
    if X < Y:
        X, Y = Y, X
        isneg = True
    for i in range(n-1,  -1 , -1):
        substraction = int(X[i]) - int(Y[i]) - carry
        if substraction < 0:
            carry = 1
            substraction += base
        else:
            carry = 0
        result = str(substraction) + result
    for i in range(len(result)):
        if result[i] != "0":
            result = result[i:]
            break
    return ("-" + result) if isneg else result 

def multiplySingleBit(X, Y, base):
    product = ""
    pro = int(X) * int(Y)
    carry = pro // base
    product = str(pro % base)
    if carry > 0:
         product = str(carry) + product
    return product
def karatsubaMultiplication(X, Y, base):
    n = max(len(X), len(Y))
    if len(X) < n:
        X = "0"*(n-len(X)) + X
    else:
        Y = "0"*(n-len(Y)) + Y 
    if n == 0: return '0'
    if n == 1: return multiplySingleBit(X, Y, base)
    fh = n // 2
    sh = n - fh

    Xf = X[:fh]
    Xs = X[fh:]

    Yf = Y[:fh]
    Ys = Y[fh:]

    P1 = karatsubaMultiplication(Xf,Yf,base)
    P3 = karatsubaMultiplication(Xs, Ys, base)
    P2 = karatsubaMultiplication(intAddition(Xf, Xs, base), intAddition(Yf, Ys, base), base)

    S1 = P1 + "0"*2*sh
    S2 = intSubstraction(P2, intAddition(P1, P3, base), base) + "0"*sh
    S3 = P3
    if (S2[0] == '-'):
        result = intSubstraction(intAddition(S1, S3, base), S2[1:], base)        
    else:
        result = intAddition(intAddition(S1, S2, base),S3, base)
    return result
if __name__ == '__main__':
    args = input("Enter numbers: ")
    args = args.split()
    if len(args) != 3:
        print("Invalid arguments. You should enter two int and it base.\n")
    X = args[0]
    Y = args[1]
    base = int(args[2])
    sumResult = intAddition(X, Y, base)
    product = karatsubaMultiplication(X, Y, base)
    print(sumResult, " ", product)