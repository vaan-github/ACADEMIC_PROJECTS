import qrcode
import cv2
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu  # GUI utility library
import csv
from datetime import datetime
import base64

st.set_page_config(
    page_title="Homepage",
)

students = {
    "04": "Meehir Chaudhary",
    "17": "Jay K",
    "05": "Hrithik Dwivedi",
    "22": "Dharmendra Mallah",
    "54": "Aniket varma"
    # add more students here
}
filename = "Attendance.csv"



def download_csv_file():
    with open(filename, "r") as file:
        csv_contents = file.read()
    b64_csv = base64.b64encode(csv_contents.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64_csv}" download="Attendance.csv">Download CSV</a>'
    
    decoded_csv = base64.b64decode(b64_csv).decode('utf-8')
    with open('Attendance.csv', 'w') as f:
        f.write(decoded_csv)
    return decoded_csv


def create_csv(roll_no, name):
    print(roll_no, name)
    with open(filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            writer.writerow(["Roll_no", "Name", "Date", "Time"])

# add new values to CSV file
    with open(filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M:%S")
        writer.writerow([roll_no, name, date, time])
    return filename

def app():
    qr_size = (250, 250)
    attendance_list = []

    qr_codes = {}

    st.write(
        "<p style='font-size: 45px; font-family: conthrax; text-align:center;'> QR based Attendance Management System</p>", unsafe_allow_html=True)
   
    # Create option menu with icons
    selected = option_menu(
        menu_title=None,
        options=["Home","Attendance", "Download"],
        default_index=0,
        orientation="horizontal",
    )

    
    if selected == "Attendance":
        
        start = st.button("Start Attendance")
        stop = st.button("Stop Attendance")
        if start:
            for student_id in students:
                qr_codes[student_id] = qrcode.make(student_id).resize(qr_size)
            
            video_capture = cv2.VideoCapture(0)
            # Set the width and height of the frame to match the video feed
            frame_width = int(video_capture.get(3))
            frame_height = int(video_capture.get(4))
            canvas = st.empty()

            while True:
                ret, frame = video_capture.read()
                
                qr_decoder = cv2.QRCodeDetector()
                data, bbox, _ = qr_decoder.detectAndDecode(frame)
                
                if bbox is not None and len(bbox) > 0:
                    for i in range(len(bbox)):
                        pt1 = (int(bbox[i][0][0]), int(bbox[i][0][1]))
                        pt2 = (int(bbox[(i+1) % len(bbox)][0][0]), int(bbox[(i+1) % len(bbox)][0][1]))
                        cv2.line(frame, pt1, pt2, (0, 255, 0), 3)
                    
                    #print(f"QR code data: {data}")
                    #print(f"Students: {students}")
                    
                    if data in students:
                        #print(data)
                        if data not in attendance_list:
                            attendance_list.append(data)
                        # print(attendance_list)
                            st.write(f"{students[data]} ({data}) attended the class.")
                        # print(f"Attendance List: {attendance_list}")
                            filename = create_csv(data, students[data])

                
                # Check if the frame was successfully captured
                if not ret:
                    break
                
                # Resize the frame to match the canvas size
                resized_frame = cv2.resize(frame, (frame_width, frame_height))
                
                # Display the frame in the canvas
                canvas.image(resized_frame, channels="BGR")
        if stop:
            st.warning("Stopped")
            st.stop()
            
                

    if selected == "Download":
        
        button = st.download_button(label="Download CSV File", data=download_csv_file(), file_name="attendance.csv")
        st.markdown(button, unsafe_allow_html=True)


if __name__ == "__main__" :
    app()