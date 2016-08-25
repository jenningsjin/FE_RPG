
### Introduction
The Intent of this project is to be able to run a script to generate printable
character sheets for a table top RPG based on the systems of Fire Emblem: Path of Radiance( sans the skill system and laguz units, though these elements may be added in later ), in addition to being able to simulate the battle system of the game, and keep track of the stats of individual units. There will be a number of overall system changes within the game proper, but in terms of base functionalities, it will emulate Fire Emblem.

The general backbone will be written in python, with GUI elements either done via a webapp or with PyQT (TBD later).
### Design Structure
*note: I'm going to use "python class" and "character class" to differentiate between the... python classes and the... ingame character classes* 

There are a number python classes. For ease of organization, and because many of them have large arrays of data associated with them as well.
##### weapons
The python class that contains all the stats for the weapons.  
##### characterGrowths
The python class that holds the chance that a unit will increase in their various stats upon level up. Unlike the Other classes, there is not a large associated dataset. While there are example growths that will be provided, the intent is to let players set their own growths within a limit of around ~350. 
##### characterCaps
The maximum values in each stat a character class can have.

##### characterClasses
This is the python class that keeps track of a given unit's numerical base stats at a given time. It contains the characterCaps and characterGrowths.

##### character
This is the python class that is the playable unit. It has all the meta-data, and keeps track of the commonly changing attributes and derived stats: attack speed, avoid, hit, and weapon inventory.

### Data and Processing
The stats, classes, and all game data is taken from Fire Emblem: Path of Radiance (FE9). The raw data itself was extracted from [Serenes Forest](http://www.serenesforest.net), and then processed into variables via script.

### Questions, Answers and Notes
##### Why Enforced Based Stats?
In classic DnD, one of the interesting choices a player makes is their stat distribution. It makes a fairly large impact on the opening stages of the game, and DnD has a lot of additionally complexity and mechanics within the battle system (e.g. 3.5e has a pretty in-depth skill system). However, in Fire Emblem, there isn't that deep complex battle system.Stats and weapons are obviously way more important, so to balance the game, there's base stats associated with each class.

##### Why 350% total growths?
In Normal Fire Emblem, you can go into a chapter with anywhere from eleven to sixteen units, and if a unit ends up being bad, you swap it out. However in a tabletop RPG... you only ever have your core party, so we want to make sure that every character stands a reasonable chance of being playable. It would probably be better to design a level-up progression, but that's not a major concern.