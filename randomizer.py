#!/usr/bin/env python3

# TODO: implement individual star restrictions, ie. needing vanish cap
# for some big boo's haunt stars, etc.

import random

STARS = [
  'BOB1', 'BOB2', 'BOB3', 'BOB4', 'BOB5', 'BOB6', 'BOB7',
  'WF1', 'WF2', 'WF3', 'WF4', 'WF5', 'WF6', 'WF7',
  'JRB1', 'JRB2', 'JRB3', 'JRB4', 'JRB5', 'JRB6', 'JRB7',
  'CCM1', 'CCM2', 'CCM3', 'CCM4', 'CCM5', 'CCM6', 'CCM7',
  'BBH1', 'BBH2', 'BBH3', 'BBH4', 'BBH5', 'BBH6', 'BBH7',
  'HMC1', 'HMC2', 'HMC3', 'HMC4', 'HMC5', 'HMC6', 'HMC7',
  'LLL1', 'LLL2', 'LLL3', 'LLL4', 'LLL5', 'LLL6', 'LLL7',
  'SSL1', 'SSL2', 'SSL3', 'SSL4', 'SSL5', 'SSL6', 'SSL7',
  'DDD1', 'DDD2', 'DDD3', 'DDD4', 'DDD5', 'DDD6', 'DDD7',
  'SL1', 'SL2', 'SL3', 'SL4', 'SL5', 'SL6', 'SL7',
  'WDW1', 'WDW2', 'WDW3', 'WDW4', 'WDW5', 'WDW6', 'WDW7',
  'TTM1', 'TTM2', 'TTM3', 'TTM4', 'TTM5', 'TTM6', 'TTM7',
  'THI1', 'THI2', 'THI3', 'THI4', 'THI5', 'THI6', 'THI7',
  'TTC1', 'TTC2', 'TTC3', 'TTC4', 'TTC5', 'TTC6', 'TTC7',
  'RR1', 'RR2', 'RR3', 'RR4', 'RR5', 'RR6', 'RR7',

  # Secret stars
  'slide1', 'slide2', 'aquarium', 
  'wing mario over the rainbow',
  'Wing Cap', 'Vanish Cap', 'Metal Cap',
  'toad basement', 'toad floor 2', 'toad floor 3',
  'rabbit1', 'rabbit2',
  # Added for completeness, the first version of the rando just puts these at
  # fixed points
  # 'BitDW', 'BitFS', 'BitS']
]

# Map from stars to star requirements.
# Intended to be used with string.startswith()
# TODO: actually do this
STAR_REQUIREMENTS = [

]

# Bowser levels are done as early as possible as a lazy alternative to
# implementing star weightings.
# Also make BOB6 the first star.
def fixed_stars(i):
  if i == 0:
    return 'BOB6'
  if i == 8:
    return 'BitDW'
  elif i == 30:
    return 'DDD1'
  elif i == 31:
    return 'BitFS'
  else:
    return None

def meets_star_requirement(candidate, i):
  # TODO: replace this with a map of level to star requirements.
  # Remove the last character ([1-7]) and do exact string matching.
  if candidate.startswith('WF') and i < 1:
    return False
  if candidate.startswith('JRB') and i < 3:
    return False
  if candidate.startswith('CCM') and i < 3:
    return False
  if candidate.startswith('BBH') and i < 12:
    return False
  if candidate.startswith('HMC') and i < 8:
    return False
  if candidate.startswith('LLL') and i < 8:
    return False
  if candidate.startswith('SSL') and i < 8:
    return False
  if candidate.startswith('DDD') and i < 30:
    return False
  if candidate.startswith('SL') and i < 31:
    return False
  if candidate.startswith('WDW') and i < 31:
    return False
  if candidate.startswith('TTM') and i < 31:
    return False
  if candidate.startswith('THI') and i < 31:
    return False
  if candidate.startswith('TTC') and i < 50:
    return False
  if candidate.startswith('RR') and i < 50:
    return False

  # Secret stars
  if candidate.startswith('slide') and i < 1:
    return False
  if candidate.startswith('aquarium') and i < 3:
    return False
  if candidate.startswith('wing mario') and i < 50:
    return False
  if candidate.startswith('Wing Cap') and i < 10:
    return False
  if candidate.startswith('Vanish Cap') and i < 8:
    return False
  if candidate.startswith('Metal Cap') and i < 8:
    return False
  if candidate.startswith('rabbit1') and i < 15:
    return False
  if candidate.startswith('rabbit2') and i < 50:
    return False
  if candidate.startswith('toad basement') and i < 8:
    return False
  if candidate.startswith('toad floor 2') and i < 31:
    return False
  if candidate.startswith('toad floor 3') and i < 50:
    return False

  return True
  

def main():
  output = []
  # Number of stars you have
  i = 0
  while i < 70:
    candidate = random.choice(STARS)

    # Level star restrictions (ie. WF requires 1 star).
    if not meets_star_requirement(candidate, i):
      continue

    fixed_star = fixed_stars(i)
    if fixed_star:
      candidate = fixed_star

    # No duplicate stars
    if candidate in output:
      continue

    output.append(candidate)
    i = i + 1

  print 'The logic is not complete so some stars may be unobtainable '
  print '(ie. it doesn\'t check that vanish cap is obtained before some bbh '
  print 'stars.  In the event that a star is unobtainable, any star may be '
  print 'taken from that level.  If no stars from that level are obtainable, '
  print 'any star in the game may be taken.\n\n'

  print '\n'.join(output)

if __name__ == '__main__':
  main()
