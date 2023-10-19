import streamlit as st

# Set page title and favicon
st.set_page_config(page_title="QR Attendance System", page_icon=":guardsman:")

# Define styles
main_style = """
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif, ethnocentric;
    line-height: 1.5;
"""

h1_style = """
    font-size: 50px;
    font-family: ethnocentric;
    color: #1F2937;
    margin-top: 80px;
    margin-bottom: 0;
"""

p_style = """
    font-size: 24px;
    color: #6B7280;
    margin-top: 20px;
"""

qr_style = """
    color: #0047AB;
"""

# Define page content
content = """
    <div style='text-align:center;'>
        <h1 style='{}'>
            <span style='{}'>QR</span> Attendance System
        </h1>
        <p style='{}'>A modern solution for attendance management using QR codes</p>
    </div>
""".format(h1_style, qr_style, p_style)

# Display page content
st.write("<style>{}</style>".format(main_style), unsafe_allow_html=True)
st.write(content, unsafe_allow_html=True)
