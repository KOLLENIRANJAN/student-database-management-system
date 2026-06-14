import oracledb

conn = oracledb.connect(
    user="system",
    password="Oracle@123", # Replace with your actual password
    dsn="localhost/XE"
)

cursor = conn.cursor()

while True:
    print("\n===== Student Database Management System =====")
    print("1. View Students")
    print("2. Add Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    # 1. VIEW ALL STUDENTS (READ)
    if choice == "1":
        cursor.execute("SELECT student_id, student_name, department, semester, cgpa FROM students ORDER BY student_id")
        rows = cursor.fetchall()

        print("\nStudent Records\n")
        for row in rows:
            print(row)

    # 2. ADD STUDENT (CREATE)
    elif choice == "2":
        sid = int(input("Student ID: "))
        name = input("Student Name: ")
        dept = input("Department: ")
        sem = int(input("Semester: "))
        cgpa = float(input("CGPA: "))

        cursor.execute(
            """
            INSERT INTO students (student_id, student_name, department, semester, cgpa)
            VALUES(:1,:2,:3,:4,:5)
            """,
            (sid, name, dept, sem, cgpa)
        )
        conn.commit()
        print("Student Added Successfully")

    # 3. SEARCH STUDENT (READ ONE)
    elif choice == "3":
        search_id = int(input("Enter Student ID to Search: "))
        cursor.execute(
            "SELECT student_id, student_name, department, semester, cgpa FROM students WHERE student_id = :1", 
            (search_id,)
        )
        row = cursor.fetchone()
        
        print("\nStudent Record Found:\n")
        if row:
            print(row)
        else:
            print("No student found with that ID.")

    # 4. UPDATE STUDENT (UPDATE)
    elif choice == "4":
        update_id = int(input("Enter Student ID to Update: "))
        
        print("Enter New Details (Leave blank to keep old value):")
        new_name = input("New Student Name: ")
        new_dept = input("New Department: ")
        new_sem = input("New Semester: ")
        new_cgpa = input("New CGPA: ")
        
        # Build dynamic updates based on what you fill out
        updates = []
        params = {}
        
        if new_name:
            updates.append("student_name = :name")
            params['name'] = new_name
        if new_dept:
            updates.append("department = :dept")
            params['dept'] = new_dept
        if new_sem:
            updates.append("semester = :sem")
            params['sem'] = int(new_sem)
        if new_cgpa:
            updates.append("cgpa = :cgpa")
            params['cgpa'] = float(new_cgpa)
            
        if updates:
            params['id'] = update_id
            sql_query = f"UPDATE students SET {', '.join(updates)} WHERE student_id = :id"
            cursor.execute(sql_query, params)
            conn.commit()
            print("Student Updated Successfully")
        else:
            print("No changes made.")

    # 5. DELETE STUDENT (DELETE)
    elif choice == "5":
        delete_id = int(input("Enter Student ID to Delete: "))
        
        cursor.execute("DELETE FROM students WHERE student_id = :1", (delete_id,))
        conn.commit()
        print("Student Record Deleted Successfully")

    # 6. EXIT
    elif choice == "6":
        break

    else:
        print("Invalid Choice")

cursor.close()
conn.close()