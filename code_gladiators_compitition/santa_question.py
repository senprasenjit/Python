import itertools
def main():
    N_M = raw_input()
    b = N_M.split(' ')
    number_of_houses = int(b[0])
    santa_days = int(b[1])
    if 1<=number_of_houses<=100000 and 1<=santa_days<=100000:
        connection_of_house = []
        path_followed =[]
        master_list=[]
        counter=0
        for x in range(0,(number_of_houses-1)):
                house_connect = raw_input()
                house_no = house_connect.split(' ')
                house_connect=[int(house_no[0]),int(house_no[1])]
                if not (1<=house_connect[0]<=number_of_houses) and ((1<=house_connect[1])<=number_of_houses):
                    counter=counter +1
                reverse_house_connect=[int(house_no[1]),int(house_no[0])]
                connection_of_house.append(list(house_connect))
                master_list.append(list(house_connect))
                master_list.append(list(reverse_house_connect))

        for y in range(0,int(santa_days)):
                santa_visit = raw_input()
                A_B = santa_visit.split(' ')
                house_connect=[int(A_B[0]),int(A_B[1])]
                if not (1<=house_connect[0]<=number_of_houses) and (1<=house_connect[1]<=number_of_houses):
                    counter=counter +1

                path_followed.append(house_connect)
        if counter==0:
            def find_next_house(master_list):
                master_list_1 = []
                for path in range(0,len(master_list)):
                    temp1 = master_list[path][-2:]


                    for x in range(0,len(connection_of_house)):
                        temp2=connection_of_house[x]
                        if ((temp1[-1] in temp2) and not (temp1[-2] in temp2)) :
                            temp3 = list(master_list[path])
                            if temp2[0]==temp1[-1]:
                                temp3.append(temp2[1])
                            else:
                                temp3.append(temp2[0])
                            master_list_1.append(temp3)
                return master_list_1
            gml=[]
            gml.append(master_list)

            while True:
                l= find_next_house(gml[-1])
                if l==[]:
                    break
                gml.append(l)
            gml1=[]
            for items in gml:
                for itm in items:
                    gml1.append(itm)

            path=[]
            for item in path_followed:
                start = item[0]
                end = item[1]
                for item_gml in gml1:
                    if item[0]==item_gml[0] and item[-1]==item_gml[-1]:
                        path.append(item_gml)

            #flat_list =[item for sublist in path for item in sublist]
            flat_list=list(itertools.chain.from_iterable(path))
            dic={}
            for x in range(1,int(house_no[0])+1):
                dic[x]=flat_list.count(x)
            valu= list(dic.values())
            count= max(valu)
            print count
            #end_time = time.time()
            #print 'time',end_time,start_time,end_time-start_time
main()