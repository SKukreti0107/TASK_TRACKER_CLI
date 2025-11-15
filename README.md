# TASK TRACKER CLI : https://github.com/SKukreti0107/TASK_TRACKER_CLI
A basic to do task list in cli ,storing tasks data in JSON using the argparse library.

# USAGE:

## ADD A TASK:
* python main.py add "Buy groceries"

## UPDATEING AND DELETING TASKS:
* python main.py update 1 "Buy groceries and cook dinner"
* python main.py delete 1

## MARKING TASKS AS IN PROGRESS OR DONE:
* python main.py mark-in-progress 1
* python main.py mark-done 1    

## LISTING TASKS :

### LISTING ALL THE TASKS:
* python main.py list

### LISTING TASKS BY STATUS:
* python main.py list done
* python main.py list to-do
* python main.py list in-progress

