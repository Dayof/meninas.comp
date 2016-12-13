# Stub gallery
from flask import Blueprint, render_template

mod = Blueprint('gallery', __name__)

@mod.route('/videos1')
def videosPageOne():
    return render_template('videos.html')

@mod.route('/photos1')
def photosPageOne():
    pages = {'lineOne': ['static/img/'+str(i)+'.jpg' for i in xrange(1,4)],
            'lineTwo': ['static/img/'+str(i)+'.jpg' for i in xrange(3,6)],
            'lineThree': ['static/img/'+str(i)+'.jpg' for i in xrange(6,9)]}

    return render_template('photos.html', pages=pages)

@mod.route('/photos2')
def photosPageTwo():
    pages = {'lineOne': ['static/img/10.jpg'],
            'lineTwo': [],
            'lineThree': []}

    return render_template('photos.html', pages=pages)
