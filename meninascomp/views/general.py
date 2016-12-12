from sqlite3 import dbapi2 as sqlite3
from flask import Flask, Blueprint, request, session, g, redirect, url_for, abort, render_template, flash

mod = Blueprint('general', __name__)

DESC = {'titulo': 'Meninas.comp'}

@mod.route('/')
def index():
    # db = get_db()
    # cur = db.execute('select title, text from entries order by id desc')
    # entries = cur.fetchall()
    return render_template('weare.html', index_data=DESC)

@mod.route('/weare')
def weAre():
    return render_template('weare.html', index_data=DESC)

@mod.route('/team')
def team():
    return render_template('team.html', index_data=DESC)

@mod.route('/gallery')
def gallery():
    return render_template('gallery.html', index_data=DESC)

@mod.route('/events')
def events():
    return render_template('events.html', index_data=DESC)

@mod.route('/contact')
def contact():
    return render_template('contact.html', index_data=DESC)
