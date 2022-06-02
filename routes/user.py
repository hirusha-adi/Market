from django.shortcuts import redirect
from flask import render_template, request, url_for, redirect, session, g, jsonify
import utils.test as test
from flask_paginate import Pagination
from database.settings import Dekstop
from models.user import User

users = test.users
users.append(User(id=1, username='admin', password='123',
                  name="Hirusha Adikari", email="i@love.you",
                  phone="+94719929929", city="home sweet home"))

users.append(User(id=2, username='hi', password='123',
                  name="Hirusha Adikari", email="i@love.you",
                  phone="+94719929929", city="home sweet home"))


def addUser(**kwargs):
    global users
    users.append(
        User(
            id=int(users[-1].id)+1,
            username=kwargs.get("username"),
            password=kwargs.get("password"),
            name=kwargs.get("name"),
            email=kwargs.get("email"),
            phone=kwargs.get("phone"),
            city=kwargs.get("city"),
        )
    )


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


def show_all_data():
    global users
    print(users)
    return "hello world"


def register():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        city = request.form['city']

        addUser(username=username, password=password,
                name=name, email=email, phone=phone, city=city)

        user = [x for x in users if x.username == username][0]
        session['user_id'] = user.id

        return redirect(url_for('profile'))
    else:
        data = {}
        data['title'] = "Hirusha"
        data['page_bottom'] = Dekstop.bottom
        data['page_top'] = Dekstop.top
        data['page_header'] = Dekstop.header
        return render_template('user/register.html', **data)


def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('user/profile.html')
