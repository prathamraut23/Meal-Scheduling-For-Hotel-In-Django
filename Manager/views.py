from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date,datetime
from Manager.models import *

# Create your views here.
def mfront(request):
    if request.user.is_authenticated:
        allorders = Order.objects.filter(orderdate = date.today() )
        dic={"order":allorders}
        for i  in allorders:
            i.dish_list=i.dish_list.split(',')
            i.quantity_list=i.quantity_list.split(',')
            i.price_list=i.price_list.split(',')

        return render(request, 'Manager/mfront.html',dic)
    return redirect('frontpage')


def history(request):
    if request.user.is_authenticated:
        allorders = Order.objects.all()
        historder =[]
        for i  in allorders:
            ot = datetime.strptime(i.orderdate,"%Y-%m-%d")
            today = datetime.strptime(str(date.today()),"%Y-%m-%d")
            diff  = today - ot
            if diff.days > 0 :
                i.dish_list=i.dish_list.split(',')
                i.quantity_list=i.quantity_list.split(',')
                i.price_list=i.price_list.split(',')
                historder.append(i)

        dic ={"order":historder}
        return render(request, 'Manager/mfront.html',dic)
    return redirect('frontpage')

def managerlogin(request):
    if request.user.is_authenticated:
        return redirect('mfront')
    return render(request, 'Manager/managerlogin.html')


def handlelogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['username']
        loginpassword=request.POST['password']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request,"SuccessFully Logged In")
            return redirect('mfront')
        else:
            return HttpResponse('<h1>Invalid Credentials. Please Try Again.</h1>')

    return HttpResponse("404- Not found")

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('frontpage')

def additems(request):
    if request.user.is_superuser:
        return render(request, 'Manager/additems.html')
    else:
        return redirect('frontpage')

def delitem(request):
    if request.user.is_superuser:
        allitems = menu_card.objects.all()
        params= {}
        params['allitems'] = allitems
        return render(request, 'Manager/deleteitems.html',params)
    else:
        return redirect('frontpage')

def add(request):
    if request.user.is_superuser:
        dishname = request.POST['dishname']
        dishcategory = request.POST['category']
        dishprice = request.POST['price']
        dishimage = request.FILES['images']
        # print(dish_name,dish_category,dish_price)

        newdish = menu_card(dish_name = dishname, dish_category = dishcategory, dish_price = dishprice, image = dishimage)
        newdish.save()
        return redirect('additems')
    else:
        return redirect('frontpage')

def delete(request):
    if request.user.is_superuser:
        dishname = request.POST["dish"]
        # print(dishname)

        dish = menu_card.objects.filter(dish_name = dishname)
        dish.delete()
        return redirect('delitem')
    else:
        return redirect('frontpage')


