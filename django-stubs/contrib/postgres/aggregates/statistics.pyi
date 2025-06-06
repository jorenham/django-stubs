from typing import Any, ClassVar

from django.db.models import Aggregate, FloatField, IntegerField

class StatAggregate(Aggregate):
    output_field: ClassVar[FloatField]
    def __init__(
        self, y: Any, x: Any, output_field: Any | None = ..., filter: Any | None = ..., default: Any | None = ...
    ) -> None: ...

class Corr(StatAggregate): ...

class CovarPop(StatAggregate):
    def __init__(
        self, y: Any, x: Any, sample: bool = ..., filter: Any | None = ..., default: Any | None = ...
    ) -> None: ...

class RegrAvgX(StatAggregate): ...
class RegrAvgY(StatAggregate): ...

class RegrCount(StatAggregate):
    output_field: ClassVar[IntegerField]  # type: ignore[assignment]

class RegrIntercept(StatAggregate): ...
class RegrR2(StatAggregate): ...
class RegrSlope(StatAggregate): ...
class RegrSXX(StatAggregate): ...
class RegrSXY(StatAggregate): ...
class RegrSYY(StatAggregate): ...

__all__ = [
    "CovarPop",
    "Corr",
    "RegrAvgX",
    "RegrAvgY",
    "RegrCount",
    "RegrIntercept",
    "RegrR2",
    "RegrSlope",
    "RegrSXX",
    "RegrSXY",
    "RegrSYY",
    "StatAggregate",
]
