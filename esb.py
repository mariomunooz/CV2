with col9:
    st.subheader("ACB Web Scrapping of players information")
    st.write("""The Liga ACB is a professional indoor basketball league in Spain, featuring 18 teams. The dataset was 
    obtained by web scraping player information, including ACB ID, name, image URL, birth place, birth date, height, 
    position, nationality, games played, and minutes played, as well as career, national team competitions, titles, 
    awards and stats per season. The data is stored in a MySQL database and the code for obtaining the data requires 
    the user to input their MySQL server password in the pipelines.py file. """)
    with st.expander('MySQL Output'):
        st.image('https://i.imgur.com/Rizm3G1.jpeg')
    if st.button('Github', key="ee_github"):
        st.write('Github opens in new browser tab')
        js = "window.open('https://github.com/mariomunooz/ACB-scrapper')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)
