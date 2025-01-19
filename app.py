from flask import Flask, request, jsonify, render_template
from models import get_all_tasks, add_task, delete_task

app = Flask(__name__)

# API Endpoint: Get all tasks
@app.route("/api/tasks", methods=["GET"])
def api_get_tasks():
    tasks = get_all_tasks()
    return jsonify(tasks)

# API Endpoint: Add a new task
@app.route("/api/tasks", methods=["POST"])
def api_add_task():
    data = request.json
    add_task(data["title"], data["description"])
    return jsonify({"message": "Task added successfully!"})

# API Endpoint: Delete a task
@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def api_delete_task(task_id):
    delete_task(task_id)
    return jsonify({"message": "Task deleted successfully!"})

# Frontend: Render homepage
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
