# Octopus Hub — Coordination Layer of Gorgon System

The **Octopus** is the central coordination and routing component of the Gorgon System.  
It receives snapshots from Crabs, stores them, organizes them, and provides a unified  
interface for higher layers — including Gorgon Bell, MAI Engine, and future dashboards.

It forms the third layer of the architecture:

```
Rhopalia → Crabs → Octopus → Gorgon Bell → MAI
```

This document covers design principles, API, data flow, best practices, and roadmap.

---

# 1. What Is the Octopus?

The **Octopus Hub** is:

- a **message bus**  
- a **metric aggregator**  
- a **lightweight storage layer**  
- a **coordination point** between all Crabs and user interfaces  

It does **not** collect metrics by itself — it relies on Crabs for data acquisition.

---

# 2. Responsibilities

### ✔ Register crabs  
Each crab has a unique name. The hub tracks all active units.

### ✔ Poll crabs when needed  
Octopus can ask any crab for a fresh snapshot.

### ✔ Store snapshots in a unified buffer  
Supports a global ring buffer (configurable size).

### ✔ Provide read APIs for UI & analytics  
- Gorgon Bell (CLI, Web, Notebook)  
- MAI Engine  
- external dashboards in future  

### ✔ Ensure consistent temporal ordering  
Octopus timestamps every snapshot it stores.

---

# 3. Current Implementation (MVP)

## 3.1 Class Interface

```python
class Octopus:
    def register_crab(self, crab): ...
    def collect_once(self, crab_name: str) -> dict: ...
    def get_buffer(self, crab_name: str) -> list: ...
```

### Internal state

```python
self.crabs: Dict[str, Crab]
self.buffers: Dict[str, Deque]
```

`buffer_size` defaults to **100**.

---

# 4. Data Flow Through Octopus

A simple synchronous flow:

```
Crab → snapshot → Octopus buffer → Gorgon Bell output
```

More detailed:

```
          [CrabGuardian]
                │
                ▼
          collect_once()
                │
                ▼
           Snapshot (dict)
                │
                ▼
+----------------------------------+
|           Octopus Hub            |
|  - timestamps                    |
|  - buffer routing                |
|  - indexing by crab_name        |
+----------------------------------+
                │
                ▼
       [GorgonBellCLI] or MAI
```

---

# 5. Snapshot Format

Every snapshot pushed to Octopus has the unified form:

```python
{
    "timestamp": 1732778016.781,
    "values": {
        "cpu": 12.5,
        "memory": 63.7,
        ...
    }
}
```

Keys are derived from rhopalia names.

Octopus **never alters sensor values** — it only stores and organizes them.

---

# 6. Registering Crabs

```python
from gorgon.core.octopus import Octopus

octo = Octopus(buffer_size=100)
octo.register_crab(crab)
```

Rules:

- crab names must be unique  
- attempting to register the same name twice should raise an error (future version)

---

# 7. Polling Crabs

## 7.1 Poll one crab

```python
snapshot = octo.collect_once("local_system")
```

## 7.2 Poll all crabs (planned)

```python
snapshots = octo.collect_all()
```

## 7.3 Scheduled polling (future)

Octopus will support:

- heartbeat polling  
- round-robin  
- multi-threaded  
- async distributed polling  

---

# 8. Accessing Stored Data

Retrieve the full historical buffer for a crab:

```python
history = octo.get_buffer("local_system")
```

### Buffer behavior:
- ring buffer (FIFO)  
- fixed size per crab  
- overwrites oldest entries  

---

# 9. Integration with Gorgon Bell

Octopus is the **only** data source for Gorgon Bell layers.

CLI example:

```python
bell = GorgonBellCLI(
    octopus=octo,
    crab_name="local_system"
)

bell.run(iterations=5)
```

Web Bell & Notebook Bell (future) will use the same API.

---

# 10. Why a Central Hub?

### ✔ Clean separation of concerns  
Sensors → Crabs → Hub → UI  
Each layer has one purpose.

### ✔ Multiple crabs  
Octopus lets you manage dozens of crabs at once.

### ✔ Consistent, unified buffer  
All UIs read from the same source of truth.

### ✔ Future distributed mode  
Remote crabs → central octopus node → dashboards.

### ✔ Storage abstraction  
Octopus controls the ring buffer and can delegate to DBs.

---

# 11. Future Features

## 11.1 Async Octopus (0.2.x)

- non-blocking polling  
- `collect_once_async()`  
- asyncio Queue for message-driven design  

## 11.2 Storage Backends (0.3.x)

Pluggable adapters:

- SQLite (local persistence)  
- DuckDB (analytics & large buffers)  
- Redis (shared memory for multi-process monitoring)  
- Parquet (long-term logs)  

## 11.3 Distributed Octopus (0.4.x+)

- remote crab ingestion  
- WebSocket / HTTP API for snapshot push  
- Octopus cluster with consistent snapshot ordering  

## 11.4 Advanced Buffer Features

- time window queries  
- downsampling  
- delta compression  
- snapshot tagging  

## 11.5 Octopus as an event bus

- notification hooks  
- trigger rules  
- integration with MAI Engine  
- real-time alerts  

---

# 12. Best Practices

### ✔ Keep crab names stable  
They’re used by Gorgon Bell and Octopus buffers.

### ✔ Use small buffers for local work  
Large buffers → use storage backend.

### ✔ Prefer one Octopus per project  
Multiple hubs complicate UI layers.

### ✔ Keep Octopus logic simple  
Heavy logic belongs to MAI Engine or Gorgon Bell.

### ✔ Use async mode for heavy pipelines  
Async polling drastically reduces latency.

---

# 13. Summary

The Octopus Hub is the **coordination brainstem** of Gorgon System:

- routes data from Crabs to UI  
- maintains unified buffers  
- timestamps and organizes snapshots  
- ready for async, distributed, and storage-heavy workflows  

It ensures the entire pipeline remains:

```
Modular → Scalable → Extensible → Bio-Inspired
```

This document will expand as features evolve.
