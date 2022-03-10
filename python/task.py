import sys
import os
  
def help():
    helps = """Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics"""
    sys.stdout.buffer.write(helps.encode())
  
  
def add(priority, string):
    f = open('task.txt', 'a')
    f.write(string+" ["+priority+"]")
    f.write("\n")
    f.close()
    string = '"'+string+'"'
    sys.stdout.buffer.write(f"Added task: {string} with prority {priority}".encode())
  
  
def ls():
    try:
        nec()
        l = 0
        for i in sorted(lst, key = lambda k : k[-2]):
            sys.stdout.buffer.write(f"{l+1}. {i}".encode())
            sys.stdout.buffer.write("\n".encode('utf-8'))
            l+=1
  
    except Exception as e:
        raise e
  
  
def delete(index):
    try:
        index = int(index)
        nec()
        with open("task.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for i in lines:
                if i.strip('\n') != lst[index]:
                    f.write(i)
            f.truncate()
        sys.stdout.buffer.write(f"Deleted item with index {index}".encode())
  
    except Exception as e:
        sys.stdout.buffer.write(f"Error: item with index {index} does not exist. Nothing deleted.".encode())
  
  
def done(index):
    try:
        nec()
        index = int(index)
        f = open('completed.txt', 'a')
        st = lst[index][:-3]
        f.write(st)
        f.write("\n")
        f.close()
        sys.stdout.buffer.write(f"Marked item as done.".encode())
          
        with open("task.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for i in lines:
                if i.strip('\n') != lst[index]:
                    f.write(i)
            f.truncate()
    except Exception as e:
        sys.stdout.buffer.write(f"Error: no incomplete item with index {index} exists.".encode())
  
  
def report():
    try:
        nec()
        kf = open('task.txt', 'r')
        sys.stdout.buffer.write(f'Pending : {len(lst)}'.encode())
        c = 1
        for each in kf:
            lines = each.strip("\n")
            sys.stdout.buffer.write(c,end="")
            sys.stdout.buffer.write(".",end=" ")
            sys.stdout.buffer.write(lines)
    
        nf = open('completed.txt', 'r')
        c = 1
        sys.stdout.buffer.write(f'Completed : {len(don)}'.encode())
        for line in nf:
            line = line.strip('\n')
            don.update({c: line})
            sys.stdout.buffer.write(str(c)+".",line)
            c = c+1
        
        
    except Exception as e:
        sys.stdout.buffer.write(
            f' Pending : {len(lst)} Completed : {len(don)}'.encode())
        
def nec():
    try:
        f = open('task.txt', 'r')
        for line in f:
            line = line.strip('\n')
            lst.append(line)
    except Exception as e:
        sys.stdout.buffer.write("There are no pending todos!".encode())
  
  
if __name__ == '__main__': 
    try:
        lst = []
        don = {}
        args = sys.argv
        if(args[1] == 'del'):
            args[1] = 'delete'    
        if(args[1] == 'add' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing todo string. Nothing added!".encode())
  
        elif(args[1] == 'done' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for marking todo as done.".encode())
  
        elif(args[1] == 'deL' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for deleting todo.".encode())
        elif(args[1] == 'add'):
            globals()[args[1]](args[2], *args[3:])
        else:
            globals()[args[1]](*args[2:])
  
    except Exception as e:
        usage = """Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics"""
        sys.stdout.buffer.write(usage.encode())
        

