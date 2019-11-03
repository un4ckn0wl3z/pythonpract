fr = open('data.txt', 'r')
file_content = fr.read()
fr.close()
print(file_content)

user_name = input('Enter your name: ')

fw = open('data.txt', 'w')
fw.write(user_name)
fw.close()