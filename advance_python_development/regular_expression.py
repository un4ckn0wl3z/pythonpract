import re

email = 'anuwat@gmail.com'
expression = '[a-z\.]+'

matches = re.findall(expression, email)
print(matches)
name = matches[0]
domain = matches[1]
print(name)
print(domain)

email = 'anuwat@gmail.com'
parts = email.split('@')
print(parts)

price = 'Price: $18,649.50'
expression = 'Price: \$([0-9,]*\.[0-9]*)'
matches = re.search(expression, price)

print(matches.group(0))
print(matches.group(1))
price_without_comma = matches.group(1).replace(',', '')
price_number = float(price_without_comma)
print(price_number)
