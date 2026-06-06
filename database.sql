CREATE TABLE students (
    student_id NUMBER PRIMARY KEY,
    student_name VARCHAR2(50),
    department VARCHAR2(30),
    semester NUMBER,
    cgpa NUMBER(3,2)
);

INSERT INTO students VALUES (101,'Niranjan','CSM',6,6.50);
INSERT INTO students VALUES (102,'Kiran','CSM',6,8.10);
INSERT INTO students VALUES (103,'Teja','CSE',6,7.80);

COMMIT;