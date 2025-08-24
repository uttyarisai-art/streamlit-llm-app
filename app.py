from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import openai
# .envからAPIキーを取得
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OPENAI_API_KEYが.envに設定されていません。")

#タイトルと説明文
st.title("専門家質問アプリ")
st.write("専門家を選択して質問することにより、あなたのお悩みを解決に役立ちます。")
selected_item = st.radio(
    "専門家を選択してください。",
    ["健康食品の専門家", "日本茶の専門家"]
)

#ラジオボタンの設定
st.divider()
if selected_item == "健康食品の専門家":
    input_message = st.text_input(label="健康食品に関する質問を入力してください。")
else:
    input_message = st.text_input(label="日本茶に関する質問を入力してください。")

# OpenAIクライアントの設定
client = openai.OpenAI(api_key=api_key)

if st.button("実行"):
    st.divider()
    if selected_item == "健康食品の専門家":
        first_completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "あなたは健康食品の専門家です。安全なアドバイスを提供してください。"},
                {"role": "user", "content": input_message}
            ],
            temperature=0.5
        )
    else:
        first_completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "あなたは日本茶の専門家です。安全なアドバイスを提供してください。"},
                {"role": "user", "content": input_message}
            ],
            temperature=0.5
        )

    if input_message:
        st.write(first_completion.choices[0].message.content)
    else:
        st.error("質問を入力してから「実行」ボタンを押してください。")