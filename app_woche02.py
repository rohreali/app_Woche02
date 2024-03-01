import streamlit as st
import pandas as pd

st.title('Wetter-App')
st.header('Das Wetter vom Dienstag dem, 27.02.2024')
st.subheader('Ortschaft: Fislisbach')

col1, col2, col3, col4 =st.columns(4)
col1.metric('Temperatur', '9 °C', '1.4 °C')
col2.metric('Wind', '7 km/h', '-31%')
col3.metric('Feuchtigkeit', '73%', '2%')
col4.metric('Niederschlagswahrscheinlichkeit', '26%', '-10%')

temperature_data = {
    'Tag': ['Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag', 'Montag', 'Dienstag'],
    'Temperatur': [10, 13, 10, 12, 10, 9, 10]
}

data = pd.DataFrame(temperature_data)

st.subheader('Temperaturvorhersage für Fislisbach')
st.write('Dies ist die Temperaturvorhersage für die nächsten 7 Tage in Fislisbach.')

st.subheader('Temperaturvorhersage')
st.line_chart(data.set_index('Tag')['Temperatur'])

with st.sidebar:
    st.subheader('Temperaturen anderer Orte')
    st.write('Hier können Sie die Temperaturen für andere Orte abrufen.')

    st.subheader('Temperaturen des gewählten Ortes:')

    stadt= st.text_input('Geben Sie den Namen Ihres Ortes ein:')

    stadt_temperatures= {
    'Fislisbach': 10,
    'Berlin': 8,
    'Paris': 10,
    'New York': 12,
    'Tokio': 5,
    'Madrid': 10,
    'Alicante': 16
    }

    if stadt:
        if stadt in stadt_temperatures:
            temperature = stadt_temperatures[stadt]
            st.write(f'Die vorhergesagte Temperatur in {stadt} beträgt {temperature} °C.')
        else:
            st.write('Die Temperatur für diesen Ort ist nicht verfügbar.')