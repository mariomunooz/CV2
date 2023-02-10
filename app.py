#  pip install requests streamlit streamlit_lottie bokeh==2.4.1
from pathlib import Path
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from bokeh.models.widgets import Div

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "CV.pdf"

st.set_page_config(
    page_title="🚀 Mario Portfolio Page 🚀",
    page_icon=":boy:",
    layout="wide",
)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


#  To get rid of the Streamlit branding stuff
local_css("css/styles.css")

#  Anchor
st.title("#")  # This anchor is needed for the page to start at the top when it is called.

# --- INTRO ---
with st.container():
    col1, col2 = st.columns((2, 1))
    with col1:
        st.title("Welcome to my Portfolio Page!")
        st.subheader("Hi, I am Mario 🤗")
        st.subheader(
            """
            I'm a Barcelona-based *Junior Data Scientist* who starts his journey in the broad field of *Machine Learning*
            """
        )
        st.write("""""")
        st.subheader(
            """
            This page is actually made with Python :snake: and the associated Streamlit library. Even though the purpose of this library is mainly data science, this page is made to showcase that even with no knowledge of Web Development you can make a nice looking portfolio page with pure Python code.
            """
        )
    with col2:
        st_lottie(
            load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_rclfnagr.json"),
            height=500,
        )

# --- ABOUT ---
with st.container():
    st.write("---")
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        st_lottie(
            load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_aaleelx7.json"),
            height=500,
        )
    with col2:
        st_lottie(
            load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_WdTEui.json"),
            height=500,
        )

    with col3:
        st.header("About")
        st.write(
            """
            I have been analysing data professionally since 2018, starting with Python, Power BI, MS Excel and CartoDB to make strategic reports for the city council of my city 🐱‍👤
            
            Short facts & milestones:
            - BEng Mathematical Engineering in Data Science (Pompeu Fabra University) (Currently in my last year) 
            - MOOC Elements of AI (University of Helsinki)
            - BA Political and Administration Sciences (University of Barcelona)
            - Professional experience in the fraud department of an investment bank
            - Helped the Hospitalet City Council in obtaining a subsidy of 2.4 million euros from Spanish Government.
            - Former Youth Basketball Coach and Analyst of Club Joventut Badalona
            - Enthusiasm for data science, machine learning and ball sports (Basketball, football and beach volleyball)
            If you are interested in building something together, have questions/suggestions about my code or just wanna connect, feel free to get in touch with me! 
            """
        )
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",)

# --- TECH STACK / SKILLS ---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Tech Stack / Skills")
        st.write(
            """
            Languages
            - Python (Scikit-learn, Pandas, Numpy, Matplotlib, Scipy), SQL, R, C, C++, Java
            Web Scrapping
            - Scrappy, Selenium, Beautiful Soup, Requests
            Parallel Programming
            - AWS, OpenMP API, OpenACC, CUDA
            Data Visualization
            - PowerBi, MS Excel, matplotlib, ggplot2, rayshader
            Databases
            - MySQL
            Hosting & Cloud
            - AWS, Streamlit Cloud 😉
            Miscellaneous
            - Git, Github
             """
        )

    with col2:
        st_lottie(
            load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_vybwn7df.json"),
            height=500,
        )

# --- PORTFOLIO ---
with st.container():
    st.write("---")
    st.header("Portfolio")
    st.write("##")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Application of classification in Marketing and Sales")
        st.write("""This project uses supervised classification techniques to identify new customers and predict 
        customer behavior in a marketing use case. It includes data preparation, model training, and identifying 
        important features to improve classification and create a business opportunity.
        """)
        with st.expander('Takeaways'):
            st.write("""
            \n- The main differences between the customer and non-customer datasets are that 
            customer has a higher number of employees and more outliers in Revenues. 
            \n- The top 3 features to discriminate 
            between non customers and customers.  Are mobile potential, an estimation of the total annual expense that a 
            company can do in telco services, including IoT. Revenue, annual incomes of the company. And the City where 
            the company is located
            \n- We have detected 208 non costumers to send to the sales managers to sell our products""")
        if st.button('Github', key="ews_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/mariomunooz/MACHINE_LEARNING/blob/main/Application_of_classification_in_Marketing_and_Sales_.ipynb')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

    with col2:
        st.subheader("Data Preparation")
        st.write(
            "In this project, we will focus on data preparation, a crucial step in any data mining project. We will cover initial steps of understanding and preparing a new dataset, including Exploratory Data Analysis, Feature engineering, dealing with missing values, standardizing numerical columns, converting categorical columns to binary variables, managing dates and periods, and generating new features")
        with st.expander('Takeaways'):
            st.write("""
            \n- The consumers of iPhone usually have more data traffic than the consumers of samsung
            \n- The customers with higher usage of data traffic also have higher billing amounts""")
        if st.button('Github', key="ccw_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/mariomunooz/Data-Mining/blob/main/Data_Mining_data_preparation.ipynb')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    with col3:
        st.subheader("Find near-duplicates using shingling")
        st.write(
            "In this project, we will detect duplicate tweets using shingling, which involves comparing the overlapping sequences of words (ngrams) to measure similarity. We will use the Jaccard index and fixed-length signatures to speed up the process and approximate the similarity.")
        with st.expander('Takeaways'):
            st.write("""
            \n - 294 documents have at least 50 signature matches, which includes both full matches and partial matches.
            \n - The tweet with the largest difference between full matches and partial matches is from an official channel and contains important information about COVID-19 during a time when information was limited.
            \n""")
        if st.button('Github', key="gee_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/mariomunooz/Data-Mining/blob/main/Data_Mining_Find_near_duplicates_using_shingling.ipynb')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)


with st.container():
    col4, col5, col6 = st.columns(3)
    with col4:
        st.subheader("Association Rules")
        st.write("""Association rule mining techniques are useful to analyze datasets consisting of transactions, 
        in which each transaction is a collection of items. We will use a well-known dataset named Instacart 
        containing more than 3 million orders of products through a grocery shopping app""")
        with st.expander('Takeaways'):
            st.write(""" 
            \n- There is a strong association between the study of Mathematical Engineering on 
            Data Science in UPF and coming from a public school, with a high confidence level of 98% and a lift of 26.00. 
            \n- There is a strong association between the study of Global Studies in UPF and coming from a private 
            school, with a high confidence level of 98% and a lift of 20.46. 
            \n- Based on basket analysis, 
            there are recommendations for purchasing related products such as "Organic Fiber & Protein Pear Blueberry & 
            Spinach Baby Food" when buying certain snacks, or "Sweeper Open Window Fresh Scent Wet Mopping Cloths Refill" 
            when buying "Sweeper Dry Sweeping Refills". These recommendations are based on the correlation found through 
            association rule mining.""")
        if st.button('Github', key="ewt_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/mariomunooz/Data-Mining/blob/main/Data_Mining_association_rules.ipynb')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

    with col5:
        st.subheader("Recommendations engines (interactions-based)")
        st.write(
            """For this project we builded and applied an item-based and model-based collaborative filtering recommenders for movies.""")
        with st.expander('Takeaways'):
            st.write("""We have compiled two separate lists of movies, each tailored to a specific genre preference. 
            The first list is recommended for individuals who enjoy superhero movies and includes films such as "X2: 
            X-Men United" and "Final Fantasy: The Spirits Within," which possess fantastical elements and feature 
            superhuman characters. The second list is recommended for those who prefer drama movies and includes 
            films such as "Lord of the Rings: The Fellowship of the Ring," "Gladiator," and "Finding Forrester,
            " which are renowned for their powerful storytelling and dramatic plot and themes.""")
        if st.button('Github', key="eb_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/mariomunooz/Data-Mining/blob/main/Data_Mining_Item_based_recsys.ipynb')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

    with col6:
        st.subheader("Outlier Analysis")
        st.write("""This analysis aims to identify whether a patient is hypothyroid by building three classes: normal 
        (not hypothyroid), hyperfunction and subnormal functioning. Both training and testing instances were used for 
        outlier detection and only 6 real attributes were considered.""")
        with st.expander('Takeaways'):
            st.write("""
            \n- The features f4 and f6 were identified as useful in differentiating between normal and abnormal thyroids.
            \n- The threshold of 0.45 outlier score was chosen as it balances accuracy and recall in this medical case.
            \n- Results for this threshold yielded an accuracy of 0.68, normal precision of 0.38, abnormal precision of 0.98, recall of 0.95, Specificity of 0.61, False positive rate of 0.39 and False negative rate of 0.05.

            """)
        if st.button('Github', key="ec_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/mariomunooz/Data-Mining/blob/main/Data_Mining_Item_based_recsys.ipynb')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)



with st.container():
    col7, col8, col9 = st.columns(3)

    with col7:
        st.subheader("Forecasting")
        st.write("""In this project we have done some time series forecasting on a weather-related time series, 
        which contains temperature, precipitation, and wind speed data for the Barcelona airport.""")
        with st.expander('Takeaways'):
            st.write("""
            \n- Seasonality is observed for temperature but not for rainfall.
            \n- Temperature follows a sinusoidal pattern, which can be used for forecasting, but rainfall does not have a set pattern that helps in predicting future values.

            """)
        if st.button('Github', key="ed_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/mariomunooz/Data-Mining/blob/main/Data_Mining_forecasting.ipynb')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

    with col8:
        st.subheader("2D and 3D Shotchart Visualisation")
        st.write("""This task involves analyzing and visualize a dataset of basketball shot coordinates and outcomes to determine 
        the effective field goal percentage and shot distribution for two teams within different shot zones on the 
        court. """)
        with st.expander('Visualisations'):
            st.image('https://i.imgur.com/CelxplN.jpeg')
        if st.button('Github', key="ee_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/mariomunooz/shotchart-visualisation-code')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

    with col9:
        st.subheader("ACB Web Scrapping of players information")
        st.write("""The Liga ACB is a professional indoor basketball league in Spain, featuring 18 teams. The dataset was 
        obtained by web scraping player information, including ACB ID, name, image URL, birth place, birth date, height, 
        position, nationality, games played, and minutes played, as well as career, national team competitions, titles, 
        awards and stats per season. The data is stored in a MySQL database and the code for obtaining the data requires 
        the user to input their MySQL server password in the pipelines.py file. """)
        with st.expander('MySQL Output'):
            st.image('https://i.imgur.com/Rizm3G1.jpeg')
        if st.button('Github', key="ek_github"):
            st.write('Github opens in new browser tab')
            js = "window.open('https://github.com/mariomunooz/ACB-scrapper')"  # New tab or window
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)



# --- CONTACT ---
with st.container():
    st.write("---")
    st.markdown("<h2 style='text-align: center;'>Contact</h2>", unsafe_allow_html=True)
    st.write("##")

    col1, col2, col3 = st.columns(3)
    with col2:
        contact_form = """
        <form action="https://formsubmit.co/41d6dd1d29966c0fa82067e358f19810" method="POST">
            <input type="hidden" name="_captcha" value="true">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

with st.container():
    for i in range(8):
        st.write("##")
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.write(
            """
            Feel free to copy this page 👍
            """
        )
    with col2:
        st.markdown("<p style='text-align: right;'>Made in 2022 with ❤, 🐍 and Streamlit</p>", unsafe_allow_html=True)
    st.write("---")
