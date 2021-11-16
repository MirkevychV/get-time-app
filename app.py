from datetime import datetime

import pytz
from flask import Flask
from flask import request
from pytz.exceptions import UnknownTimeZoneError

app = Flask(__name__)


@app.route("/get-time")
def get_time_view() -> dict:
    # Take a timezone from query arguments
    time_zone = request.args.get('timezone')
    return get_time(time_zone)


def get_time(time_zone: str) -> dict:
    """
    Return a dict {"time": current time in timezone 'time_zone'}
    """
    try:
        current_time = datetime.now(pytz.timezone(time_zone))
        time = {"time": current_time.strftime("%H:%M:%S")}
        return time
    except UnknownTimeZoneError:
        return {}  # If invalid timezone


if __name__ == "__main__":
    app.run(debug=True)
