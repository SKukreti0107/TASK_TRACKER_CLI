import argparse
import json 
from datetime import datetime as dt

class Task:
    def __init__(self,id, description):
        
        self.id = id 
        self.data = {
            "description": description,
            "status": "to-do",
            "createdAt": str(dt.now()),
            "updatedAt": str(dt.now())
        }

class TasksManager:
    def __init__(self):
        
        try:
            with open("tasks.json","r") as file:
                self.tasks = json.load(file)
                

            
        except:
            print("No existing tasks found.")
        

    def add_task(self, task: Task):
        self.tasks[task.id] = task.data

    def load_tasks(self,tasks):
        with open("tasks.json","w") as file:
            json.dump(tasks,file,indent=4)

    def update_task(self,task_id,description=None):
        if str(task_id) in self.tasks.keys():
            self.tasks[str(task_id)]["description"] = description
            self.tasks[str(task_id)]["updatedAt"] = str(dt.now())
            self.load_tasks(self.tasks)
        else:
            print("Task not found.")
        


        

def main():
    print("Task Tracker CLI")
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)
    

    #parsers for each command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", nargs="+", help="Task description")

    update_parser = subparsers.add_parser("update", help="Update an existing task")
    update_parser.add_argument("task_id", help="Task ID to update",type=int)
    update_parser.add_argument("description", nargs="+", help="New task description",)

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", help="Task ID to delete",type=int)

    mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Mark a task as in-progress")
    mark_in_progress_parser.add_argument("task_id", help="Task ID to mark as in-progress",type=int)

    mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done")
    mark_done_parser.add_argument("task_id", help="Task ID to mark as done",type=int)

    list_tasks_parser = subparsers.add_parser("list", help="List all tasks")
    list_tasks_parser.add_argument("status",choices=["to-do","in-progress","done"],nargs="?", help="Filter tasks by status")

    args = parser.parse_args()
    
    TM = TasksManager()
   
    task_id = len(TM.tasks) +1
    
    if args.command == "add":
   
        new_tasks = Task(task_id, " ".join(args.description))
        TM.add_task(new_tasks)
      
        TM.load_tasks(TM.tasks)
        print("Task added successfully.")

    if args.command == "update":
    
        task_id = int(args.task_id)
        new_description = " ".join(args.description)
        TM.update_task(task_id,new_description)
        print("Task updated successfully.")
        

    if args.command == "delete":
        task_id = str(args.task_id)
        if task_id in TM.tasks.keys():
            del TM.tasks[task_id]
            TM.load_tasks(TM.tasks)
            print("Task deleted successfully.")
        else:
            print("Task not found.")

    if args.command == "mark-in-progress":
        task_id = str(args.task_id)
        if task_id in TM.tasks.keys():
            TM.tasks[task_id]["status"] = "in-progress"
            TM.tasks[task_id]["updatedAt"] = str(dt.now())
            TM.load_tasks(TM.tasks)
            print("Task marked as in-progress.")    

    if args.command == "mark-done":
        task_id = str(args.task_id)
        if task_id in TM.tasks.keys():
            TM.tasks[task_id]["status"] = "done"
            TM.tasks[task_id]["updatedAt"] = str(dt.now())
            TM.load_tasks(TM.tasks)
            print("Task marked as done.")
        else:
            print("Task not found.")

    if args.command == "list":
        status_filter = args.status
        for id,task_details in TM.tasks.items():
            if status_filter is None or task_details["status"] == status_filter:
                data = {
                    "id": id,
                    "description": task_details["description"],
                    "status": task_details["status"],
                    "createdAt": task_details["createdAt"],
                    "updatedAt": task_details["updatedAt"]
                }
                print(data)
                print("-"*20)
    
if __name__ == "__main__":
    main()
