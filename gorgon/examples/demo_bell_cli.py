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


from gorgon.rhopalia.cpu import RhopaliumCPU
from gorgon.rhopalia.memory import RhopaliumMemory
from gorgon.crabs.guardian import CrabGuardian
from gorgon.core.octopus import Octopus
from gorgon.bell.cli import GorgonBellCLI


def main() -> None:
    """
    Demo: use GorgonBellCLI on top of Octopus and CrabGuardian.

    Flow:
        Rhopalia (CPU, Memory) -> CrabGuardian -> Octopus -> GorgonBellCLI -> console.
    """
    # Create sensors and crab
    sensors = [RhopaliumCPU(), RhopaliumMemory()]
    crab = CrabGuardian(
        name="local_system",
        sensors=sensors,
        interval=2.0,
        buffer_size=10,
    )

    # Create Octopus and register crab
    octo = Octopus(buffer_size=100)
    octo.register_crab(crab)

    # Create bell (CLI) for this crab
    bell = GorgonBellCLI(
        octopus=octo,
        crab_name="local_system",
        cpu_warn=70.0,
        cpu_crit=90.0,
        mem_warn=80.0,
        mem_crit=95.0,
    )

    # Run a short session
    bell.run(iterations=5)


if __name__ == "__main__":
    main()
