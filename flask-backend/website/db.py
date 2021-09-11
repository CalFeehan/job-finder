import mysql.connector
import os

HOST = 'sql496.main-hosting.eu'
USER = 'u497621354_callum'
PASSWORD = os.getenv('JOBFINDER_DB_PASS')
DATABASE = 'u497621354_jobfinder'
PORT = '3306'


def get_connection():
    return mysql.connector.connect(host=HOST, user=USER, passwd=PASSWORD, database=DATABASE)


def execute_query(*query):
    '''Wrapper function for non return queries'''
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(
        *query
    )
    db.commit()
    cursor.close()
    db.close()


def execute_query_with_return(*query):
    '''Wrapper function for return queries'''
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(
        *query
    )
    ret = cursor.fetchall()
    cursor.close()
    db.close()
    return ret


class User:

    @staticmethod
    def init_user_table():
        execute_query(
            '''CREATE TABLE users(
                id int AUTO_INCREMENT PRIMARY KEY,
                public_id int,
                email varchar(255),
                password varchar(255),
                date_created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                date_modified DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                )'''
        )

    @staticmethod
    def get_users():
        return (execute_query_with_return('SELECT * FROM users'))

    @staticmethod
    def check_user_exists(email):
        return any(execute_query_with_return('SELECT * FROM users WHERE email=%s', (email, )))

    @staticmethod
    def get_user_id(email):
        return execute_query_with_return('SELECT id FROM users WHERE email=%s', (email, ))[0][0]

    @staticmethod
    def get_user_email(user_id):
        return execute_query_with_return('SELECT email FROM users WHERE id=%s', (user_id, ))[0][0]

    @staticmethod
    def get_stored_password(email):
        return execute_query_with_return('SELECT password FROM users WHERE email=%s', (email, ))[0][0]

    @staticmethod
    def add_user(public_id, email, password):
        if not execute_query_with_return(
            ''' SELECT id FROM users WHERE email=%s''', (email,)
        ):
            execute_query(
                '''INSERT INTO users(
                    public_id, email, password)
                    VALUES(%s, %s, %s)
                ''', (public_id, email, password)
            )
            return True
        return False

    @staticmethod
    def login(email, password):
        '''unused as async function now does this'''
        return bool(execute_query_with_return('SELECT * FROM users WHERE email=%s AND password=%s', (email, password)))

    def change_password(user_id, new_password):
        execute_query('UPDATE users SET password=%s WHERE id=%s',
                      (new_password, user_id))

    @staticmethod
    def delete_user(user_id):
        execute_query('DELETE FROM users WHERE id=%s', (user_id,))


class Job:

    @staticmethod
    def init_job_table():
        execute_query(
            '''CREATE TABLE jobs(
                id int PRIMARY KEY,
                job_title varchar(255), 
                company varchar(255),
                location varchar(255),
                salary varchar(255),
                summary text(1020),
                closing_date date,
                application_date date,
                notes text(1020),
                job_link varchar(255),
                company_link varchar(255)
                )
                '''
        )

    @staticmethod
    def get_saved_jobs(user_id):
        return (execute_query_with_return('SELECT * FROM jobs WHERE id=%s', (user_id,)))

    @staticmethod
    def save_job(user_id, job):
        job_title = job['job_title']
        company = job['company']
        location = job['location']
        salary = job['salary']
        summary = job['summary']
        if not execute_query_with_return(
            ''' SELECT * FROM jobs WHERE id=%s AND job_title=%s AND company=%s''', (
                user_id, job_title, company)
        ):
            execute_query(
                '''INSERT INTO jobs(
                    id, job_title, company, salary, summary, location)
                    VALUES(%s, %s, %s, %s, %s, %s)
                ''', (user_id, job_title, company, salary, summary, location)
            )
            return True
        return False

    @staticmethod
    def delete_job(user_id, job):
        job_title = job['job_title']
        company = job['company']
        execute_query(
            ''' DELETE FROM jobs WHERE id=%s AND job_title=%s AND company=%s''', (
                user_id, job_title, company)
        )
