import streamlit as st 
import pandas as pd
st.sidebar.header("Services")
page = st.sidebar.selectbox("Select any of our services",["Select","Menu","Order","Reservation","About Us"])
if page=="Select":
    st.header("Gurleen's Kitchen")
    st.image("https://plus.unsplash.com/premium_photo-1661883237884-263e8de8869b?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8cmVzdGF1cmFudHxlbnwwfHwwfHx8MA%3D%3D",use_container_width=True)
    st.subheader("address")
    st.write("Ranjit Avenue,B-Block , Amritsar")
    btn=st.button("directions")
    if btn:
        st.map(latitude="31.65704",longitude="74.859485",color="purple",zoom=15)
    st.subheader("Hours")
    st.subheader("Monday and Tuesday")
    st.write("5pm-9:30pm")
    st.subheader("Wednesday-Saturday")
    st.write("5pm-10pm")
    st.subheader("Sunday")
    st.write("10pm-2pm")
    st.subheader("Contact")
    st.write("9890145678")
    st.write("gurleenkaursandhu2210@gmail.com")
    st.image("https://img.freepik.com/premium-photo/tokyo-japan-january-09-2018-chefs-are-cooking-restaurant-most-popular-delicious-japanese-snack-food-japan_175935-25.jpg?semt=ais_hybrid&w=740",use_container_width=True)
    st.header("Gurleen's Kitchen")
    st.write("Made with love and affection , Gurleen's Kitechn offers varities of healthy meals in Punjab. While we shares the influence and bold flavours of Punjab , the culinary team is always crafting new dishes inspired by Punjab produce and local flavours")
    col1,col2=st.columns(2)
    with col1:
        st.image("https://popmenucloud.com/izyapxve/4d84569e-1b1e-4f21-a6f4-0dd16174b4dc.jpg",use_container_width=True)
    with col2:
        st.image("https://img.freepik.com/free-photo/top-view-fast-food-mix-grilled-lamb-meat-cucumber-tomato-french-fries-arugula-salad-with-salmon-parmesan-cheese-grilled-chicken-breast-with-fresh-greens-bread-bas_141793-3996.jpg?semt=ais_hybrid&w=740",use_container_width=True)
if page=="Menu":
    st.title("Menu")
    col1,col2=st.columns(2)
    with col1:
        st.image("https://perthisok.com/_next/image/?url=https%3A%2F%2Fcms.perthisok.com%2Fwp-content%2Fuploads%2F2023%2F02%2Fsouth-perth-best-restaurants-ludo-Cropped.jpg&w=3840&q=75",use_container_width=True)
    with col2:
        st.image("https://media.istockphoto.com/id/1829241109/photo/enjoying-a-brunch-together.jpg?s=612x612&w=0&k=20&c=9awLLRMBLeiYsrXrkgzkoscVU_3RoVwl_HA-OT-srjQ=",use_container_width=True)
    with st.expander("Dinner"):
      with st.expander("Breads and Snacks"):
            st.write("Naan and dips")
            st.write("Kimchi")
            st.write("Special Thali")
      with st.expander("Veggies"):
            st.write("Crispy Brussels Sprouts")
            st.write("Rousted Beet")
            st.write("Chickpea fritters")
            st.write("Grilled Corn")
            st.write("Sauteed Green Beans")
            st.write("Roasted Carrots")
      with st.expander("Deserts"):
            st.write("Mango Sticky Rise")
            st.write("Vanilla Scoop")
            st.write("Blueberry sorbet")
            st.write("Coconut Sorbet")
    with st.expander("Pizza"):
            st.write("Italian")
            st.write("Chicken")
            st.write("Veg")
    with st.expander("Burger"):
            st.write("Veg")
            st.write("Non Veg")
    with st.expander("Drinks"):
            st.write("Coffee")
            st.write("Cold drink")
            st.write("Shakes") 
            st.write("Tea")   
if page=="Order":
    st.title("Order")
    col1,col2=st.columns(2)
    with col1:
        st.image("https://le-cdn.hibuwebsites.com/d6164e23cd7942efb0ede8c90ceee43f/dms3rep/multi/opt/zucco-s-family-restaurant-hero-home-26a97503-1920w.jpg",use_container_width=True)
    with col2:
        st.image("https://chateaurestaurant.com/wp-content/uploads/2024/01/hero_mobile_crop.jpg",use_container_width=True)
    name = st.text_input("Enter your name")
    age=st.number_input("Enter your age")
    if(name and age):
        st.write(f"Welcome {name} to Gurleen's Kitchen")
        phone_number= st.text_input("Enter your phone number")
        if(phone_number.isdigit and len(phone_number)==10):
            st.write(f"Your entered phone number is {phone_number}")
            order_type=st.selectbox("What food type you want to order in our menu",["Dinner","Breakfast","Brunch","Others"]) 
            if order_type=="Dinner":
                dinner=st.selectbox("What you want to select in dinner",["Breads and Snacks","Naan and dsips","Kimchi","Special Thali"])
                amount0=st.slider("How many plates you want to order",min_value=1,max_value=10,step=1)
                st.success(f"You have selected {amount0} of {dinner}")
            if order_type=="Breakfast":
                breakfast=st.selectbox("What you want to select in Breakfast",["Breads and Snacks","Naan and dsips","Kimchi","Special Thali"])
                amount1=st.slider("How many plates you want to order",min_value=1,max_value=10,step=1)
                st.success(f"You have selected {amount1} of {breakfast}")
            if order_type=="Brunch":
                brunch=st.selectbox("What you want to select in dinner",["Breads and Snacks","Naan and dsips","Kimchi","Special Thali"])
                amount2=st.slider("How many plates you want to order",min_value=1,max_value=10,step=1)
                st.success(f"You have selected {amount2} of {brunch}")
            if order_type=="Others":
                others=st.selectbox("What you want to select in dinner",["Breads and Snacks","Naan and dsips","Kimchi","Special Thali"])
                amount3=st.slider("How many plates you want to order",min_value=1,max_value=10,step=1)
                st.success(f"You have selected {amount3} of {others}")
            drinks=st.selectbox("Drinks you want to select:",["Nothing","Cold Drink","Tea","Coffee","Shakes"])
            amount4=st.slider("How many drinks you want to order",min_value=0,max_value=10,step=1)
            st.success(f"You have selected {amount4} of {drinks}")
            st.subheader("Order Summary")
            st.write(f"Name: {name}")
            st.write(f"Age: {age}")
            st.write(f"Phone Number: {phone_number}")
            st.write(f"Order Type : {order_type}")
            st.write(f"Drinks: {drinks}")
            
            btn = st.button("Place Order")
            if btn:
                st.success("Your order has been placed successfully")
        else:
            st.warning("Please enter a valid 10 digit phone mumber to proceed")
    else:
        st.warning("Please enter your name and age to proceed")
if page=="Reservation":
    st.title("Reservation")
    st.image("https://rishikeshcamps.in/wp-content/uploads/2023/05/restaarant.jpg",use_container_width=True)
    btn=st.button("Make a Reservation")
    if btn:
        st.text_input("Enter your name")
        st.text_input("Enter your email")
        st.number_input("Enter your phone number")
        st.selectbox("Select your country",["India","USA","Canada"])
        st.number_input("Enter your area pincode")
        st.text_area("Enter your address")
        st.slider("How many seats you want to reserve",min_value=1,max_value=10,step=1)
        st.date_input("Select your date of reservation")
        st.time_input("Select time")
        st.button("Submit")
if page=="About Us":
    st.title("About Us")
    st.image("https://www.mowglistreetfood.com/wp-content/uploads/2024/03/2024_07_02-MowgliLIN2-1024x683.jpg",use_container_width=True)
    st.write("Made with love and affection , Gurleen's Kitechn offers varities of healthy meals in Punjab. While we shares the influence and bold flavours of Punjab , the culinary team is always crafting new dishes inspired by Punjab produce and local flavours")
    col1,col2=st.columns(2)
    with col1:
        st.image("https://restaurantindia.s3.ap-south-1.amazonaws.com/s3fs-public/inline-images/Koa2.jpg",use_container_width=True)
    with col2:
        st.image("https://www.barangaroo.com/getmedia/9b8bc812-bbbd-49b3-9e0a-8aecd7c31ce7/eat-and-drink-lovefish-barangaroo-001.png",use_container_width=True)
           
                
