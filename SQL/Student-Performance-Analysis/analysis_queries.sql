USE StudentAnalysis;

-- Query 1: Display all students
SELECT * FROM Students;


-- Query 2: Display students who scored more than 80 marks
SELECT * FROM Students
WHERE marks > 80;


-- Query 3: Display students from the AIML department
SELECT * FROM Students
WHERE department = 'AIML';


-- Query 4: Display all unique departments
SELECT DISTINCT department
FROM Students;


-- Query 5: Display students in descending order of marks
SELECT * FROM Students
ORDER BY marks DESC;


-- ==========================================
-- STEP 5: INTERMEDIATE SQL QUERIES
-- ==========================================

-- Query 6: Count the total number of students
SELECT COUNT(*) AS total_students
FROM Students;


-- Query 7: Find the highest marks
SELECT MAX(marks) AS highest_marks
FROM Students;


-- Query 8: Find the lowest marks
SELECT MIN(marks) AS lowest_marks
FROM Students;


-- Query 9: Calculate the average marks
SELECT AVG(marks) AS average_marks
FROM Students;


-- Query 10: Count students in each department
SELECT department, COUNT(*) AS total_students
FROM Students
GROUP BY department;


-- Query 11: Calculate average marks for each department
SELECT department, AVG(marks) AS average_marks
FROM Students
GROUP BY department;


-- Query 12: Display departments with average marks above 75
SELECT department, AVG(marks) AS average_marks
FROM Students
GROUP BY department
HAVING AVG(marks) > 75;


-- ==========================================
-- STEP 6: ADVANCED SQL QUERIES
-- ==========================================

-- Query 13: Assign grades to students
SELECT *,
CASE
    WHEN marks >= 85 THEN 'A'
    WHEN marks >= 70 THEN 'B'
    WHEN marks >= 50 THEN 'C'
    ELSE 'D'
END AS grade
FROM Students;


-- Query 14: Find the student(s) with the highest marks
SELECT * FROM Students
WHERE marks = (
    SELECT MAX(marks)
    FROM Students
);


-- Query 15: Find the student(s) with the second-highest distinct marks
SELECT * FROM Students
WHERE marks = (
    SELECT MAX(marks)
    FROM Students
    WHERE marks < (
        SELECT MAX(marks)
        FROM Students
    )
);


-- Query 16: Find students who scored above the class average
SELECT * FROM Students
WHERE marks > (
    SELECT AVG(marks)
    FROM Students
);


-- Query 17: Find the department with the highest average marks
SELECT department, AVG(marks) AS average_marks
FROM Students
GROUP BY department
ORDER BY average_marks DESC
LIMIT 1;


-- Query 18: Count passed and failed students
SELECT
    CASE
        WHEN marks >= 50 THEN 'Pass'
        ELSE 'Fail'
    END AS result,
    COUNT(*) AS total_students
FROM Students
GROUP BY result;
