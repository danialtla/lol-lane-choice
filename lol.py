import random
roles = ['jg', 'mid', 'top', 'sup', 'adc']


confirmation = input("are u sure u wanna play this fking game ??(yes/y or no/n): ").strip().lower()

if confirmation in ['yes', 'y']:

     names = []

     for i in range(5):
       name = input(f"{i+1}: ")
       names.append(name)
       assignments = {}

     for name in names:
              role = random.choice(roles)
              assignments[name] = role
              roles.remove(role)

     for name, role in assignments.items():
              print(f"no life {name} go {role}  ")

elif confirmation in ['no', 'n']:
             print("welldone delete it")


else: print("you just can write y or yes or n or no")
