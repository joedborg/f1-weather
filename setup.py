from setuptools import setup

setup(
    name="f1-weather",
    version="1.0.0",
    author="Joe Borg",
    description="A weather app for Formula 1 enthusiasts",
    packages=[
        "f1_weather",
    ],
    install_requires=[
        "requests",
        "beautifulsoup4",
    ],
    entry_points={
        "console_scripts": [
            "f1-weather = f1_weather.main:cli",
        ],
    },
)
