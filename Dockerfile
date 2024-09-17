FROM python:3.9-slim

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# working directory
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# EDIT THESE
ENV EMAIL_ADDRESS='from_mail@email.com'
ENV TO_ADDRESS='to_mail@email.com'
ENV EMAIL_PASSWORD='from_mail_password'

CMD ["flask", "run"]
