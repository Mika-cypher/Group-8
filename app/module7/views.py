from flask import Blueprint, render_template

module7_bp = Blueprint('module7', __name__, template_folder='templates')
@module7_bp.route('/module7')
def module7():
    return render_template('module7.html')