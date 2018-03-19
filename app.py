from flask import Flask, request, jsonify
import urllib
app = Flask(__name__)


@app.route('/link', methods=['POST'])
def get_link():
    tracker = request.form['tracker']

    t = request.form['type']

    base_url = 'https://app.adjust.com/' + tracker

    params = {}

    if t != '':
        if t == 'request':
            deeplink = 'wheely://request/'
            if 'service_id' in request.form and request.form['service_id'] != '':
                deeplink += '?service_id=' + request.form['service_id']
        elif t == 'redeem':
            deeplink = 'wheely://redeem/'
            if 'promocode' in request.form and request.form['promocode'] != '':
                deeplink += '?code=' + request.form['promocode']
        else:
            deeplink = 'wheely://' + t + '/'

        params['deep_link'] = deeplink

    redirect = request.form['redirect']

    if redirect and redirect != '':
        params['redirect'] = redirect

    fallback = request.form['fallback']

    if fallback and fallback != '':
        params['fallback'] = fallback

    qs = urllib.urlencode(params)

    return jsonify({'link': base_url + '?' + qs})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
