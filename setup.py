from setuptools import setup

setup(
    name='AIKIF',
    version='0.1.5',
    author='Duncan Murray',
    author_email='djmurray@acutesoftware.com.au',
    packages=['aikif', 'aikif.agents','aikif.agents.aggregate','aikif.agents.explore','aikif.agents.gather','aikif.agents.learn''aikif.dataTools','aikif.environments','aikif.lib', 'aikif.ontology','aikif.toolbox', 'aikif.web_app'],
    include_package_data = True,
    package_data = {
        'aikif': ['data/*.*'],
    },    
    url='https://github.com/acutesoftware/AIKIF',
    license='GNU General Public License v3 (GPLv3)',
    description='Artificial Intelligence Knowledge Information Framework',
    long_description=open('README.txt').read(),
    install_requires=[
          'nose >= 1.0',
          'flask >= 0.10.1',
          'flask-httpauth >= 2.3.0',
          'flask-restful >= 0.3.1',
          'requests >= 2.3',
          'beautifulsoup4 >= 1.0',
          'Pillow >= 1.0',
          'xlrd >= 0.9.0',
          'pyyaml >= 3.10',
          'psutil > 0.1.0'
    ],
    classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Topic :: Database :: Front-Ends',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Software Development :: Documentation',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: System :: Logging',
    'Topic :: Text Processing',
    ],

)


