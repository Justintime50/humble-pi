# Humble Pi

A collection of Raspberry Pi projects.

[![Build Status](https://travis-ci.com/Justintime50/humble-pi.svg?branch=master)](https://travis-ci.com/Justintime50/humble-pi)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/humble-pi/badge.svg?branch=master)](https://coveralls.io/github/Justintime50/humble-pi?branch=master)
[![PyPi](https://img.shields.io/pypi/v/humble-pi)](https://pypi.org/project/humble-pi)
[![Licence](https://img.shields.io/github/license/justintime50/humble-pi)](LICENSE)

## Install

```bash
# Install tool
# TODO: Not yet available on PyPi

# Install locally
make install

# Get Makefile help
make help
```

## Usage

### Stoplight

Turn on red, yellow, and green LEDs like a stoplight, iterating multiple times. Uses pins `4 = red`, `17 = yellow`, and `27 = green`.

```bash
sudo python stoplight.py
```

**Hardware Example**

<img src="assets/stoplights.jpg" alt="Stoplights">

## Development

```bash
# Lint the project
make lint

# Run tests
make test
```
