from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from .import db
import json
from newsapi import NewsApiClient

# define "views.py" as blueprint of app
views = Blueprint('views', __name__)

#news scraper
# define initial route using decorator
@views.route('/')
def home():
    # reference in home if current user is authenticated
    return render_template ("home.html", user=current_user)

# define newspage route using decorator
@views.route('/news')
@login_required
def news():
    newsapi = NewsApiClient(api_key="319d9111dc85440e994aa5cf8341f118")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")   

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    

    mylist = zip(news, desc, img)
    # reference in home if current user is authenticated
    return render_template ("news.html", user=current_user, context= mylist)

# define notes page route using decorator
@views.route('/notes', methods=['GET','POST'])
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
    return render_template ("notes.html", user=current_user)

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