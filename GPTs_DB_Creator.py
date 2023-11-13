# Import necessary libraries
import streamlit as st
import os
import datetime
from PyPDF2 import PdfReader
import docx
import textract
import pandas as pd
import time

# Function to extract text from different file types
def extract_text(file, file_type):
    # If the file is a PDF
    if file_type == 'pdf':
        # Create a PDF reader object
        reader = PdfReader(file)
        # Extract text from each page and join them together
        text = '\n'.join([page.extract_text() for page in reader.pages if page.extract_text()])
    # If the file is a Word document
    elif file_type == 'docx':
        # Create a Document object
        doc = docx.Document(file)
        # Extract text from each paragraph and join them together
        text = '\n'.join([para.text for para in doc.paragraphs])
    # If the file is a text file
    elif file_type == 'txt':
        # Read the file and decode it to UTF-8
        text = file.read().decode('utf-8')
    # If the file is an Excel file
    elif file_type in ['xlsx', 'xls']:
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(file)
        # Convert all cells to string and concatenate with newline characters
        text = '\n'.join(df.astype(str).stack().tolist())
    # If the file is a CSV file
    elif file_type == 'csv':
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file)
        # Convert all cells to string and concatenate with newline characters
        text = '\n'.join(df.astype(str).stack().tolist())
    # If the file type is not supported
    else:
        # Return an empty string
        text = ''
    return text

# Function to append text to a file
def append_to_file(text, file_path):
    # Open the file in append mode
    with open(file_path, 'a', encoding='utf-8', errors='replace') as file:
        # add time sleep two seconds
        time.sleep(2)
        # Add a timestamp to the appended text
        file.write(f"\n\n\n### Appended your data: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        # Write the text to the file
        file.write("\n\n" + text + "\n\n")

# New function to find the latest text file in the 'db' folder
def find_latest_file(directory):
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    if not txt_files:
        return None
    latest_file = max(txt_files, key=lambda x: os.path.getmtime(os.path.join(directory, x)))
    return latest_file


# Streamlit UI
# Use HTML to center align the title with bright green color
st.markdown("""
    <h1 style='text-align: center; color: limegreen;'>💻 Auto GPTs DB Text Creator 💾</h1>
    """, unsafe_allow_html=True)
# Adding a description
st.markdown("""
##### This application allows you to upload PDF, Word, or text files and appends their content to a text file in a database folder. \
The appended data includes a timestamp and the text extracted from the uploaded file to use GPTs to manage your data as one text file to aovid potensial error in GPTs. 
The database text files are named in the format `gpts_db_<current_date>.txt`. 
This tool is useful for aggregating and storing text data from various documents in a structured format.
""")

# Create a file uploader widget
uploaded_file = st.file_uploader("Upload a file", type=['pdf', 'docx', 'txt', 'xlsx', 'xls', 'csv'])

# If a file is uploaded
if uploaded_file is not None:
    # Check if the 'db' folder exists, if not, create it
    if not os.path.exists('db'):
        os.mkdir('db')

    # Check if a file with today's date exists
    today_file_name = f"gpts_db_{datetime.datetime.now().strftime('%Y-%m-%d')}.txt"
    today_file_path = os.path.join('db', today_file_name)

    # If today's file exists, use it, otherwise find the latest file
    if os.path.exists(today_file_path):
        file_path = today_file_path
    else:
        latest_file = find_latest_file('db')
        file_path = os.path.join('db', latest_file) if latest_file else today_file_path

    print("saved file_path: ", file_path)

    # Show a spinner while the file is being processed
    with st.spinner('Processing file...'):
        # Extract the file type from the file name
        file_type = uploaded_file.name.split('.')[-1]
        # Extract text from the uploaded file
        extracted_text = extract_text(uploaded_file, file_type)

        # Append the extracted text to the file
        append_to_file(extracted_text, file_path)

    # Show a success message when the file is processed
    st.success("File processed and text appended successfully.")