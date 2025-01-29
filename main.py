# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI()

st.title('A.I 시인')
content = st.text_input("시의 주제를 선정해주세요.")
# st.write("시의 주제는 ", content)

if st.button("시 작성 요청하기"):
    with st.spinner('시 작성 중...'):
        result = chat_model.invoke(content + "에 대한 시를 써줘.") 
         # 결과가 객체일 경우, 내용만 추출
        if hasattr(result, 'content'):  
            result = result.content
        else:
            result = str(result)  # 혹시 모를 예외 처리
        st.write(result)


# print(result)

