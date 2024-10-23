


        
import subprocess
import streamlit as st
from transformers import pipeline



# Initialize the pipeline
def load_pipeline():
    try:
        pipe = pipeline("text-generation", model="openai-community/gpt2")
        return pipe
    except Exception as e:
        st.error(f"Failed to load the model: {e}")
        return None

def main():
    st.title("GPT-2 Text Generation")

    # تثبيت المكتبات
    install_requirements()

    # تحميل الـ pipeline
    pipe = load_pipeline()

    if pipe:
        # Prompt input field
        prompt = st.text_input("Enter your prompt:")

        # Generate button
        if st.button("Generate"):
            if prompt:
                # Generate text using the pipeline
                generated_text = pipe(prompt, max_length=100)
                st.text_area("Generated Text:", value=generated_text[0]['generated_text'])
            else:
                st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()
