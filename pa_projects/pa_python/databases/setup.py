from setuptools import setup


requires=[
        
 	'deform',
	'pyramid',
	'pyramid_chameleon',
	'pyramid_tm',
	'sqlalchemy',
	'waitress',
	'zope.sqlalchemy',
]

dev_requires=[
	'pyramid_debugtoolbar',
	'pytest',
	'webtest',

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
	        'console_scripts': [
                'initialize_paproject_db = paproject.initialize_db:main'
		],


	},


)
