from flask import Blueprint, render_template

module3_bp = Blueprint('module3', __name__, template_folder='templates')
@module3_bp.route('/module3')
def module3():
    return render_template('module3.html')