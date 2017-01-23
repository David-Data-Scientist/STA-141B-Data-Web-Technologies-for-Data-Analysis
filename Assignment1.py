# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 20:58:33 2017

@author: Owner
"""
from __future__ import division

##########################--- Exercise 1.1----######################
# Write a function that accepts a year as input and computes the anchor day 
# for that year's century. The modulo operator % and functions in the math 
# module may be useful. Document your function with a docstring and 
# test your function for a few different years. Do this in a new cell 
# below this one.
def Anchor_day(year):
    """
    Read the year into the Anchor Day. 
    
    Arguments: 
        year (integer): Any specific year
    
    Returns: 
        The Anchor Day of this century. 
    """
    day = (5 * ((year // 100) % 4) + 2) % 7
    return day
       
[Anchor_day(s) for s in [1783, 1888, 1954, 2016]]    

 
##########################--- Exercise 1.2----######################
# Write a function that accepts a year as input and computes the doomsday 
# for that year. Your function may need to call the function you wrote 
# in exercise 1.1. Make sure to document and test your function.
def Dooms_day(year):
    """
    Read the year into the doomsday for this year.
    
    Arguments: 
        year (integer): Any specific year
    
    Returns: 
        The doomsday for this year. 
    
    """
    day = (year % 100 + (year % 100)//4 + Anchor_day(year)) % 7
    return day
[Dooms_day(s) for s in [1783, 1888, 1900, 1953, 1954, 2016]]    
    

##########################--- Exercise 1.3----######################
# Write a function to determine the day of the week for a given day, month, 
# and year. Be careful of leap years! Your function should return a string 
# such as "Thursday" rather than a number. As usual, document and test 
# your code.
def Day_of_week(day, month, year):
    """   
    Input the specific date and return the day of the week.
    
    Arguments: 
        day, month, year (integer): Any specific date.
    
    Returns: 
        The day of this week. 
    """
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        doomsday = [11, 29, 21, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    else:
        doomsday = [10, 28, 21, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    exact_day = ((day - doomsday[month-1]) + Dooms_day(year)) % 7
    character_day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", 
    "Friday", "Saturday"]
    return character_day[exact_day]

Day_of_week(1, 1, 1887)
Day_of_week(1, 1, 1900)


##########################--- Exercise 1.4----######################
# How many times did Friday the 13th occur in the years 1900-1999? 
# Does this number seem to be similar to other centuries?

# Optimized code
def Count_Friday(century):
    """
    Read century as input and it returns the times Friday 
    occurs on the 13th of the century.
    
    Arguments: 
        day, month, year (integer): Any specific date.
    
    Returns: 
        The number of Fridays on 13th.
    """
    year = century * 100
    Day_on_13 = [Day_of_week(13, s, t) for s in xrange(1, 13) \
    for t in xrange(year, year + 100)]
    return Day_on_13.count("Friday")


### Original code
""" def occur(date):
    '
    It reads a list of days and returns how many Fridays in the list.
    
    Arguments: 
        day, month, year (integer): Any specific date.
    
    Returns: 
        The day of this week.
    '
    occurance = sum([s == "Friday" for s in date])
    return occurance

def Count_Friday(century):
    '
    Read century as input and it returns the times Friday 
    occurs on the 13th of the century.
    
    Arguments: 
        day, month, year (integer): Any specific date.
    
    Returns: 
        The number of Fridays on 13th.        
    '
    year = century * 100
    Day_on_13 = [Day_of_week(13, s, t) for s in xrange(1, 13) \
    for t in xrange(year, year + 100)]
    return occur(Day_on_13)    
"""


##########################--- Exercise 1.5----######################
# How many times did Friday the 13th occur between the year 2000 and today?
def Friday_occur_from_2000(day, month, year):
    """
    Input the current date and it returns the number of Friday 
    occured on the 13th from 2000 to today.
    
    Arguments:
        day, month, year (integer): Any specific date.
        
    Returns: 
        The number of Fridays on 13th from 2000 to today.
    """
    Day_on_13 = [Day_of_week(13, s, t) \
    for s in xrange(1, 13) for t in xrange(2000, year)]
    count_from_2000 = Day_on_13.count("Friday")
    
    if day >= 13:
        count_from_2000 += \
        [Day_of_week(13, s, year) for s in xrange(1, month+1)].count("Friday")
    else:
        count_from_2000 += \
        [Day_of_week(13, s, year) for s in xrange(1, month)].count("Friday")
    return count_from_2000

[Friday_occur_from_2000(21, 1, 2017), 
 Friday_occur_from_2000(4, 7, 2017), Friday_occur_from_2000(17, 10, 2017)]    


def read_birthdays(file_path):
    """
    Read the contents of the birthdays file into a string.
    
    Arguments:
        file_path (string): The path to the birthdays file.
        
    Returns:
        string: The contents of the birthdays file.
    """
    # f = open(file_path, 'r')
    # return f.readlines()[6:]
    with open(file_path) as file:
        return file.read()

    
birthday = read_birthdays("D:\\Davis\\Course selected\\STA141B\\birthdays.txt")


def format_birthday(birth_list):
    """
    Read a text string into a list containing birthday and birth count.
    
    Arguments:
        textstring: raw text string.
    
    Returns:
        a nested list [day, month, year, count]
    """
    # Remove space and tab from the left and right part of the string
    stripped_text = birth_list.strip("\n\t")
    # Split the date and count
    split_text = [s.split("\t") for s in stripped_text.split("\n")[6:]]                  
    split_date = [map(int, s[0].split("/")) for s in split_text]                        
    split_count = map(int, [s[1] for s in split_text])
    # Concatenate the date and count 
    merge = [split_date[i] + [split_count[i]] for i in xrange(365)]
    return merge         

list_of_birth = format_birthday(birthday)    
    
## Former function
def format_birthday2(textstring):
    """
    Read a text string into a list containing birthday and birth count.
    
    Arguments:
        textstring: raw text string.
    
    Returns:
        a nested list [day, month, year, count]
    """
    # Remove space and tab from the left and right part of the string
    stripped_text = textstring.strip("\n\t")
    # Split and get the date
    split_text = stripped_text.split("\n")[6:]
    split_text = [s.split("/") for s in split_text]
    split_text2 = [s[:2] for s in split_text]                          
    split_text3 = [s[2].split("\t") for s in split_text]
    # Merge the date and count
    merge2 = []              
    for i in xrange(365):
        merge2.append(map(int, split_text2[i] + split_text3[i]))
    return merge2
    

from collections import Counter

def count_birth(birth_list):
    """
    Read a list of birth and count the total birth by month and by day.
    
    Arguments:
        birth_list: a nested list [day, month, year, birthcount]
    
    Returns:
        the total birth by month and by day.
    """
    # Create two empty Counter
    cnt = Counter()
    cnt2 = Counter()
    for i in xrange(365):
        birth_list[i].append(Day_of_week(birth_list[i][1], birth_list[i][0], 1978))
        cnt[birth_list[i][0]] = birth_list[i][3] + cnt[birth_list[i][0]]
        cnt2[birth_list[i][4]] = birth_list[i][3] + cnt2[birth_list[i][4]]                                               
    return cnt, cnt2
    
count_birth(list_of_birth)
    
       
                                
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   

