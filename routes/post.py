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

    data['imgs'] = data['post_info']['images']

    return render_template('post/mobile.html', **data)


def new_post(ptype):
    ptype = str(ptype)

    data = {}
    data['title'] = "Hirusha"
    data['page_bottom'] = Dekstop.bottom
    data['page_top'] = Dekstop.top
    data['page_header'] = Dekstop.header

    if ptype.lower() in ("car", "vehicle"):
        data['title'] = "Hirusha"
        data['post_type'] = "car"

    elif ptype.lower() in ("land", "building"):
        data['title'] = "Hirusha"
        data['post_type'] = "land"

    elif ptype.lower() in ("electronics",):
        data['title'] = "Hirusha"
        data['post_type'] = "electronics"

    elif ptype.lower() in ("parts", "accessories"):
        data['title'] = "Hirusha"
        data['post_type'] = "parts"

    else:
        return redirect(url_for('profile'))

    return render_template('new/mobile.html', **data)


def new_post_process(mode):
    if request.method == 'POST':
        
        ProductName = request.form.get('ProductName')
        ProductPrice = request.form.get('ProductPrice')
        
        if mode == 'car':
            request.form.get()
        