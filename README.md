# Moodify

## Project Overview
Moodify is an innovative application designed to help users manage and track their moods effectively. By providing insightful analytics and suggestions based on the user's mood data, Moodify empowers individuals to improve their emotional well-being.

## Tech Stack
- **Frontend:** React
- **Backend:** Node.js, Express
- **Database:** MongoDB
- **Hosting:** Heroku
- **Libraries:** Mongoose, Axios, Redux

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/ohnohimanshu/Moodify.git
   cd Moodify
   ```
2. Install the dependencies:
   ```bash
   npm install
   ```
3. Set up environment variables:
   Create a `.env` file in the root directory and add the required environment variables.
4. Start the application:
   ```bash
   npm start
   ```

## Features
- User authentication and profiles
- Mood tracking and analytics
- Visual representations of mood trends
- Suggestions for improving mood based on data analysis.
- Integration with wearable devices for real-time mood tracking.

## Deployment Guide
1. Make sure your application is production-ready.
2. Push your code to the main branch of your GitHub repository.
3. Use Heroku CLI to create a new app:
   ```bash
   heroku create moodify-app
   ```
4. Deploy to Heroku:
   ```bash
   git push heroku main
   ```
5. Ensure all environment variables are set correctly on Heroku.
6. Open your application in the browser:
   ```bash
   heroku open
   ```

## License
This project is licensed under the MIT License.