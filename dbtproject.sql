drop database quiz_db;
CREATE DATABASE IF NOT EXISTS quiz_db;
USE quiz_db;

-- Table to store participant user accounts
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    username VARCHAR(50) UNIQUE NOT NULL,
    upassword VARCHAR(50) NOT NULL
);

-- Table to store examiner staff accounts
CREATE TABLE IF NOT EXISTS staff (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    spassword VARCHAR(50) NOT NULL
);

-- Table to store quiz questions
CREATE TABLE IF NOT EXISTS questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question_text TEXT NOT NULL,
    option1 VARCHAR(255) NOT NULL,
    option2 VARCHAR(255) NOT NULL,
    option3 VARCHAR(255) NOT NULL,
    option4 VARCHAR(255) NOT NULL,
    correct_answer INT NOT NULL CHECK (correct_answer BETWEEN 1 AND 4)
);

-- Table to store answers submitted by participants
CREATE TABLE IF NOT EXISTS answers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    question_id INT NOT NULL,
    answer INT NOT NULL CHECK (answer BETWEEN 1 AND 4),
    is_correct BOOLEAN,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (question_id) REFERENCES questions(id)
);

-- Insert sample participants (without specifying 'id' since it's auto-increment)
INSERT INTO users (username, upassword) VALUES
('participant101', 'password123'),
('participant201', 'password456');

-- Insert sample staff
INSERT INTO staff (username, spassword) VALUES
('examiner1', 'examinerpass');

-- Insert sample questions
INSERT INTO questions (question_text, option1, option2, option3, option4, correct_answer) VALUES
('What is the capital of France?', 'Berlin', 'Madrid', 'Paris', 'Rome', 3),
('Which planet is known as the Red Planet?', 'Earth', 'Mars', 'Jupiter', 'Venus', 2),
('What is the largest mammal?', 'Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus', 2);

-- View all questions
SELECT * FROM questions;
