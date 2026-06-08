# WhatsApp Chat Analyzer 

An interactive Streamlit web application that analyzes exported WhatsApp chats and generates meaningful insights through visualizations, activity trends, word clouds, emoji analysis, and user statistics.

## Live Demo

https://analyzer-whatsapp-chats.streamlit.app/

## Features

### Chat Statistics

* Total messages
* Total words exchanged
* Media messages shared
* Links shared

### Timeline Analysis

* Monthly message activity timeline
* Daily message activity timeline

### Activity Analysis

* Weekly activity distribution
* Monthly activity distribution
* User activity heatmap by day and hour

### Group Insights

* Most active users in a group chat
* User contribution percentages

### Text Analysis

* Word cloud generation
* Most common words used

### Emoji Analysis

* Emoji frequency table
* Interactive emoji distribution pie chart

### User-wise Analysis

Analyze:

* Entire group chats
* Individual participants

## Tech Stack

* Python
* Streamlit
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* WordCloud
* Emoji
* URLExtract

## Project Structure

```text
Whatsapp_Chat_Analyzer/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── stop_words.txt
└── src/
    ├── preprocess.py
    └── utilities.py
```

## Installation

### Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Whatsapp_Chat_Analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

## How to Use

1. Export a WhatsApp chat from your phone.
2. Choose **Without Media** while exporting.
3. Open the web application.
4. Upload the exported `.txt` file.
5. Select a user or analyze the entire group.
6. Explore statistics and visualizations.

## Visualizations Included

* Monthly Timeline
* Daily Timeline
* Weekly Activity Map
* Monthly Activity Map
* User Activity Heatmap
* Most Active Users
* Word Cloud
* Most Common Words
* Emoji Analysis

## Privacy

This application processes uploaded chat files only for analysis purposes. Users can upload their own WhatsApp exports and generate insights without sharing their data publicly.

## Author

Akshat

If you found this project interesting, feel free to star the repository.
