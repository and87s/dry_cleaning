from drycleaning import dryСleaning

class cleanerWidget:
    def __init__(self,cleaner=None):
        self.__cleaner=cleaner
    def getCleaner(self) -> dryСleaning:
        return self.__cleaner