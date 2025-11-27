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
