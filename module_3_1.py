calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(s):
    count_calls()
    length = len(s)
    upper_case = s.upper()
    lower_case = s.lower()
    return (length, upper_case, lower_case)

def is_contains(target_string, string_list):
    count_calls()
    target_string_lower = target_string.lower()
    return any(target_string_lower == s.lower() for s in string_list)

print(string_info('Capybara')) 
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban' 'BanAn', 'uRbAn']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print("Total calls:", calls)











