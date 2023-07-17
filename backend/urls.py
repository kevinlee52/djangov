# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name ：     urls.py
   Description :
   Author :         milli
   date ：          2022-05-23
-------------------------------------------------
"""
from django.urls import path

from backend.views import show_testcases_gp1100x, show_testcases_gs4227_xgs

urlpatterns = [
    # path("add_testcase", add_testcase, ),
    # path("show_testcases", show_testcases, ),
    path("show_testcases_gp1100x", show_testcases_gp1100x, ),
    path("show_testcases_gs4227_xgs", show_testcases_gs4227_xgs, ),
]
