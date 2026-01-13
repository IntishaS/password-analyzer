import re 

def analyze_password_strength(password):

	"""
	Analyze password strength and return score (0-100) with feedback

	Criteria:
	1. Length (8+ characters)
	2. Lowercase letters
	3. Uppercase letters
	4. Numbers
	5. Special characters
	6. Not a common password
	"""

	#Common weak passwords that user should avoid
	COMMON_PASSWORDS = {
		'password', 
		'123456', 
		'12345678', 
		'1234', 
		'qwerty', 
		'letmein', 
		'football', 
		'iloveyou', 
		'admin', 
		'welcome',
		'abc123',
		'123123',
		'monkey',
		'password1'
	}
	

	score = 0
	feedback = []
	max_score = 100

	#1. Length check (25 points)
	if len(password) >= 12:
		score += 25
		feedback.append("Password Length: 12+ characters (Excellent)")
	elif len(password) >= 8:
		score += 20
		feedback.append("Password Length:8+ characters (Good)")
	else:
		feedback.append("Password Length: Too short (minimum 8 characters)")

	#2. Lowercase letters (15 points)
	if re.search(r'[a-z]', password):
		score += 15
		feedback.append("Password contains lowercase letters")
	else:
		feedback.append("Add lowercase letters to password")

	#3. Uppercase letters (15 points)
	if re.search(r'[A-Z]', password):
		score += 15
		feedback.append("Password contains uppercase letters")
	else:
		feedback.append("Add uppercase letters to password")

	#4. Numbers (15 points)
	if re.search(r'\d', password):
		score += 15
		feedback.append("Password contains numbers")
	else:
		feedback.append("Add numbers to password")

	#5. Special characters (15 points)
	if re.search(r'[!@#$%^&*_(),.?":{}|<>-]', password):
		score += 15
		feedback.append("Password contains special characters")
	else:
		feedback.append("Add special characters to password")

	#6. Not common password(15 points)
	if password.lower() not in COMMON_PASSWORDS:
		score += 15
		feedback.append("Not a common password")
	else:
		feedback.append("Avoid common passwords")

	return score, feedback

def get_strength_level(score):
	"""Convert score to strength level"""
	if score >= 90:
		return "STRONG", "Excellent! This is a secure password."
	elif score >= 70:
		return "GOOD", "Good password but could be stronger."
	elif score >= 50:
		return "FAIR", "Moderate password, consider improvements."
	else:
		return "WEAK", "Weak password, needs significant improvements."

def main():
	"""Simple command line interface"""
	print("=" * 50)
	print("PASSWORD STRENGTH ANALYZER")
	print("=" *50)
	print("\nAnalyze the strength of your password (type 'quit' to exit)")

	while True:
		print("\n" + "-" *30)
		password = input("\nEnter a password to analyze: ")

		if password.lower() == 'quit':
			print("\nThank you for using the Password strength analyzer!")
			break

		if not password:
			print("Please enter a password")
			continue

		# Analyze password
		score, feedback = analyze_password_strength(password)
		level, message = get_strength_level(score)

		#Display results
		print(f"\nAnalysis Results")
		print(f"Password: {'*' * len(password)}")
		print(f"Score: {score}/100")
		print(f"Strength: {level}")
		print(f"Message: {message}")

		print("\nDETAILED FEEDBACK:")
		for item in feedback:
			print(f" {item}")

if __name__ == "__main__":
	main()


