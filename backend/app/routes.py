from flask import request, jsonify
from app import app, db
from app.models import User, AudioFile
from app.services.audio_service import process_audio_file
from app.utils.auth import generate_token, verify_token
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Username already exists'}), 400
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        token = generate_token(user.id)
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    filepath = f"uploads/{file.filename}"
    file.save(filepath)

    audio_file = AudioFile(filename=file.filename, filepath=filepath)
    db.session.add(audio_file)
    db.session.commit()
    
    process_audio_file(filepath)  # Process the audio file
    return jsonify({'message': 'File uploaded successfully'}), 201

@app.route('/audio-files', methods=['GET'])
def get_audio_files():
    audio_files = AudioFile.query.all()
    return jsonify([{'id': af.id, 'filename': af.filename} for af in audio_files]), 200
