from backend.models import Project, Task

def create_project(name):
    try:
        Project(name).save()
        return f"✅ Project '{name}' created."
    except Exception as e:
        return f"❌ Error: {str(e)}"

def delete_project(name):
    Project.delete(name)
    return f"🗑️ Project '{name}' deleted."

def list_projects():
    return Project.all()

def add_task(title, project_id):
    Task(title, project_id).save()
    return f"📝 Task '{title}' added."

def complete_task(task_id):
    Task.complete(task_id)
    return f"✅ Task {task_id} marked as DONE."

def delete_task(task_id):
    Task.delete(task_id)
    return f"🗑️ Task {task_id} deleted."

def get_tasks(project_id):
    return Task.by_project(project_id)