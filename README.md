## Overview
This Django application includes user authentication with the ability to log in, sign up, reset passwords, and manage user profiles. The following features are implemented:

- User authentication with either email or username and password.
- Pages for login, signup, forgot password, change password, dashboard, and profile.
- Access to certain pages is restricted based on user authentication status.

## Requirements
- Docker
- for complete functionality of reset password fill the SMTP Host email and password in env file

## How to run
To run this application, use the following Docker commands:

```bash
docker-compose build
docker-compose up
```

## Features

### Login Page
- **Fields:** 
  - Username/Email
  - Password
- **Options:** 
  - Sign Up
  - Forgot Password

### Sign Up Page
- **Fields:** 
  - Username
  - Email
  - Password
  - Confirm Password
- **Option:** 
  - Back to Login page

### Forgot Password Page
- **Requires user to be signed up**
- **Field:** 
  - Email
- **Function:** 
  - Send reset instructions (Sends an email with a password reset link)

### Change Password Page
- **Requires authentication**
- **Fields:** 
  - Old Password
  - New Password
  - Confirm Password
- **Option:** 
  - Back to Dashboard

### Dashboard Page
- **Accessible only to authenticated users**
- **Content:** 
  - Displays greeting message ("Hi, username!")
  - Links to Profile page and Change Password page
  - Option to logout

### Profile Page
- **Displays information:** 
  - Username
  - Email
  - Date Joined
  - Last Updated
- **Options:** 
  - Back to Dashboard
  - Logout

