from django.shortcuts import redirect
from flask import render_template, request, url_for, redirect, session, g
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

    data = {}
    data['title'] = "Hirusha"
    data['page_bottom'] = Dekstop.bottom
    data['page_top'] = Dekstop.top
    data['page_header'] = Dekstop.header

    return render_template('user/profile.html', page_home=True, **data)


def profile_edit():
    if not g.user:
        return redirect(url_for('login'))

    data = {}
    data['title'] = "Hirusha"
    data['page_bottom'] = Dekstop.bottom
    data['page_top'] = Dekstop.top
    data['page_header'] = Dekstop.header
    data['page_edit'] = True
    data['page_edit_errors_show'] = False
    data['page_edit_errors_list'] = []

    if request.method == 'POST':
        try:
            try:
                fname = request.form['fname']
                email = request.form['email']
                phn = request.form['phn']
                city = request.form['city']

                g.user.name = fname
                g.user.email = email
                g.user.phn = phn
                g.user.city = city
            except:
                opass = request.form['pass']
                npass = request.form['npass']
                rpass = request.form['rpass']

                if g.user.password == opass:
                    if npass == rpass:
                        g.user.password = npass
                    else:
                        data['page_edit_errors_show'] = True
                        data['page_edit_errors_list'].append(
                            'New password doesn\'t match with re-entered password'
                        )
                else:
                    data['page_edit_errors_show'] = True
                    data['page_edit_errors_list'].append(
                        'Old password is wrong'
                    )

            print(g.user)

        except Exception as _err:
            data['page_edit_errors_show'] = True
            data['page_edit_errors_list'].append(
                f'{_err}'
            )

    return render_template('user/profile.html', **data)


def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))
