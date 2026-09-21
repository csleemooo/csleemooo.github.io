"""Small GitHub API helper. Credentials stay in memory and are never printed."""
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

REPO = 'csleemooo/csleemooo.github.io'

def request(method, path, payload=None):
    env = dict(os.environ, GCM_INTERACTIVE='never', GIT_TERMINAL_PROMPT='0')
    result = subprocess.run(['git', '-c', 'safe.directory=' + os.getcwd().replace(chr(92), '/'), 'credential', 'fill'], input='protocol=https\nhost=github.com\nusername=csleemooo\n\n', text=True, capture_output=True, env=env, check=True)
    credential = dict(line.split('=', 1) for line in result.stdout.splitlines() if '=' in line)
    token = credential.get('password')
    if not token:
        raise RuntimeError('No GitHub credential available')
    req = urllib.request.Request('https://api.github.com' + path, data=json.dumps(payload).encode() if payload is not None else None, method=method, headers={'Accept': 'application/vnd.github+json', 'Authorization': 'Bearer ' + token, 'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'Chanseok-Homepage-Publisher', 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as error:
        return error.code, json.load(error)

def main():
    operation = sys.argv[1]
    if operation == 'inspect':
        status, user = request('GET', '/user')
        print(json.dumps({'user_status': status, 'login': user.get('login')}, ensure_ascii=False))
        for endpoint in ['/repos/' + REPO, '/repos/' + REPO + '/pages']:
            status, result = request('GET', endpoint)
            print(json.dumps({'endpoint': endpoint, 'status': status, **{key: result.get(key) for key in ['full_name','html_url','private','default_branch','build_type','source','message']}}, ensure_ascii=False))
    elif operation == 'create':
        status, result = request('GET', '/repos/' + REPO)
        if status == 404:
            status, result = request('POST', '/user/repos', {'name': 'csleemooo.github.io', 'description': 'Chanseok Lee — Physics-based computational imaging and inverse problems', 'homepage': 'https://csleemooo.github.io', 'private': False, 'auto_init': False})
        print(json.dumps({'status': status, 'full_name': result.get('full_name'), 'html_url': result.get('html_url'), 'message': result.get('message')}))
    elif operation == 'pages':
        status, result = request('GET', '/repos/' + REPO + '/pages')
        if status == 404:
            status, result = request('POST', '/repos/' + REPO + '/pages', {'build_type': 'legacy', 'source': {'branch': 'main', 'path': '/'}})
        print(json.dumps({'status': status, **{key: result.get(key) for key in ['html_url','status','build_type','source','message']}}, ensure_ascii=False))
    elif operation == 'status':
        for endpoint in ['/repos/' + REPO + '/pages', '/repos/' + REPO + '/pages/builds/latest']:
            status, result = request('GET', endpoint)
            print(json.dumps({'http_status': status, **{key: result.get(key) for key in ['html_url','status','commit','error','source','message']}}, ensure_ascii=False))

if __name__ == '__main__':
    main()
