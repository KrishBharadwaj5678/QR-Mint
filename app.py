import streamlit as st
import qrcode as qr

st.set_page_config(
    page_title="QR Mint",
    page_icon="icon.png",
    menu_items={
        "About":"Our intuitive tool allows you to effortlessly design and customize QR codes with a touch of creativity. Choose from a variety of colors to make your QR code uniquely yours. Start creating your custom QR codes today with QR Mint!"
    }
)

st.write("<h2 style='color:#6EACDA;'>Design Custom QR Codes with QR Mint</h2>",unsafe_allow_html=True)

data=st.text_input("Enter Data",placeholder="www.example.com")
qr_color=st.color_picker("Choose QR Code Color",value="#000000")
back_color=st.color_picker("Choose Background Color",value="#FFFFFF")
border=st.radio("Add a Border?",["Yes","No"],index=1)

btn=st.button("Generate")
if btn:
    if(len(data)>=1):
        q=qr.QRCode(version=1,border=2,box_size=11) if(border=="Yes") else qr.QRCode(version=1,border=0,box_size=11)
        q.add_data(data)
        q.make(fit=True)
        img=q.make_image(back_color=back_color,fill_color=qr_color)
        img.save("qr_mint.png")
        with open("qr_mint.png","rb+") as file:
            st.download_button("Download",file.read(),f"{data}.png")
        st.image("qr_mint.png")
    else:
        st.warning("Data Field Cannot Be Empty!")