import datetime as t
from datetime import datetime
import phone

def Choice_gender(guest_log) :
    print("*"*30)
    gender = input("\n성별 입력\n1. 남성 / 2. 여자 :")
    print("*"*30)

    if gender == '1' :
        guest_log["gender"]= 'man'
    elif gender == '2' :
        guest_log["gender"]= 'woman'
    else :
        return True

    return False

def age(guest_log) :
    print("*"*30)
    years=int(input("태어난 년도 입력 :"))
    months=int(input("태어난 월 입력 :"))
    days=int(input("태어난 일 입력 :"))
    print("*"*30)

    todayyear = datetime.today().year

    if (todayyear-years) >= 20 :
        print("성인입니다. 다음 인증을 진행해 주세요.")
    else :
        return True

    return False

def certification(guest_log) :
    print("*"*30)
    certification_num=int(input("본인 명의의 휴대폰 인증번호를 입력하세요 :"))
    print("*"*30)

    with open('phone.txt','r')  as f :
        check_number=f.readline()
    if int(check_number) == certification_num :
        print("인증이 완료되었습니다.")
    else :
        return True
    return False

def select_tabaco(tmp,tabaco) :
    tmp_list = list(tabaco.keys())

    print("*"*30)
    for i in tmp_list :
        print("\n{}.\t{}\t{}\t/금액\t:\t{}".format(i,tabaco[i]['브랜드'],tabaco[i]['제품명'],tabaco[i]['가격']))

    print("*"*30)

    s_num = 0
    while True :
        s_num = input("\n구매할 담배 번호 : ")
        if s_num in tabaco :
            break

    while True :
        try :
            count = int(input("\n구매할 담배 수량 : "))
            break
        except :
            continue

    while True :
        print("*"*30)
        print("제품명: {} / 수량 : {}".format(tabaco[s_num]['브랜드'],count))
        print("*" * 30)
        num = input("1. 확인 / 2. 취소 : ")
        print("="*30,end='\n')
        if num == '1':
            tmp[s_num] = count
            return False
        elif num == '2' :
            return True

def flow_Choice(guest_log,tabaco) :
    boolean = True
    service = 0
    tmp_tabaco = guest_log['판매']

    while boolean :
        boolean = select_tabaco(tmp_tabaco,tabaco)

    guest_log['판매']=tmp_tabaco

    while True :
        print("*"*30)
        end_flag = input("1. 다음 / 2. 다른 담배 선택 : ")
        print("*"*30,end="\n")

        if end_flag == '1' :
            return False
        elif end_flag == '2' :
            return True

def receipt(tmp_dic,tabaco) :
    total = 0
    tmp_list = list(tmp_dic.keys())
    sale_dic = {}
    count = 0
    for i in tmp_list :
        tmp = {}
        count += 1
        t = tabaco[i]['가격']*tmp_dic[i]
        total += t
        tmp['브랜드'] = tabaco[i]['브랜드']
        tmp['수량'] = tmp_dic[i]
        tmp['총금액'] = t
        sale_dic[count] = tmp

    return sale_dic,total

def select_payment():
    print("*"*30)
    payment = input("1. 카드 / 2. 현금 : ")
    print("*"*30,end='\n')
    tmp=0

    if payment == '1' :
        tmp = 1
    elif payment == '2' :
        tmp = 2
    else :
        return True, tmp

    return False, tmp


def select_card(sale_dic,total,guest_log) :
    print()
    print()
    print("========== 영수증 ==========")
    print("제품명\t수량\t금액")
    print()

    for i in sale_dic.keys():
        print("{}\t{}\t{}".format(sale_dic[i]['브랜드'],sale_dic[i]['수량'],sale_dic[i]['총금액']))

    print()
    print("*" * 30, end='\n')
    print("\ntotal : {}".format(total))
    print("*" * 30, end='\n')

    tmp = input("1. 확인 / 2. 취소 : ")

    print("*" * 30, end='\n')

    if tmp == '1' :
        print("결제 완료")
        print("*"*30)
        guest_log["결제"]= "card"
        guest_log["판매금액"] = total
        guest_log["거스름돈"] = None
        return False

    elif tmp == '2' :
        print("결제 취소")
        print("*"*15)
        return True

    else:
        print("다시 입력하세요")
        return True

def select_cash(sale_dic,total,guest_log) :
    print()
    print()
    print("========== 영수증 ==========")
    print("제품명\t수량\t금액")
    print()

    for i in sale_dic.keys():
        print("{}\t{}\t{}".format(sale_dic[i]['브랜드'],sale_dic[i]['수량'],sale_dic[i]['총금액']))

    print()
    print("*"*30,end='\n')
    print("\ntotal : {}".format(total))
    print("*"*30,end='\n')

    while True :
        tmp = input("\n받은 돈 : ")

        try :
            tmp = int(tmp)
            break
        except :
            continue

    if tmp - total < 0 :
        print("*"*30,end='\n')
        print("돈이 부족합니다")
        print("*"*30,end='\n')
        return True
    else :
        print("*"*30,end='\n')
        print("결제완료")
        print("*" * 30, end='\n')
        print("잔돈 : {}원".format(tmp-total))
        print("*" * 30, end='\n')
        guest_log["결제"]="cash"
        guest_log["판매금액"] = total
        guest_log["거스름돈"] = tmp-total
        return False

def flow_payment(guest_log,tabaco) :

    boolean = True
    select_num = 0
    tmp_tabaco=guest_log["판매"]
    sale_dic, total = receipt(tmp_tabaco,tabaco)

    while boolean :
        boolean, select_num = select_payment()

    boolean =True
    if select_num == 1 :
        while boolean :
            boolean = select_card(sale_dic,total,guest_log)
    elif select_num == 2 :
        while boolean :
            boolean = select_cash(sale_dic,total,guest_log)

    return False

def main(tabaco) :

    now = t.datetime.now()
    guest_log = {'판매':{}}
    print("*"*30)
    print(now)
    print("*"*30,end='\n')
    while Choice_gender(guest_log):
        print("\n다시 입력하세요")

    while age(guest_log):
        print("\n미성년자입니다.")

    while certification(guest_log):
        print("\n잘못된 인증입니다. 다시 시도해 주세요")

    while flow_Choice(guest_log,tabaco) :
        continue

    while flow_payment(guest_log,tabaco) :
        continue

    now_time = '{}-{}-{}/{}:{}'.format(now.year,now.month,now.day,now.hour,now.minute)

    guest_log["일시"]=now_time

    print("*"*30,end='\n')
    print()

    return(guest_log)