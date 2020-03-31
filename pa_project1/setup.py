from setuptools import setup

requires = [
    'pyramid',
    'pyramid_chameleon',
    'waitress',
]

dev_requires = [
    'pyramid_debugtoolbar',
    'pytest',
    'webtest',


]


setup(
    name='paproject',
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
    },

    entry_points={
        'paste.app_factory': [
            'main = paproject:main'
        ],
    },
)
