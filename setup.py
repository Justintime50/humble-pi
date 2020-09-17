import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = [
    'RPi.GPIO >= 0.7.0',
]

setuptools.setup(
    name='humble-pi',
    version='0.1.0',
    description='A collection of Raspberry Pi projects.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/humble-pi',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': [
            'pytest >= 6.0.0',
            'pytest-cov >= 2.10.0',
            'coveralls >= 2.1.2',
            'flake8 >= 3.8.0',
        ]
    },
    python_requires='>=3.6',
)
