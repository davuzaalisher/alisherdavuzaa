class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @cpu.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.cpu + self.memory

    def __str__(self):
        return f'cpu: {self.cpu} memory:'

    def __ge__(self, other):
        return self.__cpu <= other

    def __eq__(self, other):
        return self.__cpu >= other

    def __ne__(self, other):
        return self.__cpu != other


class Phone:
    def __init__(self, sim_card_list: list):
        self.__sim_card_list = sim_card_list

    @property
    def sim_card_list(self):
        return self.__sim_card_list

    @sim_card_list.setter
    def sim_card_list(self, value):
        self.__sim_card_list = value

    def __str__(self):
        return f"sim cards list: {self.sim_card_list}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu,memory)
        Phone.__init__(self, sim_cards_list)
    def use_gps(self, lacation):
        return f"вы сейчас находитесь {lacation}"

    def __str__(self):
        return f'cpu: {self.cpu} memory: {self.memory} sim cards list: {self.__sim_cards_list}'


lenovo = Computer(32, 16)
iphone = Phone(['megacom', 'O!'])
samsung = SmartPhone(600, 16, ["Beeline", "o!", "MegaCom"])
huawei = SmartPhone(456, 20, ["Beeline", "o!", "MegaCom"])

print(samsung.use_gps("цум"))
print(lenovo.make_computations())
print(lenovo)
print(iphone)
print(samsung)
print(huawei)