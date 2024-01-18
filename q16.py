# 16.	Write a program that will determine weather when the value of temperature and humidity is provided by the user.
# TEMPERATURE(C)      HUMIDITY(%)      WEATHER

    #   >= 30                             >=90                Hot and Humid
    #   >= 30                             < 90                 Hot
    #   <30                                >= 90               Cool and Humid
    #   <30                                 <90                 Cool
def weather(temperature,humidity):
    if temperature >= 30 and humidity >= 90:
        return "Hot and Humid"
    elif temperature >= 30 and humidity < 90:
        return "Hot"
    elif temperature < 30 and humidity >= 90:
        return "Cool and Humid"
    elif temperature < 30 and humidity < 90:    
        return "Cool"

temperature = int(input("Enter the tempreture: "))
humidity = int(input("Enter the humidity: "))

weather_report = weather(temperature, humidity)
print("Weather is:",weather_report)