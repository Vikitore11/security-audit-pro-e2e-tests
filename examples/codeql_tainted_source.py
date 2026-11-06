# TEST-ONLY vulnerability fixture. Not executable in production.
from flask import Flask, request
from examples.codeql_tainted_sink import run_dns_lookup

app = Flask(__name__)

@app.get('/scanner-only-dns')
def receive_untrusted_hostname():
    host = request.args.get('host', '')
    return run_dns_lookup(host)
