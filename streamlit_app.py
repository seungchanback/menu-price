import streamlit as st
import pandas as pd
if "menu_price_list" not in st.session_state:
    st.session_state.menu_price_list = []

st.title("식비 계산기")

sum_food_expence = 0
people_number = st.number_input("인원 수", min_value=0, max_value=20, step=1,help='1인당 13000원으로 계산')
sum_food_expence = people_number * 13000
st.write(f"계산 전(인원 당 총합 식비) : {sum_food_expence}")

with st.form("메뉴 당 식비 계산", clear_on_submit= True):
    
    temp_menu_name = st.text_input("메뉴")
    temp_price = st.text_input("메뉴 가격")
    temp_menu_people = st.number_input("인원 수", value=1)
    submitted = st.form_submit_button("Submit")
    if submitted:
        temp_menu = {
            '메뉴' : temp_menu_name,
            '메뉴 가격' : temp_price,
            '메뉴 당 인원' : temp_menu_people
         }
        st.session_state['menu_price_list'].append(temp_menu)
        st.write(sum([ int(menu['메뉴 가격']) for menu in st.session_state['menu_price_list']]))

with st.container():
    if "menu_price_list" in st.session_state:
        st.session_state['menu_price_list'] = st.multiselect('메뉴', st.session_state['menu_price_list'], st.session_state['menu_price_list'])
        st.write(pd.DataFrame(st.session_state['menu_price_list']))
    st.write(f"남은 식비 : {sum_food_expence - sum([ int(menu['메뉴 가격']) for menu in st.session_state['menu_price_list']])}")

]]
