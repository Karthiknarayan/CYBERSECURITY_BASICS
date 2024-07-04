import re

def check_password_strength(password):
    # Criteria for password strength
    criteria = {
        'length': len(password) >= 8,
        'uppercase': re.search(r'[A-Z]', password) is not None,
        'lowercase': re.search(r'[a-z]', password) is not None,
        'numbers': re.search(r'[0-9]', password) is not None,
        'special_characters': re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    }
    
    # Feedback messages
    feedback = {
        'length': "Password should be at least 8 characters long.",
        'uppercase': "Password should include at least one uppercase letter.",
        'lowercase': "Password should include at least one lowercase letter.",
        'numbers': "Password should include at least one number.",
        'special_characters': "Password should include at least one special character."
    }
    
    # Calculate strength score
    score = sum(criteria.values())
    strength = 'Weak' if score < 3 else 'Medium' if score < 5 else 'Strong'
    
    # Provide detailed feedback
    failed_criteria = [feedback[c] for c in criteria if not criteria[c]]
    detailed_feedback = "\n".join(failed_criteria)
    
    return {
        'strength': strength,
        'score': score,
        'feedback': detailed_feedback
    }

# Main program
if __name__ == "__main__":
    password = input("Enter your password: ")
    result = check_password_strength(password)
    
    print(f"Password Strength: {result['strength']}")
    print(f"Score: {result['score']}/5")
    if result['feedback']:
        print("Feedback:")
        print(result['feedback'])
    #simply to check