import os
import time
from google import genai
import streamlit as st

# Streamlit secrets ya environment variable se API key secure tarike se lena
try:
    api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
except Exception:
    api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


# ==========================================
# SISTER NIVEDITA UNIVERSITY CHATBOT
# ==========================================

# 1. College information using Dictionary

college = {
    "name": "Sister Nivedita University",
    "short_name": "SNU",
    "location": "DG 1/2, New Town, Action Area 1, Kolkata - 700156",
    "email": "info@snuniv.ac.in",
    "website": "https://www.snuniv.ac.in/"
}
# ==========================================
# SNU FAQ KNOWLEDGE BASE
# ==========================================

faq = {

    "located": 
    "Sister Nivedita University is located at DG 1/2, New Town, Action Area 1, Kolkata - 700156.",

    "website":
    "Official website: https://www.snuniv.ac.in/",

    "email":
    "SNU email: info@snuniv.ac.in",

    "engineering":
    "SNU offers Engineering programs including B.Tech courses.",

    "btech":
    "B.Tech at SNU is a 4-year undergraduate engineering program.",

    "admission":
    "Admission process: Register on the admission portal, fill the application form, pay the application fee and submit your application.",

    "timing":
    "SNU helpline timing is 10 AM to 6 PM."
}
# 2. Helpline information

helpline = {
    "numbers": [
        "7595044470",
        "7595044471",
        "7595044472",
        "7595044473",
        "1800 2588 155 (Toll Free)"
    ],
    "timing": "10 AM to 6 PM"
}

# 3. Course information

courses = [
    "Engineering",
    "Management",
    "Science",
    "Law",
    "Pharmacy",
    "Nursing",
    "Humanities",
    "Architecture",
    "Media and Design",
    "Agriculture",
    "Performing Arts"
]

# Course details

course_details = {

    "btech": {
        "duration": "4 years",
        "level": "Undergraduate",
        "eligibility": "10+2 with required subjects"
    },

    "bba": {
        "duration": "3 years",
        "level": "Undergraduate"
    },

    "mba": {
        "duration": "2 years",
        "level": "Postgraduate"
    }

}

# 4. Admission information

admission = {
    "steps": [
        "Register on the official admission portal.",
        "Fill in the application form.",
        "Pay the application fee.",
        "Submit your application.",
        "Wait for official admission confirmation."
    ],
    "website": "https://admissions.snuniv.ac.in/"
}

# 5. Function to show welcome message

def welcome():
    print("\n====================================")
    print("   WELCOME TO SNU COLLEGE CHATBOT")
    print("====================================")
    print("Hello! I am your college enquiry assistant.")
    print("How can I help you today?")
    print("\nYou can ask me about:")
    print("1. College Information")
    print("2. Courses")
    print("3. Fees")
    print("4. Admission")
    print("5. Contact and Helpline")
    print("\nType 'exit' to close the chatbot.")

# 6. Function to answer questions

def get_response(question):

    question = question.lower().strip()

    # FAQ Knowledge Base Check
    for key, answer in faq.items():
        if key in question:
            return answer

    # College information
    if any(word in question for word in
       ["about snu", "about college",
        "college information", "university information"]):
        
        return (
            f"{college['name']} ({college['short_name']}) "
            "is a university located in New Town, Kolkata."
        )

    # Course information
    elif any(word in question for word in
             ["course", "courses", "department", "branch", "program"]):

        return (
            "SNU offers courses in several disciplines:\n- "
            + "\n- ".join(courses)
            + "\nFor a specific course, visit the official website."
        )

    # Fee information
    elif any(word in question for word in
             ["fee", "fees", "cost", "scholarship", "payment"]):

        return (
            "Course fees vary depending on the programme.\n"
            "Please check the official course-wise fee information "
            "or contact the admission helpline.\n"
            + college["website"]
        )

    # Admission information
    elif any(word in question for word in
             ["admission", "apply", "application", "eligibility", "register"]):

        steps = "\n".join(
            f"{i+1}. {step}"
            for i, step in enumerate(admission["steps"])
        )

        return (
            "ADMISSION PROCESS:\n"
            + steps
            + "\nApply here: "
            + admission["website"]
        )

    # Contact and helpline information
    elif any(word in question for word in
             ["contact", "helpline", "phone", "number",
              "call", "email", "address", "location"]):

        numbers = "\n".join(helpline["numbers"])

        return (
            "SNU CONTACT INFORMATION:\n"
            "Address: " + college["location"] + "\n"
            "Email: " + college["email"] + "\n"
            "Phone Numbers:\n" + numbers + "\n"
            "Contact Hours: " + helpline["timing"]
        )

    # Greetings
    elif any(word in question for word in
             ["hello", "hi", "hey"]):

        return "Hello! Welcome to Sister Nivedita University. How can I help you?"

    # Thank you
    elif any(word in question for word in
             ["thank you", "thanks"]):

        return "You're welcome! Have a great day!"

        # Unknown question
    else:
        for _ in range(3):
            try:
                response = client.models.generate_content(
                    model="gemini-1.5-Pro",
                    contents=f"""
You are an AI assistant for Sister Nivedita University.

Answer the student's question clearly and briefly.

Student Question:
{question}
"""
                )

                return response.text

            except Exception:
                time.sleep(2)

        return "Gemini AI is busy. Please try again in a few seconds."


# 7. Main function to run chatbot

def start_chatbot():

    welcome()

    while True:

        user_question = input("\nYou: ")

        if user_question.lower().strip() in ["exit", "quit", "bye"]:
            print("Chatbot: Thank you for contacting SNU. Goodbye!")
            break

        answer = get_response(user_question)

        print("\nChatbot:", answer)


# 8. Start the chatbot

if __name__ == "__main__":
    start_chatbot()
