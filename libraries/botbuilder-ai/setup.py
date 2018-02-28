from setuptools import setup

NAME = "botbuilder-ai"
VERSION = "4.0.0.a0"
REQUIRES = [
    "botbuilder-schema>=4.0.0.a0",
    "requests>=2.18.4"]

setup(
    name=NAME,
    version=VERSION,
    url='https://www.github.com/Microsoft/botbuilder-python',
    long_description='Cognitive services extensions for Microsoft BotBuilder.',
    license='MIT',
    author='Microsoft',
    author_email='bf-reports@microsoft.com',
    description='',
    packages=["botbuilder.ai"],
    install_requires=REQUIRES,
    classifiers=[
        'Programming Language :: Python',
        'Intended Audience :: Bot Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ]
)
