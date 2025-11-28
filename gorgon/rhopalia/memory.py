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



import psutil

class RhopaliumMemory:
    """
    RhopaliumMemory — basic sensor for monitoring RAM utilization.

    This sensor returns the percentage of memory currently used.
    """

    name = "memory"

    def read(self) -> float:
        """
        Read the current system-wide memory usage.

        Returns:
            float: Memory usage percentage (0.0–100.0)
        """
        return psutil.virtual_memory().percent
