import streamlit as st


def main():
	wc_page = st.Page("word_correction.py", title = "Word Correction", icon = ":material/check:")
	od_page = st.Page("object_detection.py", title = "Object Detection", icon = ":material/search:")
	chatbot_page = st.Page("chat_bot.py", title = "Chatbot", icon = ":material/chat:")
	pg = st.navigation([wc_page, od_page, chatbot_page])
	st.set_page_config(page_title = "AIO-2024-md1", page_icon = ":material/edit:")
	pg.run()


if __name__ == '__main__':
	main()
