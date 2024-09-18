
# Webkiosk Notifier

Webkiosk Notifier monitors updates on Thapar University's webkiosk portal and sends email notifications when changes are detected. The tool scrapes content from pages like exam grades, subject details, seating plans, and more, compares it with previous data, and sends alerts for updates.

## Setup Instructions

### Prerequisites

- Python 3.9 or higher
- Docker

### Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/webkiosk-notifier.git
   cd webkiosk-notifier
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure email and login variables in `app.py`:
   - Change `EMAIL_ADDRESS`, `TO_ADDRESS`, `EMAIL_PASSWORD` with your email settings
   - Change `ROLL_NUMBER` and `PASSWORD` with your login details
   - Edit the `sem` varible with the latest ongoing semester

4. Run the Flask app:
   ```bash
   python app.py
   ```

### Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t webkiosk-notifier .
   ```

2. Run the Docker container:
   ```bash
   docker run -d -p 5000:5000 webkiosk-notifier
   ```

## Usage

The application checks for updates on the following webkiosk pages:
- Subject Details
- Exam Grades
- CGPA Report
- Seating Plan
- Datesheet
- Electives

Email notifications are triggered when updates are detected.

## License

This project is licensed under the MIT License.
