'''
Why Handle Text Files?
Text files are everywhere—they're simple, lightweight, and perfect for storing small pieces of data. In this video, we'll cover:  
1. Creating and writing a text file.  
2. Reading from a file.  
3. Appending to an existing file.  
4. A simple real-world example.
'''

# Creating and writing to a file
# with open("example_file.txt","w") as file:
#     file.write("Hello Youtube!\n")
#     file.write("This is the second line.")

# print("File have been written successfully.")

# with open("example_file.txt","a") as file:
#     file.write("\nThis line have been added later.")

# print("File have been appended successfully.")

# Reading from a file
# read(): Reads the entire file.  
# readline(): Reads one line at a time.  
# readlines(): Reads all lines into a list.  

# with open("example_file.txt","r") as file:
#     content = file.read()
#     print(content)
# print("File have been read successfully.")

# Appending to a file

# A Real-World Example
import datetime

def log_activity(activity):
    with open("log_book.txt", "a") as file:
        timestamp = datetime.datetime.now()
        file.write(f"\n{timestamp} : {activity}\n")

log_activity("Using Youtube!")
log_activity("Having food.")

