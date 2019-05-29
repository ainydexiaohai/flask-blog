from flask import Blueprint

admin_bp = Blueprint('admin', url_prefix='admin')
auth_bp = Blueprint('auth', url_prefix='auth')
blog_bp = Blueprint('blog', url_prefix='blog')