from setuptools import setup, find_packages

VERSION = '1.1.0'

setup(
    name='slack_logging',
    version=VERSION,
    description='Python2 logger/handler for slack integration',
    author='iotec',
    author_email='dev@dsp.io',
    url='https://github.com/iotgdev/slack_logging/',
    download_url='https://github.com/iotgdev/slack_logging/archive/{}.tar.gz'.format(VERSION),
    packages=find_packages(include=['slack_logging', 'slack_logging.*']),
    data_files=[],
    include_package_data=True,
    install_requires=[
        'requests>=2.19.1',
        'ujson>=1.35',
    ]
)
