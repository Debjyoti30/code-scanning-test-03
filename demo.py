def execute_user_code(user_code):
    # Code Injection Vulnerability: Directly executing user-provided code
    exec(user_code)

if __name__ == "__main__":
    # Simulate user input
    user_code = input("Enter code to execute: ")
    
    # Print the user input for logging (optional)
    print(f"Executing user code: {user_code}")
    
    # Execute the user-provided code with potential code injection
    execute_user_code(user_code)
