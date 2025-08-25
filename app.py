from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI

from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

def create_message(selected_job, concern_text):
  llm = ChatOpenAI(model_name='gpt-4o-mini', temperature=0)

  st.write(f'あなたは{selected_job}に相談しました。')
  st.write(f'相談内容: {concern_text}')
  st.write('回答を生成中...しばらくお待ち下さい。')

  try:
    messages = [
        SystemMessage(content=f'あなたは優秀な{selected_job}です。ユーザーの悩みに寄り添い、専門的な知識を活かして、わかりやすく丁寧に回答して下さい。'),
        HumanMessage(content=concern_text),
    ]
    result = llm(messages)
  except Exception as e:
      st.error(f"Error: {e}")
  return result

st.title('専門家への質問、相談Wサービス')

st.write('##### 1: 専門家選択')
st.write('相談する専門家を選択して下さい。')
st.write('##### 2: 相談内容入力')
st.write('相談内容を入力して下さい。')

st.divider()

selected_job = st.radio(
    '相談する専門家を選択して下さい。',
   [
    "医師",
    "弁護士",
    "税理士",
    "心理カウンセラー",
    "キャリアコンサルタント",
    "警察官",
    "栄養士",
    "ITエンジニア",
    "プロ野球選手",
    "教員"
  ]
)

st.divider()

concern_text = st.text_area(label='相談内容を入力して下さい。')


if st.button('相談する'):
    st.divider()

    if concern_text != '':
        response = create_message(selected_job, concern_text)
        st.write(f'回答: {response.content}')
    else:
        st.write('相談内容を入力して下さい。')