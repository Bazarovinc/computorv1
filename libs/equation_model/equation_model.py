from pydantic import BaseModel
from pydantic.typing import List, Optional, Tuple


class OtherDegrees(BaseModel):
    coefficient: Optional[float]
    degree: Optional[int]


class EquationModel(BaseModel):
    a: Optional[float] = 0
    b: Optional[float] = 0
    c: Optional[float] = 0
    other_degrees: Optional[List[OtherDegrees]] = None
    degree: Optional[int] = 0
    d: Optional[float]
    sqrt_d: Optional[float]
    x1: Optional[float]
    x2: Optional[float]
    x1_s: Optional[str]
    x2_s: Optional[str]
    steps: Optional[bool] = False
    free_form: Optional[bool] = False

    def set_degree(self):
        if int(self.a) and int(self.b) == 0:
            self.degree = 0
        elif int(self.a) == 0:
            self.degree = 1
        else:
            self.degree = 2
