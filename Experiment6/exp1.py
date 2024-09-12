def foo(n, p):
    if(n==0):
        exit
    else:
        K = n%10
        n = int(n/10)
        p = p+K+n
        print("value: ",K)
        foo(n,p)


def main():
    foo(3042,0)



if __name__ == '__main__':
    main()