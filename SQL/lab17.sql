
CREATE DATABASE Anudip1;
USE Anudip1;

CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    Gender VARCHAR(10),
    Email VARCHAR(100),
    Phone VARCHAR(15)
);
CREATE TABLE Course (
    CourseID INT PRIMARY KEY,
    CourseTitle VARCHAR(100),
    Credits INT
);
CREATE TABLE Instructor (
    InstructorID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100)
);
CREATE TABLE Enrollment (
    EnrollmentID INT PRIMARY KEY,
    EnrollmentDate DATE,
    StudentID INT,
    CourseID INT,
    InstructorID INT,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
    FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
);
CREATE TABLE Score (
    ScoreID INT PRIMARY KEY,
    CourseID INT,
    StudentID INT,
    DateOfExam DATE,
    CreditObtained INT,
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);
CREATE TABLE Feedback (
    FeedbackID INT PRIMARY KEY,
    StudentID INT,
    Date DATE,
    InstructorName VARCHAR(100),
    Feedback TEXT,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);
INSERT INTO Student VALUES
(1, 'Amit', 'Sharma', '2000-01-15', 'Male', 'amit@gmail.com', '9876543210'),
(2, 'Neha', 'Verma', '1999-05-12', 'Female', 'neha@gmail.com', '9876543211'),
(3, 'Ravi', 'Kumar', '2001-03-21', 'Male', 'ravi@gmail.com', '9876543212'),
(4, 'Pooja', 'Singh', '2002-07-18', 'Female', 'pooja@gmail.com', '9876543213'),
(5, 'Rahul', 'Jain', '1998-09-09', 'Male', 'rahul@gmail.com', '9876543214');
INSERT INTO Course VALUES
(101, 'Python Programming', 4),
(102, 'Web Development', 3),
(103, 'Database Systems', 4),
(104, 'Machine Learning', 5),
(105, 'Cloud Computing', 3);
INSERT INTO Instructor VALUES
(201, 'Suresh', 'Mehta', 'suresh@anudip.org'),
(202, 'Anita', 'Kapoor', 'anita@anudip.org'),
(203, 'Vikram', 'Rao', 'vikram@anudip.org'),
(204, 'Meena', 'Gupta', 'meena@anudip.org'),
(205, 'Arjun', 'Patel', 'arjun@anudip.org');
INSERT INTO Enrollment VALUES
(301, '2025-01-10', 1, 101, 201),
(302, '2025-01-12', 2, 102, 202),
(303, '2025-01-15', 3, 103, 203),
(304, '2025-01-20', 4, 104, 204),
(305, '2025-01-25', 5, 105, 205);
INSERT INTO Score VALUES
(401, 101, 1, '2025-03-10', 85),
(402, 102, 2, '2025-03-12', 90),
(403, 103, 3, '2025-03-15', 75),
(404, 104, 4, '2025-03-18', 80),
(405, 105, 5, '2025-03-20', 88);
INSERT INTO Feedback VALUES
(501, 1, '2025-03-21', 'Suresh Mehta', 'Very interactive sessions'),
(502, 2, '2025-03-22', 'Anita Kapoor', 'Loved the hands-on approach'),
(503, 3, '2025-03-23', 'Vikram Rao', 'Good course structure'),
(504, 4, '2025-03-24', 'Meena Gupta', 'Excellent explanations'),
(505, 5, '2025-03-25', 'Arjun Patel', 'Great examples and teaching');

select * from feedback;
select * from Score;
select * from Instructor ;
select * from Course ;
select * from Student;
select * from  Enrollment;