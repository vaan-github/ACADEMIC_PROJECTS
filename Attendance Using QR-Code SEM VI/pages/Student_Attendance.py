import qrcode
import cv2
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import csv
from datetime import datetime
import base64

st.set_page_config(
    page_title="Student Attendance Management System", page_icon=":clipboard:")

st.header("Student Attendance")


def get_students():
    # Read the students from the CSV file
    students = {}
    with open("students.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            students[row[0]] = row[1]
    return students


# Get the updated list of students
students = get_students()


def download_csv_file(subject):
    filename = f"{subject}_Attendance.csv"
    print(filename)
    with open(filename, "r") as file:
        csv_contents = file.read()
    b64_csv = base64.b64encode(csv_contents.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64_csv}" download="Attendance.csv">Download CSV</a>'

    decoded_csv = base64.b64decode(b64_csv).decode('utf-8')
    with open(filename, 'w') as f:
        f.write(decoded_csv)
    return decoded_csv


def create_csv(roll_no, name, subject):
    filename = f"{subject}_Attendance.csv"
    print(roll_no, name)
    present = 'Present'
    with open(filename, "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    with open(filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            # File is empty, write header
            writer.writerow(["Roll_no", "Name", "Subject",
                            "Date", "Time", "Attendance"])

# add new values to CSV file
    with open(filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M:%S")
        writer.writerow([roll_no, name, subject, date, time, present])
    return filename


def app():

    subject = st.selectbox(('Select Subject :'),
                           ('Maths', 'Science', 'Physics', 'Chemistry'))

    if subject == 'Maths':
        qr_size = (250, 250)
        attendance_list = []
        qr_codes = {}

        Start_Attendance = st.button('Start Attendance')
        Stop_Attendance = st.button('Stop Attendance')
        Download = st.download_button(
            label="Download CSV File", data=download_csv_file(subject), file_name=f"{subject}_attendance.csv")

        if Start_Attendance:
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
                        pt2 = (int(bbox[(i+1) % len(bbox)][0][0]),
                               int(bbox[(i+1) % len(bbox)][0][1]))
                        cv2.line(frame, pt1, pt2, (0, 255, 0), 3)

                    # print(f"QR code data: {data}")
                    # print(f"Students: {students}")d

                    if data in students:
                        # print(data)
                        if data not in attendance_list:
                            attendance_list.append(data)
                        # print(attendance_list)
                            st.write(
                                f"{students[data]} ({data}) attended the class.")
                        # print(f"Attendance List: {attendance_list}")
                            create_csv(data, students[data], subject)

                # Check if the frame was successfully captured
                if not ret:
                    break

                # Resize the frame to match the canvas size
                resized_frame = cv2.resize(frame, (frame_width, frame_height))

                # Display the frame in the canvas
                canvas.image(resized_frame, channels="BGR")
        if Stop_Attendance:
            st.warning("Stopped")
            st.stop()

    if subject == 'Science':
        qr_size = (250, 250)
        attendance_list = []
        qr_codes = {}

        Start_Attendance = st.button('Start Attendance')
        Stop_Attendance = st.button('Stop Attendance')
        Download = st.download_button(
            label="Download CSV File", data=download_csv_file(subject), file_name=f"{subject}_attendance.csv")

        if Start_Attendance:
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
                        pt2 = (int(bbox[(i+1) % len(bbox)][0][0]),
                               int(bbox[(i+1) % len(bbox)][0][1]))
                        cv2.line(frame, pt1, pt2, (0, 255, 0), 3)

                    # print(f"QR code data: {data}")
                    # print(f"Students: {students}")d

                    if data in students:
                        # print(data)
                        if data not in attendance_list:
                            attendance_list.append(data)
                        # print(attendance_list)
                            st.write(
                                f"{students[data]} ({data}) attended the class.")
                        # print(f"Attendance List: {attendance_list}")
                            create_csv(data, students[data], subject)

                # Check if the frame was successfully captured
                if not ret:
                    break

                # Resize the frame to match the canvas size
                resized_frame = cv2.resize(frame, (frame_width, frame_height))

                # Display the frame in the canvas
                canvas.image(resized_frame, channels="BGR")
        if Stop_Attendance:
            st.warning("Stopped")
            st.stop()

    if subject == 'Physics':
        qr_size = (250, 250)
        attendance_list = []
        qr_codes = {}

        Start_Attendance = st.button('Start Attendance')
        Stop_Attendance = st.button('Stop Attendance')
        Download = st.download_button(
            label="Download CSV File", data=download_csv_file(subject), file_name=f"{subject}_attendance.csv")

        if Start_Attendance:
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
                        pt2 = (int(bbox[(i+1) % len(bbox)][0][0]),
                               int(bbox[(i+1) % len(bbox)][0][1]))
                        cv2.line(frame, pt1, pt2, (0, 255, 0), 3)

                    # print(f"QR code data: {data}")
                    # print(f"Students: {students}")d

                    if data in students:
                        # print(data)
                        if data not in attendance_list:
                            attendance_list.append(data)
                        # print(attendance_list)
                            st.write(
                                f"{students[data]} ({data}) attended the class.")
                        # print(f"Attendance List: {attendance_list}")
                            create_csv(data, students[data], subject)

                # Check if the frame was successfully captured
                if not ret:
                    break

                # Resize the frame to match the canvas size
                resized_frame = cv2.resize(frame, (frame_width, frame_height))

                # Display the frame in the canvas
                canvas.image(resized_frame, channels="BGR")
        if Stop_Attendance:
            st.warning("Stopped")
            st.stop()

    if subject == 'Chemistry':
        qr_size = (250, 250)
        attendance_list = []
        qr_codes = {}

        Start_Attendance = st.button('Start Attendance')
        Stop_Attendance = st.button('Stop Attendance')
        Download = st.download_button(
            label="Download CSV File", data=download_csv_file(subject), file_name=f"{subject}_attendance.csv")

        if Start_Attendance:
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
                        pt2 = (int(bbox[(i+1) % len(bbox)][0][0]),
                               int(bbox[(i+1) % len(bbox)][0][1]))
                        cv2.line(frame, pt1, pt2, (0, 255, 0), 3)

                    # print(f"QR code data: {data}")
                    # print(f"Students: {students}")d

                    if data in students:
                        # print(data)
                        if data not in attendance_list:
                            attendance_list.append(data)
                        # print(attendance_list)
                            st.write(
                                f"{students[data]} ({data}) attended the class.")
                        # print(f"Attendance List: {attendance_list}")
                            create_csv(data, students[data], subject)

                # Check if the frame was successfully captured
                if not ret:
                    break

                # Resize the frame to match the canvas size
                resized_frame = cv2.resize(frame, (frame_width, frame_height))

                # Display the frame in the canvas
                canvas.image(resized_frame, channels="BGR")
        if Stop_Attendance:
            st.warning("Stopped")
            st.stop()


if __name__ == "__main__":
    app()
