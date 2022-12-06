from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=23)

A = 1
B = 10
C = 100
D = 1000

answer_a = 17*A+14*B+10*C+15*D
answer_b = 41*A+44*B+40*C+39*D

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b