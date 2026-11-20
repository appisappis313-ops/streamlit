import streamlit as st

st.set_page_config(page_title="حاسبة المعدل الذكية", page_icon="🎓")

st.title("🎓 حاسبة المعدل الدراسي")
st.write("أدخل درجاتك لحساب المعدل العام فوراً")

col1, col2 = st.columns(2)

with col1:
    arabic = st.number_input("اللغة العربية", min_value=0, max_value=100, value=85)
    english = st.number_input("اللغة الإنجليزية", min_value=0, max_value=100, value=85)
    math = st.number_input("الرياضيات", min_value=0, max_value=100, value=90)

with col2:
    biology = st.number_input("الأحياء", min_value=0, max_value=100, value=95)
    physics = st.number_input("الفيزياء", min_value=0, max_value=100, value=85)
    chemistry = st.number_input("الكيمياء", min_value=0, max_value=100, value=85)

if st.button("احسب المعدل", use_container_width=True):
    total = arabic + english + math + biology + physics + chemistry
    average = total / 6
    st.success(f"معدلك النهائي هو: {average:.2f}%")
    if average >= 90:
        st.balloons()
        st.info("التقدير: امتياز 🌟")
    elif average >= 50:
        st.info("النتيجة: ناجح ✅")
    else:
        st.error("النتيجة: راسب ❌")

st.markdown("---")
st.caption("تم تطوير هذا التطبيق بواسطة: عباس عبدالرحمن")
