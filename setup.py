from setuptools import setup, find_packages

from test import PyTest
from version import __version__

setup(
    name='slack_logging',
    version=__version__,
    description='Python2 logger/handler for slack integration',
    author='iotec',
    author_email='dev@dsp.io',
    url='https://github.com/iotgdev/slack_logging/',
    download_url='https://github.com/iotgdev/slack_logging/archive/{}.tar.gz'.format(__version__),
    packages=find_packages(include=['slack_logging', 'slack_logging.*']),
    data_files=[],
    test_suite='test',
    setup_requires=['pytest-runner'],
    tests_require=['mock>=2.0.0', 'pytest'],
    cmdclass={'pytest': PyTest},
    include_package_data=True,
    install_requires=[
        'requests>=2.19.1',
        'ujson>=1.35',
    ]
)
