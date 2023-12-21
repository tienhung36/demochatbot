from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.llms import OpenAI
import streamlit as st

def main():
    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV 📈")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    if csv_file is not None:
        # Set your OpenAI API key directly in the code
        openai_api_key = "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"

        agent = create_csv_agent(
            OpenAI(api_key=openai_api_key, temperature=0),
            csv_file,
            verbose=True
        )

        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))

if __name__ == "__main__":
    main()
