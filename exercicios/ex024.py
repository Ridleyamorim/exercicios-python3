name = input('Em que cidade você nasceu? ').strip().lower()
firstName = name.find(' ')
proc = 'santo' in name[:firstName] 
print(proc)

