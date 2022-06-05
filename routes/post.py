from os import EX_CANTCREAT
from django.shortcuts import redirect
from flask import render_template, request, url_for, redirect, session, g
from database.settings import Dekstop
from models.user import User
from database.mongo import Users, Posts


def post_no_id():
    return redirect(url_for('index_no_page'))


def one_post(id):
    data = {}
    data['title'] = "Hirusha"
    data['page_bottom'] = Dekstop.bottom
    data['page_top'] = Dekstop.top
    data['page_header'] = Dekstop.header

    # Get Post Info
    try:
        post = Posts.getPostByID()
        if bool(post) is False:
            return redirect(url_for('index_no_page'))
        data['post_info'] = post
    except:
        return redirect(url_for('index_no_page'))

    try:
        user = Users.getUserByUsername()
    except:
        return redirect(url_for('index_no_page'))

    return render_template('post/mobile.html', **data)
