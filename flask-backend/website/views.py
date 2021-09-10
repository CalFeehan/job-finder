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


@views.route('/profile')
def profile():
    if not session.get('user_id'):
        return redirect('/')

    return render_template("profile.html")


@views.post('/save-job')
def save_job():
    if not session.get('user_id'):
        return redirect('/')

    job = {
        'job_title': request.form['job-title'],
        'company': request.form['company'],
        'location': request.form['location'],
        'salary': request.form['salary'],
        'summary': request.form['summary']
    }
    # Tries to save job
    if Job.save_job(session['user_id'], job):
        return "Job Saved"
    # If job already saves, deletes job
    Job.delete_job(session['user_id'], job)
    return "Job Deleted"
