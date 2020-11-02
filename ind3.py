#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Дано натуральное число . Получить все его натуральные делители.

x = int(input("Chislo"))
a = int(1)
while a<=x:
    if x%a==0:
        print("{0}".format(a))
        a = int(a+1)
    else:
        a = int(a+1)