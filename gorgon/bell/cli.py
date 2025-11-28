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
from typing import Dict, Any

from gorgon.core.octopus import Octopus


class GorgonBellCLI:
    """
    GorgonBellCLI — simple textual "bell" on top of Octopus.

    Responsibilities:
        - poll Octopus for a specific crab;
        - compute simple status levels for CPU and Memory;
        - print human-friendly lines to the console.

    This is a minimal MVP, no colors or rich formatting yet.
    """

    def __init__(
        self,
        octopus: Octopus,
        crab_name: str,
        cpu_warn: float = 70.0,
        cpu_crit: float = 90.0,
        mem_warn: float = 80.0,
        mem_crit: float = 95.0,
    ) -> None:
        """
        Args:
            octopus: Octopus hub instance.
            crab_name: Name of the crab to observe.
            cpu_warn: CPU warning threshold.
            cpu_crit: CPU critical threshold.
            mem_warn: Memory warning threshold.
            mem_crit: Memory critical threshold.
        """
        self.octopus = octopus
        self.crab_name = crab_name
        self.cpu_warn = cpu_warn
        self.cpu_crit = cpu_crit
        self.mem_warn = mem_warn
        self.mem_crit = mem_crit

    def _level(self, value: float, warn: float, crit: float) -> str:
        """
        Map a numeric value to a simple status level.
        """
        if value >= crit:
            return "CRIT"
        if value >= warn:
            return "WARN"
        return "OK"

    def format_snapshot(self, snapshot: Dict[str, Any], index: int) -> str:
        """
        Build a single line of text for the given snapshot.
        """
        cpu = float(snapshot.get("cpu", 0.0))
        mem = float(snapshot.get("memory", 0.0))

        cpu_level = self._level(cpu, self.cpu_warn, self.cpu_crit)
        mem_level = self._level(mem, self.mem_warn, self.mem_crit)

        return (
            f"[{index}] "
            f"CPU: {cpu:5.1f}% ({cpu_level:4})   "
            f"MEM: {mem:5.1f}% ({mem_level:4})"
        )

    def run(
        self,
        iterations: int = 5,
        interval: float | None = None,
    ) -> None:
        """
        Poll the target crab via Octopus and print status lines.

        Args:
            iterations: How many times to poll.
            interval: Optional sleep interval between iterations.
                      If None, uses crab.interval if available,
                      otherwise defaults to 2 seconds.
        """
        if self.crab_name not in self.octopus.crabs:
            raise ValueError(f"Crab '{self.crab_name}' is not registered in Octopus.")

        crab = self.octopus.crabs[self.crab_name]
        effective_interval: float = interval or getattr(crab, "interval", 2.0)

        print(f"Starting GorgonBellCLI for crab '{self.crab_name}'...\n")

        for i in range(1, iterations + 1):
            all_snapshots = self.octopus.collect_once()
            snapshot = all_snapshots.get(self.crab_name, {})
            line = self.format_snapshot(snapshot, i)
            print(line)
            time.sleep(effective_interval)

        print("\nGorgonBellCLI session finished.")
