import streamlit as st
import pickle

st.header('Predict weight from height')
st.write('Demo of linear regression')

height = st.number_input(label = "Enter the height(inches) ", min_value= 35.0, max_value= 120.0, value = 50.00, step = 1.0)
#print(height)

submitted = st.button("Submit")
if submitted:
    pickled_model = pickle.load(open('model.pkl', 'rb'))
    weight = pickled_model.predict([[height]])
    #print(weight)
    st.write(f"Expected weight value is **{round(weight[0],2)}** pounds")