import streamlit as st
from chatbot import get_response

# Page Config
st.set_page_config(
    page_title="SNU College Enquiry Chatbot",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 SNU College Enquiry Chatbot")
st.write("Welcome! Ask me anything about Sister Nivedita University.")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! Welcome to Sister Nivedita University. How can I help you today?"
        }
    ]

# Display Previous Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User Input Box
if user_question := st.chat_input("Ask your question here..."):
    # Display user input immediately
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.write(user_question)

    # Get Bot Response with Spinner
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = get_response(user_question)
            st.write(answer)
    
    # Save Assistant Response
    st.session_state.messages.append({"role": "assistant", "content": answer})
