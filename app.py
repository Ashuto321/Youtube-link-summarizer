from transformers import pipeline

qa_model = pipeline("question-answering")

# Biased prompt
prompt_biased = "Why do people in group X often do Y?"

# Neutral prompt
prompt_neutral = "What factors influence people to engage in behavior Y?"

response_biased = qa_model({"question": prompt_biased, "context": "..."})
response_neutral = qa_model({"question": prompt_neutral, "context": "..."})

print("Biased Response:", response_biased["answer"])
print("Neutral Response:", response_neutral["answer"])











































# import streamlit as st
# from dotenv import load_dotenv

# load_dotenv() ##load all the nevironment variables
# import os
# import google.generativeai as genai

# from youtube_transcript_api import YouTubeTranscriptApi

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# prompt="""You are Yotube video summarizer. You will be taking the transcript text
# and summarizing the entire video and providing the important summary in points
# within 250 words. Please provide the summary of the text given here:  """


# ## getting the transcript data from yt videos
# def extract_transcript_details(youtube_video_url):
#     try:
#         video_id=youtube_video_url.split("=")[1]
        
#         transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

#         transcript = ""
#         for i in transcript_text:
#             transcript += " " + i["text"]

#         return transcript

#     except Exception as e:
#         raise e
    
# ## getting the summary based on Prompt from Google Gemini Pro
# def generate_gemini_content(transcript_text,prompt):

#     model=genai.GenerativeModel("gemini-pro")
#     response=model.generate_content(prompt+transcript_text)
#     return response.text

# # streamlit app
# st.title("YouTube Transcript to Detailed Notes Converter")
# youtube_link = st.text_input("Enter YouTube Video Link:")

# if youtube_link:
#     video_id = youtube_link.split("=")[1]
#     print(video_id)
#     st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

# if st.button("Get Detailed Notes"):
#     transcript_text=extract_transcript_details(youtube_link)

#     if transcript_text:
#         summary=generate_gemini_content(transcript_text,prompt)
#         st.markdown("## Detailed Notes:")
#         st.write(summary)

import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# header with Edureka 
header = '''
<div class="header">
    <p>YouTube summarizer by Edureka 
'''

# Render header without logo
st.markdown(header, unsafe_allow_html=True)

# Set background image using CSS
page_bg_img = '''
<style>
body {
    background-image: url("https://images.unsplash.com/photo-1511765224389-37f0e77cf0eb");
    background-size: cover;
}
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #262730;
    color: white;
    text-align: center;
    padding: 10px 0;
    font-family: Arial, sans-serif;
}
.header {

    left: 0;
    top: 10;
    width: 100%;
    background-color: #262730;
    color: white;
    text-align: center;
    padding: 10px 0;
    font-family: Arial, sans-serif;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Add YouTube and Edureka logos
# st.markdown("""
#     <div style="text-align: center;">
#         <img src="https://upload.wikimedia.org/wikipedia/commons/7/75/YouTube_social_white_squircle_%282017%29.svg" width="50">
#         <img src=r"C:\Users\Ashutosh Pandey\Desktop\project\edureka-veranda-logo.png" width="150">
#     </div>
# """, unsafe_allow_html=True)

# Create header with logos
st.markdown("""
    <div style="text-align: center;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/7/75/YouTube_social_white_squircle_%282017%29.svg" width="150">
    </div>
""", unsafe_allow_html=True)

# Title of the App
st.markdown("<h1 style='text-align: center; color: #black;'>Your YouTube Video Helper</h1>", unsafe_allow_html=True)

# Prompt for YouTube link
st.markdown("<h3 style='text-align: center; color: #green;'>Enter YouTube Video Link Below:</h3>", unsafe_allow_html=True)
youtube_link = st.text_input("")

# Display YouTube thumbnail if a valid link is provided
if youtube_link:
    try:
        video_id = youtube_link.split("=")[1]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    except IndexError:
        st.error("Please provide a valid YouTube link.")

prompt="""You are Yotube video summarizer. You will be taking the transcript text
 and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """

# Function to extract transcript from YouTube video
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([t["text"] for t in transcript_text])
        return transcript
    except Exception as e:
        raise e

# Function to generate a summary using Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Button to fetch and display the detailed notes
if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link)
    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)

# Footer with Edureka links
footer = '''
<div class="footer">
    <p>Learn more about AI and Machine Learning at <a href="https://www.edureka.co" style="color: #1e90ff;">Edureka</a></p>
</div>
'''
st.markdown(footer, unsafe_allow_html=True)






