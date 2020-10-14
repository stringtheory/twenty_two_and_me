import datetime

from twenty_two_and_me.life_path_calculator import life_path_calc as lpc
from twenty_two_and_me.reference_data import life_path_data


class MasterReport:
    """
    Calculates a life path number for a given date.

    Example:
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Are You A Master stringtheory?

    Birthday: Mar 11, 1979

    Life Path Number: 22/4
    The Chances of being a 22: 3.4%

         {  ☆*･゜ﾟ･*\( ◕‿◕ )/*･゜ﾟ･*☆
    22/4 is a Master Number!!!!

    ....................................8<...................

    All About Life Path 22/4:

    An individual that has life path number 22/4 is the master teacher. Therefore, t
    hey have passion and energy to engage in scholarship and share knowledge with ot
    hers as deeply and broadly as possible. Their personality develops through their
     efforts to learn and share wisdom.

    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    ASCII One Liners from:
    https://gist.github.com/stringtheory/5981819

    Parameters:
    lpn_date (datetime.date): The date being checked from years 100 - 5000
    name (str): Name used in report

    Returns:
    str: ASCII Magic

    Todo:
        * Abstract stats into base class and make seperate report class
    """

    def __init__(self, name, lpc_date):
        self.title = "Are You A Master {}?".format(name)
        self.name = name
        self.lpn_date = lpc_date

    def insert_newlines(self, string, every=80):
        """Return string with newline inserted every x letters
        TODO: split at words
        """
        lines = []
        for i in range(0, len(string), every):
            lines.append(string[i:i + every])
        return '\n'.join(lines)

    def get_life_path_data(self):
        """Print out funny copy"""
        life_path_number = lpc(self.lpn_date)
        data = next(item for item in life_path_data if item["number"] == life_path_number)
        birthday = self.lpn_date.strftime('%b %d, %Y')
        percent_string = str(round(data['percent'], 1))
        copy = self.insert_newlines(data['copy'])

        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(self.title)
        print("\nBirthday: {}".format(birthday))
        print("\nLife Path Number: {}".format(data['display_name']))
        print("The Chances of being a {}: {}%".format(life_path_number, percent_string))

        if data['master']:
            print("\n     {  ☆*･゜ﾟ･*\( ◕‿◕ )/*･゜ﾟ･*☆  ")
            print("{num} is a Master Number!!!!\n".format(num=data['display_name']))
        else:
            print("\n     (╯°□°）╯︵ ┻━┻")
            print("{} is not a Master Number but you are still special. \n".format(data['display_name']))

        print("....................................8<...................")
        print("\nAll About Life Path {}: \n".format(data['display_name']))
        print(copy)
        print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")

jane = MasterReport("Jane", datetime.date(1990, 1, 1))
jane.get_life_path_data()

stringtheory = MasterReport("stringtheory", datetime.date(1983, 11, 26))
stringtheory.get_life_path_data()

sara = MasterReport("Sara", datetime.date(1985, 3, 23))
sara.get_life_path_data()