class Spell:
    def __init__(self, incantation, name):
        self.incantation = incantation
        self.name = name
        
    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.get_description()
    
    def get_description(self):
        return 'No description'
    
    def execute(self):
        print(self.incantation)

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
        
    def get_description(self):
        return 'This charm summons an object to the caster, potentially over a significant distance'

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')
        
    def get_description(self):
        return 'Causes the victim to become confused and befuddled.'
    
def study_spell(spell):
        print(spell)

spell = Accio()
spell.execute() # Accio
study_spell(spell)
study_spell(Confundo())

'''
1)  What are the parent and child classes here?
Parent - Spell
Child - Accio, Confundo

2) What are the base and sub-classes?
Base - Spell
Sub-Classes - Accio, Confundo

3)
Accio
Summoning Charm Accio
No description
Confundus Charm Confundo
Causes the victim to become confused and befuddled.

4) The get_description method of the Confundo class gets called because the Confundo class has provided the definiton of its own
   get_description() method by overriding the parent class method.
   
5) class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
        
    def get_description(self):
        return 'This charm summons an object to the caster, potentially over a significant distance'
        
   Please see uncommented code top

'''