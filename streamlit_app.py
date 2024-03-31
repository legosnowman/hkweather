import requests
import streamlit as st
import json

APP_NAME = "HK Weather"

st.set_page_config(
    page_title=APP_NAME,
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("Sidebar")
st.header("HK Weather")

url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=en"
response = requests.get(url)

def hk_weather():
    # The API endpoint
    url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=en"

    # A GET request to the API
    response = requests.get(url)

    #Print the response
    #st.write("response: ", response)
    #st.write("JSON: ", response.json())
    
    #print(type(response_json))
    #if response == 200:
    response_json = response.json()
    st.write(response_json['generalSituation'])
    st.write(response_json['forecastDesc'])
    st.write(response_json['outlook'])
    st.write("Updated: " & response_json["updateTime"])

    st.write("<p>")
    st.write("<B>JSON</B>")
    st.write("JSON: ", response.json())
        
        #if response_json['data'][0] is not None:
        #    epi_one  = response_json['data'][0]
        #    route = epi_one['route']
        #    stop_number = epi_one['stop']
        #    eta = epi_one['eta']
        #    destination = epi_one['dest_en']
        #    list_bus = [route, stop_number, eta, destination]
        #else:
        #    list_bus = ["N/A", "N/A", "N/A", "N/A", "N/A"]

    #else:
    #    list_bus = ["N/A", "N/A", "N/A", "N/A", "N/A"]

    #print (type(epi_one))
    #print(epi_one)
    #print('Route: ', epi_one['route'])
    #print('Stop: ', epi_one['stop'])
    #print('Estimated Arrival Time: ', epi_one['eta'])
    #print('Destination: ', epi_one['dest_en'])



    return 

hk_weather()
