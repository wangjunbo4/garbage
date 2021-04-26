'''
Author: Gtylcara.
Date: 2021-04-26 14:10:32
LastEditors: Gtylcara.
LastEditTime: 2021-04-26 22:09:39
'''
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

import json
import time


def login(request):

    return HttpResponse("login")


def register(request):
    
    return HttpResponse("reg")

def thirdParty(request):

    return HttpResponse("thirdparty")
