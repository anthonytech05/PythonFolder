

#  write, read, append .. binary format, byte  mode = r, w,a 
# file_reader = open('C:/Users/CHIDI/OneDrive/Desktop/Pythonfolder/calculator.py','r')
# content = file_reader.read()
# print('------------------------------')
# print(content)
# print('------------------------------')

# file_reader.close()

file_writer = open('C:/Users/CHIDI/OneDrive/Desktop/Pythonfolder/storage/details.txt','w')
file_writer.write('\nCALL 911')
print('content written successfully to file')

file_writer.close()
