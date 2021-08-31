from flask import Blueprint, render_template, request, redirect, session, jsonify
from .combine_jobs import get_combined_jobs
from .db import Job
from .contact import send_email

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template("index.html")


@views.route('/dashboard')
def dashboard():
    if not session.get('user_id'):
        return redirect('/')

    return render_template("dashboard.html")


@views.route('/search', methods=['GET', 'POST'])
def search():
    if not session.get('user_id'):
        return redirect('/')

    if request.method == 'GET':
        return render_template("search.html")

    job_title = request.form['job_title']
    location = request.form['location']

    jobs = get_combined_jobs(job_title, location)
    return jsonify(jobs)
#    return render_template('search.html', jobs=jobs)


@views.route('/contact', methods=['GET', 'POST'])
def contact():
    if not session.get('user_id'):
        return redirect('/')

    if request.method == 'GET':
        return render_template("contact.html")

    contact_name = request.form['contact-name']
    contact_email = request.form['contact-email']
    contact_company = request.form['contact-company']
    contact_phone = request.form['contact-phone']
    contact_interest = request.form['contact-interest']
    contact_message = request.form['contact-message']

    if send_email(contact_name, contact_email, contact_company, contact_phone, contact_interest, contact_message):
        # return jsonify({'success': 'login'})
        pass
    # return jsonify({'error': 'Email could not be sent'})
    return redirect('/contact')


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
