"""ADVANCED SECURITY BENCHMARK FIXTURES.

Deliberately insecure code for static analyzers only.
No web server is started; none of these functions is invoked.
Never deploy or import these functions in a production application.
"""

from pathlib import Path

import requests
from flask import redirect, render_template_string, request


def unsafe_server_side_request():
    # Positive: attacker-controlled URL forwarded to an outbound HTTP client.
    address = request.args["target"]
    return requests.get(address, timeout=5).text


def unsafe_path_read():
    # Positive: attacker-controlled file path used for local file read.
    candidate = request.args["path"]
    return Path(candidate).read_text(encoding="utf-8")


def unsafe_template_render():
    # Positive: user-supplied template source interpreted by Jinja.
    template_source = request.args["template"]
    return render_template_string(template_source)


def unsafe_external_redirect():
    # Positive: attacker-controlled redirect target.
    return redirect(request.args["next"])


def safe_local_file_read():
    # Negative: fixed file path, no user-provided traversal input.
    return Path("README.md").read_text(encoding="utf-8")


def safe_fixed_redirect():
    # Negative: constant application-local redirect.
    return redirect("/dashboard")


def safe_fixed_template():
    # Negative: fixed template with auto-escaped user input.
    return render_template_string("<p>{{ name }}</p>", name=request.args.get("name", ""))
