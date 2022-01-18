
def addToList(tasks, amount):
    for i in range(amount):
        task = []
        print("-------- NEW TASK -------")
        tname = input("Enter the name of the task:")
        task.append("To do -> " + tname)
        deadline = input("Enter the deadline date of the task:")
        task.append("DeadLine -> " + deadline)
        description = input("Enter the description of the task:")
        task.append("Description -> " + description)
        tasks.append(task)
    return tasks

def removeTask(tasks, amount):
    print(tasks)
    rtask = int(input("Enter the number of the task you want to remove"))
    if rtask > amount:
        print("1")





def searchTheTask(rtask, tasks):

