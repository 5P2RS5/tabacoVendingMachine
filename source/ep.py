import management
import datetime as t

def re_stock(tabaco) :
    with open ("D:/project/cabaco.txt","w") as f :

        for i in tabaco.keys() :
            f.write("{}/{}/{}/{}/{}\n".format(i,tabaco[i]['브랜드'],tabaco[i]['제품명'],tabaco[i]['가격'],tabaco[i]['재고']))

def make_day_sale(month,day,day_sale):

    with open ("D:/project/"+month+day+"매출.txt",'w') as f :

        for i in day_sale.keys() :
            f.write("{}/{}\n".format(i,day_sale[i]))

def make_month_sale(month,day_sale):
    tmp_dic = management.month_margin(month)
    month_sale = tmp_dic[month]
    f_dic = {}

    for i in month_sale.keys() :
        total = month_sale[i] + day_sale[i]
        f_dic[i] = total

    with open("D:/project/"+month+"월 매출.txt",'w') as f :

        for i in f_dic.keys() :
            f.write("{}/{}\n".format(i,f_dic[i]))

def main(tabaco,day_sale) :

    now = t.datetime.now()
    month = now.month
    day = now.day

    if month < 10 :
        month = '0'+str(month)
    else :
        month = str(month)

    if day < 10 :
        day = '0'+str(month)
    else :
        day = str(day)

    re_stock(tabaco)
    make_day_sale(month,day,day_sale)
    make_month_sale(month,day_sale)