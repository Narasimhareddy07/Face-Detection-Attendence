CREATE DATABASE face_attendance;

USE face_attendance;

CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    time DATETIME DEFAULT CURRENT_TIMESTAMP
);
SELECT * FROM attendance;