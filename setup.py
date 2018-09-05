from setuptools import setup, find_packages

setup(
    name='slack_logging',
    version='1.0.1',
    description='Python2 logger/handler for slack integration',
    author='iotec',
    author_email='dev@dsp.io',
    url='https://github.com/iotgdev/slack_logging/',
    download_url='https://github.com/iotgdev/slack_logging/archive/1.0.1.tar.gz',
    packages=find_packages(include=['slack_logging', 'slack_logging.*']),
    data_files=[],
    include_package_data=True,
    install_requires=[
        'requests==2.19.1',
        'ujson==1.35',
    ]
)
