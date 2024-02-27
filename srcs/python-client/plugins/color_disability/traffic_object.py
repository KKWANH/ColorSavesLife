LIGHT = 1
SIGN = 2
UNKNOWN = 0

class TrafficObject:
    def __init__(self, _roi, _type):
        self.roi = _roi
        self.type = UNKNOWN
        if _type == 1:
            self.type = LIGHT
        elif _type == 2:
            self.type = SIGN
    
    def getRoi(self):
        return self.roi
    def getType(self):
        return self.type