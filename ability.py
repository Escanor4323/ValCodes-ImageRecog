class ability:
    # Atributtes
    # Todo
    def __init__(self
                 , name_abilityStr="Def"
                 , rangeInt=0
                 , damageInt=None
                 , blindingBool=False
                 , repositioningBool=False
                 , repositioningRangeFloat=0.0):
        # declaration
        self.name_ability = name_abilityStr
        self.range = rangeInt
        self.damage = damageInt
        self.blinding = blindingBool
        self.reposition = repositioningBool
        self.repositionRange = repositioningRangeFloat

    def get_abilityName(self):
        return self.name_ability

    def get_rangeImpact(self):
        return self.range

    def get_damage(self):
        return self.damage

    def get_blindingProper(self):
        return self.blinding

    def get_range(self):
        return self.range

    def get_repositionProper(self):
        return self.reposition

    def get_repositionRange(self):
        return self.repositionRange
