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



import time

from gorgon.rhopalia.cpu import RhopaliumCPU
from gorgon.rhopalia.memory import RhopaliumMemory
from gorgon.crabs.guardian import CrabGuardian


def main() -> None:
    """
    Simple demo: poll CPU and Memory a few times and print snapshots.

    This is a minimal vertical slice:
        Rhopalia (CPU, Memory) -> CrabGuardian -> console output.
    """
    sensors = [RhopaliumCPU(), RhopaliumMemory()]
    crab = CrabGuardian(
        name="local_system",
        sensors=sensors,
        interval=2.0,
        buffer_size=10,
    )

    print("Starting Gorgon demo (CPU + Memory)...\n")

    for i in range(5):
        snapshot = crab.collect_once()
        cpu = snapshot["cpu"]
        mem = snapshot["memory"]
        print(f"[{i+1}] CPU: {cpu:5.1f}%   MEM: {mem:5.1f}%")
        time.sleep(crab.interval)

    print("\nDemo finished.")


if __name__ == "__main__":
    main()

