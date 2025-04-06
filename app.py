from flask import Flask, request, render_template

app = Flask(__name__)

# Function to check password strength
def check_password_strength(password):
    """
    Check if the password meets the strength criteria:
    Minimum 8 characters, at least one uppercase letter,
    at least one lowercase letter, at least one digit,
    """
    
    # Return if the password is empty or less than the minimum length
    if len(password) < 8:
        return False
    
    # check if the password
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-+?_=,<>/" # special characters
    
    # Loop through each character in the password
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
            
    return has_upper and has_lower and has_digit and has_special # return True if all conditions are met

# Route for the home page
@app.route('/', methods=['GET', 'POST'])

def index():
    message = None # message variable to store the result
    if request.method == 'POST':
        password = request.form.get('password', '')
        
        # if password is empty, return an error message
        if not password.strip():
            message = 'Password cannot be empty!'
        
        # Validate the password strength
        elif check_password_strength(password):
            message = 'Password is strong!'
            
            # Check if the password is in the list of common passwords
        else:
            message = 'Password is weak. Make sure it has:<br>'
            message += '- At least 8 characters<br>'
            message += '- At least one uppercase letter<br>'
            message += '- At least one lowercase letter<br>'
            message += '- At least one digit<br>'
            message += '- At least one special character<br>'
    
    return render_template('index.html', message=message)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
