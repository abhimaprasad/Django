from django.shortcuts import render, redirect
from accounts.models import Account

# Create your views here.
from accounts.forms import AccountCreateForm,LoginForm,BalanceCheckForm,TransferAmountForm

def Transfer(request):
    form=TransferAmountForm
    context={}
    context["form"]=form
    if (request.method == 'POST'):
        form = TransferAmountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("balance")

    return render(request, "accounts/transferamount.html",context)

def createAccount(request):
    templatename="accounts/accountcreate.html"
    form=AccountCreateForm()
    context={}
    context["form"]=form
    if(request.method=='POST'):
        form=AccountCreateForm(request.POST)
        if form.is_valid():
            personname = form.cleaned_data.get("personname")
            accno = form.cleaned_data.get("accno")
            acctype =form.cleaned_data.get("acctype")
            balance =form.cleaned_data.get("balance")
            phonenumber = form.cleaned_data.get("phonenumber")
            mpin = form.cleaned_data.get("mpin")
            obj=Account(personname=personname,accno=accno,acctype=acctype,balance=balance,phonenumber=phonenumber,mpin=mpin)
            obj.save()
            return render(request, templatename, context)


    return render(request,templatename,context)


def loginView(request):
    form=LoginForm
    context={}
    context["form"]=form
    if (request.method == 'POST'):
        form = LoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get("phonenumber")
            pin = form.cleaned_data.get("mpin")
            try:
                object=Account.objects.get(phonenumber=phone)
                if((object.phonenumber==phone))&((object.mpin==pin)):
                    print("user is exist")
                    return render(request,"accounts/accounthomepage.html")
            except Exception as e:
                print("invalid credentials")
                context["form"]=form
                return render(request,"accounts/login.html", context)

    return render(request, "accounts/login.html", context)

def balanceEnq(request):
    form=BalanceCheckForm()
    context={}
    context["form"]=form
    if (request.method == 'POST'):
        form = BalanceCheckForm(request.POST)
        if form.is_valid():
            mpin = form.cleaned_data.get("mpin")
            try:
                object=Account.objects.get(mpin=mpin)
                context["balance"]=object.balance
                return render(request, "accounts/checkbalance.html", context)
            except Exception as e:
                context["form"]=form
                return render(request, "accounts/checkbalance.html", context)

                return render(request,"accounts/login.html", context)

    return render(request,"accounts/checkbalance.html",context)