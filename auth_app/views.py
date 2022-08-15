from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from newsapi import NewsApiClient

# define "views.py" as blueprint of app
views = Blueprint('views', __name__)


#news scraper
# define initial route using decorator
@views.route('/')
def home():
    # reference in home if current user is authenticated
    return render_template("home.html", user=current_user)


# ---------------AJ START-----------#
# define AJ newspage route using decorator
@views.route('/aj')
@login_required
def newsAJ():
    newsapi = NewsApiClient(api_key="319d9111dc85440e994aa5cf8341f118")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")

    articles = topheadlines['articles']

    newsAJ = []
    descAJ = []
    imgAJ = []
    urlAJ = []

    for i in range(len(articles)):
        myarticles = articles[i]

        newsAJ.append(myarticles['title'])
        descAJ.append(myarticles['description'])
        imgAJ.append(myarticles['urlToImage'])
        urlAJ.append(myarticles['url'])

    mylist = zip(newsAJ, descAJ, imgAJ, urlAJ)
    # reference in home if current user is authenticated
    return render_template("aj.html", user=current_user, context=mylist)


#---------------------AJ END--------------#
#---------------------WSJ START-----------#
@views.route('/wsj')
@login_required
def newsWSJ():
    newsapi = NewsApiClient(api_key="319d9111dc85440e994aa5cf8341f118")
    topheadlines = newsapi.get_top_headlines(sources="the-wall-street-journal")

    articles = topheadlines['articles']

    newsWSJ = []
    descWSJ = []
    imgWSJ = []
    urlWSJ = []

    for i in range(len(articles)):
        myarticles = articles[i]

        newsWSJ.append(myarticles['title'])
        descWSJ.append(myarticles['description'])
        imgWSJ.append(myarticles['urlToImage'])
        urlWSJ.append(myarticles['url'])

    mylist = zip(newsWSJ, descWSJ, imgWSJ, urlWSJ)
    # reference in home if current user is authenticated
    return render_template("wsj.html", user=current_user, context=mylist)


#---------------------WSJ END-----------#
#---------------------Verge START-----------#


# define Verge newspage route using decorator
@views.route('/verge')
@login_required
def newsVerge():
    newsapi = NewsApiClient(api_key="319d9111dc85440e994aa5cf8341f118")
    topheadlines = newsapi.get_top_headlines(sources="the-verge")

    articles = topheadlines['articles']

    newsVerge = []
    descVerge = []
    imgVerge = []
    urlVerge = []

    for i in range(len(articles)):
        myarticles = articles[i]

        newsVerge.append(myarticles['title'])
        descVerge.append(myarticles['description'])
        imgVerge.append(myarticles['urlToImage'])
        urlVerge.append(myarticles['url'])

    mylist = zip(newsVerge, descVerge, imgVerge, urlVerge)
    # reference in home if current user is authenticated
    return render_template("verge.html", user=current_user, context=mylist)


#---------------------Verge END--------------#
#---------------------TechRadar START-----------#


@views.route('/techradar')
@login_required
def newsTR():
    newsapi = NewsApiClient(api_key="319d9111dc85440e994aa5cf8341f118")
    topheadlines = newsapi.get_top_headlines(sources="techradar")

    articles = topheadlines['articles']

    newsTR = []
    descTR = []
    imgTR = []
    urlTR = []

    for i in range(len(articles)):
        myarticles = articles[i]

        newsTR.append(myarticles['title'])
        descTR.append(myarticles['description'])
        imgTR.append(myarticles['urlToImage'])
        urlTR.append(myarticles['url'])

    mylist = zip(newsTR, descTR, imgTR, urlTR)
    # reference in home if current user is authenticated
    return render_template("techradar.html", user=current_user, context=mylist)


#---------------------TR END-----------#
#---------------------Reuter START-----------#


@views.route('/reuters')
@login_required
def newsReuters():
    newsapi = NewsApiClient(api_key="319d9111dc85440e994aa5cf8341f118")
    topheadlines = newsapi.get_top_headlines(sources="reuters")

    articles = topheadlines['articles']

    newsReuters = []
    descReuters = []
    imgReuters = []
    urlReuters = []

    for i in range(len(articles)):
        myarticles = articles[i]

        newsReuters.append(myarticles['title'])
        descReuters.append(myarticles['description'])
        imgReuters.append(myarticles['urlToImage'])
        urlReuters.append(myarticles['url'])

    mylist = zip(newsReuters, descReuters, imgReuters, urlReuters)
    # reference in home if current user is authenticated
    return render_template("reuters.html", user=current_user, context=mylist)


#---------------------Reuters END-----------#


# define notes page route using decorator
@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    # publish notes to backend using POST method
    if request.method == 'POST':
        note = request.form.get('note')
        # check for length of note
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    # reference in home if current user is authenticated
    return render_template("notes.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    # take in data from POST request
    note = json.loads(request.data)

    #access noteId attribute
    noteId = note['noteId']
    # look for note that has id
    note = Note.query.get(noteId)
    #check if exists
    if note:
        # if user owns the note
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})