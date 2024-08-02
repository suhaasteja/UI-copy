import streamlit as st
import random
from dataclasses import dataclass
from typing import Literal
import base64

sample_responses = [
    """
        Of course! To start your research, you can follow these steps:

        Choose a Topic: Think about what interests you within your field of study. Consider the guidelines of your assignment and choose a topic that is broad enough to find information on but focused enough to not be overwhelming.

        Create a Research Question: Develop a specific research question that will guide your research. Think about the "who, what, where, when, and why" aspects of your topic to help formulate a clear question.

        Background Research: Conduct some preliminary research to familiarize yourself with the topic. Use encyclopedias, textbooks, or reliable websites to gain a basic understanding.

        Identify Keywords: Identify the main concepts of your research question and come up with relevant keywords that you can use when searching for sources.

        Search for Sources: Utilize library databases, online journals, and academic websites to find scholarly articles, books, and other sources related to your topic.

        Evaluate Sources: Make sure to critically evaluate the credibility and relevance of the sources you find to ensure they are suitable for your research.

        Take Notes: As you read through sources, take notes on key points, quotes, and ideas that you may want to include in your research.

        Organize Your Research: Keep track of your sources and notes in an organized manner to make it easier to reference them later.

        If you need help with any specific step or have a particular topic in mind, feel free to share, and I can assist you further!

        For more information, please check: https://libguides.sjsu.edu/glst1b"""
]

@dataclass
class Message:
    origin: Literal["user", "ai"]
    message: str


def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
            #  background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
            background-color: #D2D2D2;
             background-size: contain
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


def load_css():
    # set_bg_hack("./static/bg_img.png")
    with open("./static/styles.css", "r") as file:
        css = f"<style>{file.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)




def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []

def on_click_callback():
    user_prompt = st.session_state.user_prompt
    st.session_state.history.append(Message('user', user_prompt))
    ai_response = ""

    # for event in replicate.stream(
    # "meta/meta-llama-3-70b-instruct",
    # input={ "prompt": user_prompt },
    # ):
    #     ai_response += str(event)

    ai_response = random.choice(sample_responses)
    st.session_state.history.append(Message("ai", ai_response))


initialize_session_state()
load_css()

# st.title("Kingbot GPT")
st.markdown(
        """
        <div style="display: flex; align-items: center; justify-content: center; width: 100%">
            <img src="app/static/kingbot_icon.png" width="55" height="55" style="margin-right: 10px; object-fit: contain">
            <h1>KingbotGPT</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

with st.expander("How does it work?"):
    # st.subheader("Terms & Policy")
    st.markdown(
        """
        KingbotGPT is an experimental python-based bot created by the university library's artificial intelligence (AI) team at San Jose State University. 
        The service is based on the Retrieval Augmented Generation (RAG) method which allows the use of local data to provide the informational content and library website links in a chatbot's response. Local datasets for Kingbot include crawled library website pages, library website research guides, and frequently-asked-questions from previous instances of Kingbot. 
        Langchain and Streamlit are open-source software tools that were used for the user interface, local data, and to manage interactions with the large-language model (LLM). The chatbot relies on the OpenAI API, specifically GPT 3.5 for the LLM component. 
        Please note, AI tools are known to provide incorrect and biased information (known as hallucinations), Kingbot is no exception. Occasionally, Kingbot might also reference external websites outside of the scope of its local data. In addition, the web crawl used for its local data is indexed once a week, which may not reflect the most updated library website information. Users are solely responsible for verifying the accuracy of chatbot responses and are responsible for their reliance on the information provided. We highly encourage users to verify answers with the library website or by contacting a librarian. 
        By using Kingbot, users are acknowledging that they have read, understood, and agreed to our chatbot policy(link), including all terms and conditions, disclaimers, and associated risks.


        Disclaimers
        Kingbot may provide incorrect and biased information.While Kingbot uses  local library website pages and a retrieval augmented generation (RAG) method for its machine learning algorithm, Kingbot's responses are automated and can be unpredictable. The accuracy, relevancy, and completeness of chatbot responses is not guaranteed. We recommend verifying with the library website or by asking a librarian. 
        Kingbot is intended to provide information about the library and library resources. It is for educational and informational purposes only, and may produce faulty or inaccurate information outside of the scope of its local data. 
        Kingbot may occasionally provide links to external sites not operated by the library. If you click on one of those links, you will be directed to the third party's site. SJSU Library is not responsible for the content or privacy policies of third-party sites referred by Kingbot.
        Users are solely responsible for their interactions with Kingbot and their reliance on the information provided. Users are solely responsible for verifying the accuracy of chatbot responses before using or sharing them. 
        The SJSU Library is not responsible or liable for any actions, damages, or losses incurred as a result of using Kingbot.
        Users should refrain from entering any personal, confidential or sensitive information. 
        Users must refrain from entering harmless information. Conversations are continuously reviewed by librarians and library staff on the library AI team.
        Anonymized prompts and chatbot responses may be used for blog posts, research articles, and other educational or informational purposes.


        Contact Us
        If you have any questions about this policy, please contact: 
        Sharesly.Rodriguez@sjsu.edu
        """
    )


with st.sidebar:
    st.markdown(
        """
        <div style="display: flex; align-items: center; justify-content: flex-start; width: 100%">
            <img src="app/static/sjsu_library_logo.png" width="100%" height="100%" style="margin-right: 10px; object-fit: contain">
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("")
    st.markdown("")
    st.markdown(
        """
        KingbotGPT is an experimental python-based bot created by the university library's artificial intelligence (AI)
        team at San Jose State University. It is our newest model of the original After-Hours Kingbot Chatbot. 
        Kingbot is intended to provide basic information about the library and library resources. 
        Kingbot is not a research tool or a replacement for librarian and library staff expertise."""
    )


chat_container = st.container()
input_container = st.form("chat-form", clear_on_submit = True, border=False)

st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

with chat_container:
    for chat in st.session_state.history:
        div = f"""
            <div class="chat-row {"" if chat.origin == "ai" else "row-reverse"}">
                <img src="app/static/{"kingbot_icon.png" if chat.origin == "ai" else "user_icon.png"}" width=30 height=30 class="chat-icon" />
                <div class="chat-bubble {"ai-bubble" if chat.origin == "ai" else "user-bubble"}">
                    {chat.message}
                </div>
            </div>
        """
        st.markdown(div, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
        

# with input_container:
#     cols = st.columns((6, 1))
#     cols[0].text_input(
#         "Chat",
#         # "Hello ",
#         placeholder="Start Typing",
#         label_visibility="collapsed",
#         key="user_prompt"
#     )
#     cols[1].form_submit_button(
#         "submit",
#         on_click=on_click_callback
#     )

# st.chat_input(placeholder="type something" )

# Example prompts
example_prompts = [
    "Get information about library hours",
    "Get information about study rooms",
    "Library events this week",
    "Strategies to start your research",
]

# example_prompts_help = [
#     "Look for a specific card effect",
#     "Search for card type: 'Vampires', card color: 'black', and ability: 'flying'",
#     "Color cards and card type",
#     "Specifc card effect to another mana color",
#     "Search for card names",
#     "Search for card types with specific abilities",
# ]

button_cols = st.columns(4)
button_cols_2 = st.columns(4)

button_pressed = ""

if button_cols[0].button(example_prompts[0]):
    button_pressed = example_prompts[0]
elif button_cols[1].button(example_prompts[1]):
    button_pressed = example_prompts[1]
elif button_cols[2].button(example_prompts[2]):
    button_pressed = example_prompts[2]
elif button_cols[3].button(example_prompts[3]):
    button_pressed = example_prompts[3]

st.chat_input(placeholder="Ask me anything about the SJSU Library!", key="user_prompt", on_submit=on_click_callback)