from db_config import get_connection

def get_all_tasks():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM tasks ORDER BY created_at DESC;")
            return cursor.fetchall()

def add_task(title, description):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO tasks (title, description) VALUES (%s, %s);", (title, description))
            conn.commit()

def delete_task(task_id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM tasks WHERE id = %s;", (task_id,))
            conn.commit()
