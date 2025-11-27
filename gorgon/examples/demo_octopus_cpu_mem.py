import time

from gorgon.rhopalia.cpu import RhopaliumCPU
from gorgon.rhopalia.memory import RhopaliumMemory
from gorgon.crabs.guardian import CrabGuardian
from gorgon.core.octopus import Octopus


def main() -> None:
    """
    Demo: register a CrabGuardian in Octopus and poll it a few times.

    Flow:
        Rhopalia (CPU, Memory) -> CrabGuardian -> Octopus -> console.
    """
    # Create sensors
    sensors = [RhopaliumCPU(), RhopaliumMemory()]

    # Create crab
    crab = CrabGuardian(
        name="local_system",
        sensors=sensors,
        interval=2.0,
        buffer_size=10,
    )

    # Create octopus (hub) and register the crab
    octo = Octopus(buffer_size=100)
    octo.register_crab(crab)

    print("Starting Gorgon demo with Octopus (CPU + Memory)...\n")

    for i in range(5):
        all_snapshots = octo.collect_once()
        snapshot = all_snapshots["local_system"]
        cpu = snapshot["cpu"]
        mem = snapshot["memory"]
        print(f"[{i+1}] CPU: {cpu:5.1f}%   MEM: {mem:5.1f}%")
        time.sleep(crab.interval)

    print("\nDemo finished.")
    print(f"Octopus buffered records: {len(octo.get_buffer())}")


if __name__ == "__main__":
    main()
