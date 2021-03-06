from wrapper import Protocol
from Comment import comment

def antIA(ant):
    # ANT PROGRAM
    ant.explore()
    ant.say("coucou")

def nestIA(nest):
    # NEST PROGRAM

    comment(str(nest))

    if nest.memory[0] == 0:
        nest.setMemoryLocation(0, 1)
        nest.commitMemory()
        nest.newAnt(0)

    elif nest.memory[0] == 1:
        nest.setMemoryLocation(0, 2)
        nest.commitMemory()
        nest.antOut(0, 50, 0, 0)


while True:
    nameEntity, entity = Protocol.readInput()
    if nameEntity == 'ANT':
        antIA(entity)
    elif nameEntity == 'NEST':
        nestIA(entity)

    Protocol.exit()
