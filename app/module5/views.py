from flask import Blueprint, render_template

module5_bp = Blueprint('module5', __name__, template_folder='templates')
@module5_bp.route('/module5')
def module5():
    return render_template('module5.html')