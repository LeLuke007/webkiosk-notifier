# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define environment variable
ENV EMAIL_ADDRESS='knightdarkhero@gmail.com'
ENV TO_ADDRESS='adityasaini2004@gmail.com'
ENV EMAIL_PASSWORD='dvid btvn iqxn btag'

# Run the application
CMD ["flask", "run"]
