#import modules for all sub-.py files
import numpy as np
import matplotlib.pyplot as plt
from enum import Enum
import random as random
import pygad
import torch
import torch.nn as nn
import torch.optim as optim

#Import all files in each sub-folder of the pocksward module
from .fairground import *
from .planet import *
from .solarSystem import *
from .nn import *
