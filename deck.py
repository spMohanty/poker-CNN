#!/usr/bin/env python

import random
import itertools


class Deck:
    self.cards = [str(x) for x in range(1, 10)] + ["J", "Q", "K"]
    self.suits = ["c", "d", "h", "s"]
    def __init__():
        self.deck = ["".join(x) for x in list(itertools.product(cards, suits))]


    @property
    def size():
        return len(self.deck)

    def shuffle():
        """
            Shuffles the deck
        """
        random.shuffle(self.deck)

    def serve(number_of_cards):
        """
            Serves a certain number of cards from the top of the deck

            Args:
                number_of_cards (list): Number of cards to serve

            Returns:
                List of cards
                or
                False if not enough cards are available in deck
        """
        if number_of_cards < self.size:
            return False
        else:
            _serve = self.deck[:number_of_cards]
            self.deck = self.deck[number_of_cards:]
            return _serve
