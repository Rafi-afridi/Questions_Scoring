import streamlit as st
import pandas as pd

# Read the CSV file
data = pd.read_csv("questions.csv")

# Initialize variables
scores = {}

# Display all questions and options
def display_questions():
    for index, question in data.iterrows():
        st.markdown(f"**Q{index + 1}: {question['Question']}**")
        options = [f"Option {i + 1}" for i in range(4)]
        selected_option = st.radio(f"Options", options=options, key=f"question_{index}")
        score_column = f"Score {options.index(selected_option) + 1}"
        scores[index] = int(question[score_column])

# Streamlit app
def main():
    st.title("MCQ Quiz")
    display_questions()

    # Submit button
    if st.button("Submit"):
        total_score = sum(scores.values())
        st.success(f"Questions Submitted! Your total score is: {total_score}")

# Run the app
if __name__ == "__main__":
    main()