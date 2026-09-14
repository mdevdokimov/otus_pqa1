import os

import requests
from flask import Flask, render_template_string, request

app = Flask(__name__)


@app.after_request
def add_security_headers(response):
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Server"] = "Secure Web Server"
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; style-src 'self' 'unsafe-inline';"
    )
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    app_version = os.environ.get("APP_VERSION", "development")
    weather_data = None
    city = ""

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if city:
            try:
                response = requests.get(
                    f"https://wttr.in/{city}?format=j1&lang=ru", timeout=5
                )
                if response.status_code == 200:
                    data = response.json()
                    condition = data["current_condition"][0]
                    weather_data = {
                        "temp": condition["temp_C"],
                        "humidity": condition["humidity"],
                        "desc": condition.get(
                            "lang_ru", [{"value": condition["weatherDesc"][0]["value"]}]
                        )[0]["value"],
                    }
                    print(weather_data)
            except ValueError:
                weather_data = "ошибка"

    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(base_dir, "templates", "index.html")

    with open(template_path, "r", encoding="utf-8") as f:
        html_template = f.read()

    return render_template_string(
        html_template, weather=weather_data, city=city, version=app_version
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec B104
