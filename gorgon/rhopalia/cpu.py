import psutil

class RhopaliumCPU:
    """
    RhopaliumCPU — basic sensor for monitoring CPU utilization.

    This sensor returns the current CPU usage percentage.
    It is designed to be extremely lightweight and polled frequently.
    """

    name = "cpu"

    def read(self) -> float:
        """
        Read the current system-wide CPU utilization.

        Returns:
            float: CPU usage percentage (0.0–100.0)
        """
        return psutil.cpu_percent(interval=0.1)
