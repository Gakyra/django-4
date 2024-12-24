import sqlite3

conn = sqlite3.connect('app.db')
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    text TEXT NOT NULL,
    user INTEGER,
    likes INTEGER DEFAULT 0,
    created_at DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY(user) REFERENCES user(id)
)
""")


cursor.execute("""
INSERT INTO user (name, password, email) VALUES
('Alice', 'alice123', 'alice@example.com'),
('Bob', 'bob123', 'bob@example.com'),
('Charlie', 'charlie123', 'charlie@example.com');
""")


cursor.execute("""
INSERT INTO post (text, title, content, user, likes) VALUES
('First post', 'Title 1', 'Content 1', 1, 10),
('Second post', 'Title 2', 'Content 2', 2, 5),
('Third post', 'Title 3', 'Content 3', 3, 15),
('Fourth post', 'Title 4', 'Content 4', 1, 8),
('Fifth post', 'Title 5', 'Content 5', 2, 20);
""")


cursor.execute("""
UPDATE user SET password = 'new_password' WHERE id IN (1, 3)
""")

cursor.execute("SELECT * FROM user")
users = cursor.fetchall()
print("Users:", users)


cursor.execute("SELECT * FROM post")
posts = cursor.fetchall()
print("Posts:", posts)


cursor.execute("DELETE FROM post WHERE id = 5")
conn.commit()


cursor.execute("SELECT * FROM post WHERE likes > 100;")
posts_with_likes = cursor.fetchall()
print("Posts with more than 100 likes:", posts_with_likes)


cursor.execute("""
SELECT user.name, COUNT(post.id) as post_count 
FROM user 
JOIN post ON user.id = post.user 
GROUP BY user.id 
HAVING post_count > 2;
""")
users_with_many_posts = cursor.fetchall()
print("Users with more than 2 posts:", users_with_many_posts)


cursor.execute("""
SELECT user.name, SUM(post.likes) as total_likes 
FROM user 
JOIN post ON user.id = post.user 
GROUP BY user.id;
""")
users_likes_sum = cursor.fetchall()
print("Users and total likes on their posts:", users_likes_sum)


cursor.execute("""
SELECT user.name, MAX(post.likes) as max_likes 
FROM user 
JOIN post ON user.id = post.user 
WHERE post.created_at >= '2023-01-01'
GROUP BY user.id;
""")
users_max_likes_2023 = cursor.fetchall()
print("Users and their maximum likes on posts since 2023:", users_max_likes_2023)


conn.close()
