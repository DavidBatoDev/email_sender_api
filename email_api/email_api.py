from flask import Flask, request, jsonify
from email_api.email_sender.email_sender import EmailSender
from email_api.email_sender.config import SMTP_SERVER, SMTP_PORT, EMAIL_USER, EMAIL_PASSWORD


app = Flask(__name__)

# Initialize EmailSender
email_sender = EmailSender(SMTP_SERVER, SMTP_PORT, EMAIL_USER, EMAIL_PASSWORD)

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.json
        subject = data.get('subject')
        body = data.get('body')
        to_emails = data.get('to_emails')
        is_html = data.get('is_html', False)

        if not subject or not body or not to_emails:
            return jsonify({"error": "Missing required fields (subject, body, to_emails)"}), 400

        email_sender.send_email(subject, body, to_emails, is_html)
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
