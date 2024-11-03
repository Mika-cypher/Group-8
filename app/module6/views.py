from flask import Blueprint, render_template

module6_bp = Blueprint('module6', __name__, template_folder='templates')
@module6_bp.route('/module6')
def module6():
    return render_template('module6.html')