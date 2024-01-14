import streamlit as st
import numpy as np
from PIL import Image
from detect import StoneDetectionModel

if __name__=="__main__":
    model = StoneDetectionModel("./yolov8n.pt")
    input_image = None
    
    st.title("Stone Detection")
    detect_clicked  =False
    # to show file uploader widget
    uploaded_file = st.file_uploader("" , type=[".png" , ".jpg" , ".jpeg"])
    
    if uploaded_file is not None :
        #get image info
        byte_data = uploaded_file.getvalue()
        
        input_image = Image.open(uploaded_file)
        modified_image=np.asarray(input_image.copy()) #get it as RGB
        
        # making a button
        if st.button("detect"):
            detect_clicked=True
            
        # then making 2 columns view
        col1,col2 = st.columns([1,1])
        
        with col1 :
            #show image in column1 if exists
            if input_image:
                st.image(input_image)

        with col2 :
            if detect_clicked:
                model.inference(input_image)
                image_with_bboxes = model.show_results(modified_image)
                
                #show result image on streamlit
                st.image(image_with_bboxes)
                detect_clicked = False