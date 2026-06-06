# Student Database Management System

A robust, terminal-based Command Line Interface (CLI) application built to manage student records dynamically. This project demonstrates full **CRUD** operational capabilities by establishing a secure backend relational database connection between **Python** and an **Oracle Database** environment.

---

## 🛠️ Tech Stack & Architecture

* **Programming Language:** Python 3.x
* **Database Management System:** Oracle Database Express Edition (XE)
* **Database Driver:** Modern `oracledb` Thin/Thick client library

---

## 🚀 Core Features & Database Mapping

The application maps frontend console selections directly to backend relational database operations:

| Feature | Description | SQL Operation |
| :--- | :--- | :--- |
| **Add Student** | Generates new validated student profiles in the database. | `INSERT` |
| **View Students** | Fetches and formats all records into a structured terminal grid. | `SELECT` |
| **Search Student** | Targets and reads a single specific profile using a unique identifier. | `SELECT ... WHERE` |
| **Update Student** | Dynamically changes specific student metrics while preserving others. | `UPDATE` |
| **Delete Student** | Removes records safely with an integrated confirmation checkpoint. | `DELETE` |

---

## 🏗️ Database Schema

The underlying table structure implemented inside Oracle SQL for this system:

```sql
CREATE TABLE students (
    student_id NUMBER PRIMARY KEY,
    student_name VARCHAR2(50) NOT NULL,
    department VARCHAR2(30),
    semester NUMBER,
    cgpa NUMBER(3,2)
);

student-database-management-system/
│
├── student_management.py    # Main Python application source code 
├── database.sql             # SQL script for table schema initialization
└── requirements.txt         # Project dependencies (oracledb)