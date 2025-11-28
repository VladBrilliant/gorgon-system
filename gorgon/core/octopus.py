"""
GORGON System — https://github.com/VladBrilliant/gorgon-system
© 2025 Vladimir Brilliantov

Creator of the GORGON System architecture:
Rhopalia Sensors, Crabs Monitoring Agents, Octopus Hub,
Gorgon Bell, MAI Engine.

All concepts, terminology, and architectural patterns introduced in this project
originated with the author.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
"""


from __future__ import annotations

import time
from typing import Protocol, Dict, Any, List


class Crab(Protocol):
    """
    Protocol for crab-like monitoring units.

    Any object that implements this protocol can be registered
    in the Octopus hub.
    """

    name: str

    def collect_once(self) -> Dict[str, Any]:
        """
        Poll the crab once and return a snapshot of sensor values.

        Returns:
            dict: Mapping sensor_name -> reading_value
        """
        ...


class Octopus:
    """
    Octopus — central hub for Gorgon System.

    Responsibilities:
        - register and manage crabs (monitoring units);
        - poll all registered crabs on demand;
        - keep a lightweight in-memory buffer of records.

    This is a synchronous MVP implementation. Later we can:
        - add async support;
        - plug in external storage backends (DB, message bus, etc).
    """

    def __init__(self, buffer_size: int = 1000) -> None:
        """
        Args:
            buffer_size: Maximum number of records stored in memory.
        """
        self.buffer_size = buffer_size
        self.crabs: Dict[str, Crab] = {}
        self.buffer: List[Dict[str, Any]] = []

    def register_crab(self, crab: Crab) -> None:
        """
        Register a crab in the hub.

        If a crab with the same name already exists, it will be replaced.
        """
        self.crabs[crab.name] = crab

    def unregister_crab(self, name: str) -> None:
        """
        Remove a crab from the hub by its name.

        If the crab does not exist, this is a no-op.
        """
        self.crabs.pop(name, None)

    def list_crabs(self) -> List[str]:
        """
        Return a list of registered crab names.
        """
        return list(self.crabs.keys())

    def collect_once(self) -> Dict[str, Dict[str, Any]]:
        """
        Poll all registered crabs exactly once.

        Returns:
            dict: Mapping crab_name -> {sensor_name -> reading_value}
        """
        all_snapshots: Dict[str, Dict[str, Any]] = {}
        timestamp = time.time()

        for name, crab in self.crabs.items():
            values = crab.collect_once()
            all_snapshots[name] = values

            self._store(
                {
                    "timestamp": timestamp,
                    "crab": name,
                    "values": values,
                }
            )

        return all_snapshots

    def _store(self, record: Dict[str, Any]) -> None:
        """
        Store a single record in the internal buffer, respecting buffer_size.
        """
        self.buffer.append(record)
        if len(self.buffer) > self.buffer_size:
            # drop the oldest record
            self.buffer.pop(0)

    def get_buffer(self) -> List[Dict[str, Any]]:
        """
        Get a shallow copy of the internal buffer for inspection.
        """
        return list(self.buffer)
