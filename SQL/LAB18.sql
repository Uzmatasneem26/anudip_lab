CREATE DATABASE EMPLOYEE;
USE EMPLOYEE ;
CREATE TABLE EMPLOYEE (EMP_ID INT PRIMARY KEY,FIRST_NAME VARCHAR(50),LAST_NAME VARCHAR(50),AGE INT ,EMAIL VARCHAR(50));
INSERT INTO EMPLOYEE VALUES 
(101,"uzma","tasneem",22,"uzma@gmail.com"),
(102,"sabah","alia",19,"sabah@gmail.com"),
(103,"zaiba","tabassum",22,"zaiba@gmail.com");
SELECT FIRST_NAME,LAST_NAME 
FROM EMPLOYEE;
UPDATE EMPLOYEE SET AGE=33 WHERE EMP_ID=103;
SELECT * FROM EMPLOYEE WHERE AGE>30;
UPDATE EMPLOYEE SET AGE=AGE+1 WHERE AGE >25;
SELECT * FROM EMPLOYEE ;


CREATE TABLE DOCTOR(
 DOCTORID INT PRIMARY KEY ,
 DOCTORNAME VARCHAR(50));
CREATE TABLE PATIENT (
PATIENTID INT PRIMARY KEY ,
PATIENTNAME VARCHAR(50),
AGE INT , GENDER VARCHAR(50),
DISEASE VARCHAR(50),
DOCTORID INT ,
FOREIGN KEY (DOCTORID) REFERENCES DOCTOR (DOCTORID));
CREATE TABLE EMERGENCYCONTACT (
CONTACTID INT PRIMARY KEY,
PATIENTID INT ,
CONTACTNAME VARCHAR(50),
RELATIONSHIP VARCHAR(50),
PHONE INT ,
EMAIL VARCHAR(50),
FOREIGN KEY (PATIENTID) REFERENCES PATIENT (PATIENTID));

INSERT INTO Doctor (DoctorID, DoctorName)
VALUES (1, 'Dr. Brown'),
       (2, 'Dr. Green');

INSERT INTO Patient (PatientID, PatientName, Age, Gender, Disease, DoctorID)
VALUES (101, 'Alice Smith', 29, 'F', 'Diabetes', 1),
       (102, 'Mark Davis', 40, 'M', 'Hypertension', 2);

INSERT INTO EmergencyContact (ContactID, PatientID, ContactName, Relationship, Phone, Email)
VALUES (1, 101, 'John Smith', 'Husband', 111111, 'john@example.com'),
       (2, 101, 'Sarah White', 'Sister', 222222, 'sarah@example.com'),
       (3, 102, 'Lisa Davis', 'Wife', 333333, 'lisa@example.com');

SELECT 
    p.PatientID,
    p.PatientName,
    p.Age,
    p.Gender,
    p.Disease,
    d.DoctorName,
    ec.ContactName,
    ec.Relationship,
    ec.Phone,
    ec.Email
FROM Patient p
JOIN Doctor d ON p.DoctorID = d.DoctorID
JOIN EmergencyContact ec ON p.PatientID = ec.PatientID;
