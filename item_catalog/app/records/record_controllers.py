# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.records.record_forms import LoginForm

# Import module models (i.e. User)
from app.records.record_model import Base, Genre, Artist, Record

engine = create_engine('sqlite:///app.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Define the blueprint: 'auth', set its url prefix: app.url/auth
recordBase = Blueprint('auth', __name__)

# Set the route and accepted methods
@recordBase.route('/', methods=['GET', 'POST'])
def showRecords():
    records = session.query(Record).order_by(asc(Record.title))
    print records

    return render_template("records/welcome.html", records = records)