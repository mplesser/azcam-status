"""
Browser-based status application.
"""

from flask import Blueprint, render_template

import azcam

status = Blueprint(
    "status",
    __name__,
    static_folder="static_status",
    template_folder="",
)


@status.route("/status", defaults={"page": "status"}, methods=["GET"])
def show_status(page):
    return render_template(f"{page}.html")


def load():
    if azcam.db.get("webserver") is not None:
        azcam.db.webserver.app.register_blueprint(status)

    azcam.log("Loaded azcam_status")
