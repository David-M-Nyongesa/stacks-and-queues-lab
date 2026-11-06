import random

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def select_and_announce_winner(self):
        if self.is_empty():
            print("No customers in the queue. No winner can be selected.")
            return None

        winner_index = random.randint(0, self.size() - 1)
        winner = self.items[winner_index]

        processed = []
        for _ in range(winner_index + 1):
            processed.append(self.dequeue())

        print(f"Processed entries: {processed}")
        print(f"🎉 The winner is: {winner}!")
        return winner


if __name__ == "__main__":
    raffle = Queue()
    for i in range(1, 21):
        raffle.enqueue(f"Customer #{i}")

    print(f"Front of the queue: {raffle.peek()}")
    raffle.select_and_announce_winner()
    print(f"Still in the queue: {raffle.items}")
