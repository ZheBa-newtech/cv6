def analyze_password(password,min_length=8,require_digit=True,require_upper=True,require_symbol=False,banned_words=None):
    rules1 = 0
    rules2 = 0
    missing_rules = []
    rules2 += 1

    if banned_words is None:
        banned_words = ['heslo', 'password', '1234']
    
    if len(password) >= min_length:
        rules1 += 1
    else:
        missing_rules.append("min_length")

    if require_digit:
        rules2 += 1
        if any(pr.isdigit() for pr in password):
            rules1 += 1
        else:
            missing_rules.append("digit")

    if require_upper:
        rules2 += 1
        if any(pr.isupper() for pr in password):
            rules1 += 1
        else:
            missing_rules.append("upper")

    symbols = "!@#$%^&*()-_=+[]{};:,.?"
    if require_symbol:
        rules2 += 1
        if any(pr in symbols for pr in password):
            rules1 += 1
        else:
            missing_rules.append("symbol")
    rules2 += 1
    if any(word in password.lower() for word in banned_words):
        missing_rules.append("banned_word")
    else:
        rules1 += 1

    score_percent = int((rules1 / rules2) * 100)
    is_strong = len(missing_rules) == 0
    return is_strong, score_percent, missing_rules

result1 = analyze_password("Test1234", 8, True, True, False, None)
print("1:", result1)
print("1 pokus")
result2 = analyze_password("Test1234", 10, require_symbol=True)
print("2:", result2)
print("2 pokus")
result3 = analyze_password("Test1234", require_symbol=False)
print("3:", result3)
print("3 pokus")
result4 = analyze_password("Admin123!",banned_words=["admin", "root", "user"])
print("4:", result4)
print("4 pokus")
