import re
regex="[a-z\.a-z0-9]+@[a-zA-Z]+\.(ac)\.(in)"
email="vikas.s2021@vitstudent.ac.in"
if(re.search(regex,email)):
    print("EMAIL:",email)
else:
    print("INVALID EMAIL") 

regex="[0-9A-Z0-9]"
registernumber="19MCA0021"
if(re.search(regex,registernumber)):
    print("REGISTER NUMBER:",registernumber)
else:
    print('INVALID NUMBER')