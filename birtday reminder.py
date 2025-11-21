import datetime

# Get today's date
current_date = datetime.date.today().strftime('%Y-%m-%d')
current_date_lst = current_date.split('-')

# Predefined birthday log
bday_log = [
   ('Ayushi', ('1999', '10', '19')),
   ('Yash', ('1999', '04', '21')),
]

# Function to get ordinal suffix
def ordinal(n):
    if 10 <= n % 100 <= 20:
        return 'th'
    else:
        return {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')

# Option to add a birthday
add = input('To add birthday type go: ').strip().lower()
if add.startswith('go'):
    new = input('Add birthday (yyyy-mm-dd): ').strip()
    name = input('Whose bday? ').strip()
    try:
        year, month, day = new.split('-')
        bday_log.append((name, (year, month, day)))
    except ValueError:
        print("❌ Invalid date format. Use yyyy-mm-dd.")

# Check birthdays
for birthday in bday_log:
    if current_date_lst[1] == birthday[1][1] and current_date_lst[2] == birthday[1][2]:
        age = int(current_date_lst[0]) - int(birthday[1][0])
        print(f"🎉 It's {birthday[0]}'s {age}{ordinal(age)} Birthday!")
