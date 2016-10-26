#!/usr/bin/python
from  datetime import date

name=raw_input('please input your name: ')
print 'hello', name
age=raw_input('please input your age: ')
print 'your birth year: ', date.today().year-int(age)
