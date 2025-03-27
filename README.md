# Social Media App

## Overview
This is a Django-based social media application that allows users to interact with each other through posts, comments, and a follower system. Users can register, create posts, comment on posts, manage followers, and search for other users.

## Features
- **User Authentication**: Register, login, and manage user accounts.
- **Post Management**: Create, edit, and delete posts.
- **Comment System**: Comment on specific posts.
- **Follow System**: Follow and unfollow users.
- **User Search**: Search for users by their username.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Django (>=4.0)
- Virtual Environment (Recommended)

### Setup
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <project-folder>
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser (optional but recommended for admin access):
   ```sh
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```
7. Access the application at: `http://127.0.0.1:8000/`

## Usage
- **Register/Login**: Users can sign up and log in to access features.
- **Create a Post**: Users can create posts that appear on their profile.
- **Comment on Posts**: Users can comment on posts to interact with others.
- **Edit/Delete Posts**: Users can modify or remove their own posts.
- **Follow Users**: Users can follow or unfollow others to stay updated on their posts.
- **Search Users**: Users can search for others by their usernames.

## Technologies Used
- Django (Backend Framework)
- Django Built-in Database (SQLite)
- Bootstrap (Frontend Framework)
- 

## Contributing
Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Add new feature"`
4. Push to the branch: `git push origin feature-name`
5. Create a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any queries, feel free to reach out via email or create an issue in the repository.
