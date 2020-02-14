import sys

def not_serious():
    print('You are not taking this serious. You are on your own.')

def balance_w_interest(principle, rate, frequency):
    balance = (principle * (1+ rate/(100*frequency))**frequency)
    return balance
#Returns the new balance after principal grows at rate with frequency

def int_charge(principle, rate, frequency):
    int_ = balance_w_interest(principle, rate, frequency) - principle
    return int_
#Returns how much interest is charged for a given principle at a given annual rate and frequency compounded in a year

def inflation_adj(amount, years):
    inf_adj = amount*(1.03)**years
    return inf_adj
#Returns the inflation adjusted value of a given amount after however many years at an inflation rate of 3%

def compound_addition_growth(amount, rate, addition, years):
    compound = amount
    for time in years:
        compound = balance_w_interest(compound, rate, 12) + addition
    return compound
#Returns amount after compound growth ate a given rate with consistent additions for however many years

print('Welcome to your personal financial center! I shall be your financial advisor. Let us look at your current financial standing.')
print('How much do you have saved? If you owe money instead, please add a negative sign.')
try:
    cash = float(input())
except ValueError:
    not_serious()
    sys.exit()
if cash < 0:
    print('Looks like you have a negative equity. We must fix that first before moving on. What percent of interest is charged on your loans?')
    int_rate = float(input())
    interest = int_charge(-cash, int_rate, 12)
    print('What is your annual income after taxes?')
    income = float(input())
    if income <= interest:
        print('You do not make enough to pay off your debt. Please claim bankruptcy. Will you take my advice?')
        bank = input()
        if bank.lower() == 'yes':
            print('Good. You are a smart person. You can return here after you have done so.')
        if bank.lower() == 'no':
            print('Then you will need a higher paying job or marry rich. When you have done either one, you can return and we can move forward.')
        else:
            not_serious()
    else:
        print('How much is your annual expense?')
        expense = float(input())
        if (expense + interest) >= income:
            print('At this rate, you will always stay in debt. Would you be able to reduce your annual expense or increase your annual income?')
            ans = input()
            if ans.lower() == 'yes':
                print('Great! Come back when you have done either one or both.')
            elif ans.lower() == 'no':
                print('Then you should consider filing for bankruptcy. Come back when you have done so.')
            else:
                not_serious()
        else:
            remainder = income - expense
            loan = -cash
            yr = 0
            while loan > 0:
                yr = yr + 1
                loan = loan - remainder + int_charge(loan, int_rate, 12)
            print('It will take you a minimum of ' + str(yr) + ' years to pay off the loan. You can reduce this time by increasing your income or reducing your expenses.')
            print('You may return when you pay off your loan.')
else:
    if cash > 1000000000:
        print('My, you are a billionaire. You do not need me, but I shall continue anyway.')
    print('How old are you?')
    age = input()
    while not age.isdecimal():
        print('Please provide an integer value for your age.')
        age = input()
    age = int(age)
    if age >= 65:
        print('Unforuntately, I am unsure I would be able to help you. You are already of retired age.')
        sys.exit()
    elif age <0:
        print('You must teach me how to have a negative age.')
        sys.exit()
    elif age < 18:
        print('It is very wise of you to have come to see me. You have been taught well. Bless your parents.')
    elif age > 55:
        print('I hope you have seen financial guidance previous to now. You do not have many years to alter your financial circumstances.')
    print('At what age do you intend to retire?')
    rtage = input()
    while not rtage.isdecimal():
        print('Please provide an numeric value of what age you would like to retire.')
        rtage = input()
    rtage = int(rtage)
    if rtage <= age:
        print('I do not know how to go back in time. Goodbye.')
        sys.exit()
    yrs_left = rtage - age
    print('Looks like you would like to retire in ' + str(yrs_left) + ' years')
    print('What do you expect your annual expense to be after you retire?')
    expense = float(input())
    print('Did you consider inflation?')
    ans = input()
    if ans.lower() == 'yes':
        print('Good.')
    elif ans.lower() == 'no':
        expense = inflation_adj(expense, yrs_left)
    else:
        not_serious()
        sys.exit()
    print('How much annual income do you expect to get after you retire, such as a pension or social security? You can answer 0 if you would like to be conservative.')
    ret_income = float(input())*0.7
    if ret_income > expense:
        print('It appears your expected retired income will be enough to support you after retirement. You are in good shape.')
        sys.exit()
    else:
        print('It appears your retirement income alone might not be enough to support your retired life when we take taxes into consideration.')
        print('You will need additional income, like passive income, or have extra savings to make up the difference.')
    print('Would you like to consider having a passive income stream or to have extra savings?')
    ans = input()
    while (not ans.startswith('passive')) and (ans.lower() != 'extra savings'):
            print('I do not understand. Please pick one of the two choices.')
            ans = (input())
    if ans == 'extra savings':
        print('What is length of your life expectancy? Because your savings will be limited after you retire, we will need to consider the length of time your savings will have to support you for.')
        old_age = int(input())
        yrs_retired = old_age - rtage
        savings_needed = expense 
        for y in range (yrs_retired):
            savings_needed = savings_needed + expense*(1.03)**y
        savings = savings_needed - (yrs_retired * ret_income)
        print('You will need $' + str(round(savings,2)) + ' saved when you retire. You will need to save $' + str(round((savings - cash),2)) + ' more.')
        print('You will have to save $' + str(round((savings - cash)/yrs_left,2)) + ' each year on average.')
    else:
        invest = (expense-ret_income)/0.07
        print('By the time you retire, you will need $' + str(round(invest,2)) + ' in the market. You will still need to save $' + str(round((invest - cash),2)) + ' more.')
        print('How much are you investing into the market each year?')
        rep_inv = int(input())
        total_inv = cash
        for y in range (yrs_left):
            total_inv = (total_inv + rep_inv)*(1.1)
        if total_inv < invest:
            print('Unfortunately, you are not contributing enough towards the market. You must invest more. You will only have $' + str(round((total_inv),2)) + ' by then.')
            z = 1
            while total_inv < invest:
                z = z + 0.05
                total_inv = cash
                for y in range (yrs_left):
                    total_inv = (total_inv + z*rep_inv)*(1.1)
            print('However, if you can increase you annual contribution towards the martket to $' + str(round(z*rep_inv,2)) + ', you will be able to save enough.')
        else:
            print('If you keep that up, you will be ready to retire at ' + str(rtage) + '.')
            print('You would have $' + str(round(total_inv,2)) + ' saved by the time you intend to retire.')
            total_inv = cash
            rtage = age
            while total_inv < invest:
                rtage = rtage + 1
                total_inv = (total_inv + rep_inv)*(1.1)
            print('You can even retire earlier if you would like. At this rate you can retire at the age of ' + str(rtage) + '.')
