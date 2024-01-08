
# ByteWave

ByteWave is a simple Flask web application for uploading, downloading, and managing files from remote hosts. It provides a user-friendly interface for handling file operations using a web browser and CLI.
This file upload technique can be valuable for the students preparing for the OSCP exam.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/sazzad1337/ByteWave.git

2. Run the Flask application:

	```bash
	python bytewave.py

## Features


   - **File Upload:**
   
     **Linux:**
     ```bash
     curl -F "file=@FILENAME" http://IP/upload
     ```

     **Windows PowerShell:**
     ```bash
     (New-Object System.Net.WebClient).UploadFile('http://IP/upload', 'FILENAME')
     ```


   - **Manage Files:**
   
     ```bash
     http://IP/files
     ```