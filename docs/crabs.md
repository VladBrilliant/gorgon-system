# Crabs — Monitoring Units of Gorgon System

Crabs are **monitoring agents** that own sensors (Rhopalia),  
control how often they are polled, manage local buffers,  
and provide structured metric snapshots to the rest of the system.

Crabs form the second layer of the architecture:

```
Rhopalia → Crabs → Octopus → Gorgon Bell
```

This document describes crab design, types, APIs, lifecycle, and best practices.

---

# 1. What Is a Crab?

In the Gorgon architecture:

- **Rhopalia** collect *one metric*  
- **Crabs** collect many sensor readings and turn them into **snapshots**  
- **Octopus** aggregates snapshots  
- **Gorgon Bell** visualizes and analyzes them  

A crab is effectively a **portable sensor hub**.

Crabs are designed to be:

- modular  
- lightweight  
- attachable to any pipeline  
- easy to copy between projects  
- configurable per use-case  
- future-compatible with async polling and distributed modes  

---

# 2. Current Crab Implementation: `CrabGuardian`

The MVP crab type is `CrabGuardian`.

It is:

- synchronous  
- lightweight  
- simple to embed anywhere  
- perfect for CPU/RAM/ETL monitoring  
- compatible with Octopus Hub  

## 2.1 Class Interface

```python
class CrabGuardian:
    name: str
    sensors: List[Rhopalium]
    interval: float
    buffer_size: int

    def collect_once(self) -> dict: ...
    def run_forever(self): ...
```

Readable snapshot format:

```python
{
    "timestamp": <float>,
    "values": {
        "cpu": 41.2,
        "memory": 67.5,
    }
}
```

---

# 3. Sensor Attachment

A crab can have **one or many** rhopalia:

```python
crab = CrabGuardian(
    name="system",
    sensors=[RhopaliumCPU(), RhopaliumMemory()],
    interval=2.0,
)
```

Attach process-level sensors:

```python
crab = CrabGuardian(
    name="training_job",
    sensors=[
        RhopaliumCPU(),
        RhopaliumMemory(),
        RhopaliumProcessCPU(pid=1234),
    ],
    interval=1.0,
)
```

Attach custom sensors:

```python
crab = CrabGuardian(
    name="etl_latency",
    sensors=[RhopaliumSQLLatency(query="SELECT 1")],
    interval=0.5,
)
```

---

# 4. Crab Lifecycle

## 4.1 Single Snapshot

```python
metrics = crab.collect_once()
print(metrics)
```

## 4.2 Continuous Monitoring

```python
crab.run_forever()
```

`run_forever()` performs:

1. read all sensor values  
2. store snapshot in local buffer  
3. sleep (`interval`)  
4. repeat  

## 4.3 Integration with Octopus

Crabs are meant to be used with **Octopus Hub**:

```python
octo = Octopus()
octo.register_crab(crab)

snapshot = octo.collect_once("system")
```

---

# 5. Crab Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | str | Identifier used for buffers & Bell |
| `sensors` | list | Attached rhopalia |
| `interval` | float | Poll frequency in seconds |
| `buffer_size` | int | Local ring buffer size |

### Additional planned parameters

- `mode` (sync / async)  
- `jitter` (random delay to avoid load spikes)  
- `multi_interval` (different intervals per sensor)  

---

# 6. Crab Types (Present & Future)

## 6.1 `CrabGuardian` (MVP)

- synchronous  
- simple polling loop  
- ideal for local monitoring, Jupyter, ML jobs  

## 6.2 `CrabSleeper` (planned)

- low-frequency polling  
- good for long-running ETL  
- optimized for minimal overhead  

## 6.3 `CrabWatchdog` (planned)

- high-frequency  
- aggressive alerting  
- can detect runaway processes  

## 6.4 `CrabTrainer` (future)

- designed for ML/DL training  
- pairs with GPU sensors  
- understands epoch/batch boundaries  

## 6.5 `CrabDistributed` (future)

- runs on remote machines  
- pushes snapshots to central Octopus cluster  

---

# 7. Example — Full Integration

```python
from gorgon.rhopalia.cpu import RhopaliumCPU
from gorgon.rhopalia.memory import RhopaliumMemory
from gorgon.crabs.guardian import CrabGuardian
from gorgon.core.octopus import Octopus
from gorgon.bell.cli import GorgonBellCLI

crab = CrabGuardian(
    name="local_system",
    sensors=[RhopaliumCPU(), RhopaliumMemory()],
    interval=2.0,
    buffer_size=10,
)

octo = Octopus()
octo.register_crab(crab)

bell = GorgonBellCLI(octopus=octo, crab_name="local_system")
bell.run(iterations=5)
```

---

# 8. When to Use Crabs

### ✔ Monitoring ML training  
Track CPU, RAM, GPU, batch timing.

### ✔ Diagnosing ETL bottlenecks  
Track disk IO + SQL latency + memory spikes.

### ✔ Benchmarking algorithms  
Compare performance between runs.

### ✔ Observing pipelines in Jupyter notebooks  
See resource usage around heavy operations.

### ✔ Testing model performance over time  
Integrate with Octopus to produce data graphs.

---

# 9. Best Practices

### ✔ Keep crabs small  
One crab = one monitoring unit.

### ✔ Use multiple crabs for complex pipelines  
Example:

- `crab_data_ingest`
- `crab_preprocessing`
- `crab_training`
- `crab_export`

### ✔ Keep buffer sizes modest  
Large buffers → use Octopus with storage backend.

### ✔ Tune `interval` based on workload  
- 0.5s for high-frequency jobs  
- 2–5s for ML training  
- 10–30s for ETL  

### ✔ Use per-sensor intervals (future feature)

### ✔ Prefer async crabs for heavy environments

---

# 10. Roadmap for Crabs

| Version | Feature |
|---------|---------|
| 0.1.0 | Code cleanup, configurable APIs |
| 0.2.0 | **Async CrabGuardian** |
| 0.3.0 | CrabSleeper, CrabWatchdog |
| 0.4.0 | CrabTrainer (ML ops) |
| 0.5.0 | Distributed Crabs |
| 1.0.0 | Stable API for long-running services |

---

# 11. Summary

Crabs are:

- the **central operational unit** of Gorgon System  
- sensor owners  
- snapshot producers  
- buffer managers  
- Octopus feeders  
- first layer that understands “time”  

They are lightweight, portable, and designed for:

- ML  
- ETL  
- data pipelines  
- system diagnostics  
- research & experiments  

This document will expand as new crab types are introduced.
