import streamlit as st

# Dummy quiz data
quiz_data = {
    1: {
        "question": "What is the capital of France?",
        "answers": ["Paris", "Berlin", "Madrid", "Rome"],
        "correct_answers": ["Paris"],
        "explanation": "Paris is the capital of France.",
        "status": "NO",
    },
    2: {
        "question": "What is 2 + 2?",
        "answers": ["3", "4", "5", "6"],
        "correct_answers": ["4"],
        "explanation": "The answer is 4 because 2 + 2 equals 4.",
        "status": "NO",
    },
    3: {
        "question": "Select the programming languages:",
        "answers": ["Python", "English", "Java", "C++"],
        "correct_answers": ["Python", "Java", "C++"],
        "explanation": "Programming languages are Python, Java, and C++.",
        "status": "NO",
    },
}

# Initialize session state for answers
if 'given_answers' not in st.session_state:
    st.session_state.given_answers = {}

# Function to display a question
def show_question(id, question, answers, correct_answers, explanation, status):
    with st.container(border=True):
        st.write(f":blue[({id}). {question}]")
        selected_answers = []
        
        if status == "YES":
            for i, answer in enumerate(answers, start=1):
                st.write(f"({i}). {answer}")
        else:
            for i, answer in enumerate(answers, start=1):
                if st.checkbox(f"({i}). {answer}", key=f"{id}_{answer}"):
                    selected_answers.append(answer)
        
        # Display explanation and correct answers after submission (optional, controlled elsewhere)
        return {
            "selected": selected_answers,
            "correct_answers": correct_answers,
            "explanation": explanation,
        }

# Display questions dynamically
for id, data in quiz_data.items():
    result = show_question(
        id, 
        data["question"], 
        data["answers"], 
        data["correct_answers"], 
        data["explanation"], 
        data["status"]
    )
    # Save the selected answers, correct answers, and explanation in session state
    st.session_state.given_answers[id] = result

if st.button("Submit"):
    st.write("Submitted Answers:")
    total = 0
    grand_total = 0
    for id, result in st.session_state.given_answers.items():
        with st.container(border=True):
            st.write(f":blue[({id}). {quiz_data[id]['question']}]")
            wrong_answers = 0
            correct_answers = 0
            weight = float(len(result['correct_answers']))
            for i, answer in enumerate(quiz_data[id]['answers'], start=1):
                # Check if the answer is selected
                if answer in result['selected']:
                    if answer in result['correct_answers']:
                        correct_answers += 1
                        st.write(f":green[({i}). {answer} ✓]")
                    else:
                        wrong_answers += 1
                        st.write(f":red[({i}). {answer} ✗]")
                else:
                    # Display unselected correct answers in green
                    if answer in result['correct_answers']:
                        st.write(f":green[({i}). {answer}]")
                    else:
                        st.write(f"({i}). {answer}")

            # Show the explanation
            st.write(f"Explanation: {result['explanation']}")
            st.write(weight)
            marks = correct_answers-(wrong_answers*0.5)
            st.write(f":orange[Marks: {marks}/{weight}]")
            total = total+marks
            grand_total = grand_total+weight
        
    st.header(f"Full marks: {total*100/grand_total}%")

            
