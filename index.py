from flask import Flask, jsonify
from requests_html import HTMLSession
from datetime import datetime
from inscriptis import get_text
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import difflib
import os

app = Flask(__name__)

# Configuration
LOGIN_URL = 'https://webkiosk.thapar.edu/CommonFiles/UserAction.jsp'
EMAIL_ADDRESS = 'knightdarkhero@gmail.com'
TO_ADDRESS = 'adityasaini2004@gmail.com'
EMAIL_PASSWORD = 'dvid btvn iqxn btag'

sem = '2324EVESEM' #2425ODDSEM
payload = {
    'UserType': 'S',
    'MemberCode': "102206286",
    'Password': "adian1811",
    'BTNSubmit': 'Submit'
}

webpages = [
    {
        'name': 'Subject Details',
        'url': 'https://webkiosk.thapar.edu/StudentFiles/Academic/Studregdetails.jsp'
    },
    # {
    #     'name': 'Exam Grades',
    #     'url': 'https://webkiosk.thapar.edu/StudentFiles/Exam/StudentEventGradesView.jsp?x=&exam='+sem+'&Subject=ALL'
    # },
    {
        'name': 'CGPA Report',
        'url': 'https://webkiosk.thapar.edu/StudentFiles/Exam/StudCGPAReport.jsp'
    },
    # {
    #     'name': 'Seating Plan',
    #     'url': 'https://webkiosk.thapar.edu/StudentFiles/Exam/StudViewSeatPlan.jsp'
    # },
    # {
    #     'name': 'Datesheet',
    #     'url': 'https://webkiosk.thapar.edu/StudentFiles/Exam/StudViewDateSheet.jsp'
    # },
    {
        'name': 'Electives',
        'url': 'https://webkiosk.thapar.edu/StudentFiles/Academic/PRStudentView.jsp'
    }
    # Add more entries here for other webpages
]

def fetch_content(session, url):
    session.post(LOGIN_URL, data=payload)
    response = session.get(url)
    element = get_text(response.text)
    return str(element)

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_ADDRESS
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, TO_ADDRESS, msg.as_string())

# Main function
def main():
    session = HTMLSession()
    update = []
    for page in webpages:
        url = page['url']
        name = page['name']
        content_file = f'content_{name}.txt'
        current_content = fetch_content(session, url)

        if os.path.exists(content_file):
            with open(content_file, 'r') as file:
                previous_content = file.read()
        else:
            previous_content = ''

        if previous_content != current_content:
            diff = '\n'.join(difflib.unified_diff(previous_content.splitlines(), current_content.splitlines()))
            print('Sending Email')
            send_email(f'Webkiosk Updated: {name}', current_content)

            with open(content_file, 'w') as file:
                file.write(current_content)
        update.append(name)
    
    return update,datetime.now()

@app.route('/')
def index():
    update,time = main()
    return jsonify({
        'status': 'Script executed',
        'last_run': time.strftime("%d/%m/%Y %H:%M:%S"),
        'last_update': update
    })

if __name__ == '__main__':
    app.run()