import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 AI Language Translator")
st.write("Translate text into multiple languages with voice output.")

# Supported Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Russian": "ru",
    "Arabic": "ar",
    "Portuguese": "pt"
}

text = st.text_area("Enter Text")

target_language = st.selectbox(
    "Select Target Language",
    list(languages.keys())
)

if st.button("Translate"):

    if text.strip():

        try:
            target_code = languages[target_language]

            translated_text = GoogleTranslator(
                source="auto",
                target=target_code
            ).translate(text)

            st.success("Translation Successful")

            st.subheader("Translated Text")
            st.write(translated_text)

            # Save history
            with open("history.txt", "a", encoding="utf-8") as file:
                file.write(
                    f"Original: {text}\nTranslated: {translated_text}\n{'-'*50}\n"
                )

            # Voice Output
            tts = gTTS(
                text=translated_text,
                lang=target_code.split("-")[0],
                slow=True
            )

            tts.save("audio.mp3")

            st.subheader("🔊 Voice Output")
            audio_file = open("audio.mp3", "rb")
            st.audio(audio_file.read())

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter text.")

# Show History
if st.button("Show History"):

    if os.path.exists("history.txt"):

        with open("history.txt", "r", encoding="utf-8") as file:
            st.text(file.read())

    else:
        st.info("No history available.")

# Clear History
if st.button("Clear History"):

    open("history.txt", "w").close()
    st.success("History Cleared Successfully")