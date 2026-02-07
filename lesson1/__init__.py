def lesson():
    s= input("Enter the string: ") # Hello
    key = input("Enter the key: ") # keyke
    result = ""
    j =0
    for i in s:
        c=''
        if j<len(key):
            c= chr((ord(i) + ord(key[j])+32)%127)
            j += 1
        if j>=len(key):
            j=0
            c = chr((ord(i) + ord(key[j])+32) % 127)
            j+=1
        result+=c
    print(result)


# def lesson():
#     a= input("Enter a: ") # test167test !
#     c = input("Enter c: ")
#     l1uniqe = []
#     l2uniqe = []
#     d1stats = dict()
#     d1stats = dict()
#     print(L)
#     for f in L:
#         for b in f:
#             if b not in l1uniqe:
#                 l1uniqe.append(b)
#
#
#
#     for i in l:
#         count = 0
#         for j in a:
#             if i == j:
#                 count += 1
#         d1[i] = count
#     print(d1)
#         print(a)



 # for i in a:
 #       count = 0
 #       for j in a:
 #           if i == j:
 #               count += 1
 #       l.append(i)
 #       print(i + ": " + str(count))
 #       a = a.replace(i, '')
 #       # print(a)

lesson()