from flask import render_template
from datetime import datetime, timedelta, date
import nasa_api
from run import app

SECRET_KEY = "KiEVTEhfZhZamuaQ3Hj2TjjHYYAkASrDbgxXT9f0"


@app.route('/')
def index():
    # KiEVTEhfZhZamuaQ3Hj2TjjHYYAkASrDbgxXT9f0
    today = date.today()
    previous_date = today - timedelta(days=1)
    print(today)
    print(previous_date)

    nasa_api_response = nasa_api.get_data(SECRET_KEY, today)

    previous_nasa_api_response = nasa_api.get_data(SECRET_KEY, previous_date)

    im_url = nasa_api.get_url(nasa_api_response)
    im_url_previous = nasa_api.get_url(previous_nasa_api_response)

    present_date = nasa_api.get_date(nasa_api_response)
    yesterday = nasa_api.get_date(previous_nasa_api_response)

    nasa_api.download_image(im_url, present_date)
    nasa_api.download_image(im_url_previous, yesterday)

    return render_template("index.html", present_date=present_date, yesterday=yesterday, nasa_api=nasa_api, previous_nasa_api_response=previous_nasa_api_response,nasa_api_response=nasa_api_response)


@app.route('/science')
def science():
      return render_template('science.html')
















  #d = datetime.date.today()
    #da = datetime.datetime.now()
    #print(" Todays date ", d)

    # taking input as the date

    # carry out conversion between string
    # to datetime object
    #Begindate = datetime.strptime(Begindatestring, "%Y-%m-%d")

  #pic_path =f'static/temp/{date}.jpg'
  # nasa_api.convert_image(pic_path)
 
