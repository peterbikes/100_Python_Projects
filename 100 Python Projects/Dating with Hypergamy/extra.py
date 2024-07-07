# extra.py

import random

INSTRUCTIONS = """
A number of single men and women are locked together for a longer while in a villa or on an island, for the sake of a TV show. Because they spend quite some time together, all of them seek a partner to date. They are all shallow people, and they only care about looks, aka physical attractiveness when it comes to dating. Looks levels range from 1 to 10.

The unwritten rules for their choice of partner are the following:
  1) Women never date men below their own looks level.
  2) Women are content with one partner, and when they have it, they don't look for a second man (yeah, I know, but let's assume this for this kata).
  3) Because women are hypergamous, they never settle for a man who's not at least 2 levels above their own, unless he's an 8 or above (but even then, the first rule applies).
  4) Men of level 8 or above (aka Chads) try to get 2 women, men below that are content with one.
  5) When women have a choice between two equally glamorous Chads, they prefer the one without a girlfriend.
  6) Both women and men try to get the best looking date(s) they can get.

These rules have nothing to do with reality of course.

You'll be given a list of looks levels representing the men, and another list representing the women. Return a list of the looks levels of the men who stay alone, sorted from hideous to handsome.
"""

# objects
class Woman:
    def __init__(self, looks_level):
        self.name = random.choice(women_names)
        self.looks_level = looks_level
        self.set_emoji()

    def set_emoji(self):
        if self.looks_level <= 3:
            self.emoji = "👹"
        elif self.looks_level > 7:
            self.emoji = "👸"
        else:
            self.emoji = "👩"

    def __lt__(self, other):
        return self.looks_level < other.looks_level

    def __eq__(self, other):
        return self.looks_level == other.looks_level

class Man:
    def __init__(self, looks_level):
        self.name = random.choice(men_names)
        self.is_chad = looks_level > 7
        self.looks_level = looks_level
        self.partners = []
        self.set_emoji()

    def add_partner(self, partner):
        self.partners.append(partner)

    def set_emoji(self):
        if self.looks_level <= 3:
            self.emoji = "🧌"
        elif self.looks_level > 7:
            self.emoji = "🤴"
        else:
            self.emoji = "👨"

# functions
def get_number_list(prompt):
    while True:
        try:
            input_str = input(prompt).strip()
            if ',' in input_str:
                number_list = [int(num) for num in input_str.split(',')]
            else:
                number_list = [int(num) for num in input_str.split()]
            
            # Validate numbers are within range 0 to 10
            if all(0 <= num <= 10 for num in number_list):
                return number_list
            else:
                print("Please enter numbers between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas or spaces.")
            
def instructions():
    while True:
        view_instructions = input("Do you wish to view the instructions, or have you read the README? y/n: ").strip().lower()
        if view_instructions == "y":
            print(INSTRUCTIONS)
            return True
        elif view_instructions == "n":
            print("Let's proceed with the program.")
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def create_objects_from_list(looks_levels, class_type):
    objects = []
    for level in looks_levels:
        objects.append(class_type(level))
    return objects

# names for men and woman

men_names = [
    "James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles",
    "Christopher", "Daniel", "Matthew", "Anthony", "Donald", "Mark", "Paul", "Steven", "Andrew", "Kenneth",
    "Joshua", "Kevin", "Brian", "George", "Edward", "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan",
    "Jacob", "Gary", "Nicholas", "Eric", "Jonathan", "Stephen", "Larry", "Justin", "Scott", "Brandon",
    "Benjamin", "Samuel", "Gregory", "Frank", "Alexander", "Raymond", "Patrick", "Jack", "Dennis", "Jerry",
    "Tyler", "Aaron", "Henry", "Douglas", "Peter", "Jose", "Adam", "Zachary", "Nathan", "Walter",
    "Harold", "Kyle", "Carl", "Arthur", "Gerald", "Roger", "Keith", "Jeremy", "Terry", "Lawrence",
    "Sean", "Christian", "Albert", "Joe", "Ethan", "Austin", "Jesse", "Willie", "Billy", "Bryan",
    "Bruce", "Jordan", "Ralph", "Roy", "Noah", "Dylan", "Eugene", "Wayne", "Alan", "Juan",
    "Louis", "Russell", "Gabriel", "Randy", "Philip", "Harry", "Vincent", "Bobby", "Johnny", "Howard"
]

women_names = [
    "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen",
    "Nancy", "Margaret", "Lisa", "Betty", "Dorothy", "Sandra", "Ashley", "Kimberly", "Donna", "Emily",
    "Michelle", "Carol", "Amanda", "Melissa", "Deborah", "Stephanie", "Rebecca", "Laura", "Sharon", "Cynthia",
    "Kathleen", "Amy", "Shirley", "Angela", "Helen", "Anna", "Brenda", "Pamela", "Nicole", "Ruth",
    "Katherine", "Samantha", "Christine", "Emma", "Catherine", "Virginia", "Debra", "Rachel", "Janet", "Carolyn",
    "Maria", "Heather", "Diane", "Julie", "Joyce", "Victoria", "Kelly", "Christina", "Lauren", "Joan",
    "Evelyn", "Olivia", "Judith", "Megan", "Cheryl", "Martha", "Andrea", "Frances", "Hannah", "Jacqueline",
    "Ann", "Gloria", "Jean", "Alice", "Teresa", "Sara", "Janice", "Doris", "Madison", "Julia",
    "Grace", "Judy", "Abigail", "Marie", "Denise", "Beverly", "Amber", "Theresa", "Marilyn", "Danielle"
]



