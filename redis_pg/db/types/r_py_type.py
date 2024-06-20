from typing import TypeVar

import dill
from redis.typing import EncodableT

from redis_pg.db.types.r_primitive import RPrimitive

T = TypeVar("T")


class RPyType(RPrimitive[T]):
    def _encode(self, value: T) -> EncodableT:
        return dill.dumps(value)

    def _decode(self, encoded: bytes) -> T:
        return dill.loads(encoded)  # noqa: S301

