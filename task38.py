def add_entry(directory, name, phone):
    directory[name] = phone

def delete_entry(directory, name):
    if name in directory:
        del directory[name]

def update_entry(directory, name, new_phone):
    if name in directory:
        directory[name] = new_phone

def find_entry(directory, name):
    return directory.get(name, "Not found")
    
# Использование:

directory = {}
add_entry(directory, "John Doe", "1234567890")
print(directory) # {'John Doe': '1234567890'}

update_entry(directory, "John Doe", "0987654321")
print(directory) # {'John Doe': '0987654321'}

print(find_entry(directory, "John Doe")) # 0987654321

delete_entry(directory, "John Doe")
print(directory) # {}

print(find_entry(directory, "John Doe")) # Not found
