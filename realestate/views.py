from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from realestate.forms import EstateForm, LandForm, HouseForm, CustomerForm, PaymentForm, TitleForm
from realestate.models import Customer, Estate, House, Land, Payment, Title

from realestate.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def getestates(request):
    estates = Estate.objects.all()

    serialized_data = EstateSerializer
    (estates, many==True)
    return Response(serialized_data.data)

@api_view(["GET"])
def gethouses(request):
    houses = House.objects.all()

    serialized_data = HouseSerializer
    (houses, many==True)
    return Response(serialized_data.data)

@api_view(["GET"])
def getlands(request):
    lands = Land.objects.all()

    serialized_data = LandSerializer
    (lands, many==True)
    return Response(serialized_data.data)

@api_view(["GET"])
def getcustomers(request):
    customers = Customer.objects.all()

    serialized_data = CustomerSerializer
    (customers, many==True)
    return Response(serialized_data.data)

@api_view(["GET"])
def getpayments(request):
    payments = Payment.objects.all()

    serialized_data = PaymentSerializer
    (payments, many==True)
    return Response(serialized_data.data)

@api_view(["GET"])
def gettitles(request):
    titles = Title.objects.all()

    serialized_data = TitleSerializer
    (titles, many==True)
    return Response(serialized_data.data)

@login_required
def index_view(request):
    return render(request, 'index.html')

@login_required
def realestate_list_view(request):
    return render(request, 'realestate_list.html')

@login_required
def add_estate_view(request):
    message = ''
    if request.method == "POST":
        estate_form = EstateForm(request.POST)

        if estate_form.is_valid():
            estate_form.save()

            messages.success(request, "Estate Added Successfully")
    else:
        estate_form = EstateForm()

    estates = Estate.objects.all()

    context = {
        'form':estate_form,
        'msg': message,
        'estate': estates
    }

    return render(request, "add_estate.html", context)

@login_required
def add_land_view(request):
    message = ''
    if request.method == "POST":
        land_form = LandForm(request.POST)

        if land_form.is_valid():
            land_form.save()

            messages.success(request, "Land Added Successfully")
    else:
        land_form = LandForm()

    lands = Land.objects.all()

    context = {
        'form':land_form,
        'msg': message,
        'land': lands
    }

    return render(request, "add_land.html", context)

@login_required
def add_house_view(request):
    message = ''
    if request.method == "POST":
        house_form = HouseForm(request.POST, request.FILES)

        if house_form.is_valid():
            house_form.save()

            messages.success(request, "House Added Successfully")
    else:
        house_form = HouseForm()

    houses = House.objects.all()

    context = {
        'form':house_form,
        'msg': message,
        'house': houses
    }

    return render(request, "add_house.html", context)

@login_required
def add_customer_view(request):
    message = ''
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)

        if customer_form.is_valid():
            customer_form.save()

            messages.success(request, "Customer Added Successfully")
    else:
        customer_form = CustomerForm()

    customers = Customer.objects.all()

    context = {
        'form':customer_form,
        'msg': message,
        'customer': customers
    }

    return render(request, "add_customer.html", context)

@login_required
def add_payment_view(request):
    message = ''
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)

        if payment_form.is_valid():
            payment_form.save()

        messages.success(request, "Payment Added Successfully")
    else:
        payment_form = PaymentForm()

    payments = Payment.objects.all()

    context = {
        'form':payment_form,
        'msg': message,
        'payment': payments
    }

    return render(request, "add_payment.html", context)

@login_required
def add_title_view(request):
    message = ''
    if request.method == "POST":
        title_form = TitleForm(request.POST , request.FILES)

        if title_form.is_valid():
            title_form.save()

            messages.success(request, "Title Added Successfully")
    else:
        title_form = TitleForm()

    title = Title.objects.all()

    context = {
        'form':title_form,
        'msg': message,
        'title': title
    }

    return render(request, "add_title.html", context)

@login_required
def edit_estate_view(request, estate_id):
    estate = Estate.objects.get(id=estate_id)
    message = ""

    if request.method == "POST":
        estate_form = EstateForm(request.POST, instance=estate)

        if estate_form.is_valid():
            estate_form.save()
            messages.success(request, "Changes saved Successfully!")
            return redirect(add_estate_view)
        else:
            messages.danger(request, "Form has Invalid data!")
    else:
        estate_form = EstateForm(instance=estate)
    
    context = {
        'form': estate_form,
        'estate': estate,
        'message': message,
    }

    return render(request, 'edit_estate.html', context)

@login_required
def edit_land_view(request, land_id):
    land = Land.objects.get(id=land_id)
    message = "" 

    if request.method == "POST":
        land_form = LandForm(request.POST, instance=land)

        if land_form.is_valid():
            land_form.save()
            messages.success(request, "Changes saved Successfully!")
            return redirect(add_land_view)
        else:
            messages.danger(request, "Form has Invalid data!")
    else:
        land_form = LandForm(instance=land)

    context = {
        'form': land_form,
        'land': land,
        'message': message,
    }

    return render(request, 'edit_land.html', context)

@login_required
def edit_house_view(request, house_id):
    house = House.objects.get(id=house_id)
    message = ""

    if request.method == "POST":
        house_form = HouseForm(request.POST, instance=house)

        if house_form.is_valid():
            house_form.save()
            messages.success(request, "Changes saved Successfully!")
            return redirect(add_house_view)
        else:
            messages.danger(request, "Form has Invalid data!")
    else:
        house_form = HouseForm(instance=house)
    
    context = {
        'form': house_form,
        'house': house,
        'message': message,
    }

    return render(request, 'edit_house.html', context)

@login_required
def edit_customer_view(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    message = ""

    if request.method == "POST":
        customer_form = CustomerForm(request.POST, instance=customer)

        if customer_form.is_valid():
            customer_form.save()
            messages.success(request, "Changes saved Successfully!")
            return redirect(add_customer_view)
        else:
            messages.danger(request, "Form has Invalid data!")
    else:
        customer_form = CustomerForm(instance=customer)
    
    context = {
        'form': customer_form,
        'customer': customer,
        'message': message,
    }

    return render(request, 'edit_customer.html', context)

@login_required
def edit_payment_view(request, payment_id):
    payment = Payment.objects.get(id=payment_id)
    message = ""

    if request.method == "POST":
        payment_form = PaymentForm(request.POST, instance=payment)

        if payment_form.is_valid():
            payment_form.save()
            messages.success(request, "Changes saved Successfully!")
            return redirect(add_payment_view)
        else:
            messages.danger(request, "Form has Invalid data!")
    else:
        payment_form = PaymentForm(instance=payment)
    
    context = {
        'form': payment_form,
        'payment': payment,
        'message': message,
    }

    return render(request, 'edit_payment.html', context)

@login_required
def edit_title_view(request, title_id):
    title = Title.objects.get(id=title_id)
    message = ""

    if request.method == "POST":
        title_form = TitleForm(request.POST, instance=title)

        if title_form.is_valid():
            title_form.save()
            messages.success(request, "Changes saved Successfully!")
            return redirect(add_title_view)
        else:
            messages.danger(request, "Form has Invalid data!")
    else:
        title_form = TitleForm(instance=title)
    
    context = {
        'form': title_form,
        'title': title,
        'message': message,
    }

    return render(request, 'edit_title.html', context)

@login_required
def delete_estate_view(request, estate_id):
    estate = Estate.objects.get(id=estate_id)

    estate.delete()

    messages.success(request, "Estate Deleted!")
    
    return redirect(add_estate_view)

@login_required
def delete_land_view(request, land_id):
    land = Land.objects.get(id=land_id)

    land.delete()

    messages.success(request, "Land Deleted!")

    return redirect(add_land_view)

@login_required
def delete_house_view(request, house_id):
    house = House.objects.get(id=house_id)

    house.delete()

    messages.success(request, "House Deleted!")

    return redirect(add_house_view)

@login_required
def delete_customer_view(request, customer_id):
    customer = Customer.objects.get(id=customer_id)

    customer.delete()

    messages.success(request, "Customer Deleted!")

    return redirect(add_customer_view)

@login_required
def delete_payment_view(request, payment_id):
    payment = Payment.objects.get(id=payment_id)

    payment.delete()

    messages.success(request, "Payment Deleted!")

    return redirect(add_payment_view)

@login_required
def delete_title_view(request, title_id):
    title = Title.objects.get(id=title_id)

    title.delete()

    messages.success(request, "Title Deleted!")

    return redirect(add_title_view)

def sign_up_view(request):
     
    if request.method == "POST":
        sign_up_form = UserCreationForm(request.POST)

        if sign_up_form.is_valid():
            sign_up_form.save()
            message = 'User created successfully'
        else:
            message = 'Something went wrong'
    else:
        sign_up_form = UserCreationForm()
    
    context ={
        'form': sign_up_form,
    }

    return render(request, 'registration/sign_up.html', context)