from datetime import datetime, timedelta, date
from RED import nasa_api
import json

NasaApI_KEY='KiEVTEhfZhZamuaQ3Hj2TjjHYYAkASrDbgxXT9f0'


def utils_of_index_page():
     # KiEVTEhfZhZamuaQ3Hj2TjjHYYAkASrDbgxXT9f0
    today = date.today()
    #today = today - timedelta(days=1)
    previous_date = today - timedelta(days=1)
    print(today)
    print(previous_date)

    nasa_api_response = nasa_api.get_data(NasaApI_KEY, today)
    print("todays --",type(nasa_api_response))

    previous_nasa_api_response = nasa_api.get_data(NasaApI_KEY, previous_date)
    print("\nprevious days --",previous_nasa_api_response['url'])
    jsondata = json.dumps(previous_nasa_api_response)
    print(jsondata)


    im_url = nasa_api.get_url(nasa_api_response)
    im_url_previous = nasa_api.get_url(previous_nasa_api_response)

    present_date = nasa_api.get_date(nasa_api_response)
    yesterday = nasa_api.get_date(previous_nasa_api_response)

    nasa_api.download_image(im_url, present_date)
    nasa_api.download_image(im_url_previous, yesterday)
    pass