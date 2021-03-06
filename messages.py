import helpers, json

actionList = json.loads(helpers.read_file('{}/{}'.format(helpers.path('util'), 'action-list.json')))

def statusMessage():
	if len(actionList['actions']) > 0:
		print("")
		for item in actionList['actions']:
			print('''[ {} {} ]\t\t{}'''.format(actionList['alias'], item['name'], item['description']))
		print("")
	else:
		print('''
AliasPal2 is working successfully!
''')

def done():
	print('''
[ Process Completed ]
''')

def example():
	print('''
process working!
''')

def where_result(ALIAS, STR):
	print('''

ALIAS:       {}

POINTS TO:   {}'''.format(helpers.decorate('cyan', ALIAS), helpers.decorate('green', STR)))