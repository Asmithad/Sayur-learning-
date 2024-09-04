#Google and find the tax slabs for income tax for India. Write a program to calculate the income tax for an #individual. Input is Salary. Optional input - any deductions.
#Code:

# Get user input for salary
salary = float(input("Enter salary: "))
# Check if the entered salary is zero or negative and prompt the user to enter a correct salary
if salary <= 0:
    print("Enter correct salary!!")
else:
    # Get user input for deductions
    deduction = float(input("Enter deductions (optional): "))
 # Check if the deduction is negative or greater than the salary and prompt the user to enter a correct deduction
    if deduction < 0 or deduction > salary:
        print("Enter correct deduction!!")
    else:
        # Calculate taxable income after deductions
        taxableIncome = salary - deduction

        # Initialize tax rate and calculate income tax
        if taxableIncome <= 300000:
            print("No tax")
        elif 300000 < taxableIncome <= 600000:
            # Initialize tax rate as 5%
            taxRate = 0.05
            #Income Tax=(TaxableIncome−Lower Limit)×Tax Rate
            incomeTax = (taxableIncome - 300000) * taxRate
            print("Your income tax is: ", incomeTax)
        elif 600000 < taxableIncome <= 900000:
            # Initialize tax rate as 10%
            taxRate = 0.10
            #Income Tax=(Taxable Income−Lower Limit)×Tax Rate+Fixed Amount
            incomeTax = (taxableIncome - 600000) * taxRate + 15000
            print("Your income tax is: ", incomeTax)
        elif 900000 < taxableIncome <= 1200000:
            # Initialize tax rate as 15%
            taxRate = 0.15
            #Income Tax=(Taxable Income−Lower Limit)×Tax Rate+Fixed Amount
            incomeTax = (taxableIncome - 900000) * taxRate + 45000
            print("Your income tax is: ", incomeTax)
        elif 1200000 < taxableIncome <= 1500000:
            # Initialize tax rate as 20%
            taxRate = 0.20
            #Income Tax=(Taxable Income−Lower Limit)×Tax Rate+Fixed Amount
            incomeTax = (taxableIncome - 1200000) * taxRate + 90000
            print("Your income tax is: ", incomeTax)
        else:
            # Initialize tax rate as 30%
            taxRate = 0.30
            #Income Tax=(Taxable Income−Lower Limit)×Tax Rate+Fixed Amount
            incomeTax = (taxableIncome - 1500000) * taxRate + 150000
            print("Your income tax is: ", incomeTax)

