#!/bin/python

import sys

s, t = raw_input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = raw_input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = raw_input().strip().split(' ')
m, n = [int(m), int(n)]
apple = map(int, raw_input().strip().split(' '))
orange = map(int, raw_input().strip().split(' '))

apple_counter = 0
orange_counter = 0
for distance in apple:
    if distance < 0:
        continue
    if t >= distance + a >= s:
        apple_counter += 1

for distance in orange:
    if distance > 0:
        continue
    if t >= distance + b >= s:
        orange_counter += 1

print apple_counter
print orange_counter
