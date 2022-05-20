#!/usr/bin/env python3


classinfo = {'all': [
         {'name': 'Cat',
          'skill level': 'amazing',
          'spirit animal': 'Chinchilla',
          'super power': 'Body Part Substitution'},
         {'name': 'Chris',
          'skill level': 'astonishing',
          'spirit animal': 'Chipmunk',
          'super power': 'Camouflage'},
         {'name': 'Dao',
          'skill level': 'astounding',
          'spirit animal': 'Clam',
          'super power': 'Bone Manipulation'},
         {'name': 'David',
          'skill level': 'awe-inspiring',
          'spirit animal': 'Clownfish',
          'super power': 'Claw Retraction'},
         {'name': 'Henwin',
          'skill level': 'breathtaking',
          'spirit animal': 'Cobra',
          'super power': 'Deflection'},
         {'name': 'Herman',
          'skill level': 'imposing',
          'spirit animal': 'Condor',
          'super power': 'Fang Retraction'},
         {'name': 'Jose',
          'skill level': 'inspiring',
          'spirit animal': 'Constrictor',
          'super power': 'Helicopter Propulsion'},
         {'name': 'Justin',
          'skill level': 'magnificent',
          'spirit animal': 'Coral',
          'super power': 'Invisibility'},
         {'name': 'Kris',
          'skill level': 'majestic',
          'spirit animal': 'Cougar',
          'super power': 'Immobility'},
         {'name': 'Mannie',
          'skill level': 'miraculous',
          'spirit animal': 'Coyote',
          'super power': 'Immutability'},
         {'name': 'Marcos',
          'skill level': 'spectacular',
          'spirit animal': 'Crab',
          'super power': 'Invulnerability'},
         {'name': 'Marshall',
          'skill level': 'staggering',
          'spirit animal': 'Crane',
          'super power': 'Jet Propulsion'},
         {'name': 'Michael',
          'skill level': 'stunning',
          'spirit animal': 'Crawdad',
          'super power': 'Invulnerability'},
         {'name': 'Mike',
          'skill level': 'stupefying',
          'spirit animal': 'Crocodile',
          'super power': 'Muscle Manipulation'},
         {'name': 'Nikko',
          'skill level': 'sublime',
          'spirit animal': 'Crow',
          'super power': 'Needle Projection'},
         {'name': 'Phil',
          'skill level': 'wonderful',
          'spirit animal': 'Cuckoo',
          'super power': 'Prehensile Tongue'},
         {'name': 'Ryan',
          'skill level': 'wondrous',
          'spirit animal': 'Cicada',
          'super power': 'Regenerative Healing Factor'},
         {'name': 'Sachin',
          'skill level': 'affecting',
          'spirit animal': 'Damselfly',
          'super power': 'Replication'},
         {'name': 'Samekh',
          'skill level': 'arresting',
          'spirit animal': 'Deer',
          'super power': 'Self-Detonation'},
         {'name': 'Will',
          'skill level': 'august',
          'spirit animal': 'Dingo',
          'super power': 'Super Strength'}]}



name= classinfo['all'][13]['name']
skill= classinfo['all'][13]['skill level']
superPower=classinfo['all'][13]['super power']
spiritAnimal=classinfo['all'][13]['spirit animal']
print(f"My name is {name} and my spirit animal is {spiritAnimal}.")
print(f"My name is {name} and my skills are {skill}.")
print(f"My name is {name}  and my super power is {superPower}.")

temp=classinfo['all']

for x in range(temp.__len__()): 
    name= temp[x]['name']
    skill= temp[x]['skill level']
    superPower=temp[x]['super power']
    spiritAnimal=temp[x]['spirit animal']
    print(f"My name is {name} and my spirit animal is {spiritAnimal}.")
    print(f"My name is {name} and my skills are {skill}.")
    print(f"My name is {name} and my super power is {superPower}.")

print('*******************************')

for y in temp:
    print(f"My name is {y['name']} and my spirit animal is {y['spirit animal']}.")
    print(f"My name is {y['name']} and my skills are {y['skill level']}.")
    print(f"My name is {y['name']} and my super power is {y['super power']}.")