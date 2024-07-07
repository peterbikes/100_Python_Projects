#! /usr/bin/python3

import extra
import os

os.system('clear')

print("\033[1m-- DATING WITH HYPERGAMY --\033[0m")

extra.instructions()

women = extra.get_number_list("Enter the looks levels for women (0-10): ")
men = extra.get_number_list("Enter the looks levels for men (0-10): ")

women_objects = extra.create_objects_from_list(women, extra.Woman)
men_objects = extra.create_objects_from_list(men, extra.Man)

print("\n\033[1m-- CONTENDERS --\033[0m")

print("Women:")
for woman in women_objects:
    print(f"{woman.emoji} {woman.name}, level: {woman.looks_level}")

print("\nMen:")
for man in men_objects:
    print(f"{man.emoji} {man.name}, level: {man.looks_level}")

print()

def match_maker(queen, men):
    for guy in men:
        if guy.is_chad and guy.looks_level >= queen.looks_level and len(guy.partners) < 2:
            if not guy.partners:
                guy.partners.append(queen)
                return men;
            else:
                for check_single in men:
                    if check_single.looks_level < queen.looks_level:
                        continue
                    if check_single.is_chad and check_single.looks_level >= queen.looks_level and not check_single.partners:
                        check_single.partners.append(queen)
                        return men
            guy.partners.append(queen)
            return men
        elif guy.looks_level >= queen.looks_level + 2 and not guy.partners:
            guy.partners.append(queen)
            return men
    return men 

# Find the woman with the highest looks_level
while women_objects:
    queen = max(women_objects, key=lambda x: x.looks_level)
    women_objects.remove(queen)
    match_maker(queen, men_objects)
    
def print_man_partners(men_objects):
    for man in men_objects:
        if not man.partners:
            continue
        print(f"{man.emoji} {man.name} ({man.looks_level}), is paired with ", end="")
        for i, partner in enumerate(man.partners):
            if i == len(man.partners) - 1:
                print(f"{partner.emoji} {partner.name} ({partner.looks_level})")
            else:
                print(f"{partner.emoji} {partner.name} ({partner.looks_level}) and ", end="")

print("\n\033[1m-- RESULTS --\033[0m")
print_man_partners(men_objects)
print("\nAs this is a crappy tv show, all the others were left unpaired and are not even worth mentioning.")
