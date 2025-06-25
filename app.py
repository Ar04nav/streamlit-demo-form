import streamlit as st
#Button code:
if st.button("Click Me"):
    st.success("Button Clicked!")

#checkbox:
if st.checkbox("Show/Hide"):
    st.write("You checked the box!")
