import pytest
from classes import *


def test_power(test):
   assert test.power(False) == False
   assert test.power(True) == True

def test_channel(test):
   assert test.channel_up() == 0
   assert test.channel_up() == 1
   assert test.channel_up() == 2
   assert test.channel_up() == 3

   assert test.channel_down() == 3
   assert test.channel_down() == 2
   assert test.channel_down() == 1
   assert test.channel_down() == 0

def test_volume(test):
   assert test.volume_up() == 0
   assert test.volume_up() == 1
   assert test.volume_up() == 2

   assert test.volume_down() == 2
   assert test.volume_down() == 1
   assert test.volume_down() == 0