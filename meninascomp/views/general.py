from sqlite3 import dbapi2 as sqlite3
from flask import Flask, Blueprint, request, session, g, redirect, url_for, abort, render_template, flash

mod = Blueprint('general', __name__)

@mod.route('/')
def index():
    # db = get_db()
    # cur = db.execute('select title, text from entries order by id desc')
    # entries = cur.fetchall()
    return render_template('weare.html')

@mod.route('/weare')
def weAre():
    return render_template('weare.html')

@mod.route('/gallery')
def gallery():
    pages = {'lineOne': ['static/img/'+str(i)+'.jpg' for i in xrange(1,4)],
            'lineTwo': ['static/img/'+str(i)+'.jpg' for i in xrange(3,6)],
            'lineThree': ['static/img/'+str(i)+'.jpg' for i in xrange(6,9)]}

    return render_template('gallery.html', pages=pages)

@mod.route('/events')
def events():
    return render_template('events.html')

@mod.route('/contact')
def contact():
    return render_template('contact.html')

@mod.route('/sidebar')
def sidebar():
    return render_template('sidebar.html')
