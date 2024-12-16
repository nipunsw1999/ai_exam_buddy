import streamlit as st

# Dummy quiz data
quiz_data = {
    1: {
        "question": "What is supervised learning?",
        "answers": [
            "A type of learning where the model learns from labeled data",
            "A type of learning where the model learns from unlabeled data",
            "A type of learning that does not involve data",
            "A type of learning focused only on clustering",
        ],
        "correct_answers": ["A type of learning where the model learns from labeled data"],
        "explanation": "Supervised learning involves training a model on labeled data, where each input is paired with its corresponding output.",
        "status": "NO",
    },
    2: {
        "question": "Which of the following are examples of machine learning algorithms?",
        "answers": ["Linear Regression", "K-Means Clustering", "Decision Trees", "WordPress"],
        "correct_answers": ["Linear Regression", "K-Means Clustering", "Decision Trees"],
        "explanation": "Linear Regression, K-Means Clustering, and Decision Trees are machine learning algorithms, while WordPress is a content management system.",
        "status": "NO",
    },
    3: {
        "question": "What is overfitting in machine learning?",
        "answers": [
            "When the model performs well on training data but poorly on unseen data",
            "When the model performs equally well on both training and unseen data",
            "When the model fails to learn from the data",
            "When the model focuses on irrelevant features",
        ],
        "correct_answers": ["When the model performs well on training data but poorly on unseen data"],
        "explanation": "Overfitting occurs when a model learns the training data too well, including noise, resulting in poor generalization to new data.",
        "status": "NO",
    },
    4: {
        "question": "Which of the following are types of neural networks?",
        "answers": ["Convolutional Neural Networks (CNN)", "Recurrent Neural Networks (RNN)", "Support Vector Machines (SVM)", "Feedforward Neural Networks"],
        "correct_answers": ["Convolutional Neural Networks (CNN)", "Recurrent Neural Networks (RNN)", "Feedforward Neural Networks"],
        "explanation": "CNN, RNN, and Feedforward Neural Networks are types of neural networks, while SVM is a different machine learning algorithm.",
        "status": "NO",
    },
    5: {
        "question": "What is the purpose of a validation dataset in machine learning?",
        "answers": [
            "To train the model",
            "To test the model's performance on unseen data",
            "To tune the model's hyperparameters",
            "To replace the training dataset",
        ],
        "correct_answers": ["To tune the model's hyperparameters"],
        "explanation": "A validation dataset is used to fine-tune hyperparameters and avoid overfitting without touching the test dataset.",
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

            
