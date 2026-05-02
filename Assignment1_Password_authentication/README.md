# Assignment 1: Password Authentication

## Overview
A secure password authentication system that validates password strength and implements secure password hashing with salt.

## Features
- **Password Strength Validation**: Checks for minimum length (8 chars), uppercase, lowercase, numbers, and special characters
- **Secure Hashing**: Uses PBKDF2-HMAC-SHA256 with salt for password storage
- **Login System**: Verifies entered passwords against stored hashes

## How It Works
1. User creates a password that meets strength requirements
2. Password is hashed with a random salt and stored securely
3. User can log in by entering their password
4. System verifies the entered password against the stored hash

## Requirements
- Python 3.x
- Built-in libraries: `hashlib`, `os`, `re`

## Usage
```bash
python pass.py
```

Follow the prompts to create a password and test the login system.

## Key Concepts
- Password hashing with salt
- Regular expressions for validation
- PBKDF2 key derivation function
