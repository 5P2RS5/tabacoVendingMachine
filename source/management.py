import datetime as t

def month_margin(month) :

    with open ("D:/project/{}월 매출.txt".format(month),'r') as f :
        tmp_dic = {}
        tmp_month = {}

        while True :
            line = f.readline()
            if line == '' :
                break
            line = line.rstrip('\n')
            tmp_list = line.split('/')
            tmp_month[tmp_list[0]] = int(tmp_list[1])

        tmp_dic[month] = tmp_month

        return tmp_dic

def main(tabaco,day_sale) :
    now = t.datetime.now()

    month = now.month
    day = now.day

    if month < 10 :
        month = '0'+str(month)

    else :
        month = str(month)

    if day < 10 :
        day = '0' + str(day)

    else :
        day = str(day)

    while True :
        try :
            print("*"*30)
            s_num = int(input("1. 일 매출 / 2. 월 매출 / 3. 종료 : "))
            print("*"*30,end='\n')
        except :
            continue

        if s_num == 1:
            print(" 일 매 출")
            print("*"*30)
            for i in day_sale.keys():
                if i == 'card' or i == 'cash' :
                    continue
                else :

                    print("{}. {} : {}".format(i,tabaco[i]['브랜드'],day_sale[i]))

            print("{} : {}\n{} : {}".format('cash',day_sale['cash'],'card',day_sale['card']))
            print("*"*30,end='\n')
            print()

        elif s_num == 2 :

            dic = month_margin(month)
            tmp_dic = dic[month]
            print(" 월 매 출")
            print("*"*30)
            for i in tmp_dic.keys() :
                if i == 'card' or i == 'cash' :
                    continue
                else :
                    print("{}. {} : {}".format(i,tabaco[i]['브랜드'],tmp_dic[i]))

                print("*"*30,end ='\n')
                print("{} : {} \n{} : {}\n".format("cash",tmp_dic['cash'],'card',tmp_dic['card']))
                print("*"*30,end="\n")
                print()

        elif s_num == 3 :
            break

        else :
            print("*"*30)
            print("다시 입력하세요")
            print("*"*30,end='\n')
            print()

