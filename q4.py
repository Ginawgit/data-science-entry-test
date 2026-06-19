#Task 1#
def string_reverse(s):
    if not isinstance(s, str):
        print("The input must be a string.")
    return s[::-1]

#Task 2#
string_reverse("Hello World")
'dlroW olleH'

string_reverse("Python")
'nohtyP'
