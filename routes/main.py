from flask import render_template, request


def index():

    user_agent = request.headers.get('User-Agent').lower()

    if ("iphone" in user_agent) or ("android" in user_agent):
        return render_template('items/mobile.html')
    else:
        return render_template('items/desktop.html')
