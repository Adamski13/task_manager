from lib.to_do import *

# ```Given an empty string, the output is False```
def test_for_empty_string():
    result = contains_todo("")
    assert result == False


#```Given a string that contains TODO, output is True```
def test_if_string_contains_TODO():
    result = contains_todo("This text contains TODO hurray")
    assert result == True

# ```Given a string that doesnt contain TODO, output is False```
def test_if_string_doesnt_contain_TODO():
    result = contains_todo("Hey, there's nothing to do here.")
    assert result == False


#```Given a string that contains todo, output is False```
def test_if_string_contains_non_capital_todo():
    result = contains_todo("This text contains todo, hurray or not?")
    assert result == False

#```Given a string that contains TODO! with punctuation, output is True```
def test_if_string_contains_TODO_with_punctuation():
    result = contains_todo("Hey Adam, do you remember todays !TODO! Plants need watering")
    assert result == True

#```Test for different data type. Only string is valid input therefore only string returns True```
def test_if_input_is_string():
    result = contains_todo(["this", "text", "TODO", "is", "list"])
    assert result == False