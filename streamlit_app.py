import streamlit as st
import pandas as pd

st.write('App')
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

if 'view_state' not in st.session_state:
  st.session_state.view_state = False

view_button = st.button('View')

if view_button or st.session_state.view_state:
  edited_data = st.data_editor(df)
  st.write(st.session_state)
