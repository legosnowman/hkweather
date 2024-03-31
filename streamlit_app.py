import requests
import streamlit as st
import json
import streamlit.components.v1 as components

APP_NAME = "HK Weather"

st.set_page_config(
    page_title=APP_NAME,
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("Sidebar")



#url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=en"
#response = requests.get(url)

def hk_weather():
    # The API endpoint
   
    with st.sidebar:
        with st.form("weather_form"):
            lang = st.radio("Language",("English", "Traditional Chinese"))
            check_fn=st.form_submit_button("Go")

    if lang == "English":
        st.header("HK Weather")
        st.subheader("Information provided by Hong Kong Observatory")
        url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=en"
    else:
        st.head("香港 天氣")
        st.subheader("資料由香港天文台提供")
        url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=tc"

    
    #url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=tc"

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
    st.write("Updated: " + response_json["updateTime"])

    #st.write("JSON: ", response.json())
        
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
