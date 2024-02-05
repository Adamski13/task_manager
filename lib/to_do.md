
## 1. Describe the Problem
#As a user
#So that I can keep track of my tasks
#I want to check if a text includes the string `#TODO`.



## 2. Design the Function Signature

def contains_todo(text):
    return True or False (boolean)

nouns: tasks, text, user
verbs: track, check

input: text
output: boolean

assumptions:
only returns true if TODO is all uppercase.


## 3. Create Examples as Tests

```Given an empty string, the output is False```

```Given a string that contains TODO, output is True```

```Given a string that doesnt contain TODO, output is False```

```Given a string that contains todo, output is False```

```Given a string that contains TODO! with punctuation, output is True```

```Test for different data type. Only string is valid input therefore returns False```

