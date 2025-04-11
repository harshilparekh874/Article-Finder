# Article-Finder

Article-Finder is a web application built with Flask that allows users to search for articles from multiple sources—including academic publications via CrossRef, news articles via NewsAPI, and Wikipedia articles via the MediaWiki API. It features a modern, responsive UI built with Tailwind CSS.

# Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Running Locally](#running-locally)
- [Deployment](#deployment)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

# Features

- **Multi-Source Search:**  
  Search for articles from multiple sources:
  - **Academic Articles:** Retrieves scholarly content using the [CrossRef API](https://api.crossref.org/).
  - **News Articles:** Gathers current news via the [NewsAPI](https://newsapi.org/).
  - **Wikipedia Articles:** Fetches article details from the [MediaWiki API](https://www.mediawiki.org/wiki/API:Main_page).
- **Responsive Design:**  
  Built with Tailwind CSS, Article-Finder offers a modern and responsive experience on desktops, tablets, and mobile devices.
- **Dynamic Content Rendering:**  
  Utilizes Flask and Jinja2 templates to dynamically process search queries and render results.

# How It Works

1. **User Input:**  
   Users enter their search query and select the search type (academic, news, or Wikipedia) through a web form.
2. **API Integration:**  
   - For academic searches, the app queries the CrossRef API.
   - For news searches, it queries the NewsAPI.
   - For Wikipedia searches, it queries the MediaWiki API.
3. **Results Display:**  
   The retrieved data is processed and rendered dynamically into HTML templates for display.

# Project Structure

Article-Finder/ ├── app.py # Main Flask application ├── requirements.txt # Project dependencies └── templates/ # HTML templates ├── index.html # Home page template └── results.html # Search results page template

bash
Copy

# Installation and Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/harshilparekh874/Article-Finder.git
   cd Article-Finder
Create a Virtual Environment and Install Dependencies:

bash
Copy
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Running Locally
To run the application locally, execute:

bash
Copy
python app.py
Then, open your browser and navigate to http://127.0.0.1:5000/ to use Article-Finder.

Deployment
Article-Finder can be deployed on platforms such as Render.

Render Settings:

Build Command:

bash
Copy
pip install -r requirements.txt
Start Command (Production Recommended):

bash
Copy
gunicorn app:app --preload
Alternatively, for testing purposes:

bash
Copy
python app.py
Root Directory:
If your app.py and templates folder are at the repository root, leave this setting blank; otherwise, set it to the subdirectory containing your application files.

Configuration
API Keys:
In app.py, update the NewsAPI key by replacing:

python
Copy
NEWS_API_KEY = "5671956c374a43e699defd6923b1b02c"
with your actual NewsAPI key.

Search Types:
The application supports three search types:

academic

news

wikipedia

Troubleshooting
Template Not Found:
Ensure that the templates directory is in the same folder as app.py and that the file names are exactly index.html and results.html (case-sensitive).

No Search Results:
If queries return no results, try using specific, known keywords and verify API responses with debug print statements.

Connection Errors:
Check that your API keys are valid, confirm your network connection, and inspect error logs to troubleshoot issues with external API calls.

Contributing
Contributions are welcome!
Feel free to fork this repository and submit pull requests for improvements or bug fixes. For major changes, please open an issue first to discuss your proposed changes.

License
This project is open source and available under the MIT License.

Contact
For questions, suggestions, or feedback, please contact harshilparekh874@gmail.com.

