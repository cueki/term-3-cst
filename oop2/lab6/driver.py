"""
Implements the observer pattern and simulates a simple auction.
"""

import random


class Auctioneer:
    """
    The auctioneer acts as the "core". This class is responsible for
    tracking the highest bid and notifying the bidders if it changes.
    """

    def __init__(self):
        self._bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        self._bidders.append(bidder)

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        self._bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def _notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        for bidder in self._bidders:
            if bidder is not self._highest_bidder:
                bidder(self)

    def accept_bid(self, bid, bidder):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """
        if bid > self._highest_bid:
            prev_bidder = self._highest_bidder
            prev_bid = self._highest_bid
            self._highest_bid = bid
            self._highest_bidder = bidder
            if prev_bidder is not None:
                print(
                    f"{bidder} bidded {bid} in response to "
                    f"{prev_bidder}'s bid of {prev_bid}!"
                )
            self._notify_bidders()

    @property
    def highest_bid(self):
        return self._highest_bid

    @property
    def highest_bidder(self):
        return self._highest_bidder


class Bidder:
    def __init__(self, name, budget=100, bid_probability=0.35, bid_increase_perc=1.1):
        self._name = name
        self._bid_probability = bid_probability
        self._budget = budget
        self._bid_increase_perc = bid_increase_perc
        self._highest_bid = 0

    def __call__(self, auctioneer):
        new_bid = auctioneer.highest_bid * self._bid_increase_perc
        if new_bid <= self._budget and random.random() < self._bid_probability:
            self._highest_bid = new_bid
            auctioneer.accept_bid(new_bid, self)

    def __str__(self):
        return self._name


class Auction:
    """
    Simulates an auction. Is responsible for driving the auctioneer and
    the bidders.
    """

    def __init__(self, bidders):
        """
        Initialize an auction. Requires a list of bidders that are
        attending the auction and can bid.
        :param bidders: sequence type of objects of type Bidder
        """
        self._bidders = bidders
        self._auctioneer = Auctioneer()
        for bidder in bidders:
            self._auctioneer.register_bidder(bidder)

    def simulate_auction(self, item, start_price):
        """
        Starts the auction for the given item at the given starting
        price. Drives the auction till completion and prints the results.
        :param item: string, name of item.
        :param start_price: float
        """
        print(f"Auctioning {item} starting at {start_price}")
        self._auctioneer.accept_bid(start_price, Bidder("Starting Bid"))

        print(
            f"\n\nThe winner of the auction is: "
            f"{self._auctioneer.highest_bidder} at "
            f"${self._auctioneer.highest_bid}"
        )

        print(f"\n\nHighest Bids Per Bidder")
        for bidder in self._bidders:
            print(f"Bidder: {bidder}        Highest Bid: {bidder._highest_bid}")


def main():
    bidders = []

    # Hardcoding the bidders.
    bidders.append(Bidder("Jojo", 3000, random.random(), 1.2))
    bidders.append(Bidder("Melissa", 7000, random.random(), 1.5))
    bidders.append(Bidder("Priya", 15000, random.random(), 1.1))
    bidders.append(Bidder("Kewei", 800, random.random(), 1.9))
    bidders.append(Bidder("Scott", 4000, random.random(), 2))

    item = input("Enter the name of the item being auctioned: ")
    start_price = float(input("Enter the starting price: "))

    print("\n\nStarting Auction!!")
    print("------------------")
    my_auction = Auction(bidders)
    my_auction.simulate_auction(item, start_price)


if __name__ == "__main__":
    main()
