#!/usr/bin/env python

import numpy as np
import random
import itertools


class Deck:
    self.cards = [str(x) for x in range(1, 10)] + ["J", "Q", "K"]
    self.suits = ["c", "d", "h", "s"]

    def reset():
        """
            Resets the deck
        """
        self.deck = ["".join(x) for x in list(itertools.product(cards, suits))]

    def __init__():
        reset()

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

    def serve_hole():
        """
            Serve "hole"(s); two cards at the beginning of the play
        """
        return serve(2)

    def serve_flop():
        """
            Serve "flops"(s); three cards placed face-up at
            the beginning of the game
        """
        return serve(3)

    def serve_turn():
        """
            Serve "turn street" or "fourth street"; the additional single card
            made public after the flop
        """
        return serve(1)

    def serve_river():
        """
            Serve "river" or "fifth street"; the final single card
            made public after the fourth street
        """
        return serve(1)

    def encode_card(_c):
        """
            Returns the encoded version of the card as a numpy ndarray
        """
        assert(len(_c) == 2)
        _temp = np.zeroes((17, 17))
        # Note, ideally a matrix of shape (4, 13) should suffice
        # But zero-padding to 17x17 helps with convolutions and max pooling
        # (According to the paper, and also the referenced work by Clark and Storkey 2014)
        _temp[self.suits.index(_c[1]), self.cards.index(_c_[0])] = 1
        return _temp
