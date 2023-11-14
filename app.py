import streamlit as st
import requests
from PIL import Image

#Setting page header
#emoji cheat sheet: https://www.webfx.com/tools/emoji-cheat-sheet
#https://www.youtube.com/watch?v=VqgUkExPvLY
st.set_page_config(page_title="My Webpage", layout="wide")

#Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

#---- LOAD ASSETS ----
img_f1 = Image.open("images/f1_2021.jpg")
img_nfl = Image.open("images/nfl.jpg")
img_lda = Image.open("images/lda_topics.png")
img_jh = Image.open("images/jack_3.jpg")


#-----HEADER SECTION-----
with st.container():
    st.subheader("Hi, I'm Jack")
    st.title("A data professional from Chicago")
    st.header("My Professional Experience")
    st.write('##')
    st.write(
    """
    My professional experience covers the entire analytics lifecycle. I have developed enterprise data warehouses in Snowflake; led Tableau implementations; and led machine learning pipelines.
    My industry focus has been primarily focused on financial services, both in a Consulting and industry focus. I started my career as an investment Research & Strategy at LaSalle Investment Management, and joined another firm a few years later.
    After spending 6 years focused on real estate markets & private equity, I pivoted into Consulting to broaden my horizons. I started out at a boutique consulting firm in Chicago focused on data analytics consulting, 
    and currently work for Deloitte, where I help companies use machine learning to transform financial planning. On my current client engagements I utilize tools like Databricks, Snowflake, and EC2 to deliver accurate forecasts & timely pipelines.
    """
    )

#----WHAT I DO----
with st.container():
    st.write("----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Who I Am")
        st.write("##")
        st.write(
    """
    I am a data professional currently working as a Senior Consultant at Deloitte. I love music, sports, and learning new things. This is a website to track my personal analytics work. 
    Most of my 'for fun' analytics projects involve sports data of some sort; I have no special conviction about sports data, but it's more fun to analyze things you're interested in!
    In my professional career, I've worked with lots of softwares used data to do many things -- summarize performance, predict the future, organize business metrics -- so in my personal interest, it's all about staying sharp & doing things that are fun.
    The projects in this site are by no means enterprise-worthy, and mostly exploratory in nature, but I enjoyed them & that's what counts!
    
    """
        )
    with right_column:
        st.image(img_jh, width = 450)
        
#---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_f1, width = 300)
    with text_column:
        st.subheader("F1 Analysis")
        st.write(
    """
    I did a quick analysis of F1's 2021 season to understand how each driver fared against his teammate. I used Python & wrote a simple analysis.
    This analysis is summarized in several key charts -- nothing fancy -- but I like it because, as an avid F1 fan, the conclusions from the analytics ring true with the 'eye test' of what happened that season.
    """ 
        )
        st.markdown("[Check out the code:](https://github.com/jackhopper/F1-Analysis/blob/main/f1_all_quali_analysis.ipynb)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_nfl, width = 300)
    with text_column:
        st.subheader("Big Data Bowl 2023")
        st.write(
    """
    I did an analysis as part of the 'Big Data Bowl' 2023 with some classmates to analyze NFL data about defenses. 
    I wanted to understand if there was a way to predict whether a lineman would be beaten by a defender, using a basic set of descriptive data and play outcomes. 
    I was not able to build a successful model; still, this was a fun, self-guided exercise in data exploration and model building in R, and I enjoyed it.
    """   
        )
        st.markdown("[Check out the code:](https://htmlpreview.github.io/?https://github.com/jackhopper/data-bowl-23/blob/main/big_data_bowl_jh.html)")
        
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lda, width = 300)
    with text_column:
        st.subheader("Text Analysis - Family Documents")
        st.write(
    """
    As I finished grad school, I wanted to make sure the analytics techniques I learned didn't go to waste. 
    As I was finishing up the class 'Unstructured Data Analytics,' my family started going through my grandfather's old writings. They were fascinating to read.
    I thought this could be a fun test case to apply a cool method I learned about in school called 'LDA' text analytics: unsupervised Machine Learning that groups discrete topics together within a text document.
    """   
        )
        st.markdown("[Check out the code:](https://htmlpreview.github.io/?https://github.com/jackhopper/Document-Classification/blob/main/RSB-Memoir-Classification.html)")
        
        
###-- CONTACT ---
with st.container():
    st.write("---")
    st.header("Get in Touch with Me!")
    st.write("##")
    
    #Documentation: https://formsubmit.co/ 
    contact_form = """
    <form action="https://formsubmit.co/jackhopper24@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your name" required>
     <input type="email" name="email" placeholder = "Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """
    
    left_column, right_column = st.columns(2)
    with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()