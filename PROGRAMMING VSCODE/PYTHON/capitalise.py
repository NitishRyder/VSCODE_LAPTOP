def capitalize_first_last_letters(str1):
     str1 = result = str1.title()
     result =  ""
     for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]  

print(capitalize_first_last_letters("vit"))
print(capitalize_first_last_letters("university"))
print(capitalize_first_last_letters("vellore"))
print(capitalize_first_last_letters("tamilnadu"))
print(capitalize_first_last_letters("india"))

