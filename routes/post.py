from flask import render_template, request, url_for, redirect, session, g
from database.settings import Dekstop
from models.user import User
from database.mongo import Users, Posts
from datetime import datetime

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
    
    if mode == 'car':
    
        data = {
            "id": int(Posts.getLastPost()['id']) + 1,
            "username": str(g.user['username']),
            "date": str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")),
            "type": "car",

            "name": request.form.get('ProductName'),
            "price": request.form.get('ProductPrice'),
            "details": request.form.get('ProductDescription'),

            "fields": {
                "ctype": request.form.get('VehicleType'),
                "condition": request.form.get('VehicleCondition'),
                "make": request.form.get('VehicleMake'),
                "model": request.form.get('VehicleModel'),
                "yom": request.form.get('yom'),
                "transmission": request.form.get('VehicleTransmission'),
                "fueltype": request.form.get('VehicleFuel'),
                "engine": request.form.get('VehicleEngineCapacity'),
                "mileage": request.form.get('VehicleMileage'),
                "options": ""
            },
            "images": [
                "",
                ""
            ]
        }
        
        Posts.addPost(data=data)
    
    elif mode == 'land':
        data = {
            "id": int(Posts.getLastPost()['id']) + 1,
            "username": str(g.user['username']),
            "date": str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")),
            "type": "land",

            "name": request.form.get('ProductName'),
            "price": request.form.get('ProductPrice'),
            "details": request.form.get('ProductDescription'),

            "fields": {
                "ptype": request.form.get('PropertyType'),
                "btype": request.form.get('PurchaseType'),
                "size": request.form.get('Size'),
                "options": ""
            },
            "images": [
                "",
                ""
            ]
        }
        
        Posts.addPost(data=data)
        
    elif mode == 'electronics':
        data = {
            "id": int(Posts.getLastPost()['id']) + 1,
            "username": str(g.user['username']),
            "date": str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")),
            "type": "electronics",

            "name": request.form.get('ProductName'),
            "price": request.form.get('ProductPrice'),
            "details": request.form.get('ProductDescription'),

            "fields": {
                "make": request.form.get('Make'),
                "model": request.form.get('Model'),
                "yom": request.form.get('yom'),
                "power": request.form.get('PowerRequirement'),
                "options": ""
            },
            "images": [
                "",
                ""
            ]
        }
        
        Posts.addPost(data=data)
    
    elif mode == 'parts':
        data = {
            "id": int(Posts.getLastPost()['id']) + 1,
            "username": str(g.user['username']),
            "date": str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")),
            "type": "electronics",

            "name": request.form.get('ProductName'),
            "price": request.form.get('ProductPrice'),
            "details": request.form.get('ProductDescription'),

            "fields": {
                "make": request.form.get('Make'),
                "model": request.form.get('Model'),
                "yom": request.form.get('yom'),
                "whatfor": request.form.get('WhatFor'),
                "size": request.form.get('Size'),
                "options": ""
            },
            "images": [
                "",
                ""
            ]
        }
        
        Posts.addPost(data=data)

    return "Testing"
