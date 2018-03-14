#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# Copyright : see accompanying license files for details

"""
AuToGraFS: Automatic Topological Generator for Framework Structures.
Addicoat, M. a, Coupry, D. E., & Heine, T. (2014).
The Journal of Physical Chemistry. A, 118(40), 9607–14. 
"""

__all__     = ["autografs","framework","utils"]
__author__  = "Damien Coupry"
__credits__ = ["Prof. Matthew Addicoat"]
__license__ = "MIT"
__maintainer__ = "Damien Coupry"
__version__ = 2.0
__status__  = "alpha"

from autografs.autografs import Autografs
from autografs.framework import Framework