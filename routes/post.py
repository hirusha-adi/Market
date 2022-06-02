from django.shortcuts import redirect
from flask import render_template, request, url_for, redirect, session, g
import utils.test as test
from flask_paginate import Pagination
from database.settings import Dekstop
from models.user import User


def one_post():

    data = {}
    data['title'] = "Hirusha"
    data['page_bottom'] = Dekstop.bottom
    data['page_top'] = Dekstop.top
    data['page_header'] = Dekstop.header

    # user_agent = request.headers.get('User-Agent').lower()
    # if ("iphone" in user_agent) or ("android" in user_agent):
    return render_template('post/mobile.html', **data)
    # else:
    # return render_template('post/desktop.html', **data)
