import streamlit as st
multi = st.multiselect("Choose multiple:", ['Red', 'Blue', 'Green'])
st.write("Selections:", multi)