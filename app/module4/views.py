from flask import Blueprint, render_template

module4_bp = Blueprint('module4', __name__, template_folder='templates')
@module4_bp.route('/module4')
def module4():
    return render_template('module4.html')