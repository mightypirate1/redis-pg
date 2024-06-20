from typing import TypeVar

from redis.typing import EncodableT

from redis_pg.db.types.r_type import RType

T = TypeVar("T")


class RPrimitive(RType[T]):
    def _setter(self, encoded: EncodableT | bytes) -> None:
        self._connection.set(self._key, encoded)

    def _getter(self) -> bytes | None:
        return self._connection.get(self._key)  # type: ignore
