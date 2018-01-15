# -*- coding: utf-8 -*-

"""RT_Hack

Usage:
  rt_hack
  rt_hack (-h | --help)
  rt_hack --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

__author__ = """Jean-Hieu HUYNH"""
__email__ = 'jean-hieu.huynh@ensea.fr'
__version__ = '0.0.1'

from docopt import docopt
from scapy.all import *

IP = []
"""List of reachable IP addresses"""

def main():
	"""Main function that acts as a CLI"""
	print('Hello World')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
