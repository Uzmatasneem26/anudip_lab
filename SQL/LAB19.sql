use anudip1;
create table employee (
e_id int primary key ,
e_name varchar(50),
e_department varchar(50),
salary float(20));

insert into employee values
(1,'uzma','ece',300000),
(2,'sabah','cse',400000),
(3,'zaiba','ise',300000);

select * from employee;

select e_department ,
avg(salary) as average_salary 
from employee 
group by e_department ;

select * from student;

SELECT * FROM STUDENT 
WHERE DATEOFBIRTH >2009-06-16;

SELECT * FROM STUDENT 
WHERE FIRSTNAME LIKE 'A%'or
FIRSTNAME LIKE 'J%';

CREATE TABLE PERSON (
PERSONID INT PRIMARY KEY ,
FIRSTNAME VARCHAR(20),
LASTNAME VARCHAR(20),
AGE INT);

CREATE TABLE Employee1 (
emp_id INT PRIMARY KEY,
first_name VARCHAR(255),
last_name VARCHAR(255),
age INT
);

INSERT INTO PERSON VALUES 
(101,'JOHN','STEVE',30),
(102,'MARIYA','JOSEPH',25),
(103,'DANIAL','GOUSE',15);

INSERT INTO EMPLOYEE1 VALUES
(101,'PRIYA','HS',22),
(102,'ROSHINI','MYLANAHALLI',25),
(103,'USHARANI','K',20);

SELECT PERSONID AS ID,
FIRSTNAME AS fIrst_name,
LASTNAME AS last_name ,
AGE  FROM PERSON
UNION
SELECT emp_id ,
first_name,
last_name ,
age FROM EMPLOYEE1;

SELECT s.StudentID, s.FirstName, s.LastName, e.EnrollmentID, e.CourseID
FROM Student s
RIGHT JOIN Enrollment e 
ON s.StudentID = e.StudentID;

SELECT S.STUDENTID,S.FIRSTNAME,S.LASTNAME,E.ENROLLMENTID,E.COURSEID 
FROM STUDENT S
LEFT OUTER JOIN ENROLLMENT E
ON S.STUDENTID=E.STUDENTID;

SELECT s.StudentID, s.FirstName, s.Email, e.EnrollmentID, e.CourseID
FROM Student s
LEFT JOIN Enrollment e 
ON s.StudentID = e.StudentID
UNION
SELECT s.StudentID, s.FirstName, s.Email, e.EnrollmentID, e.CourseID
FROM Student s
RIGHT JOIN Enrollment e 
ON s.StudentID = e.StudentID;