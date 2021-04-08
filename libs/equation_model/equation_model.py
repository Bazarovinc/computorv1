from pydantic import BaseModel
from pydantic.typing import Optional


class EquationModel(BaseModel):
    a: Optional[float] = 0
    b: Optional[float] = 0
    c: Optional[float] = 0
    degree: Optional[int] = 2
    d: Optional[float]
    sqrt_d: Optional[float]
    x1: Optional[float]
    x2: Optional[float]
    x1_s: Optional[str]
    x2_s: Optional[str]
    steps: Optional[bool] = False

    def make_degree(self):
        if self.a == 0:
            self.degree = 1
