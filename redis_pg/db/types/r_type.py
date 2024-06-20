from abc import ABC, abstractmethod
from typing import Generic, TypeVar

import redis
from redis.typing import EncodableT

T = TypeVar("T")


class RType(ABC, Generic[T]):
    def __init__(self, key: str, connection: redis.Redis, default: T | None = None) -> None:
        self._key = key
        self._connection = connection
        self._default = default
        self._lock_key = f"{key}:lock"

    @abstractmethod
    def _encode(self, value: T) -> EncodableT | bytes: ...

    @abstractmethod
    def _decode(self, encoded: bytes) -> T: ...

    @abstractmethod
    def _setter(self, encoded: EncodableT | bytes) -> None: ...

    @abstractmethod
    def _getter(self) -> bytes | None: ...

    @property
    def value(self) -> T:
        val = self.get()
        if val is None:
            if self._default is None:
                raise ValueError(f"Key {self._key} not found and no default provided")
            return self._default
        return val

    def set(self, value: T) -> None:
        with self._connection.lock(self._lock_key):
            self._setter(self._encode(value))

    def get(self) -> T | None:
        value = self._getter()
        if value is None:
            return None
        return self._decode(value)
