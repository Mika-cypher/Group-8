from flask import Blueprint, render_template

module2_bp = Blueprint('module2', __name__, template_folder='templates')
@module2_bp.route('/module2')
def module2():
    return render_template('module2.html')