# _*_ coding:utf-8 _*_

from flask import Blueprint     #������ͼ

home = Blueprint("home",__name__) #������ͼ

import app.home.views #������ͼ

