# from urllib.request import urlopen
# import json
# from pprint import pprint as pp


# url = "https://covidtracking.com/api/states/daily"
# response = urlopen(url)
# j = json.load(response)
# pp(j)

from flask import Flask, render_template, url_for
from cgitb import text
import json
from lib2to3.pgen2 import driver
from django import urls
from selenium.webdriver.chrome.service import Service

from jinja2 import Environment, FileSystemLoader
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time




app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Credits")
def Credits():
    return render_template("Credits.html")

@app.route("/Nepal/")
def Nepal():
    serv_obj = Service("C:\Program Files (x86)\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)

    driver.get("https://www.worldometers.info/coronavirus/country/nepal/")
    driver.maximize_window()

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.implicitly_wait(10)
    Nepaldatas = driver.find_elements(By.CSS_SELECTOR, "div.maincounter-number")
    NepaltotalCases = Nepaldatas[0].text
    NepaltotalDeaths = Nepaldatas[1].text
    NepaltotalRecovered = Nepaldatas[2].text
    return render_template("Nepal.html",NepaltotalCases= NepaltotalCases, NepaltotalDeaths= NepaltotalDeaths, NepaltotalRecovered= NepaltotalRecovered)

@app.route("/World/")
def World():
    serv_obj = Service("C:\Program Files (x86)\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)

    driver.get("https://www.worldometers.info/coronavirus/")
    driver.maximize_window()

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.implicitly_wait(10)
    datas = driver.find_elements(By.CSS_SELECTOR, "div.maincounter-number")
    totalCases = datas[0].text
    totalDeaths = datas[1].text
    totalRecovered = datas[2].text

    element = driver.find_element(By.CLASS_NAME, 'panel-heading')
    element.click()

    #div.number-table-main
    activeDatas = driver.find_elements(By.CSS_SELECTOR, "div.number-table-main")
    currentlyInfected = activeDatas[0].text
    return render_template("World.html",totalCases= totalCases, totalDeaths= totalDeaths, totalRecovered= totalRecovered, currentlyInfected= currentlyInfected)


@app.route("/Nepal/newCases/")
def NepalNewCases():
    return render_template("NewCasesRecorded.html")


@app.route("/Nepal/newDeaths/")
def NepalNewDeaths():
    return render_template("NewDeathsRecorded.html")


   


# @app.route('/login/')
# def login():
#     return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)