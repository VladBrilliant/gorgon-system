from __future__ import annotations

import time
from typing import List, Dict, Any, Protocol


class Rhopalium(Protocol):
    """
    Protocol for Rhopalia sensors.

    Any sensor that implements this protocol can be attached to CrabGuardian.
    """

    name: str

    def read(self) -> float:
        ...


class CrabGuardian:
    """
    CrabGuardian — basic monitoring unit that owns a set of Rhopalia sensors.

    Responsibilities:
        - poll attached sensors at a given interval;
        - keep a lightweight in-memory buffer of recent readings;
        - optionally forward data to a higher-level hub (Octopus) later.
    """

    def __init__(self, name: str, sensors: List[Rhopalium], interval: float = 5.0, buffer_size: int = 100):
        """
        Args:
            name: Logical name of this crab (e.g. 'training_resources').
            sensors: List of sensor instances (Rhopalia) to poll.
            interval: Polling interval in seconds.
            buffer_size: Maximum number of records kept in the local buffer.
        """
        self.name = name
        self.sensors = sensors
        self.interval = interval
        self.buffer_size = buffer_size
        self.buffer: List[Dict[str, Any]] = []

    def collect_once(self) -> Dict[str, Any]:
        """
        Poll all attached sensors exactly once.

        Returns:
            dict: Mapping sensor_name -> reading_value
        """
        snapshot: Dict[str, Any] = {}
        for sensor in self.sensors:
            snapshot[sensor.name] = sensor.read()

        # add timestamp
        record = {
            "timestamp": time.time(),
            "values": snapshot,
        }

        self._store(record)
        return snapshot

    def _store(self, record: Dict[str, Any]) -> None:
        """
        Store a single record in the local buffer, respecting buffer_size.
        """
        self.buffer.append(record)
        if len(self.buffer) > self.buffer_size:
            # drop the oldest record
            self.buffer.pop(0)

    def run_forever(self) -> None:
        """
        Continuously poll sensors at the configured interval.

        This is a simple blocking loop for the MVP.
        In the future we may add an async version.
        """
        try:
            while True:
                self.collect_once()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            # graceful stop when user presses Ctrl+C
            return
 
