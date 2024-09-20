import streamlit as st
st.title("Kanaku Puli")
n1= st.number_input("Enter number 1:")
n2= st.number_input("Enter number 2:")
def areasq(x,y):
    return x*y
def perrec(x,y):
    return 2(x+y)
def percir(x):
    return 2(x)
def areacir(x):
    return 2(3.14*x**2)
if st.button("Kootuthal"):
    st.title(int(n1)+int(n2))
if st.button("Kaliyudhal"):
    st.title(int(n1)-int(n2))
if st.button("Perukudhal"):
    st.title(int(n1)*int(n2))
if st.button("Vaguthal"):
    st.title(int(n1)//int(n2))
if st.button("Sadhuram"):
    st.title(areasq(n1,n2))
 
