from flask import Blueprint, render_template

bp = Blueprint(
    'home', __name__,
    static_folder='../static',
    template_folder='../templates'
)


@bp.route('/')
def index():
    return render_template('home.html')

# from flask import Flask, render_template

# app = Flask(__name__)


# @app.route('/')
# def main_page():
#     return render_template('home.html')

# if __name__ == '__main__':
#     app.run(debug=True)
