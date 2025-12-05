
--TASK 1
CREATE TABLE Members (
    member_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    join_date DATE
);

CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(200),
    author VARCHAR(100),
    available BOOLEAN
);

CREATE TABLE Loans (
    loan_id INT PRIMARY KEY,
    member_id INT,
    book_id INT,
    loan_date DATE,
    return_date DATE,
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

--TASK 2
INSERT INTO Members (member_id, name, email, join_date) VALUES
(1, 'Mahvish', 'abc@123.gmail.com', '2025-10-16'),
(2, 'Harshitha', 'def@gmail.com', '2025-10-10'),
(3, 'Anjali', 'ghi@gmail.com', '2025-10-24');

INSERT INTO Books (book_id, title, author, available) VALUES
(110, 'Atomic Habits', 'James Clear', TRUE),
(120, 'Rich Dad Poor Dad', 'Robert Kiyosaki', TRUE),
(130, 'The Power of Habit', 'Charles Duhigg', FALSE),
(140, 'The Alchemist', 'Paulo Coelho', TRUE);

INSERT INTO Loans (loan_id, member_id, book_id, loan_date, return_date) VALUES
(1, 1, 130, '2025-10-10', NULL),
(2, 2, 110, '2025-10-12', '2025-10-20'),
(3, 3, 120, '2025-10-15', NULL);

--TASK 3
SELECT*from Members WHERE join_date > '2025-09-01';
SELECT * FROM Members;
SELECT * FROM Books;
SELECT * FROM Loans;
SELECT 
    Books.book_id,
    Books.title,
    Books.author,
    Loans.loan_date,
    Loans.return_date
FROM Loans
JOIN Books ON Loans.book_id = Books.book_id
JOIN Members ON Loans.member_id = Members.member_id
WHERE Members.name = 'Mahvish';

--TASK 4
UPDATE Books
SET available = FALSE
WHERE book_id = 110;

DELETE FROM Members
WHERE member_id = 3;
DELETE FROM Members
WHERE member_id = 3;

SELECT * FROM Loans
WHERE member_id = 3 AND return_date IS NULL;
