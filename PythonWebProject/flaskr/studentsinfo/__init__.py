from flask import Blueprint

# 创建student对象
student = Blueprint('studentsinfo', __name__)
# 导入views,这个必须放在这！！！
from flaskr.studentsinfo import views
