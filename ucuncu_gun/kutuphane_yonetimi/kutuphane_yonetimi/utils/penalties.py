class PenaltyStrategy:
    def calculate(self, days_late: int) -> float:
        ...

class NoPenalty(PenaltyStrategy):
    def calculate(self, days_late: int) -> float:
        return days_late * 0.0

class StandartPenalty(PenaltyStrategy):
    def calculate(self, days_late: int) -> float:
        return days_late * 5.0

class StrictPenalty(PenaltyStrategy):
    def calculate(self, days_late: int) -> float:
        return days_late * 10.0
    
