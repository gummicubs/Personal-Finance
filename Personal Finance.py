import sys

def not_serious():
    print('You are not taking this serious. You are on your own.')

def int_charge(principle, rate, frequency):
    int_ = (principle * (1+ rate/(100*frequency))**frequency) - principle
    return int_

print('Welcome to your personal financial center! I shall be your financial advisor. Let us look at your current financial standing.')
print('How much do you have saved? If you owe money instead, please add a negative sign.')
try:
    cash = float(input())
except ValueError:
    not_serious()
    sys.exit()
if cash < 0:
    print('Looks like you have a negative equity. We must fix that first before moving on. What percent of interest is charged on your loans?')
    int_rate = input()
    int_rate = float(iT_rate)
    interest = int_charge(-cash, int_rate, 12)
    print('What is your annual income after taxes?')
    income = int(input())
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
        expense = int(input())
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
                loan = (loan*(1+iT_rate/12)**12)-remainder
            print('It will take you a minimum of ' + str(yr) + ' years to pay off the loan. You can reduce this time by increasing your income or reducing your expenses.')
            print('You may return when you pay off your loan.')
else:
    if cash > 1000000000:
        print('My, you are a billionaire. You do not need me, but I shall continue anyway.')
    print('How old are you?')
    age = int(input())
    if age >= 65:
        print('Unforuntately, I am unsure I would be able to help you. You are already of retired age.')
        sys.exit()
    elif age < 18:
        print('It is very wise of you to have came to see me. You has been taught well. Blessed you parents.')
    elif age > 55:
        print('I hope you have seen financial guidance previous to now. You do not have many years to alter your financial circumstances.')
    print('Do you intend to retire at the age of 65?')
    ans = input()
    if ans.lower() == 'yes':
        rtage = 65
    elif ans.lower() == 'no':
        print('What age do you intend to retire?')
        rtage = int(input())
        if rtage < age:
            print('I do not know how to go back in time. Goodbye.')
            sys.exit()
    else:
        not_serious() 
        sys.exit()
    yrs_left = rtage - age
    print('Looks like you would like to retire in ' + str(rtage-age) + ' years')
    print('What do you expect you annual expense to be after you retire?')
    expense = int(input())
    print('Did you consider inflation?')
    ans = input()
    if ans.lower() == 'yes':
        print('Good.')
    elif ans.lower() == 'no':
        expense = expense*(1.03)**yrs_left
    else:
        print('You are not answering my question. You are on your own. I am very busy') 
        sys.exit()
    print('Are you planning to live off of your passive income or savings?')
    ans = input()
    while (ans != 'passive income') and (ans != 'savings'):
            print('I do not understand. Please pick one of the two choices.')
            ans = (input())
    if ans == 'savings':
        print('How old are you expecting to live up to? You cannot live forever on your savings.')
        old_age = int(input())
        yrs_retired = old_age - rtage
        savings_needed = expense
        for y in range (yrs_retired):
            savings_needed = savings_needed + expense*(1.03)
        print('You will need $' + str(round(savings_needed,2)) + ' saved when you retire. You will need to save $' + str(round(savings_needed - cash),2) + ' more.')
        print('You will have to save $' + str(round((savings_needed - cash)/yrs_left,2)) + ' each year on average.')
    else:
        invest = expense/0.07
        print('By the time you retire, you will need $' + str(round(invest,2)) + ' in the market. You will still need to save $' + str(round((invest - cash),2)) + ' more.')
        print('How much are you investing into the market each year?')
        rep_inv = int(input())
        total_inv = cash
        for y in range (yrs_left):
            total_inv = (total_inv + rep_inv)*(1.07)
        if total_inv < invest:
            print('Unfortunately, you are not contributing enough towards the market. You must invest more. You will only have $' + str(round((total_inv),2)) + ' by then.')
            print('You would only have $' + str(round(total_inv,2)) + ' by the time you intend to retire.')
        else:
            print('If you keep that up, you will be ready to retire at ' + str(rtage) + '.')
            print('You would have $' + str(round(total_inv,2)) + ' saved by the time you intend to retire.')