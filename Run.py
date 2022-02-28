import messages as msg
import helpers

# settings = helpers.get_settings()

def execute(ARGS):
	argDict = helpers.arguments(ARGS)
	alias = helpers.kv_set(argDict, 'alias')
	showAlias = helpers.kv_set(argDict, 'where')

	if showAlias:
		if '/' in showAlias:
			base = helpers.run_command_output('basename {}'.format(showAlias), False).replace('\n', '')
			prefixPath = helpers.run_command_output('dirname {}'.format(showAlias), False).replace('\n', '')
			showAlias = '{}/{}'.format(prefixPath, base)
		else:
			base = showAlias
			prefixPath = helpers.run_command_output('pwd', False).replace('\n', '')
			showAlias = '{}/{}'.format(prefixPath, showAlias)
		
		aScript1 = '''tell application "Finder"'''
		aScript2 = '''set theItem to (POSIX file "{ALIAS}") as alias'''.format(ALIAS = showAlias)
		aScript3 = '''if the kind of theItem is "alias" then'''
		aScript4 = '''get the posix path of (original item of theItem as text)'''
		aScript5 = '''end if'''
		aScript6 = '''end tell'''

		result = helpers.run_command_output("""osascript -e '{}' -e '{}' -e '{}' -e '{}' -e '{}' -e '{}'""".format(aScript1, aScript2, aScript3, aScript4, aScript5, aScript6), False)

		msg.where_result(base, result)
	
	elif alias:
		atPath = helpers.kv_set(argDict, 'at')

		if not atPath:
			atPath = helpers.run_command_output('pwd', False).replace('\n', '')
		
		if '/' in alias:
			base = helpers.run_command_output('basename {}'.format(alias)).replace('\n', '')
			prefixPath = helpers.run_command_output('dirname {}'.format(showAlias)).replace('\n', '')
			alias = '{}/{}'.format(prefixPath, base)
		else:
			prefixPath = helpers.run_command_output('pwd').replace('\n', '')
			alias = '{}/{}'.format(prefixPath, alias)

		atPathNormalized = atPath.replace('~/', helpers.path('user')).replace('/Users/', 'Macintosh HD:Users/').replace('/', ':').replace('\n', '')
		aliasNormalized = alias.replace('~/', helpers.path('user')).replace('/Users/', 'Macintosh HD:Users/').replace('/', ':').replace('\n', '')

		# print("\n\nosascript -e 'tell application \"Finder\" to make new alias file at \"{AT_PATH}\" to \"{TO_PATH}\"'\n\n".format(AT_PATH = atPathNormalized, TO_PATH = aliasNormalized))
		helpers.run_command("\n\nosascript -e 'tell application \"Finder\" to make new alias file at \"{AT_PATH}\" to \"{TO_PATH}\"'\n\n".format(AT_PATH = atPathNormalized, TO_PATH = aliasNormalized))

	msg.done()