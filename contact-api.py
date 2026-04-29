from flask import Flask, request, jsonify
import smtplib
import html
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timezone

app = Flask(__name__)

RECIPIENT = "sunny@sunnysmith.com"
SENDER = "noreply@sunnysmith.com"

@app.route("/api/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    subject = request.form.get("subject", "").strip() or "Website Contact"
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        return jsonify({"error": "Missing required fields"}), 400

    if len(name) > 200 or len(email) > 200 or len(subject) > 500 or len(message) > 10000:
        return jsonify({"error": "Field too long"}), 400

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    text_body = (
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Time: {timestamp}\n"
        f"Subject: {subject}\n\n"
        f"Message:\n{message}\n"
    )

    html_body = (
        f"<h3>New Contact Form Submission</h3>"
        f"<p><strong>Name:</strong> {html.escape(name)}</p>"
        f"<p><strong>Email:</strong> {html.escape(email)}</p>"
        f"<p><strong>Time:</strong> {timestamp}</p>"
        f"<p><strong>Subject:</strong> {html.escape(subject)}</p>"
        f"<hr>"
        f"<p>{html.escape(message).replace(chr(10), '<br>')}</p>"
    )

    msg = MIMEMultipart("alternative")
    msg["From"] = f"SunnySmith.com <{SENDER}>"
    msg["To"] = RECIPIENT
    msg["Reply-To"] = email
    msg["Subject"] = f"[Contact] {subject}"
    msg.attach(MIMEText(text_body, "plain"))
    msg.attach(MIMEText(html_body, "html"))

    try:
        with smtplib.SMTP("localhost", 25) as s:
            s.send_message(msg)
        return jsonify({"ok": True}), 200
    except Exception as e:
        app.logger.error(f"Mail send failed: {e}")
        return jsonify({"error": "Failed to send"}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
