# Django Project Setup

To run this Django project, follow the steps below:

1. **Install Python**

   Make sure Python is installed on your system. You can check by running:

   ```bash
   python --version
   ```
   *If it is not installed, go to [python.org](https://www.python.org/) and download that version of python based on your OS.*
2. **Create a Virtual Environment**
   Create a virtual environment according to your operating system:

   On Linux / macOS:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   On Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. **Install Required package**
   After activating the virtual environment, install all required packages using:
   ```bash
   pip install -r requirements.txt
   ```
## Now you can run the Project by using:
  On Linux / macOS:
  ```bash
  python3 manage.py runserver
  ```
  On Windows:
  ```bash
  python manage.py runserver
  ```
