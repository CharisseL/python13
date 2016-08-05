import sys
import pickle

class Mary:

    def __init__(self):
        self.mary_messages = []
        try:
          self.mary_messages = self.deserialize()
        except FileNotFoundError:
          pass

    def serialize(self):
        '''
        write mary's messages into memories.txt

        '''
        with open('memories.txt', 'wb+') as m:
            pickle.dump(self.mary_messages, m)

    def deserialize(self):
        try:
            with open('memories.txt', 'rb') as m:
                all_messages = pickle.load(m)

        except FileNotFoundError:
                all_messages = {"Mary": [], "Margaret": []}
        return all_messages

    def deserialize(self):
        try:
            with open('memories.txt', 'rb') as m:
                all_messages = pickle.load(m)

        except FileNotFoundError:
            all_messages = {"Mary": [], "Margaret": []}
        except EOFError:
            all_messages = {"Mary": [], "Margaret": []}
        return all_messages

    def add_mary_messages(self, message):
        self.mary_messages["Mary"].append(message)
        self.serialize()

    def prompt(self):
        new_message = input("What's your message? > ")

    def print_all_messages(self):
        for messages in self.mary_messages["Mary"]:
            print("Mary: " + self.mary_messages)
        for messages in self.marg_messages["margaret"]:
            print("margaret: " + self.marg_messages)


if __name__ == '__main__':
    mary = Mary()
    message = sys.argv[1] if len(sys.argv) > 1 else None

    if message is not None:
        print("adding new message \n")
        mary.add_mary_messages(message)
    else:
        print("printing all messages \n")
