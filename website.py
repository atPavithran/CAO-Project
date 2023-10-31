import streamlit as st
import pandas as pd
from src import Operations as op
from PIL import Image

menu = {
    "Munch": {"price": 5, "image": r"src/item1.jpg"},
    "Ball-Point Pen": {"price": 7, "image": r"src/item2.jpg"},
    "Lays": {"price": 10, "image": r"src/item3.jpg"},
    "5Stars": {"price": 5, "image": r"src/item4.jpg"},
    "Black Pen": {"price": 7, "image": r"src/item5.jpg"},
}

cart = {}

st.markdown("<h1 style='text-align: center; color: #F5F5DC'>SHOPPING CART</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: center; color: #F5F5DC'>MENU</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
column = [col1, col2]

st.write("<div style='text-align: center;'>", unsafe_allow_html=True)
i = 0
for item_name, details in menu.items():
    if i < len(menu.items())/2 :  
        i += 1
        with col1:
            st.markdown(f"<h3 style='text-align: left; color: pink'>{item_name}</h3>", unsafe_allow_html=True)
            st.write("Price:", details['price'])
            image = Image.open(details['image'])
            st.image(image, width=200)
    else:
        with col2:
            st.markdown(f"<h3 style='text-align: left; color: pink'>{item_name}</h3>", unsafe_allow_html=True)
            st.write("Price:", details['price'])
            image = Image.open(details['image'])
            st.image(image, width=200)


st.markdown(f"<h3 style='text-align: left; '>Your Cart</h3>", unsafe_allow_html=True)
cart_items = []
for item in menu.keys():
    quantity = st.slider(f"Select quantity of {item}", 0, 10, 0)
    if quantity > 0:
        cart_items.append((item, quantity, menu[item]["price"]))

if not cart_items:
    st.write("Your cart is empty.")
else:
    st.subheader("Cart Contents")
    df = pd.DataFrame(cart_items, columns=["Item Name", "Quantity", "Price per Item"])
    st.table(df)

st.markdown(f"<h2 style='text-align: left;'>ENTER DISCOUNT FROM SCRATCH CARD!!!</h2>", unsafe_allow_html=True)
discount = st.number_input("DISCOUNT", min_value=0, max_value=100, step=1)
st.markdown(f"<h2 style='text-align: left;'>ENTER CASHBACK AMOUNT!!!</h2>", unsafe_allow_html=True)
cashback = st.number_input("CASHBACK", min_value=0, max_value=100, step=1)

if st.button("Calculate"):
    final_cart = []
    st.write("Cost calculation for each item with booth multiplication: \n")
    for item, qty, price in cart_items:
        if qty>0:   
            product = op.boothmultiplication(price,qty)
            final_cart.append((item,qty,price,product))
    d = pd.DataFrame(final_cart, columns=["Item", "Qty", "Price", "Cost"])
    st.table(d)
    sum = 0
    st.write("Total Calculation with binary addition: \n")
    for i in final_cart:
        sum = op.binaryaddition(sum,i[3])
    st.subheader(f"Total cost of the cart is: ${sum}")
    st.markdown(f"<h2 style='text-align: left; color: green'>YOU HAVE GOT A CASHBACK OF ${cashback}</h2>", unsafe_allow_html=True)
    st.write()
   
    st.markdown('<p style = "color: red; font-size: 10;">Binary subtraction is used to calculate the net total</p>', unsafe_allow_html=True)
    sum = op.binarysubtraction(sum,cashback)

    st.markdown(f"<h2 style='text-align: left; color: green'>YOU HAVE GOT A DISCOUNT OF {discount}%</h2>", unsafe_allow_html=True)
    d = op.simplify_fraction(discount,100)
    st.markdown('<p style = "color: red; font-size: 10;">Restoring division is used to calculate the discount</p>', unsafe_allow_html=True)
    temp , d = op.restoringdivision(sum,d[1])
    st.write(f"Discount is ${d}")

    st.markdown('<p style = "color: red; font-size: 10;">Binary subtraction is used to calculate the FINAL total</p>', unsafe_allow_html=True)
    sum = op.binarysubtraction(sum,d)
    st.markdown(f"<h2 style='text-align: left; color: green'>YOUR NET TOTAL IS:  ${sum}</h2>", unsafe_allow_html=True)




    


