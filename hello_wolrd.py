# Simple greeting program
def greet_user(name: str) -> str:
    """
    Generate a personalized greeting message
    Args:
        name: The user's name
    Returns:
        A formatted greeting string
    """
    return f"Hello, {name}! Welcome to modern software engineering."

def main():
    """Main function to run the greeting program"""
    user_name = input("Enter your name: ")
    greeting = greet_user(user_name)
    print(greeting)

if __name__ == "__main__":
    main()

