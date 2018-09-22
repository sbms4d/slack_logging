import os
from setuptools import setup, find_packages


about = {
    'here': os.path.abspath(os.path.dirname(__file__))
}

with open(os.path.join(about['here'], 'version.py')) as f:
    exec (f.read(), about)

try:
    with open(os.path.join(about['here'], 'test', '__init__.py')) as f:
        exec (f.read(), about)
except IOError:
    pass  # we only ship tests with dev versions

with open(os.path.join(about['here'], 'README.md')) as f:
    about['readme'] = f.read()

setup(
    # available in PKG-INFO
    name='slack_logging',
    version=about['__version__'],
    description='Python logger/handler for slack integration',
    url='https://github.com/iotgdev/slack_logging/',
    author='iotec',
    author_email='dev@dsp.io',
    license='MIT',
    download_url='https://github.com/iotgdev/slack_logging/archive/{}.tar.gz'.format(about['__version__']),
    long_description=about['readme'],
    platforms=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],

    # Package Properties
    packages=find_packages(include=['slack_logging', 'slack_logging.*']),
    include_package_data=True,
    test_suite='test',
    setup_requires=['pytest-runner'],
    tests_require=['mock>=2.0.0', 'pytest'],
    cmdclass={'pytest': about.get('PyTest')},
    install_requires=[
        'requests>=2.19.1',
        'ujson>=1.35',
    ]
)
