# _*_ coding:utf-8 _*_

from flask import Blueprint     #导入蓝图

home = Blueprint("home",__name__) #创建蓝图

import app.home.views #导入视图

