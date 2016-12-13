from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.config.from_object('config')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from views import general, gallery
app.register_blueprint(general.mod)
app.register_blueprint(gallery.mod)

if __name__ == '__main__':
    app.run()
