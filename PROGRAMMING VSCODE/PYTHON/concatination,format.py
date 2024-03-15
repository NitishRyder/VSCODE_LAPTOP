#concatenate str to other str 
age=27               #F-strings 
name='John'
txt=f'Hello{name}.You are{age}years old'
print(txt)

speed =25
time = 2
txt= f'The distance travelled is {speed*time}miles'
print(txt)

val=12.3756
a=f'{val:.2f}'
print(a)

val=12.3756
a=f'{val:.3f}'
print(a)

val=12.3756
a=f'{val:.5f}'
print(a)
