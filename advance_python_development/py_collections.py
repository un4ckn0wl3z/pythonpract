"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""

from collections import Counter

device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]

temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.0])  # 2


# my_dict = {'hello': 5}
# print(my_dict['hi'])\\

# default dict
from collections import defaultdict

coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

# alma_masters = {}
#
# for coworker, place in coworkers:
#     if coworker not in alma_masters:
#         alma_masters[coworker] = []
#     alma_masters[coworker].append(place)
#
# print(alma_masters)

alma_masters = defaultdict(list)
for coworker, place in coworkers:
    alma_masters[coworker].append(place)

# alma_masters.default_factory = None
# alma_masters.default_factory = int

print(alma_masters)
print(alma_masters['Rolf'])
print(alma_masters['Anne'])


my_company = 'Haxtivitiez'
coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]

coworker_companies = defaultdict(lambda: my_company)
for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies)
print(coworker_companies['Jen'])  # Teclado
print(coworker_companies['Rolf'])  # Apple Inc.


from collections import OrderedDict
o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 12
o['Jen'] = 3

print(o)
o.move_to_end('Rolf')
print(o)
o.move_to_end('Jen', last=False)
print(o)
o.popitem()
print(o)

from collections import namedtuple

# account = ('checking', 1850.90)
#
# print(account[0])  # name
# print(account[1])  # balance

Account = namedtuple('Account', ['name', 'balance'])
account = Account('checking', 1850.90)
print(account)  # Account
print(account.name)  # name
print(account.balance)  # name

name, balance = account

print(name)  # name
print(balance)  # name

accNamedtuple = Account._make(('checking', 1850.90))
print(accNamedtuple)
print(accNamedtuple._asdict())

from collections import deque # Thread safe

friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))
friends.append('Jose')
friends.appendleft('Anthony')

print(friends)

friends.pop()
print(friends)

friends.popleft()
print(friends)



