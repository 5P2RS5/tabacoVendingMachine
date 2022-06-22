wdef check_tabaco(tabaco) :

    tabaco_key = list(tabaco.keys())
    print("*"*30)
    print("현재 재고 현황 \n")
    print("*"*30,end='\n')

    for i in tabaco_key :

        print(tabaco[i]['제품명']," : ",tabaco[i]["재고"])
    print("*"*30,end='\n')

def check_order(tabaco):
    tabaco_key = list(tabaco.keys())
    count = 0
    order_list = {}
    print("*"*30)
    for i in tabaco_key :
        if tabaco[i]['재고'] < 30 :
            print(tabaco[i]['제품명'],'의 재고가',tabaco[i]['재고'],'개 입니다. 재고를 채워주세요')
            order_list[i] = tabaco[i]
            count += 1
    if count == 0 :
        print("재고를 채울 담배가 없습니다.\n")
        print("*"*30,end='\n')

    else :
        print("*"*30)
        select = input("1. 발주 / 2. 취소 : ")
        print("*"*30,end='\n')

        if select == '1' :

            for i in list(order_list.keys()) :
                if i not in list(tabaco.keys()) :
                    continue

                tabaco[i]['재고'] = 200
            print("*"*30)
        elif select == '2':
            print("취소하였습니다.")

        else :
            print("잘못 입력하셨습니다. 다시 입력해주세요.")
        print("*"*30,end='\n')

def main(tabaco) :
    while True :
        print("*"*30)
        select = input("1. 재고확인 / 2.채울필요 있는 재고 확인 / 3. 종료 : ")
        print("*"*30,end='\n')

        if select == '1' :
            check_tabaco(tabaco)
        elif select == '2' :
            check_order(tabaco)
        elif select == '3' :
            break
        else :
            print("잘못입력하셨습니다. 다시 입력해주세요")
            print("*"*30,end='\n')
