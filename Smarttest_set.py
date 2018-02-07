def smartSet(lst):
    bnr_lst = []
    countOne = {}
    smartset = set()
    for d in lst:
        bnr_lst.append('{0:b}'.format(int(d)))

    for d in bnr_lst:
        c = d.count('1')
        if c in countOne:
            countOne[c].append(d)
        else:
            countOne[c]=[d]

    for d in countOne.keys():
        countOne[d].sort()
        smartset.add(int(countOne[d][0],2))
    return list(smartset)



while True:
    try:
        s = raw_input()
    except EOFError:
        break


print repr(s)

#caseNo=input('Please provide the testcase numbers:')
#for d in range(caseNo):
#    inNum = input('Please provide the test length:')
#    inList = raw_input('Please provide the list')
#    lst = inList.split()
#    smartset = smartSet(lst)
#    print " ".join(str(x) for x in smartset)
#