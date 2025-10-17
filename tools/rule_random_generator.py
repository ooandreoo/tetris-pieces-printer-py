import random

class RuleRandomGenerator:
    def __init__(self, domain: list, maximum_repetitions: int, penalty: int):
        print(domain,maximum_repetitions,penalty)
        if(len(domain) <= ((penalty + maximum_repetitions - 1)//maximum_repetitions)):
            raise ValueError("The following condition needs to be respected: (Length of domain) > (Penalty time + Max. Allowed Repetitions - 1) \\ (Max. Allowed Repetitions)")
        self.domain = domain
        self.maximum_repetitions = maximum_repetitions
        self.penalty = penalty

        self.last_value_index = None
        self.repeated_times = 0
        self.waiting_values = []
        self.waiting_values_comeback = []
        self.turn = 1

    def generate_random_value(self):
        random_value = self.get_value_from_domain()
        self.incorporate_values_with_expired_penalty()
        self.increase_turn()
        return random_value

    def increase_turn(self):
        self.turn+= 1

    def incorporate_values_with_expired_penalty(self):
        if(len(self.waiting_values_comeback) != 0 and self.waiting_values_comeback[0] == self.turn):
            self.domain.append(self.waiting_values.pop(0))
            self.waiting_values_comeback.pop(0)


    def get_value_from_domain(self):
        index = self.get_random_index_from_domain()
        value = self.domain[index]


        if(index == self.last_value_index):
            self.repeated_times+= 1
        else:
            self.last_value_index = index
            self.repeated_times = 1

        if(self.repeated_value_met_penalty_criteria()):
            self.send_repeated_value_to_waiting_list()

        return value

    def send_repeated_value_to_waiting_list(self):
        self.waiting_values.append(self.domain[self.last_value_index])
        self.waiting_values_comeback.append(self.turn+self.penalty)
        self.domain.pop(self.last_value_index)
        self.last_value_index = None

    def repeated_value_met_penalty_criteria(self):
        return self.repeated_times == self.maximum_repetitions

    def get_random_index_from_domain(self):
        return random.randint(0,len(self.domain)-1)
