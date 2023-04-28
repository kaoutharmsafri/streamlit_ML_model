import streamlit as st
import pandas as pd
import joblib
import numpy as np
import streamlit as st
image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrWomd9b3prDEAoQIj0SZhcBj0RDzOdS25K-lmyZo&s'
link = 'https://github.com/kaoutharmsafri/streamlit_ML_model.git'
mdsef = 'https://lh3.googleusercontent.com/HgmxZ0Elx6MwjHXoomiG20On6YV9Whw60tmrQVM-YduVJT3uFYErzxCC3hcDNFSlamPS1a64WFkkDhiH5vwNIiB8n-331_ELMRsGbKfDtTw9mFveUj7rKcNt7LxYcE3Z4A=w1280'

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f'<a href="{link}"><img src="{image}" width="30px" height="30px"></a>', unsafe_allow_html=True)
with col2:
    st.write('')
with col3:
    st.image(mdsef, width=100)

st.markdown("""
<style>
    h1 {
        color: #ff4b4b;
        font-size: 36px;
        text-align:center;
    }
    a {
        color: #ff4b4b;
    }
</style>
""", unsafe_allow_html=True)

st.write("""
# Profit prediction from Startup spendings App
This app predicts the **Profit** that a startup can make!
""")
mul_reg=open("multiple_linear_model.pkl","rb")
ml_model=joblib.load(mul_reg)

st.sidebar.header('User Input Parameters')


def user_input_features():
    state = st.sidebar.radio(
    "Select a state :",
    ('New York', 'California', 'Florida'))

    if state == 'New York':
        st.sidebar.write('You selected New York.')
        NewYork = 1.0
        California = 0.0
        Florida = 0.0
    elif state == 'California':
        st.sidebar.write("You selected California.")
        NewYork = 0.0
        California = 1.0
        Florida = 0.0
    elif state == 'Florida':
        st.sidebar.write("You selected Florida.")
        NewYork = 0.0
        California = 0.0
        Florida = 1.0
    RnD_Spend = st.sidebar.number_input('Research and Development Spendings in USD:',key='RnD_Spend')
    Admin_Spend = st.sidebar.number_input('Administration Spendings in USD:',key='Admin_Spend')
    Market_Spend = st.sidebar.number_input('Marketing spendings in USD:',key='Market_Spend')

    data = {'state': state,
            'RnD_Spend': RnD_Spend,
            'Admin_Spend': Admin_Spend,
            'Market_Spend': Market_Spend}
    features = pd.DataFrame(data, index=[0])
    pred_args=[NewYork,California,Florida,RnD_Spend,Admin_Spend,Market_Spend]
    pred_args_arr=np.array(pred_args)
    pred_args_arr=pred_args_arr.reshape(1,-1)
    model_prediction=ml_model.predict(pred_args_arr)
    model_prediction=round(float(model_prediction),2)
    return features,model_prediction

df,prediction = user_input_features()

st.subheader('User Input parameters')
st.write(df)

st.subheader('Prediction')
st.markdown(f'<h1 style="text-align:left;font-size:23px;">{prediction}</h1>', unsafe_allow_html=True)

fsjes = 'https://lh4.googleusercontent.com/dx5d9yF13P_2Sh2F3fs4Xf_UhoIE4fkgNd5OG1gbeazW6BG_PV9J2iLDl5qDqqksW6Gfq-QzTZgBebsoTSUe_fmSe6sA2qWB8LZiNVdcMNmFRVar96VunZuJVaee7rs3Mw=w1280'
uae = 'https://lh4.googleusercontent.com/ljSifZp8JYupVA7RxN_sd46i7ZWa_NBwj3NTVjAVEsGQAzMLdpOTvHDKoUc1-FXejF9gL7bCkkZcvkP9LcsTBb78wv2NyhqZ-A4NJ012W76NwYsusYPeXQrkh3mqqq-5wQ=w1280'

col1, col2 = st.columns(2)
with col1:
    st.image(uae, width=100)
with col2:
    st.image(fsjes, width=100)
