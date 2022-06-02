from django.shortcuts import redirect
from flask import render_template, request, url_for, redirect, session, g
import utils.test as test
from flask_paginate import Pagination
from database.settings import Dekstop
from models.user import User

users = test.users
users.append(User(id=1, username='hi', password='pwd'))
users.append(User(id=2, username='admin', password='123'))


def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))
        else:
            return redirect(url_for('login'))
    else:
        data = {}
        data['title'] = "Hirusha"
        data['page_bottom'] = Dekstop.bottom
        data['page_top'] = Dekstop.top
        data['page_header'] = Dekstop.header

        return render_template('user/login.html', **data)


def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('user/profile.html')
