#File Word Replacer

x = input("Enter the word to be replaced : ")
y = input("Enter the replacing word : ")

with open('input.txt','r') as file1 :
    content = file1.read().lower().replace(x,y)

with open('output.txt','w') as file2 :
    file2.write(content)

print(f"Result : {content}")