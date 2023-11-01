# Pseudo-code

# if >= 1 && <= 7 
#     return 1 fine

# else if >= 8 && <= 14 
#     return 5 fine 

# else 14 days 
#     return 5 plus 1 for each day 


# Implementation - Imperative
days = 1
fineAmountPerDay = 1

if days >= 1 and days <= 7:
    print('£1 fine')
elif days >= 8 and days <= 14:
    print('£5 fine')
elif days >= 15:
    # working out
    daysExceeded = days - 14;
    fineAmount = 5 + (daysExceeded * fineAmountPerDay)
    print(fineAmount) 
    

# Implementation - Procedural

def get_chargable_days(days):
    weeks = (days / 7);
    amount_of_week_end_days = weeks * 2;
    days = days - amount_of_week_end_days;
    return days

def days_are_within_range(days, min, max):
    return (days >= min and days <= max)


def get_loan_fine(days):
    days = get_chargable_days(days);
    
    if days_are_within_range(days, 1, 7):
        print('£1 fine')
    elif days_are_within_range(days, 8, 14):
        print('£5 fine')
    elif days >= 15:
        # working out
        daysExceeded = days - 14;
        fineAmount = 5 + (daysExceeded * 1)
        print(fineAmount) 


