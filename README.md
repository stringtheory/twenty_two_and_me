# 22andme

I was told, by a wise jazz musician, that in Numerology, I am a 22. 
He had only ever met one other 22  in his entire life! 

So I asked the question:
**What are the chances of being a 22?** 

The internet could not provide the correct answer, so I wrote some code. 

Answer: *A little over 3%*

## Numerology Report Generator

Files:
* life_path_calculator.py - takes a date and returns a life path number
* numerology_report.py - Ascii Art Report
* reference_data.py - data referenced from other files
* twenty_two_stats_report.py - Data tables for the jazz musician.
                                 
Todo:
- [ ] add date validation check
- [ ] add tests

Scope Creep:
- [ ] make it work in the command line or a framework
- [x] fix description text wrapping
- [ ] clean up reference_data.py reporting 
- [ ] more ASCII Art?

Instructions for calculations:
https://www.tokenrock.com/numerology/life_path/

## numerology_report.py Results Example

```
    Example:
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Are You A Master stringtheory?

    Birthday: Aug 11, 1983

    Life Path Number: 22/4
    The Chances of being a 22: 3.4%

         {  ☆*･゜ﾟ･*\( ◕‿◕ )/*･゜ﾟ･*☆
    22/4 is a Master Number!!!!

    ....................................8<...................

    All About Life Path 22/4:

    An individual that has life path number 22/4 is the master teacher. Therefore, 
    they have passion and energy to engage in scholarship and share knowledge with 
    others as deeply and broadly as possible. Their personality develops through their
    efforts to learn and share wisdom.

    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


## twenty_two_stats_report.py Results Example
```

## reference_data.py Results Example

```
LIFE PATH PERCENTAGES
Start Date: 01/01/1981
End Date: 12/31/1981
Total Days: 365
╒═════════════╤══════════╤═══════════╕
│   life path │   day ct │         % │
╞═════════════╪══════════╪═══════════╡
│           1 │       41 │ 11.2329   │
├─────────────┼──────────┼───────────┤
│           2 │       11 │  3.0137   │
├─────────────┼──────────┼───────────┤
│           3 │       40 │ 10.9589   │
├─────────────┼──────────┼───────────┤
│           4 │       34 │  9.31507  │
├─────────────┼──────────┼───────────┤
│           5 │       41 │ 11.2329   │
├─────────────┼──────────┼───────────┤
│           6 │       41 │ 11.2329   │
├─────────────┼──────────┼───────────┤
│           7 │       41 │ 11.2329   │
├─────────────┼──────────┼───────────┤
│           8 │       42 │ 11.5068   │
├─────────────┼──────────┼───────────┤
│           9 │       40 │ 10.9589   │
├─────────────┼──────────┼───────────┤
│          11 │       28 │  7.67123  │
├─────────────┼──────────┼───────────┤
│          22 │        5 │  1.36986  │
├─────────────┼──────────┼───────────┤
│          33 │        1 │  0.273973 │
╘═════════════╧══════════╧═══════════╛



LIFE PATH TWO 22 BIRTHDAYS FOR 01/01/1981 - 12/31/1981
╒════════════╤═══════╤═════════╤════════╤═════════════╕
│ date       │   day │   month │   year │   life path │
╞════════════╪═══════╪═════════╪════════╪═════════════╡
│ 08-11-1983 │     8 │      11 │      3 │          22 │
├────────────┼───────┼─────────┼────────┼─────────────┤
│ 08-29-1983 │     8 │      11 │      3 │          22 │
├────────────┼───────┼─────────┼────────┼─────────────┤
│ 11-08-1983 │    11 │       8 │      3 │          22 │
├────────────┼───────┼─────────┼────────┼─────────────┤
│ 11-17-1983 │    11 │       8 │      3 │          22 │
├────────────┼───────┼─────────┼────────┼─────────────┤
│ 11-26-1983 │    11 │       8 │      3 │          22 │
╘════════════╧═══════╧═════════╧════════╧═════════════╛
```
