from flask import Flask,render_template,request
from datetime import date, datetime
import requests,os


app = Flask(__name__)

# route for 404 error handler
@app.errorhandler(404)
def page_not_found(error):
    #logging.error("Page not found: %s", (request.path))
    return render_template('404.html', title='404 Error', msg=request.path)

# route for 405 error handler
@app.errorhandler(405)
def page_not_found(error):
    #logging.error("Method is not allowed: %s", (request.path))
    return render_template('404.html', title='405 Error', msg=request.path) 

@app.route("/")
def index():

    return render_template('index.html')


@app.route("/weather", methods=['POST'])
def weather():
    if request.method == 'POST':
        city_name = request.form['location']
        city_name = city_name.upper()
        #print(city_name)
        api_key = os.environ['weather_api']
       
        #print(os.environ['weather_api'])
        url= "http://api.openweathermap.org/data/2.5/weather?q="
        full_url = url+city_name+"&appid="+api_key
        req = requests.get(full_url)
        data = req.json() 
        #print(data)
        if data['cod'] == '404':
            #print("Invalid City :- {}, Please Check you city name again".format(city_name))
            return render_template('index2.html')
        else:
            temp = data["main"]["temp"]
            temp_city = round(float(temp - 273.15),1)
            desc = data["weather"][0]["main"]
            pressure = data["main"]["pressure"] 
            humidiy = data["main"]["humidity"] 
            wind_speed = data["wind"]["speed"]
            country = data["sys"]["country"]
            lon = data["coord"]["lon"]
            lat = data["coord"]["lat"]
            sea_level = data["wind"]["deg"] 
            visibility = data["visibility"]
            date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
            
            # print("______________________________________________________________________")
            # print("")
            # print("Weather Data for - {} City ||  {} ".format(city_name.upper(),date_time))
            # print("______________________________________________________________________")

            # #print("Current Country is {} C".format(humidiy) )
            # #print("Current humidiy is {} C".format(humidiy) )
            # print("")
            # print("Current Temprature (In cel) is :- {} C".format(temp_city) )
            # print("Current Peather description is :- {} ".format(desc) )
            # print("Current Pressure is :- {} hpa".format(pressure) )
            # print("Current Humidiy is :- {} %".format(humidiy) )
            # print("Current Wind Speed is :- {} kmph".format(wind_speed) )
            # print("Longitute is :- {} ".format(lon) )
            # print("Lattitute Wind Speed is :- {} ".format(lat) )
            # print("Sea Level is :- {} ".format(sea_level) )
            # print("Visibility is :- {} ".format(visibility) )
    
        
    #return render_template('weather.html',City=city_name)
    return render_template('weather.html',temp=temp_city,desc=desc,pressure=pressure,humidiy=humidiy,wind_speed=wind_speed,
                             country=country,date_time=date_time,city_name=city_name,lon=lon,
                             lat=lat,visibility=visibility,sea_level=sea_level)


if __name__ == '__main__':
    app.run()

