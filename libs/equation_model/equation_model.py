from pydantic import BaseModel
from pydantic.typing import List, Optional, Tuple


class OtherDegrees(BaseModel):
    coefficient: Optional[float]
    degree: Optional[int]


class EquationModel(BaseModel):
    a: Optional[float] = 0
    b: Optional[float] = 0
    c: Optional[float] = 0
    other_degrees: Optional[List[OtherDegrees]]
    degree: Optional[int] = 2
    d: Optional[float]
    sqrt_d: Optional[float]
    x1: Optional[float]
    x2: Optional[float]
    x1_s: Optional[str]
    x2_s: Optional[str]
    steps: Optional[bool] = False

    def make_degree(self):
        if self.other_degrees is None:
            if int(self.a) and int(self.b) == 0:
                self.degree = 0
            elif int(self.a) == 0:
                self.degree = 1
        else:
            for part in self.other_degrees:
                if int(part.coefficient) != 0:
                    self.degree = part.degree
                    break


