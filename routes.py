from flask import  render_template
import nasa_api
from run import app

SECRET_KEY = "KiEVTEhfZhZamuaQ3Hj2TjjHYYAkASrDbgxXT9f0"















@app.route('/')
def index():
    #KiEVTEhfZhZamuaQ3Hj2TjjHYYAkASrDbgxXT9f0
    nasa_api_response = nasa_api.get_data(SECRET_KEY)
    im_url=nasa_api.get_url(nasa_api_response)
    date = nasa_api.get_date(nasa_api_response)

    #pic_path =f'static/temp/{date}.jpg'

    nasa_api.download_image(im_url, date)
    
    #nasa_api.convert_image(pic_path)



    


    return render_template("index.html", date=date, nasa_api=nasa_api, nasa_api_response=nasa_api_response)
