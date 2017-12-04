from day1.captcha import Captcha
from day2.checksum import Checksum
from day3.memory import Memory
from day4.passphrase import Passphrase

print('***************')
print('**** Day 1 ****')
print('***************')
captcha = Captcha(open('./day1/input.txt').read())
print('- Part One: ' + str(captcha.solve_part_one()))
print('- Part Two: ' + str(captcha.solve_part_two()))

print('***************')
print('**** Day 2 ****')
print('***************')
checksum = Checksum(open('./day2/input.txt').read())
print('- Part One: ' + str(checksum.solve_part_one()))
print('- Part Two: ' + str(checksum.solve_part_two()))

print('***************')
print('**** Day 3 ****')
print('***************')
memory = Memory(open('./day3/input.txt').read())
print('- Part One: ' + str(memory.solve_part_one()))
print('- Part Two: ' + str(memory.solve_part_two()))

print('***************')
print('**** Day 4 ****')
print('***************')
memory = Passphrase(open('./day4/input.txt').read())
print('- Part One: ' + str(memory.solve_part_one()))
print('- Part Two: ' + str(memory.solve_part_two()))
