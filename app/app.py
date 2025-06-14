import streamlit as st
from search_movie import search_movie as sm
from main import main as mn
from main import recomend as rd

st.title('Hello👋')
st.title("Welcome to Automated movie 🎥 recomender!")
country_map = {
    "Spain": "ES",
    "Mexico": "MX",
    "Argentina": "AR",
    "Russia": "RU",
    "Colombia": "co",
    "United States": "us",
    "United Kingdom": "gb"
}
country_names = list(country_map.keys())
country_of_choice_name = st.selectbox('Country: ',country_names, 0)
country_of_choice = country_map[country_of_choice_name]
if __name__ == '__main__':
    movie_ids, movie_titles = mn(country_of_choice)
    recomended_movies = []
    user_in = st.slider('please enter the number of movies you want to be recomended:',1, len(movie_ids),1)

    with st.spinner("Fetching recommendations..."):
        for i in range(user_in):
            recomended_movie = rd(movie_ids)
            recomended_movies.append(recomended_movie)
        for recomends in recomended_movies:
            Released_date, Genre, cast, duration, country, desc, img = sm(movie_ids[recomends])
            movie_url = f"https://myflixerz.to/movie/{movie_ids[recomends]}"
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(img)
            with col2:
                st.markdown(f"""
                <div style="background-color:#1a1a1a;padding:10px 10px 8px 8px;border-radius:12px;box-shadow:0 2px 8px #0001;">
                <h3 style="color:#e50914;margin-bottom:0.2em;">🎬 <a href="{movie_url}" target="_blank" style="color:#e50914;text-decoration:none;"><b>{movie_titles[recomends]}</b></a></h3>
                <p> 📅 {Released_date}</p>
                <p>🎭 {Genre}</p>
                <p>👥 {cast}</p>
                <p>⏳ {duration}</p>
                <p>🌎 {country}</p>
                </div>
                """, unsafe_allow_html=True)
                with st.expander("📝 Description"):
                    st.write(desc)
            st.markdown("---")
    st.markdown(
        """
        <hr style="margin-top:40px;margin-bottom:10px;">
        <div style="text-align:center; color: #888; font-size: 1.1em;">
            Made with ❤️‍🔥 by <b>Akafi Hirsi</b> &middot; Powered by <a href="https://github.com/Kafi-Hersi" target="_blank" style="color:#e50914;">Akafi</a>
            <br>
            <span style="font-size:0.9em;">Movie data from <a href="https://myflixerz.to" target="_blank" style="color:#e50914;">MyFlixerz</a></span>
            <br><br>
            <span style="font-size:0.95em; color:#aaa;">
                <b>Safety & Copyright Notice:</b><br>
                This project is for educational and demonstration purposes only.<br>
                All movie data is sourced from MyFlixer. I am not affiliated with MyFlixer, nor do I intend to misuse their data.<br>
                No copyright infringement is intended. I love MyFlixer and am one of their users.<br>
                If you are from MyFlixer and have concerns, please <a href="https://gmail.com/"> contact me </a> and I will take immediate action.
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )
