if __name__ == "__main__":
    digits = list(map(int,input().split()))
    print(list(str(i) for i in str(int(''.join([str(i) for i in digits]))+1)))