# Enter your code here. Read input from STDIN. Print output to STDOUT

def dec2bin(num):
    push = ''
    while num > 0:
        rem = num%2
        push = (str(rem)) + push
        num /= 2
    return push

T = int(raw_input())

if 1<=T<=1000:
    for _ in xrange(T):
        n = int(raw_input())
        if 1<=n<=2**31:
            print dec2bin(n)