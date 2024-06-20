import redis
from redis.typing import EncodableT

from redis_pg.db.types.r_primitive import RPrimitive


class RInt(RPrimitive[int]):
    def __init__(self, key: str, connection: redis.Redis, default: int | None = None) -> None:
        super().__init__(key, connection, default=default)

    def _encode(self, value: int) -> EncodableT:
        return value

    def _decode(self, encoded: bytes) -> int:
        return int(encoded)
