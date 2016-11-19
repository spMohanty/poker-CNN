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

    def encode_card(_c):
        """
            Returns the encoded version of the card as a numpy ndarray
        """
        assert(len(_c) == 2)
        _temp = np.zeroes((17, 17))
        # Note, ideally a matrix of shape (4, 13) should suffice
        # But zero-padding to 17x17 helps with convolutions and max pooling
        # (According to the paper, and also the referenced work by Clark and Storkey 2014)
        _temp[self.suits.index(_c[1]), self.cards.index(_c[0])] = 1
        return np.array(_temp)

    def encode_cards(_c):
        """
            Returns the encoded version of a list of cards as a numpy ndarray
        """
        assert(len(_c) > 0 and len(_c[0]) == 2)

        _temp = [0]*len(_c)
        for _idx, c in enumerate(_c):
            _temp[_idx] = encode_card(_c[_idx])
        return np.array(_temp)

    def shuffle():
        """
            Shuffles the deck
        """
        random.shuffle(self.deck)

    def serve(number_of_cards, encoded=False):
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
            if encoded:
                return encode_cards(_serve)
            else:
                return _serve

    def serve_hole(encoded):
        """
            Serve "hole"(s); two cards at the beginning of the play
            Args:
                encoded : Boolean value deciding if the encoded version of
                the card(s) should be returned
        """
        return serve(2, encoded)

    def serve_flop(encoded):
        """
            Serve "flops"(s); three cards placed face-up at
            the beginning of the game
            Args:
                encoded : Boolean value deciding if the encoded version of
                the card(s) should be returned
        """
        return serve(3, encoded)

    def serve_turn(encoded):
        """
            Serve "turn street" or "fourth street"; the additional single card
            made public after the flop
            Args:
                encoded : Boolean value deciding if the encoded version of
                the card(s) should be returned
        """
        return serve(1, encoded)

    def serve_river(encoded):
        """
            Serve "river" or "fifth street"; the final single card
            made public after the fourth street
            Args:
                encoded : Boolean value deciding if the encoded version of
                the card(s) should be returned
        """
        return serve(1, encoded)
