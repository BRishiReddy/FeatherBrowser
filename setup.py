from setuptools import setup

App=['browser.py']
OPTIONS = {
	'argv_emulation':True,
}
setup(
	app = App,
	options = {'py2app':OPTIONS},
	setup_requires=['py2app']

	)