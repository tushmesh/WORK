from flask import Flask, request, render_template_string
import threading
import time
import requests
import secrets
import base64
import hashlib
import webbrowser
import jwt # type: ignore

# Configuration
tenant = 'eff4a4ad-46e1-45b6-a7cd-695cbb6e92e4'
client_id = '932693b6-709a-4278-b4a0-19aec44f92a6'
redirect_uri = 'http://localhost:3000/'
scope = 'api://932693b6-709a-4278-b4a0-19aec44f92a6/.default/Directory.Read.All'
state = '12345'
code_challenge_method = 'S256'
grant_type = 'authorization_code'
client_secret = '<<ADD SECRET>>'

# HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PCG-Copilot Authentication Status</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #f0f0f0; }
        .status-container { text-align: center; padding: 20px; border: 1px solid #ccc; border-radius: 10px; background-color: #fff; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
        .status { font-size: 2em; margin-top: 10px; color: {{ color }}; }
        h1 { color: #333; }
    </style>
</head>
<body>
    <div class="status-container">
        <h1>PCG-Copilot Authentication Status</h1>
        <div id="status" class="status">{{ status }}</div>
    </div>
</body>
</html>
"""

# Utility functions
def generate_code_verifier(length=43):
    return secrets.token_urlsafe(length)[:length]

def generate_code_challenge(code_verifier):
    return base64.urlsafe_b64encode(hashlib.sha256(code_verifier.encode()).digest()).decode().rstrip('=')

# Generate code verifier and challenge
code_verifier = generate_code_verifier()
code_challenge = generate_code_challenge(code_verifier)

# Flask app
app = Flask(__name__)

@app.route('/')
def callback():
    code = request.args.get('code')
    if code:
        token_response = get_oauth_token(code)
        access_token = token_response.get('access_token')
        decoded_token = jwt.decode(access_token, options={"verify_signature": False})
        print(decoded_token)
        return render_template_string(html_template, status='Authenticated', color='green')
    return render_template_string(html_template, status='Not Authenticated', color='red')

def get_oauth_token(code):
    token_url = f'https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token'
    payload = {
        'client_id': client_id,
        'scope': scope,
        'code': code,
        'redirect_uri': redirect_uri,
        'grant_type': grant_type,
        'code_verifier': code_verifier,
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(token_url, data=payload, headers=headers).json()

def run_flask_app():
    app.run(port=3000)

def perform_oauth_get_request():
    url = f'https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize'
    params = {
        'client_id': client_id,
        'response_type': 'code',
        'redirect_uri': redirect_uri,
        'response_mode': 'query',
        'scope': scope,
        'state': state,
        'code_challenge': code_challenge,
        'code_challenge_method': code_challenge_method,
    }
    return requests.Request('GET', url, params=params).prepare().url

def main_code():
    time.sleep(5)
    print("The app TokenGenerator is running...")
    response_url = perform_oauth_get_request()
    webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open(response_url)

if __name__ == '__main__':
    threading.Thread(target=run_flask_app).start()
    main_code()
