# Rhopalia Sensors — Gorgon System

Rhopalia are **atomic, bio-inspired sensors**, modeled after jellyfish neural nodes.  
Each sensor is responsible for **one metric** and provides a unified, minimal API.

This document explains:

- what rhopalia are  
- how to use them  
- when to use each sensor  
- existing sensors  
- future sensors  
- extension guide  

---

# 1. What Are Rhopalia?

In Gorgon System architecture:

```
Rhopalia → Crabs → Octopus → Gorgon Bell
```

Rhopalia represent the **sensory layer** of the system.

A Rhopalium is:

- atomic (measures one thing)
- stateless
- lightweight
- extremely fast
- safe for synchronous & async environments
- pluggable into any crab

Unified interface:

```python
class Rhopalium(Protocol):
    name: str
    def read(self) -> float: ...
```

---

# 2. Current Sensors (MVP)

The following sensors are implemented in the current version:

| Sensor | Source | Purpose | Category | Overhead |
|--------|--------|----------|-----------|----------|
| **RhopaliumCPU** | psutil | CPU usage (%) | system | low |
| **RhopaliumMemory** | psutil | RAM usage (%) | system | low |

---

# 3. Sensor Selection Guide

## 3.1 CPU Sensor (`RhopaliumCPU`)

### Use when:
- diagnosing ML training bottlenecks  
- monitoring CPU-bound pipelines  
- detecting overloads / stuck jobs  
- helping tune ETL multiprocessing  

### Avoid when:
- CPU is mostly idle and the focus is I/O (use network/disk)  
- on GPU-heavy workloads (use GPU sensors)  

### Parameters:
None — CPU load is system-wide.

---

## 3.2 Memory Sensor (`RhopaliumMemory`)

### Use when:
- data preprocessing uses large batches  
- pandas / PyTorch hogs RAM  
- ETL pipelines spill to swap  
- model training approaches OOM  

### Avoid when:
- workloads use GPU RAM only  
- memory is heavily compressed (container environments)  

### Parameters:
None — RAM usage is system-wide.

---

# 4. Future Sensors

These sensors are planned and appear in the roadmap.

| Sensor | Source | Purpose | Category | Overhead |
|--------|--------|----------|-----------|----------|
| **RhopaliumDisk** | psutil | Disk usage, R/W load | system | low |
| **RhopaliumNetIO** | psutil | Network throughput | system | low |
| **RhopaliumGPU** | NVML / torch | GPU usage, VRAM | compute | medium |
| **RhopaliumSQLLatency** | custom | Query latency ms | data | medium |
| **RhopaliumFSWatch** | watchdog | File system events | infra | medium |
| **RhopaliumContainerState** | Docker SDK | Container health | infra | low |
| **RhopaliumTemp** | OS sensors | System temperature | system | low |
| **RhopaliumProcessCPU** | psutil | Specific PID CPU | process | low |
| **RhopaliumProcessMemory** | psutil | Specific PID RAM | process | low |

---

# 5. Example — Using Rhopalia

Minimal usage:

```python
from gorgon.rhopalia.cpu import RhopaliumCPU
from gorgon.rhopalia.memory import RhopaliumMemory

cpu = RhopaliumCPU()
mem = RhopaliumMemory()

print(cpu.read())
print(mem.read())
```

Using with a crab:

```python
from gorgon.crabs.guardian import CrabGuardian
from gorgon.rhopalia.cpu import RhopaliumCPU
from gorgon.rhopalia.memory import RhopaliumMemory

crab = CrabGuardian(
    name="system",
    sensors=[RhopaliumCPU(), RhopaliumMemory()],
    interval=2.0,
)
```

---

# 6. How to Create a New Rhopalium

Rhopalia are intentionally simple.  
A new sensor usually requires 5–10 lines of code.

Example: Disk usage sensor

```python
import psutil

class RhopaliumDisk:
    """
    Measures total disk usage percentage.
    """
    name = "disk"

    def read(self) -> float:
        return psutil.disk_usage('/').percent
```

Register it inside any crab:

```python
crab = CrabGuardian(
    name="job_disk_monitor",
    sensors=[RhopaliumDisk()],
    interval=1.0,
)
```

---

# 7. Best Practices

### ✔ Keep sensors atomic
One sensor = one metric.  
Do not combine CPU + RAM into one class.

### ✔ Never store state
Sensors should not:

- cache results  
- keep counters  
- block execution  

Crab handles state, not Rhopalia.

### ✔ Keep overhead low
Sensors must be too cheap to measure themselves.

### ✔ Use psutil for system metrics  
It is battle-tested and cross-platform.

### ✔ Separate system / process / data sensors
Gorgon System treats these groups differently.

---

# 8. Summary

Rhopalia form the foundation of Gorgon System:

- tiny  
- pluggable  
- safe  
- atomic  
- fast  
- extendable  

They map cleanly into the bio-inspired architecture:

```
Rhopalia (sensors)
     ↓
Crabs (monitoring units)
     ↓
Octopus (hub)
     ↓
Gorgon Bell (UI / analysis)
```

This document will grow as additional sensors are introduced.
