import random

def generate_random_integer(min_value, max_value):
    """
    Generates a random integer within a specified range.
    
    Args:
        min_value (int): The minimum value of the range.
        max_value (int): The maximum value of the range.
        
    Returns:
        int: A random integer within the range [min_value, max_value].
    """
    return random.randint(min_value, max_value)

def select_random_operator():
    """
    Selects a random arithmetic operator from the list (+, -, *).
    
    Returns:
        str: A random operator as a string.
    """
    return random.choice(['+', '-', '*'])

def create_math_problem(num1, num2, operator):
    """
    Creates a math problem string and calculates the correct answer based on the operator.
    
    Args:
        num1 (int): The first operand.
        num2 (int): The second operand.
        operator (str): The arithmetic operator, either '+', '-', or '*'.
        
    Returns:
        tuple: A tuple containing:
            - str: The math problem as a string.
            - int: The correct answer to the problem.
    """
    problem = f"{num1} {operator} {num2}"
    
    # Calculate the answer based on the operator
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        raise ValueError("Invalid operator.")
    
    return problem, answer

def math_quiz():
    """
    Runs the Math Quiz Game, which presents a series of math problems to the user and 
    calculates their score based on correct answers.
    """
    score = 0  # Track the player's score
    total_questions = 3  # Number of questions to be asked

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate two random numbers and a random operator
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = select_random_operator()

        # Create a math problem and get the correct answer
        problem, correct_answer = create_math_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Handle invalid input from the user
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue  # Skip to the next question if input is invalid

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    # Display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
