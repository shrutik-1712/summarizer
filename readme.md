# Project Submission Date
28-07-2024

# Project Name
Text Summarizer using Ollama-2.0:5B

# Author Name
Shrutik Dawane

# Project Description
A text summarizer using ollama model 2:0.5B to able to summarizer text accordingly.

# Project Setup

0. install ollama from the website
    1. in CMD write the command pip install ollama
    1. in CMD write the command ollama run qwen2:0.5b to install it to the locally

2. Install Python
    1. Download and Install Python (3.5 < version < 3.12)

3. Create a new virtual environment and activate it.
    1. python3 -m virtualenv venv
    2. \venv\Scripts\activate


4. Install the following packages using Python Package Manager: requests, ollama, virtualenv
    1. pip install <package_name>
    or you can directly install 
    1. pip install -r reqirements.txt
    to install all the dependencies


5. Pull the Ollama-2.0: 5B Model from the Ollama registry
    1. pull ollama Ollama-2.0:5B


6. Freeze the requirements to a requirements.txt file for easy access in future project setup.
    1. pip freeze > requirements.txt

7. Create a new file that contains the text to summarize.
8. Excute the main code file.
    1. If you want to used input your own text file 
        A. please use this command
            a. python main.py -t "your text"
    2. if you want to use a file use this command.
        A. python main.py --file sample.txt