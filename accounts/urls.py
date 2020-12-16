
from django.contrib import admin
from django.urls import path,include
from .views import createAccount,loginView,balanceEnq,Transfer,AccountActivity
urlpatterns = [
    path("createAccount",createAccount,name="createaccount"),
    path("login",loginView,name="login"),
    path("balance",balanceEnq,name="balance"),
    path("transfer",Transfer,name="transfer"),
    path("history",AccountActivity,name="accountactivity"),
]
