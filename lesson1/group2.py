def fun():
    s=input("Enter the string: ") # Hello World!j
    k = input("Enter the key: ") #keykeykeykeyk Shjk&98
    j = 0
    result = ""
    for i in range(len(s)):
        si = (ord(s[i]))
        if j<len(k):
            ki = (ord(k[j]))
            res = ((si + ki) % 128)
            if res<=32: res+=32
            result+=chr(res)
            j+=1
        else:
            j=0
            ki = (ord(k[j]))
            res = ((si + ki) % 128)
            if res <= 32: res += 32
            result += chr(res)
            j+=1
    print(result)
    print(len(result),len(s))
fun()


    # l 3 k
    # j 2 e
    # i 1 y
    # h 1 k
    # lst = list()
    # for i in s:
    #     count = 0
    #     for j in s:
    #         if i==j:
    #          count+=1
    #     if i not in lst:
    #         lst.append(i)
    #         print(i,count)


