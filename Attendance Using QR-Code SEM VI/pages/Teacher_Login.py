import streamlit as st
import csv
import qrcode
import base64
import io
from PIL import Image


st.set_page_config(page_title="Teacher Login Portal", page_icon=":guardsman:")


def init_state():
    state = st.session_state
    if "students" not in state:
        state.students = {
            "04": "Meehir Chaudhary",
            "17": "Jay K",
            "05": "Hrithik Dwivedi",
            "22": "Dharmendra Mallah",
            "54": "Aniket varma"
            # add more students here
        }
    return state


# Create a Streamlit app to add students
def add_student():
    # Initialize the session state
    init_state()

    # Get the session state
    state = st.session_state

    # Add a header and a form to add a new student
    st.header("Add Student")
    id_input = st.text_input("Roll No")
    name_input = st.text_input("Student Name")
    add_button = st.button("Add Student")

    # If the add button is clicked, add the new student to the dictionary
    if add_button:
        state.students[id_input] = name_input
        st.success(f"{name_input} added to the list of students!")

        # Generate QR code for roll number
        # Create QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(id_input)
        qr.make(fit=True)
        qr_image = qr.make_image(fill='black', back_color='white')

        # Convert QR code image to bytes-like object
        # Convert to bytes
        img_byte_arr = io.BytesIO()
        qr_image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        # Display QR code image using st.image

        img = st.image(
            img_byte_arr, caption='QR code for roll number: ' + id_input)

        # Add a download button for the image
        st.download_button(
            label="Download image",
            data=img_byte_arr,
            file_name="image.jpg",
            mime="image/jpeg"
        )

        state.students[id_input] = name_input
        st.success(f"{name_input} added to the list of students!")

        with open("students.csv", "w") as csvfile:
            writer = csv.writer(csvfile)
            for id, name in state.students.items():
                writer.writerow([id, name])

    # Display the current list of students
    print(state.students)


# Create a Streamlit app with a login form
def login_page():
    # Get the session state
    state = st.session_state

    # Set the page title and display the login form
    st.header("Teacher Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    # If the login button is clicked, check the credentials
    if login_button:
        if username == "teacher" and password == "1234":
            # If the credentials are correct, set the state and call the add_student function
            state.logged_in = True
            add_student()
        else:
            st.error("Invalid username or password")


# Run the app
if __name__ == "__main__":
    # Initialize the state of the app
    state = init_state()

    # If the user is logged in, call the add_student function
    if getattr(st.session_state, "logged_in", False):
        add_student()
    # Otherwise,

    # Otherwise, display the login form
    else:
        login_page()
