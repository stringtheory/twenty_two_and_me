# -----------------------------------------------------------
# How to calculate a Life Path Number:
#
# https://www.tokenrock.com/numerology/life_path/
# RULE 1
# The correct way to calculate the Life Path Number is to group the Month, Day, and Year,
# and add them individually, reduce to a single number for each, then reduce them to a single number.
#
# Birth Date: May 4, 1977
#
# May = 5
# 4 = 4
# 1977 = (1 + 9 + 7 + 7) = 24 = (2 + 4) = 6
#
# Then add the totals from each above group
# (5 + 4 + 6) = 15 = (1 + 5) = 6
#
# RULE 2
# Next lets look at the second rule. Do not reduce the Numbers 11 or 22 (1 + 1 = 2 or 2 + 2 = 4)
# if they show up in the groups during the calculation, until the final calculation.
#
# Birth Date: July 29, 1974
#
# July = 7
# 29 = (2 + 9) = 11 (Do Not Reduce)
# 1974 = (1 + 9 + 7 + 4) = 21 = (2 + 1) = 3
# (7 + 11 + 3) = 21 = (2 + 1) = 3
#
# RULE 3
# If final calculation is 33 return 33.
# Note No years add to 33 from 1-5000 except for 33.
#
# TODO(dew): Checking with numerologist on if 33 is reduced
# -----------------------------------------------------------

import datetime

LPN_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33]


def split_reduce(n):
    """
    Adds digits in a given number until reduced to 1-9 or 11, 22, 33
    """
    if n in LPN_LIST:
        return n
    else:
        # turn number into strings, makes a list, converts to ints, adds
        nl = map(int, str(n))
        new_n = sum(nl)
        return split_reduce(new_n)


def life_path_calc(lpn_date):
    """
    Calculates a life path number for a given date.

    Parameters:
    lpn_date (datetime.date): The date being checked from years 100 - 5000

    Returns:
    int: The Life Path Number
    """

    date_frags = [lpn_date.day, lpn_date.month, lpn_date.year]
    reduced_frags = []

    for date_frag in date_frags:
        reduced_frags.append(split_reduce(date_frag))

    life_path_number = sum(reduced_frags)

    return split_reduce(life_path_number)


def main():
    ## quick test set  3, 22, 8, 6, 7, 5, 4
    print(life_path_calc(datetime.date(1990, 1, 1)))
    print(life_path_calc(datetime.date(1979, 3, 11)))
    print(life_path_calc(datetime.date(1980, 4, 13)))
    print(life_path_calc(datetime.date(1969, 3, 23)))
    print(life_path_calc(datetime.date(2002, 11, 1)))
    print(life_path_calc(datetime.date(2010, 7, 4)))
    print(life_path_calc(datetime.date(1999, 3, 18)))


if __name__ == "__main__":
    main()
