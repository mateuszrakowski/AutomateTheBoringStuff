# 1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.
spam = 2

assert spam > 10, "Spam is less than 10."


# 2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
eggs = "eggs"
bacon = "eGgS"

assert eggs.lower() != bacon.lower(), "Eggs and bacon are the same."


# 3. Write an assert statement that always triggers an AssertionError.
assert True != True, "Always false."