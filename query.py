"""Skills 5: SQLAlchemy & AJAX

This file is used in Part 2 and 3 of Skills 5: SQLAlchemy & AJAX. You need to
complete Part 1 first, otherwise this part of the assessment won't work.

Be sure to read the instructions before you get started.
"""

from model import db, Human, Animal


##############################################################################
# PART 2: QUERIES


def q1():
    """Return the human with the id 2."""

    # select human-object from humans where id = 2 (primary key)

    return Human.query.get(2)


def q2():
    """Return the FIRST animal with the species 'fish'."""

    return Animal.query.filter(Animal.animal_species == 'fish').first()


def q3():
    """Return all animals that were born after 2015.


    Do NOT include animals without birth years.
    """

    return Animal.query.filter(Animal.birth_year > 2015).all()


def q4():
    """Return the humans with first names that start with 'J'."""

    return Human.query.filter(Human.fname.like('J%')).all()


def q5():
    """Return all animals whose birth years are NULL in the database."""

    return Animal.query.filter(Animal.birth_year == None).all()


def q6():
    """Return all animals whose species is 'fish' OR 'rabbit'."""

    return Animal.query.filter(Animal.animal_species.in_(['rabbit', 'fish'])).all()


def q7():
    """Return all humans whose email addresses do NOT contain 'gmail'."""

    return Human.query.filter(db.not_(Human.email.like('%gmail%'))).all()


##############################################################################
# PART 3: NAVIGATING RELATIONSHIPS

# **Use SQLAlchemy relationships for each function**

# 1. Write a function, print_directory, which does not take any arguments
#    and prints out each human (once) with a list of their animals.
#
#    The output should look like this (with tabs to indent each animal name under
#    a human's name)
#
#       Human_first_name Human_last_name
#           Animal name (animal species)
#           Animal name (animal species)
#
#       Human_first_name Human_last_name
#           Animal name (animal species)

def print_directory():
    """Prints out all humans in the humans table, along with their animals 
    and their species"""

    # Replace this with your code
    for human in Human.query.all():
        print(human.fname, human.lname)
        for animal in human.animals:
            print('\t', animal.name, ('(' + animal.animal_species + ')'))


# 2. Write a function, find_humans_by_animal_species, which takes in an animal
#    species and *returns a list* of all of Human objects who have animals of
#    that species.

def find_humans_by_animal_species(species):
    """Replace this with a good docstring."""

    # Replace this with your code


if __name__ == "__main__":
    from server import app
    from model import connect_to_db

    connect_to_db(app)
