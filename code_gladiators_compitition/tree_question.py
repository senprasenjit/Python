def main():
    input_nodes = input()
    if (1 <= input_nodes <= 100):
        inp = raw_input()
        A1 = inp.split(' ')
        Ai = []
        condi = True
        count=0
        for x2 in A1:
            if (-1 <= int(x2) <= (input_nodes - 1)):
                Ai.append(int(x2))
            else:
                condi = False
                break
        if condi:
            remove = input()
            if (0 <= remove <= (input_nodes - 1)):

                def func_del(l1):
                    for y in range(len(l1) - 1, -1, -1):
                        x = l1[y]

                        if lis[x] == []:

                            del lis[x]
                        else:
                            func_del(lis[x])



                            # input() #[-1,0,0,0,1,1,3,3,3,2,9,9,6,7,8]

                # for x in range(0,input_nodes):
                #    Ai.append(input("value of Ai"))

                # -1 0 0 0 1 1 3 3 3 2 9 9 6 7 8


                lis = []
                for y in range(0, input_nodes):
                    n = 0
                    lis1 = []
                    for x in range(0, input_nodes):
                        if Ai[x] == y:
                            if x == remove:
                                continue
                            else:
                                lis1.append(x)
                    lis.append(lis1)
                # print lis
                b = lis[remove]

                func_del(lis[remove])
                if remove<=len(lis):
                    del lis[remove]

                if len(lis)==1 and lis[0]==[]:
                    print '0'
                else:
                    print lis.count([])
            '''else:
                raise Exception('This is the exception you expect to handle')
        else:
            raise Exception('This is the exception you expect to handle')
    else:
        raise Exception('This is the exception you expect to handle')'''


main()