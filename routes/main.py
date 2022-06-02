from django.shortcuts import redirect
from flask import render_template, request, url_for, redirect, session, g
import utils.test as test
from flask_paginate import Pagination
from database.settings import Dekstop


def index_no_page():
    return redirect(url_for('index', page=1))


def index(page):
    current_page = int(page)
    list_all = test.items
    list_length = len(list_all)
    per_page = 4

    pagination = Pagination(
        per_page=per_page,
        page=current_page,
        total=list_length,
        href=str(url_for('index', page=1))[:-1] + "{0}"
    )

    max_possible_page = (list_length // per_page)+1
    if current_page > max_possible_page:
        current_page = max_possible_page
    min_index = (current_page*per_page) - per_page
    max_index = (min_index + per_page)

    data = {}
    data['title'] = "Hirusha"
    data['items'] = list_all[min_index:max_index]
    data['pagination'] = pagination
    data['page_bottom'] = Dekstop.bottom
    data['page_top'] = Dekstop.top
    data['page_header'] = Dekstop.header

    # user_agent = request.headers.get('User-Agent').lower()
    # if ("iphone" in user_agent) or ("android" in user_agent):
    return render_template('items/mobile.html', **data)
    # else:
    # return render_template('items/desktop.html', **data)
