if __name__ == "__main__":
    digits = list(map(int,input().split()))
    son = 0
    son_len = len(digits)-1
    for i in digits:
        son+= i*pow(10,son_len)
        son_len-=1
    son+=1
    digits.clear()
    for i in str(son):
        digits.append(i)
    print(digits)