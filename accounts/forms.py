
from django import forms
from django.forms import ModelForm
from accounts.models import TransferDetails
from accounts.models import Account


class AccountCreateForm(forms.Form):
    personname = forms.CharField(max_length=150)
    accno = forms.CharField(max_length=18)
    acctype = forms.CharField(max_length=50)
    balance = forms.IntegerField()
    phonenumber = forms.CharField(max_length=12)
    mpin = forms.CharField(max_length=4)


class LoginForm(forms.Form):
    phonenumber = forms.CharField(max_length=15)
    mpin = forms.CharField(max_length=4)


class BalanceCheckForm(forms.Form):
    mpin = forms.CharField(max_length=4)
    def clean(self):
        cleaned_data = super().clean()
        mpin = cleaned_data.get("mpin")
        try:
            object = Account.objects.get(mpin=mpin)
            if(object):
                pass
        except:
            msg="you are provided invalid pin"
            self.add_error("mpin",msg)





class AccountCreateForm(forms.Form):
    personname = forms.CharField(max_length=150)
    accno = forms.CharField(max_length=18)
    acctype = forms.CharField(max_length=50)
    balance = forms.IntegerField()
    phonenumber = forms.CharField(max_length=12)
    mpin = forms.CharField(max_length=4)


class TransferAmountForm(ModelForm):
    class Meta:
        model = TransferDetails
        fields = "__all__"
    def clean(self):
        cleaned_data = super().clean()
        mpin = cleaned_data.get("mpin")
        acno = cleaned_data.get("accno")
        amount = cleaned_data.get("amount")
        print(mpin, ",", acno, ",", amount)
        try:
            object = Account.objects.get(mpin=mpin)

            if(object):
                if(object.balance<amount):
                    msg = "insuffient balance"
                    self.add_error("amount", msg)
            pass
        except:
            msg="you are provided invalid pin"
            self.add_error("mpin",msg)
        try:
            object = Account.objects.get(accno=acno)

            if (object):
                pass
        except:
            msg = "you are provided invalid account number"
            self.add_error("accno", msg)


