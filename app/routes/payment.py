from flask import Blueprint, render_template

bp = Blueprint(
    'payment', __name__,
    static_folder='../static',
    template_folder='../templates'
)


@bp.route('/donate')
def donate():
    return render_template('payment.html')
