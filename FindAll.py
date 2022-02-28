import messages as msg
import helpers

# settings = helpers.get_settings()

def execute():
	results = helpers.run_command_output('mdfind kMDItemKind="Alias"')
	print(helpers.decorate('green', results))
	msg.done()
