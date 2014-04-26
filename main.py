# -*- coding: utf-8 -*-
## @author Vangelis Banos
"""
Main Web App Loop
"""
import datetime
import feedparser
import requests

from flask import Flask, render_template, request
from etc import settings

App = Flask(__name__)


@App.template_filter('strftime')
def _jinja2_filter_datetime(tstamp):
    """Format timestamp integer to dd-mm-yyyy"""
    return datetime.datetime.fromtimestamp(float(tstamp)).strftime('%d-%m-%Y')


@App.template_filter('human_number')
def _jinja2_filter_number(number):
    """Utility function to format number 100000 -> 100.000"""
    if number:
        return '{:,}'.format(int(number)).replace(",", ".")


@App.route("/")
def home():
    """Home page """
    response = requests.get("http://yperdiavgeia.gr/decisions/statistics.json")
    return render_template('home.html', statistics=response.json())


@App.route("/about")
def about():
    """About application information page"""
    return render_template('about.html')


# DIAVGEIA URLS
@App.route("/diavgeia-search", methods=['GET'])
def diavgeia_search():
    """Diavgeia search"""
    if request.args.get('search'):
        query = request.args.get('query')
        response = requests.get(settings.DECISIONS_URL + query)
        doc = feedparser.parse(response.text)
        total = doc['feed']['opensearch_totalresults']
        return render_template(
            'diavgeia-search-results.html',
            results=doc['entries'],
            total=total, query=query
        )
    else:
        return render_template('diavgeia-search-form.html')


@App.route("/diavgeia-search-ajax", methods=['GET'])
def diavgeia_search_ajax():
    """AJAX callback to search diavgeia pages beyond the 1st one"""
    if request.args.get('query') and request.args.get('page'):
        query = request.args.get('query')
        page = request.args.get('page')
        url = settings.DECISIONS_URL + query + "/page:" + page
        response = requests.get(url)
        doc = feedparser.parse(response.text)
        return render_template(
            'diavgeia-search-results-ajax.html',
            results=doc['entries']
        )


@App.route("/decision/<did>", methods=['GET'])
def view_decision(did):
    """Diavgeia view decision"""
    url = "http://yperdiavgeia.gr/decisions/view/%s.json" % did
    response = requests.get(url)
    return render_template('diavgeia-view.html', decision=response.json())


# PROCUREMENT URLS
@App.route("/procurements-search", methods=['GET'])
def procurements_search():
    """Form to search procurements and contracts"""
    if request.args.get('search'):
        query = request.args.get('query')
        response = requests.get(settings.PROCUREMENTS_URL + query)
        doc = feedparser.parse(response.text)
        total = doc['feed']['opensearch_totalresults']
        return render_template(
            'procurements-search-results.html',
            results=doc['entries'],
            total=total,
            query=query
        )
    else:
        return render_template('procurements-search-form.html')


@App.route("/procurements-search-ajax", methods=['GET'])
def procurements_search_ajax():
    """AJAX callback to search procurements and contracts
       beyond the 1st page"""
    if request.args.get('query') and request.args.get('page'):
        query = request.args.get('query')
        page = request.args.get('page')
        url = settings.PROCUREMENTS_URL + query + "/page:" + page
        response = requests.get(url)
        doc = feedparser.parse(response.text)
        return render_template(
            'procurements-search-results-ajax.html',
            results=doc['entries']
        )


@App.route("/procurement/<pid>", methods=['GET'])
def view_procurement(pid):
    """Procurements view doc"""
    url = "http://yperdiavgeia.gr/procurements/view/%s.json" % pid
    print url
    response = requests.get(url)
    return render_template(
        'procurements-view.html',
        procurement=response.json()
    )


# LAWS URLS
@App.route("/laws-search", methods=['GET'])
def laws_search():
    """Form to search Greek Government Gazzette (FEK)"""
    if request.args.get('search') and request.args.get('query'):
        query = request.args.get('query')
        response = requests.get(settings.LAWS_URL + query)
        doc = feedparser.parse(response.text)
        total = doc['feed']['opensearch_totalresults']
        return render_template(
            'laws-search-results.html',
            results=doc['entries'], total=total, query=query
        )
    else:
        return render_template('laws-search-form.html')


@App.route("/laws-search-ajax", methods=['GET'])
def laws_search_ajax():
    """AJAX callback to search laws beyond the 1st page"""
    if request.args.get('query') and request.args.get('page'):
        query = request.args.get('query')
        page = request.args.get('page')
        response = requests.get(settings.LAWS_URL + query + "/page:" + page)
        doc = feedparser.parse(response.text)
        return render_template(
            'laws-search-results-ajax.html',
            results=doc['entries']
        )


@App.route("/law/<lawid>", methods=['GET'])
def view_law(lawid):
    """Laws view doc"""
    response = requests.get("http://yperdiavgeia.gr/laws/view/%s.json" % lawid)
    return render_template('laws-view.html', law=response.json())
