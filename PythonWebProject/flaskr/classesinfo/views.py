from . import classinfo

@classinfo.route("/")
def index():
    return f"<a>this is a class</a>"