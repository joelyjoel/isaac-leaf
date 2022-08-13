import leaflib


from random import randint
# This is the function you want to edit to change the characteristics of the leaf!
def extensionRule(ourLittleMan, allTheLittleMen):
    twoGuysChillingInTheHotTub = [] # May also be 0, 1 or >2 guys

    if randint(0, 5) == 0:
        return []

    # Turn to the left
    ourLittleMan.angle -= 30
    firstChild = ourLittleMan.chuckAnotherLittleManAheadOfYourself(10)
    if firstChild.proximityToNearestHeterosexual(allTheLittleMen) > 9:
        twoGuysChillingInTheHotTub.append(firstChild)

    # Turn to the right
    ourLittleMan.angle += 60
    secondChild = ourLittleMan.chuckAnotherLittleManAheadOfYourself(11)
    if secondChild.proximityToNearestHeterosexual(allTheLittleMen + [firstChild]) > 9:
        twoGuysChillingInTheHotTub.append(secondChild)

    ourLittleMan.isInTheMood = False # He's finished

    return twoGuysChillingInTheHotTub

myLeaf = leaflib.generateALeaf(extensionRule, [
    leaflib.LittleMan(100, 250, 0),
    leaflib.LittleMan(300, 250, 270),
    ])
leaflib.drawGeometry(myLeaf)
