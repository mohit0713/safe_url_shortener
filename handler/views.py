# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
import json
from django.shortcuts import render, render_to_response

API_key = "AIzaSyAVVEZE8mSQcNZ3REEinWPQWSqTypfr64w"


def url_handler(request):
    long_url = request.GET.get('long_url', None)
    short_url = None
    if long_url:
        short_url = shortener_url(long_url)
    return render_to_response('url_form.html', {'short_url': short_url})


def shortener_url(long_url):
    google_url = "https://www.googleapis.com/urlshortener/v1/url?key=" + API_key
    data = json.dumps({'longUrl': long_url})
    result = requests.post(google_url, headers={'content-type': 'application/json'}, data=data)
    short_url = result.json()['id']
    return short_url
