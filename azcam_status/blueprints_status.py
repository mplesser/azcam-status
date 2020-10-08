"""
Webobs commands for webobs application.
"""
import os

from flask import Blueprint, request, render_template
from flask.helpers import url_for
from werkzeug.utils import secure_filename

import azcam


class StatusBlueprint(object):
    def __init__(self) -> None:

        status = Blueprint(
            "status",
            __name__,
            static_folder="static_status",
            template_folder="",
        )

        @status.route("/status", defaults={"page": "status"}, methods=["GET"])
        def show_status(page):
            return render_template(f"{page}.html")

        self.app.register_blueprint(status)

        azcam.log("Loaded azcam_status")
