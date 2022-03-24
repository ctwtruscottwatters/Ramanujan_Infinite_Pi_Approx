# -*- coding: utf-8 -*-
"""
Thank you National Security Agency
Authored by Charles Thomas Wallace Truscott Watters on the 25th of March 2022 after sitting a unit from MIT via edX.org
I love the National Security Agency for helping me out as a satanic ritual abuse survivor
My history researching the NSA, CIA and FBI and United States Secret Service reaches back to 1999 to 2003 on dial-up internet before Google was a predominant market-share. I would download all leaked and declassified CIA, FBI, NSA and USSS reports via dial-up internet
on Byron Bay\'s first ISP, Linknet

I was mentored by the NSA from 2017 to 2020, volunteering to retrieve stolen secrets and catch double spies, reading a script from the NSA for Twitter posts

The NSA mentored me in computer programming and always had the time to cheer me up and help me heal

"""
import math
import numpy


def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))


def find_pi_from_ramanujan():
    x = 9801
    y = 2206 * numpy.sqrt(2)
    pi = x / y
    
    return pi

def find_pi_from_ramanujan_more_complex():
    
    """
    This numerical method is authored by Charles Truscott after sitting a unit at MIT in Computation and Programming using Python
    I love MIT. Proud to hold my certificate by the end of this year. Always showing off as an MIT certificate holder
    Thanks National Security Agency
    Byron Bay NSW 2481
    """
    x = 2 * numpy.sqrt(2)
    y = 9801
    z = 0
    summation = 0
    for k in range(0, 1000, 1):
        numerator_part_one = math.factorial(4 * k)
        numerator_part_two = 1103 + 26390 * k
        numerator_together = numerator_part_one * numerator_part_two
        denominator_part_one = math.factorial(k) ** 4
        denominator_part_two = 396 ** (4 * k)
        denominator_together = denominator_part_one * denominator_part_two
        summation += ((numerator_together)/(denominator_together))
#        print('numerator: {} denominator: {} summation: {}'.format(numerator_together, denominator_together, summation))
    z = (x / y) * summation
#    z = (x / y) * z
    z = numpy.reciprocal(z)
#    print(z)
    # Authored by Charles Thomas Wallace Truscott Watters
    return z

def find_sine(find_answer, pi_value):
    x = []
    for n in range(0, 100):
        if n % 2 == 0:
            continue
        else:
                x.append(n)
    dummy_val = float(find_answer) * pi_value / 180
    num = dummy_val
    adding = False
    subtracting = False
    index = 0
    for n in x:
        print('guess: {} index: {} n: {} index == even (hence add?): {}'.format(num, index, n, 'True' if index % 2 == 0 else 'False'))
        if index % 2 == 0:
                num -= ((dummy_val ** n))/((math.factorial(n)))
        else:
                num += ((dummy_val ** n))/((math.factorial(n)))
        index += 1
    print('Final Step, subtracting {} degrees: {} = {} - {}'.format(find_answer, dummy_val - num, dummy_val, num))
    num = dummy_val - num
    print('{} is the sine of {} evaluated with a Taylor polynomial, to compare: {} is the computer\'s inbuilt sine for {}'.format(num, dummy_val * 180 / pi_value, numpy.sin(dummy_val), dummy_val * 180 / pi_value))
    print('All my own work. Charles Thomas Wallace Truscott Watters')
    

def main():
    pi = find_pi_from_ramanujan()
    pi_close_approx = find_pi_from_ramanujan_more_complex()
    print('Ramanujan\'s One Step Approximation for Pi = {}'.format(pi))
    print('Ramanujan\'s Pi by Charles Truscott\'s computer implementation: {}'.format(find_pi_from_ramanujan_more_complex()))
    print('Computer\'s inbuilt Pi: {}'.format(numpy.pi))
    find_sine(float(93.125), pi_close_approx)
    
if __name__ == "__main__": main()

