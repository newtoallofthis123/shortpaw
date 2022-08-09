from ast import arg
from shortener.brain import *
from flask import request, make_response, jsonify, redirect, render_template, flash, get_flashed_messages
from shortener import app, db
from shortener.models import Bin

app_name = "https://shortpaw.herokuapp.com"

@app.route('/')
def short_paw():
    prev_url = str(request.cookies.get('url_hash'))
    return render_template('home.html', ran_quote=ran_quote(), prev_url=prev_url)

@app.route('/<hash>')
def short_url(hash):
    url_info = get_og(hash)
    if url_info == "No Such Url":
        return redirect('/404')
    else:
        visit_add(hash)
        return render_template('redirect.html', ran_quote=ran_quote(), url_info=url_info)

@app.route('/qr', methods=["POST", "GET"])
def qr():
    qr_code_engine(request.values.get("url"))
    stuff_dict = {}
    with open("shortener/static/assets/images/qr_code.svg", "r") as file:
        stuff = file.read()
        stuff_dict["stuff"] = str(stuff).replace('<?xml version="1.0" encoding="UTF-8"?>', '')
        print(stuff_dict)
        return stuff_dict

@app.route('/create', methods=["POST", "GET"])
def create():
    url = request.values.get("url")
    url_info = creation_engine(url)
    url_response = make_response(jsonify(url_info))
    final_url = app_name + "/go/" + url_info["hash"]
    qr_code_engine(final_url)
    url_response.set_cookie('latest_url', url)
    url_response.set_cookie('url_hash', f'{url_info["hash"]}')
    return url_response

@app.route('/custom_create', methods=["POST", "GET"])
def custom_create():
    url = request.values.get("url")
    custom_url = request.values.get("custom_url")
    url_info = custom_creation_engine(url, custom_url)
    url_response = make_response(jsonify(url_info))
    final_url = app_name + "/go/" + url_info["hash"]
    qr_code_engine(final_url)
    url_response.set_cookie('latest_url', url)
    url_response.set_cookie('url_hash', f'{url_info["hash"]}')
    return url_response

@app.route('/go/<hash>')
def go(hash):
    url_info = get_og(hash)
    if url_info == "No Such Url":
        return redirect('/404')
    else:
        visit_add(hash)
        redirect_response = make_response(redirect(url_info.og_url, code=302))
        redirect_response.set_cookie("url", url_info.og_url)
        redirect_response.set_cookie("time", time_cal())
        return redirect_response

@app.route('/info/<hash>')
def info(hash):
    url_info = get_og(hash)
    if url_info == "No Such Url":
        return redirect('/404')
    else:
        visit_add(hash)
        return render_template('info.html', ran_quote=ran_quote(), url_info=url_info)
    
@app.route('/color', methods=["POST", "GET"])
def color():
    colors = ran_color()
    return colors

@app.route('/about')
def about():
    code_content = "# POST API for ShortPaw\nimport requests\n\n# Normal Url\nrequest_url = 'https://shortpaw.herokuapp.com/api'\ndata = {'url': 'https://netflix.com'}\n# returns {'og_url': 'https://netflix.com', 'hash': 'tw28dekl', 'time':  '16:32:46 2022-01-27'}\n# Custom Url\n\nrequest_url = 'https://shortpaw.herokuapp.com/custom_api'\ndata = {'url': 'https://netflix.com', 'custom_url': 'netflix'}\n# returns {'og_url': 'https://netflix.com', 'hash': 'netflix', 'time':  '16:32:46 2022-01-27'}"
    about_response = make_response(render_template("about.html", ran_fact=ran_fact(), code_content=code_content))
    return about_response

@app.route('/credits')
def credits():
    return render_template("credits.html")

@app.route('/404')
def error():
    return render_template("404.html", quote=ran_quote())

@app.route('/dog')
def dog():
    return render_template("dog.html")

@app.route('/contact')
def contact():
    return render_template("contact.html", ran_fact=ran_fact())

@app.route('/api', methods=["POST", "GET", "PUT"])
def api():
    if request.method == 'POST':
        url = request.values.get("url")
        url_info = jsonify(creation_engine(url))
        return url_info
    if request.method == 'PUT':
        url = request.values.get("url")
        url_info = jsonify(creation_engine(url))
        return url_info
    return {"request url": "/api", "type": "api_request", "data_to_give": "url='url_to_shorten'", "hash_type": "random", "author": "NoobScience"}

@app.route('/custom_api', methods=["POST", "GET", "PUT"])
def custom_api():
    if request.method == 'POST':
        url = request.values.get("url")
        custom_url = request.values.get("custom_url")
        url_info = jsonify(custom_creation_engine(url, custom_url))
        return url_info
    if request.method == 'PUT':
        url = request.values.get("url")
        custom_url = request.values.get("custom_url")
        url_info = jsonify(custom_creation_engine(url, custom_url))
        return url_info
    return {"request url": "/custom_api", "type": "api_request", "data_to_give": "url='url_to_shorten'&custom_url='custom_hash'", "hash_type": "custom", "author": "NoobScience"}
