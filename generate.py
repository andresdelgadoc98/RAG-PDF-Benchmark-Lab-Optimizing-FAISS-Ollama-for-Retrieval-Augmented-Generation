from src.utils import retrival,functions
import pandas as pd
from src.utils.llm import get_chat_response
from dotenv import load_dotenv
load_dotenv()
import os
embedding_model = os.getenv("NAME_FILE_OUTPUT")


def main():
    df = pd.read_csv('questions.csv', delimiter=',', quotechar='"', skipinitialspace=True)
    questions = df['questions']
    answers = df['answers']
    results_data = []
    for question, answer in zip(questions, answers):
        print("Question:", question)
        results = retrival.retrival(question)
        prompt = functions.generate_prompt(results, question)
        response = get_chat_response(prompt)
        results_data.append({"questions": question, "answers": response,'expect answers':answer})
    results_df = pd.DataFrame(results_data)
    results_df.to_excel(embedding_model + '.xlsx', index=False)


if __name__ == "__main__":
    main()