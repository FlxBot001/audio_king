Here's the complete README in code format for you to copy:

```markdown
# Audio Streaming Application

## Overview

The **Audio Streaming Application** is a robust backend service designed for streaming audio content. Built with Flask, this application enables users to register, log in, upload audio files, and stream them efficiently. It aims to provide a seamless user experience with a focus on security and performance.

## Features

- **User Registration and Authentication**: Secure user sign-up and login with JWT token-based authentication.
- **Audio File Uploads**: Users can upload audio files, which are processed and stored for streaming.
- **Audio Processing**: Automatic conversion of uploaded files to a preferred format (e.g., MP3) for compatibility.
- **List Uploaded Audio Files**: Users can retrieve a list of all uploaded audio files.
- **RESTful API**: Well-defined API endpoints for easy integration and access.

## Technologies Used

- **Backend**: Flask
- **Database**: SQLite (can be configured for PostgreSQL or MySQL)
- **Audio Processing**: Pydub
- **Authentication**: JWT (JSON Web Tokens)
- **Environment Management**: Python venv

## Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git

### Steps to Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd audio-streaming-app/backend
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file with your configurations**:
   ```bash
   SECRET_KEY=your-secret-key
   DATABASE_URL=sqlite:///db.sqlite
   ```

5. **Initialize the database**:
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

6. **Run the application**:
   ```bash
   python run.py
   ```

### API Endpoints

| Method | Endpoint        | Description                               |
|--------|-----------------|-------------------------------------------|
| POST   | /register       | Register a new user                      |
| POST   | /login          | Login to get a JWT token                 |
| POST   | /upload         | Upload an audio file                      |
| GET    | /audio-files    | List all uploaded audio files            |

### Example Usage

#### Register a New User
```bash
curl -X POST http://localhost:5000/register -H "Content-Type: application/json" -d '{"username": "testuser", "password": "securepassword"}'
```

#### Upload an Audio File
```bash
curl -X POST http://localhost:5000/upload -F "file=@path_to_your_audio_file.mp3" -H "Authorization: Bearer <your_token>"
```

#### List Uploaded Audio Files
```bash
curl -X GET http://localhost:5000/audio-files -H "Authorization: Bearer <your_token>"
```

## Contributing

We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [Flask](https://flask.palletsprojects.com/) for the lightweight framework.
- Thanks to [Pydub](https://pydub.com/) for the audio processing capabilities.
- Special thanks to contributors and the open-source community.
```

Feel free to modify any parts to fit your project better!