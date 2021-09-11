from flask import Blueprint, render_template, request, redirect, session, jsonify
from .combine_jobs import get_combined_jobs
from .db import Job
from .contact import send_email
import json


views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template("index.html")


@views.post('/search')
def search():
    data = request.get_json(silent=True)
    job_title = data['job_title']
    location = data['location']
    jobs = get_combined_jobs(job_title, location)
    print(jobs)
    return jsonify(jobs)


@views.post('/contact')
def contact():
    data = request.get_json(silent=True)
    contact_name = data['name']
    contact_email = data['email']
    contact_company = data['company']
    contact_phone = data['phone']
    contact_interest = data['interestedIn']
    contact_message = data['message']

    if send_email(contact_name, contact_email, contact_company, contact_phone, contact_interest, contact_message):
        return jsonify({'success': 'Message sent'})

    return jsonify({'error': 'Message could not be sent'})


@views.post('/save-job')
def save_job():
    #   being used temporarily, storing all jobs against my user.
    session['user_id'] = 1
    data = request.get_json(silent=True)
    job = {
        'job_title': data['title'],
        'company': data['company'],
        'location': data['location'],
        'salary': data['salary'],
        'summary': data['summary']
    }
    print(job)
    # Tries to save job
    if Job.save_job(session['user_id'], job):
        return jsonify({'saved': 'saved'})
    # If job already saves, deletes job
    Job.delete_job(session['user_id'], job)
    return jsonify({'deleted': 'deleted'})


@views.get('/get-jobs')
def get_jobs():
    session['user_id'] = 1
    for i in Job.get_saved_jobs(session['user_id']):
        data = {
            'job title': i[2],
            'company': i[3],
            'location': i[4],
            'salary': i[5],
            'summary': i[6],
            'closing date': i[7],
            'application date': i[8],
            'notes': i[9],
            'job link': i[10],
            'company link': i[11],
        }
    print(data)
    return str(data)
