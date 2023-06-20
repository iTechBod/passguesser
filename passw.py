inputs = []

while True:
    user_input = input("Enter a piece of information (type 'i am done' to exit): ")
    
    if user_input.lower() == "i am done":
        break
    
    inputs.append(user_input)

# Generate unique passwords from the inputs
passwords = []
for i in range(len(inputs)):
    for j in range(len(inputs)):
        if i != j:
            password = inputs[i] + inputs[j]
            passwords.append(password)

# Write the passwords to a text file
filename = "passwords.txt"
with open(filename, "w") as file:
    for password in passwords:
        file.write(password + "\n")

print(f"Passwords created and saved to '{filename}' file.")
