import sys

def clean(field):
    zeros = field.copy()
    for k, v in zeros.items():
        if v == 0:
            del field[k]
#Remove 0's in a dictionary

def edit(Category, category):
    while True:
        print('Above is everything we have collected for you on ' + category + 's so far. Is it accurate?')
        ans = input().lower()
        if ans == 'yes':
            print('Great we shall wrap up this section.')
            break
        elif ans == 'no':
            print('Which of the above ' + category + 's would you like to edit? If you would like to add a new one on, what would you like to call it?')
            name = input().lower()
            print('What is the corresponding ' + category + ' for ' + name + '?')
            key = float(input())
            Category[name] = key
            clean(Category)
            profile(Income, Expense, Savings, Debt , Investment)
        else:
            print('I don\'t understand. Would you like to edit your ' + category + ' above?')
#Edits a dictionary

def annual_expenses():
    exp = {}
    print('How much do you spend on housing each month?')
    exp['housing'] = float(input()) * 12
    print('How much do you spend on food each month?')
    exp['food'] = float(input()) * 12
    print('Do you have a car?')
    while True:
        ans = input()
        if (ans.lower() != 'yes') and (ans.lower() != 'no'):
            print('Please answer the question. Do you have at least one car?')
            continue
        else:
            break
    if ans.lower() == 'yes':
        print('Do you pay for car insurance annually?')
        while True:
            ans = input()
            if ans.lower() == 'yes':
                print('How much do you pay car insurance per year?')
                exp['car_insurance']= float(input())
                break
            elif ans.lower() == 'no':
                print('How much do you pay for car insurance per month?')
                exp['car_insurance'] = float(input()) * 12
                break
            else:
                print('That does not answer my question. Do you pay your car insurance once a year?')
                continue
        print('How much do you spend on gas for your car per month?')
        exp['vehicle_gas'] = float(input()) *12
    print('How much do you spend on public transportation costs, such train ticket per month?')
    exp['transportation'] = float(input()) *12
    print('How much do you spend on your monthly utilities on average?')
    exp['utilities'] = float(input())*12
    print('Do you have any other monthly expenses. Examples of such expense might be child care or a monthly subscription?')
    while True:
        ans = input()
        if (ans.lower() != 'yes') and (ans.lower() != 'no'):
            print('Please answer the question. Do you have any other types of monthly expenses we have not accounted for?')
            continue
        elif ans.lower() == 'yes':
            print('What type of monthly expense is it?')
            spending = input()
            print('How much do you spend on ' + spending + ' per month?')
            exp[spending] = float(input())*12
            print('Do you have other monthly expenses?')
        else:
            break
    while True:
        print('What type of expenses do you have that does not occur on a monthly basis? Some examples are life insurance or tuition.')
        print('If there are no more expenses, please enter "Done".')
        spending = input()
        if spending.lower() == 'done':
            break
        else:
            print('How much do you spend on ' + spending + '?')
            cost = float(input())
            print('How often do you spend this expense per year?')
            f = int(input())
            exp[spending] = cost*f
    return exp
#Determines annual expense in a dictionary

def total(source):
    sum = 0
    for k, v in source.items():
        sum += float(str(v))
    return sum
#Determines total in a dictionary

def profile(income, expense, savings, debt, investment):
    print('1. Income '.center(50,'-'))
    income_sum = 0
    for k, v in income.items():
        print('     ' + k.ljust(30,'.') + str(v).rjust(5,' '))
        income_sum += float(str(v))
    print('     Total Annual Income'.ljust(35, '.') + str(income_sum).rjust(5,' ') + '\n')
    print('2. Expense '.center(50,'-'))
    expense_sum = 0
    for k, v in expense.items():
        print('     ' + k.ljust(30,'.') + str(v).rjust(5,' '))
        expense_sum += float(str(v))
    print('     Total Annual Expense'.ljust(35, '.') + str(expense_sum).rjust(5,' ') + '\n')
    print('3. Savings '.center(50,'-'))
    for k, v in savings.items():
        print('     ' + k.ljust(30,'.') + str(v).rjust(5,' '))
    print('4. Debt '.center(50,'-'))
    for k, v in debt.items():
        print('     ' + k.ljust(30,'.') + str(v).rjust(5,' '))
    print('5. Investments '.center(50,'-'))
    for k, v in investment.items():
        print('     ' + k.ljust(30,'.') + str(v).rjust(5,' '))


print('Welcome to your personal financial center! I shall be your financial advisor. \n Please excuse our appearance as we are under renovation.')
print('Well, let\'s get started shall we? Let\'s first take a look at your current financial standing.')
print('We will create a profile for you that covers five difference categories; \n 1. Income \n 2. Expense \n 3. Savings \n 4.  Debt \n 5. Investment')
Income = {}
Expense = {}
Savings{}
Debt = {}
Investment = {} 

print('Let\'s start filling out with the first category, income. For our purposes, income is consider money that you receive available for personal consumption.')
print('Will you be providing pre-tax income or post-tax income?')
while True:
    tx = input()
    if (tx.startswith('pre')) or (tx.startswith('post')):
        break
    else:
        print('Please specify if you will be providing pre-tax or post-tax income. Pre-tax income is income is the gross income on your paystub. Post-tax income is the amount you see on your paycheck.')
print('How many sources of income, not including any investments, do you have on a monthly basis? These are income you receive approximately 12 times a year.')
while True:
    try:
        x = int(input())
        break
    except ValueError:
        print('Please enter an integer that corresponds to how many sources of monthly income you receive.')
if x <= 0:
    print('You\'ve stated you have no sources income on a consistent monthly basis.')
    x = 0
elif x == 1:
    print('Name your source of income.')
    job = input()
    print('How much income does ' + job + ' provide you on a monthly basis?')
    mon_wage = float(input())
    Income[job] = mon_wage*12
else:
    i = 0
    print('Name one source of your monthly income.')
    while i < x:
        job = input()
        print('How much income does ' + job + ' provide you on a monthly basis?')
        mon_wage = float(input())
        Income[job] = mon_wage*12
        if i == x:
            break
        i +=1
        print('Name another source of your monthly income.')
while True:
    print('What is a source of income you receive that we have not accounted for? This income can be from contracted work or annual bonuses.')
    print('If we have accounted for all your annual income, enter "Done".')
    job = input()
    if job == 'done':
        break
    else:
        print('How much income does ' + job + ' provide you?')
        wage = float(input())
        print('How many times do you receive this income per year?')
        f = int(input())
        Income[job] = wage*f

profile(Income, Expense, Savings, Debt, Investment)
edit(Income, 'income')

print('Now that we have collected all the information regarding your annual income, let\'s move to the expense category.')
print('For our purposes, expenses refer to any payments that you make for services and goods.')
if tx.startswith('pre'):
    print('Since you are providing pre-tax income, income tax is an expense we have to account for. We will use 30 percent of your annual income, but please keep in mind this value does vary for each individual.')
Expense = annual_expenses()
if tx.startswith('pre'):
    income_sum = total(Income)
    Expense['income tax'] = 0.3 * income_sum

profile(Income, Expense, Savings, Debt, Investment)
clean(Expense)
edit(Expense, 'expense')

income_sum = total(Income)
expense_sum = total(Expense)
print('Let\'s take a moment to review these two sections before moving forward, as these are the inflow and outflow of your finances.')





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
