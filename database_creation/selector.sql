-- Get all tasks for specific user
SELECT * 
FROM tasks 
WHERE user_id = 1;

-- Select tasks with specific status
SELECT * 
FROM tasks
WHERE status_id IN (SELECT id 
    FROM status 
    WHERE name = 'new');

-- Update task status
UPDATE tasks 
SET status_id = 2 
WHERE id = 1;

-- Get list of users who have no tasks
SELECT * 
FROM users
WHERE id NOT IN (SELECT user_id 
    FROM tasks);

-- Add new task for specific user
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('title', 'description', 1, 1);

-- Get all tasks which are not completed
SELECT *
FROM tasks
WHERE status_id NOT IN (SELECT id
    FROM status
    WHERE name = 'completed');

-- Delete task by id
DELETE 
FROM tasks 
WHERE id = 1;

-- Get list of users with specific email
SELECT *
FROM users
WHERE email LIKE '%@example.com';

-- Update user fullname
UPDATE users
SET fullname = 'Bill Gates'
WHERE id = 1;

-- Get count of tasks grouped by status
SELECT status.name, COUNT(tasks.id) AS total_tasks
FROM tasks
JOIN status ON tasks.status_id = status.id
GROUP BY status.name;

-- Get tasks assigned to users with specific email domain
SELECT t.title, t.description, t.status_id, u.fullname, u.email
FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';

-- Get list of tasks without descriptions
SELECT *
FROM tasks
WHERE description IS NULL;

-- Select users and their tasks in specific status
SELECT u.fullname, t.title, t.description, s.name
FROM users u
JOIN tasks t ON u.id = t.user_id
JOIN status s ON t.status_id = s.id
WHERE s.name = 'in progress';

-- Select users and count of their tasks
SELECT u.fullname, COUNT(t.id) AS total_tasks
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;
