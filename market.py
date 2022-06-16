from flask import Flask, g
from routes.main import *
from routes.post import *
from routes.user import *
from database import settings
from database.mongo import Users

app = Flask(__name__)
app.secret_key = "VerySecret12345"


# Index Page
app.add_url_rule("/", 'index_no_page', index_no_page, methods=['GET'])
app.add_url_rule("/<page>", 'index', index, methods=['GET'])

# Login and Register and Manage Profile
app.add_url_rule("/login", 'login', login, methods=['GET', 'POST'])
app.add_url_rule("/register", 'register', register, methods=['GET', 'POST'])
app.add_url_rule("/logout", 'logout', logout, methods=['GET'])
app.add_url_rule("/profile", 'profile', profile, methods=['GET'])
app.add_url_rule("/profile/edit", 'profile_edit',
                 profile_edit, methods=['GET', 'POST'])

# Posts
app.add_url_rule("/post", 'post_no_id', post_no_id, methods=['GET'])
app.add_url_rule("/post/<id>", 'one_post', one_post, methods=['GET'])
app.add_url_rule("/new/post/<ptype>", 'new_post', new_post, methods=['GET'])
app.add_url_rule("/new/data/<mode>", 'new_post_process',
                 new_post_process, methods=['GET', 'POST'])


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = Users.getUserByID(id=session['user_id'])
        g.user = user


if __name__ == "__main__":
    app.run(
        settings.Web.host,
        port=settings.Web.port,
        debug=settings.Web.debug
    )
