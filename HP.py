#Let's learn how to concatened strings with madlib

Name = input("Name: ")
Object = input("Obejct: ")
weapon = input("Weapon: ")
onomatopeia = input("onomatopeia: ")

madlib = f"BOOM. They knocked again. {Name} awake.\
Where’s the {Object}?” he said stupidly.\
There was a crash behind them and Uncle Vernon\
came skidding into the room. He was holding a {weapon} in\
his hands — now they knew what had been in the\
long, thin package he had brought with them.\
“Who’s there?” he shouted. “I warn you — I’m armed!”\
There was a pause. Then —\
{onomatopeia}!\
The door was hit with such force that it swung clean\
off its hinges and with a deafening crash landed flat\
on the floor."

print(madlib)