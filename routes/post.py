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
        _post = Posts.getPostByID(id=int(id))
        if bool(_post) is False:
            return redirect(url_for('index_no_page'))
        data['post_info'] = _post
    except:
        return redirect(url_for('index_no_page'))

    try:
        _user = Users.getUserByUsername(username=_post['username'])
        if bool(_user) is False:
            return redirect(url_for('index_no_page'))
        data['user_info'] = _user
    except:
        return redirect(url_for('index_no_page'))

    try:
        pass
    except:
        return redirect(url_for('index_no_page'))

    data['imgs'] = ["https://www.w3schools.com/w3css/img_mountains.jpg",
                    "https://www.w3schools.com/w3css/img_snowtops.jpg",
                    "https://www.w3schools.com/w3css/img_forest.jpg"]

    return render_template('post/mobile.html', **data)


def new_post_car():
    data = {}
    data['title'] = "Hirusha"
    data['page_bottom'] = Dekstop.bottom
    data['page_top'] = Dekstop.top
    data['page_header'] = Dekstop.header

    return render_template('new/car.html', **data)
