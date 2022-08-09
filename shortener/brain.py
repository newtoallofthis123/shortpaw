from datetime import datetime, date
import json
import random
import string
import requests
from shortener import app, db
from shortener.models import Bin


def hash_gen_engine():
    """[summary]

    Returns:
        [type]: [description]
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    whole =  lower + upper + digits
    hash_string = random.sample(whole, 8)
    hash = "".join(hash_string)
    return hash

def time_cal():
    current_t = datetime.now()
    current_date = str(date.today())
    current_t_f = current_t.strftime("%H:%M:%S")
    timeAnddate = (f'{current_t_f} {current_date}')
    return timeAnddate

def visit_add(hash):
    add_url = Bin.query.filter_by(hash=hash).first()
    add_url.visits = int(add_url.visits) + 1
    db.session.add(add_url)
    db.session.commit()
    db.session.refresh(add_url)

def add_reserve(url, time, hash):
    visits = 0
    add_url = Bin(og_url=url, visits=visits, hash=hash, time=time)
    db.session.add(add_url)
    db.session.commit()
    db.session.refresh(add_url)
    short_url_info = {"og_url": url, "visits": visits, "hash": hash, "time": time}
    return short_url_info

def creation_engine(url):
    time = time_cal()
    og_url = url
    url_hash = hash_gen_engine()
    url_info = add_reserve(og_url, time, url_hash)
    return url_info

def custom_hash(hash):
    hash_check = Bin.query.filter_by(hash=hash).first()
    if hash_check:
        return hash_gen_engine()
    else:
        return hash

def check_dups(hash):
    hash_check = Bin.query.filter_by(hash=hash).first()
    if hash_check:
        return True
    else:
        return False

def custom_creation_engine(url, hash):
    """[summary]

    Args:
        url ([type]): [description]
        hash (bool): [description]

    Returns:
        [type]: [description]
    """
    time = time_cal()
    og_url = url
    url_hash = custom_hash(hash)
    url_info = add_reserve(og_url, time, url_hash)
    return url_info

def get_og(hash):
    content = Bin.query.filter_by(hash=hash).first()
    if content == None:
        return "No Such Url"
    else:
        return content

def debug_engine(table):
    debug_content = table.query.all()
    return debug_content

def undo():
    db.session.rollback()

def ran_quote():
    quotes_page = json.loads(requests.get("https://api.quotable.io/random?maxLength=120").content)
    quote_list = [quotes_page["content"], quotes_page["author"]]
    return quote_list

def ran_fact():
    fact_page = json.loads(requests.get("https://useless-facts.sameerkumar.website/api").content)
    fact = fact_page["data"]
    return fact

def qr_code_engine(url):
    import pyqrcode
    qr_code = pyqrcode.create(url)
    qr_code.svg('shortener/static/assets/images/qr_code.svg', background="white", scale=8)

def ran_color():
    color_list = ("red", "yellow", "green", "blue")
    color = random.choice(color_list)
    colors = {
        "main": "main_" + color,
        "body": "body_" + color
    }
    return colors
