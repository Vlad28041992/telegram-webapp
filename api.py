from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
app.config['DEBUG'] = True  # Показываем ошибки

# Укажи полный путь к базе
DB_PATH = "C:/Users/mrn-v/MyReviewPanel/tasks.db"  # <-- проверь, тмм или другая папка

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT id, platform, description, city, direction, price FROM task")
        rows = cursor.fetchall()
        conn.close()

        tasks = []
        for row in rows:
            tasks.append({
                "id": row[0],
                "platform": row[1],
                "description": row[2],
                "city": row[3],
                "direction": row[4],
                "price": row[5],
            })

        return jsonify(tasks)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=8000)