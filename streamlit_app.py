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
if 'edited_rows' not in st.session_state:
  st.session_state.edited_rows = None

st.write(st.session_state)

view_button = st.button('View')

if view_button or st.session_state.view_state:
  st.session_state.view_state = True
  edited_data = st.data_editor(df)
  st.write(st.session_state)
