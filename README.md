# Chunk-reading aid tool
This tool is actively under development to enhance L2 English reading on reading speed and comprehension.  
Chunk reading, also called slash or phrase reading, involves breaking text into meaningful multiword units for easier processing. 
This strategy, widely used in L2 learning, enhances reading and listening fluency.  
This tool displayed passages in consecutive chunks, with the center of each text chunk on the screen.  
The participants were instructed to focus on the center of each chunk and to move their gaze steadily downward as additional chunks were presented. 
By shifting the participants' reading strategy from word-by-word reading to chunk-based reading, this design aimed to enhance reading comprehension by reducing the eye fixation durations.

## Features
- **Deployment Options:** Run the software (.exe) either locally.

## How to Use

### Installation

**Prerequisites:**
 - Python 3.10.6
 - flask >= 2.3.2
 - flask_cors >= 3.0.10

**Code:**
 - Clone the repository to your local machine:
 - [Learn Git with tutorials](https://www.atlassian.com/git)

### Running Locally
 - Run [exe](https://github.com/hayashik/peda-chunk-reading-tool/releases/tag/1.0.0) file in your local Windows.
 - Python

   1. Install Python3 into your PC:
   [Python.org](https://www.python.org/downloads/)
   2. Install the required dependencies:
   ```pip install -r requirements.txt```
   3. Now that the Python environment is set up, you can run the project locally:
   ```python main.py```
   4. If you see the following message, please open the URL in your browser:
```
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8080
Press CTRL+C to quit
```

### Reading text
 - Place a backslash ( \\ ) at the beginning and end of the chunk you have selected, excluding the start and end of the sentence.
 - See sample_text.txt.

### Interface
 - Use the button below to read the text file.
 - "Display duration:" Set the interval for each chunk to appear in seconds.
 - "Maximum number of display lines:" Set number of lines are displayed. The top line will no longer be displayed.
 - "Font size:" Set font size
