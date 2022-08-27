import streamlit as st

if "menu_price_list" not in st.session_state:
    st.session_state.menu_price_list = []

st.title("식비 계산기")

sum_food_expence = 0
people_number = st.number_input("인원 수", min_value=0, max_value=20, step=1,help='1인당 13000원으로 계산')
sum_food_expence = people_number * 13000
st.write(f"계산 전(인원 당 총합 식비) : {sum_food_expence}")

with st.form("메뉴 당 식비 계산", clear_on_submit= True):
    
    temp_price = st.text_input("메뉴 가격")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.session_state['menu_price_list'].append(int(temp_price))
        st.write(st.session_state['menu_price_list'])
        st.write(sum(st.session_state['menu_price_list']) )
        

st.write(f"남은 식비 : {sum_food_expence - sum(st.session_state['menu_price_list'])}")





