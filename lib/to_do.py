#As a user
#So that I can keep track of my tasks
#I want to check if a text includes the string `#TODO`.
#task_list, search, text)

def contains_todo(text):
    task_word = 'TODO'
    if isinstance(text, str) and task_word in text:
        return True
    else:
        return False
    
    