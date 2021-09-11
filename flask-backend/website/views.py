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
    # Tries to save job
    if Job.save_job(session['user_id'], job):
        return jsonify({'success': 'saved'})
    # If job already saves, deletes job
    Job.delete_job(session['user_id'], job)
    return jsonify({'success': 'deleted'})
