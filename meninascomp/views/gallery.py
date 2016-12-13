# Stub gallery
from flask import Blueprint, render_template

mod = Blueprint('gallery', __name__)

@mod.route('/gallery1')
def pageOne():
    pages = {'lineOne': ['static/img/'+str(i)+'.jpg' for i in xrange(1,4)],
            'lineTwo': ['static/img/'+str(i)+'.jpg' for i in xrange(3,6)],
            'lineThree': ['static/img/'+str(i)+'.jpg' for i in xrange(6,9)]}

    return render_template('gallery.html', pages=pages)

@mod.route('/gallery2')
def pageTwo():
    pages = {'lineOne': ['static/img/10.jpg'],
            'lineTwo': [],
            'lineThree': []}

    return render_template('gallery.html', pages=pages)
