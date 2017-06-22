# -*- coding:utf-8 -*-
#定义现实中的功能类
class Person:

    def __init__(self,name,sex,age,fig):
        self.name = name
        self.sex = sex
        self.age = age
        self.fig = fig
    def grassland(self,fig):
        self.fig = self.fig - 200
    def practice(self,fig):
        self.fig = self.fig-100
