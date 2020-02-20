from setuptools import setup


requires=[

	'pyramid',
	'waitress'
]

dev_requires=[
	'pyramid_debugtoolbar',

]

setup(
	name='paproject',
	install_requires=requires,
	extras_require={
		'dev':dev_requires,
	},
	entry_points={
		'paste.app_factory':[
			'main=paproject:main'

		],


	},


)
