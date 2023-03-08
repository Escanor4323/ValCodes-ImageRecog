# creating class agent
import ability


class newAgent:
    # Constructor
    def __init__(self, name="def", ability_list=None, ability_image=None):
        if ability_list is None and name == "":
            ability_list = []
        self.name = name
        self.ability_list = ability_list
        self.ability_image = ability_image

    def get_AbilityList(self) -> list:
        return self.ability_list

    def get_AgentName(self) -> str:
        return self.name
