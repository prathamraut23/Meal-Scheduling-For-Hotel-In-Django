from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from Manager.models import *
from datetime import date,datetime
# import pywhatkit

global cusname 
global cusmember 
global cusphone
global custime 

def frontpage(request):
    if request.user.is_authenticated:
        return redirect('mfront')
    return render(request, 'Mainweb/frontpage.html')

def booking(request):
    return render(request, 'Mainweb/booking.html')

def meal(request):
    global cusname, cusmember, cusphone, custime
    cusname = request.POST['fullname']
    cusmember = request.POST['member']
    cusphone = request.POST['phone']
    custime = request.POST['time']

    if len(cusphone)!=10:
        messages.error(request,"Phone number is invalid")
        return render(request, 'Mainweb/booking.html')

    Breakfast = menu_card.objects.filter(dish_category = "breakfast")
    Brev = menu_card.objects.filter(dish_category = "beverages")
    Roti = menu_card.objects.filter(dish_category = "roti")
    Sabji = menu_card.objects.filter(dish_category = "sabji")

    params ={}
    params['Breakfast'] = Breakfast
    params['Brev'] = Brev
    params['Roti'] = Roti
    params['Sabji'] = Sabji
    return render(request, 'Mainweb/meal.html',params)

def order(request):
    global cusname
    global cusphone
    global cusmember
    global custime
    allitems = menu_card.objects.all()
    alldish = []
    allprice = []
    allquantity = []
    dishtotal = []
    total = 0
    offer =""
    for i in allitems:
        quantity = (request.POST[i.image])
        if len(quantity)!=0:
            alldish.append(i.dish_name)
            allprice.append(i.dish_price)
            allquantity.append(quantity)

    for i in range(len(allprice)):
        total+=int(allprice[i])*int(allquantity[i])
        dishtotal.append(int(allprice[i])*int(allquantity[i]))

    day = datetime.now() 
    if str(day.strftime("%A")) == "Sunday":
        total = 0.9*total
        offer += "10% off On Sunday" 

    x=alldish.copy()
    y=allprice.copy()
    z=allquantity.copy()
    u=dishtotal.copy()

    n = len(x)
    bill ={
        'display_dish' : x,
        'display_price' : y,
        'display_quantity' : z,
        'display_dishtotal' : u,
        'display_total' : total,
        'offer' : offer,
        'nn' : range(n),

    }

    print(bill)
    alldish =','.join(alldish)
    allprice =','.join(allprice)
    allquantity =','.join(allquantity)

    myorder = Order(fullname=cusname, phoneno = cusphone, orderdate=date.today(), sheduletime=custime,dish_list=alldish,quantity_list=allquantity,price_list=allprice,members=cusmember,total=total)

    myorder.save()
    # print(cusname)
    # wattsapp messaging
    # max_len=0
    # for i in alldish:
    #     if len(i)>max_len:
    #         max_len=len(i)
    # st='Dish'+"            "+"Quantity"+"    "+"Price\n"
    # for i in range(len(alldish)):
    #     st+=str(alldish[i])+"     "+str(allquantity[i])+"   "+str(allprice[i])+"\n"
    # st+="Total="+str(total)
    # p_string="+91"+str(cusphone)
    # p_string="+91"+str(cusphone)
    # l=str(datetime.now().time()).split(":")
    # pywhatkit.sendwhatmsg(p_string,st,int(l[0]),int(l[1])+4)
    # -------------------------------------------



    # wattsapp messaging
    # max_len=0
    # for i in alldish:
    #     if len(i)>max_len:
    #         max_len=len(i)
    # st='Dish'+"            "+"Quantity"+"    "+"Price\n"
    # for i in range(len(dish_l)):
    #     st+=str(dish_l[i])+"     "+str(dish_q[i])+"   "+str(dish_p[i])+"\n"
    # st+="Total="+str(sum)
    # p_string="+91"+str(dic['phoneno'])
    # l=str(datetime.now().time()).split(":")
    # pywhatkit.sendwhatmsg(p_string,st,int(l[0]),int(l[1])+1)
    # -------------------------------------------

    return render(request, 'Mainweb/bill.html', bill)
