from flask import Blueprint, render_template

module1_bp = Blueprint('module1', __name__, template_folder='templates')
@module1_bp.route('/module1')
def module1():
    return render_template('module1.html')

