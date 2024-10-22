
# Resume Analysis AI

This is a web application that allows users to upload their resumes and get analysis based on AI models. The analysis provides insights into the structure, formatting, and content quality of resumes, helping users optimize them for better results in job applications.

## Features

- **Resume Upload**: Users can upload their resume files in PDF format.
- **AI-Based Analysis**: The app leverages AI to analyze resumes for formatting, keyword matching, content quality, and more.
- **Real-time Feedback**: Provides instant feedback on how to improve resumes.
- **PDF Preview**: Displays a preview of the uploaded resume file for easy reference.

## Tech Stack

- **Frontend**: React, Material UI for UI components.
- **Backend**: Django/Flask (adjust as necessary), REST API to handle file uploads and trigger AI analysis.
- **AI Integration**: OpenAI models for text analysis.
- **State Management**: React hooks like `useState`, `useEffect`.
- **File Handling**: Uses JavaScript `File` and `URL` APIs to handle PDF uploads and previews.

## Prerequisites

- **Node.js** (v14 or later)
- **npm** or **yarn** for dependency management
- **Python** (v3.9 or later) for backend setup

## Installation

1. **Clone the Repository**:

   ```bash
   git clone git@github.com:serifenuruysal/ResumeAnalysisAI.git
   cd ResumeAnalysisAI
   ```

2. **Install Frontend Dependencies**:

   ```bash
   cd frontend
   npm install
   ```

3. **Install Backend Dependencies**:

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

## Environment Variables

Create a `.env` file in the root directory to store environment variables such as API keys, database credentials, etc.

Example:

```
REACT_APP_API_URL=http://localhost:8000/api
```

## Running the Application

1. **Start the Frontend**:

   ```bash
   cd frontend
   npm start
   ```

   The app will be running on `http://localhost:3000`.

2. **Start the Backend**:

   ```bash
   cd backend
   python manage.py runserver
   ```

   The backend will be running on `http://localhost:8000/api`.
