import pay
import update
import management
import gmanagement
import ep
import phone

with open('D:/project/cabaco.txt','r') as f:
    tabaco = {}
    day_sale = {'card':0,"cash":0}

    while True :
        tmp_dic = {}
        line = f.readline()
        line = line.rstrip('\n')

        if(line==""):
            break

        st_list = line.split('/')

        tmp_dic['제품명'] = st_list[1]
        tmp_dic['브랜드'] = st_list[2]
        tmp_dic['가격'] = int(st_list[3])
        tmp_dic['재고'] = int(st_list[4])

        tabaco[st_list[0]] = tmp_dic
        day_sale[st_list[0]] = 0

    while True :
        print("*"*30)
        print("1. 결제 \n2.물품 관리\n3.매출 관리\n4.종료")
        print("*"*30,end='\n')
        select_num = input('선택 : ')

        if select_num == '1' :
            tmp = pay.main(tabaco)
            update.main(tabaco,tmp,day_sale)

        elif select_num == '2' :
            gmanagement.main(tabaco)

        elif select_num == '3' :
            management.main(tabaco,day_sale)

        elif select_num == '4' :
            ep.main(tabaco,day_sale)
            break

        else :
            print("다시 선택 하세요\n")