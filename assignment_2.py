#************************************
# Name: Meghan McClaskey
# Date: 02/04/2020
# Program Description: This script will compute the BMI and the general retirement age of the user.
#************************************
import math

print("*** Welcome to the BMI/retirement calculator! *** \n")

while True:
	
	print("Option 1: Caclulate your BMI. ")
	print("Option 2: Caclulate your retirement age.")
	print("Option 3: Exit the program. \n")

	print("** Please select an option by inputting the number of the option. (ex. 1, 2, or 3) ** \n")
	selection = input("Selection:")
	
	if selection == 1:
		while True:
			
			try:
				weightPounds = int(input("Please input your weight in pounds: "))

			except (NameError, RuntimeError, TypeError, ValueError, IOError):
				print("Sorry, your input is not understood.")
				continue

			if weightPounds < 0:
				print("Your weight cannot be less than zero.")
				continue

			if weightPounds > 500:
				print("Weights above 500lbs are not supported.")
				continue

			else:
				break

		while True:
			
			try:
				heightInches = int(input("Please input your height in inches: "))

			except (NameError, RuntimeError, TypeError, ValueError, IOError):
				print("Sorry, your input is not understood.")
				continue

			if heightInches < 0:
				print("Your height cannot be less than zero.")
				continue

			if heightInches > 100:
				print("Heights above 100 inches are not supported.")
				continue

			else:
				break

		weightKilos = weightPounds * 0.45

		heightMeters = heightInches * 0.025

		metersSquared = heightMeters * heightMeters

		bmi =  weightKilos / metersSquared

		print("Your BMI is: " + str(bmi))
		print("-----------------------------")

	elif selection == 2:
		while True:

			try:
				currAge = int(input("Please input your current age: "))

			except (NameError, RuntimeError, TypeError, ValueError, IOError):
				print("Sorry your input is not understood.")

			if currAge < 18:
				print("Your age cannot be less than 18.")
				continue

			if currAge > 100:
				print("Your age cannot be more than 100.")
				continue

			else:
				break

		while True:
			
			try:
				currSalary = int(input("Please input your current salary: "))

			except (NameError, RuntimeError, TypeError, ValueError, IOError):
				print("Sorry your input is not understood.")

			if currSalary < 10000:
				print("Your salary cannot be less than $10000.")
				continue

			if currSalary > 15000000:
				print("Your salary cannot be more than $15,000,000.")
				continue

			else:
				break

		while True:

			try:
				desiredGoal = int(input("Please input your desired retirement goal:"))

			except (NameError, RuntimeError, TypeError, ValueError, IOError):
				print("Sorry your input is not understood.")

			if desiredGoal < 100000:
				print("Your desired savings goal cannot be less than $0.")
				continue

			if desiredGoal > 20000000:
				print("Your desired savings goal cannot be more than $20,000,000.")
				continue

			else:
				break

		death = 100
		percentSave = 0.35

		annualSav = currSalary * 0.35
		numYearsSaving = math.ceil(desiredGoal/annualSav)
		ageReach = numYearsSaving + currAge

		print("")

		print("The age you will be able to retire at with your current goal is: " + str(ageReach))

		if ageReach > 100:
			print("You will not reach the goal before death.")

		print("-----------------------------")

	elif selection == 3:
		print("Thank you for using the BMI/retirement calculator!")
		break
	else:
		print("\n")
		print("*** Your selection is not supported. Please input a 1, 2, or 3. ***")

		
