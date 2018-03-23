#-*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

# WEBアプリ 定義
app = Flask(__name__)

# ORM 定義
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flask_ziptoaddress?charset=utf8'

db = SQLAlchemy(app)

class MstAddress(db.Model):
    """
    """
    id = db.Column(db.Integer, primary_key=True)
    jiscode = db.Column(db.String(255))
    zipcode_old = db.Column(db.String(255))
    zipcode = db.Column(db.String(255))
    pref_kana = db.Column(db.String(255))
    city_kana = db.Column(db.String(255))
    street_kana = db.Column(db.String(255))
    pref = db.Column(db.String(255))
    city = db.Column(db.String(255))
    street = db.Column(db.String(255))
    flag1 = db.Column(db.Integer)
    flag2 = db.Column(db.Integer)
    flag3 = db.Column(db.Integer)
    flag4 = db.Column(db.Integer)
    flag5 = db.Column(db.Integer)
    flag6 = db.Column(db.Integer)

    def __init__(self,
                 jiscode,
                 zipcode_old,
                 zipcode,
                 pref_kana,
                 city_kana,
                 street_kana,
                 pref,
                 city,
                 street,
                 flag1,
                 flag2,
                 flag3,
                 flag4,
                 flag5,
                 flag6
    ):
        """
        """
        self.jiscode = jiscode
        self.zipcode_old = zipcode_old
        self.zipcode = zipcode
        self.pref_kana = pref_kana
        self.city_kana = city_kana
        self.street_kana = street_kana
        self.pref = pref
        self.city = city
        self.street = street
        self.flag1 = flag1
        self.flag2 = flag2
        self.flag3 = flag3
        self.flag4 = flag4
        self.flag5 = flag5
        self.flag6 = flag6

    def __str__(self):
        return "{} {} {}".format(self.pref, self.city, self.street)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/zip/<string:zipcode>/address.json")
def get_address(zipcode):
    """
    """

    mst_address = MstAddress.query.filter_by(zipcode=zipcode)
    
    result_code = ""
    addresses = []

    if mst_address.count():

        result_code = "ok"

        for a in mst_address.all():
            addresses.append({
                "zipcode": a.zipcode,
                "pref": a.pref,
                "city": a.city,
                "town": a.street,
                "pref_kana": a.pref_kana,
                "city_kana": a.city_kana,
                "street_kana": a.street_kana,
            })
        
    else:
        result_code = "error"
    
    result = {
        "result": result_code,
        "addresses": addresses,
    }
    
    return jsonify(result)
