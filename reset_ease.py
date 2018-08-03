# reset_ease.py

# import the main window object (mw) from aqt
from aqt import mw
# import showInfo
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

# Add a option to reset the ease factor of the selected cards

# String that will be used to get the cards you want to change the ease factor
# The string should be formated just like you would at the browser of cards
# So you should probably test the string in the browser before using the add-on
select_cards = "is:review 'deck:Core 2K'"

# Ease factor that the cards will be changed to.
# Note that the number should be multiplied by 10.
# e.g 250% = 2500
ease_factor = 2250

def changeEase():
    """ Changes the ease factor of cards selected by the query"""
    # Returns the ID's of the selected cards in a list
    cards = mw.col.findCards(select_cards)
    # Counter for the number of cards actually modified
    changed_cards = 0
    for card_id in cards:
        # Retrieves the card object via the ID in cards
        card = mw.col.getCard(card_id)
        # Change the ease factor
        if card.factor < 2250:
            card.factor = ease_factor
            changed_cards += 1
        # Flush the card
        card.flush()
    showInfo(str(changed_cards) + " cards changed!") 

# Action that will be added to the menu
action = QAction("Reset Ease Factor", mw)
# Set it to call changeEase when it's clicked
action.triggered.connect(changeEase)
# Add action to the tools menu
mw.form.menuTools.addAction(action)
