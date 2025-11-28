# Gorgon System — Architecture

This document describes the internal architecture of **Gorgon System**:  
its conceptual layers, responsibilities, data flow, and extension strategy.

---

# 1. Architectural Overview

Gorgon System is designed as a **four-layer modular monitoring framework**:

1. **Rhopalia** — atomic sensors  
2. **Crabs** — monitoring units that own sensors  
3. **Octopus** — central hub and system coordinator  
4. **Gorgon Bell** — analysis & presentation layer  

These layers form a full vertical pipeline:

```
Rhopalia → Crabs → Octopus → Gorgon Bell
```

Each layer is independent, extensible, and replaceable.

---

# 2. Rhopalia — Sensors Layer

**Rhopalia** are tiny, atomic classes that fetch *one metric* each time they are called.

They form the “neural endings” of the system.

## 2.1 Responsibilities

- Read a single metric  
- Expose a unified interface  
- Stay extremely lightweight  

Unified sensor protocol:

```python
class Rhopalium(Protocol):
    name: str
    def read(self) -> float: ...
```

## 2.2 Current Sensors (MVP)

| Sensor | Source | Description |
|--------|--------|-------------|
| `RhopaliumCPU` | psutil | System CPU load (%) |
| `RhopaliumMemory` | psutil | System RAM usage (%) |

## 2.3 Design Principles

- No global state  
- No shared memory  
- No dependencies between sensors  
- Fast to initialize / fast to destroy  
- Easy to extend: Disk, Network, GPU, SQL latency, filesystem sensors planned  

---

# 3. Crabs — Monitoring Units

**Crabs** own multiple Rhopalia and know **how, when, and how often** to poll them.

They are the “intermediate ganglia” of the system.

## 3.1 Responsibilities

- Own and manage a list of sensors  
- Produce snapshots via `collect_once()`  
- Maintain a local ring buffer  
- Optionally run continuous loops (`run_forever`, async version planned)

## 3.2 Current Implementation: `CrabGuardian`

- synchronous polling  
- configurable interval  
- lightweight in-memory buffer  
- returns structured snapshots:  

```python
{
    "timestamp": <float>,
    "values": {
        "cpu": 41.2,
        "memory": 67.5
    }
}
```

## 3.3 Design Intent

Crabs are intended to be:

- **pluggable** (drop-in units)  
- **portable** (can be attached to any pipeline or script)  
- **extendable** (different crab types: Guardian, Sleeper, Watchdog, Trainer, etc.)  

---

# 4. Octopus — Central Hub

The **Octopus Hub** is the coordination center of Gorgon System.

It receives snapshots from crabs, stores them, and exposes them to UI layers.

## 4.1 Responsibilities

- Register/unregister crabs  
- Poll all crabs (`collect_once()`)  
- Maintain a global ring buffer  
- Provide snapshot history (`get_buffer`)  
- Serve as a message bus for UI/MAI

## 4.2 Data Flow Through Octopus

```
CrabGuardian → snapshot → Octopus buffer → Gorgon Bell
```

## 4.3 Future Extensions

- async internal polling  
- pluggable storage engines:  
  - SQLite  
  - DuckDB  
  - Redis  
  - shared memory ring buffers  
- distributed mode (multi-node monitoring)  
- remote metrics ingestion  
- permissioned access control  

---

# 5. Gorgon Bell — Analysis & Presentation Layer

This is where raw numbers become *human-interpretable signals*.

The Bell “rings” when something goes wrong.

## 5.1 Current Implementation: `GorgonBellCLI`

- pulls data from Octopus for a particular crab  
- computes simple status levels:  
  - OK  
  - WARN  
  - CRIT  
- prints clean, readable output for console workflows  
- serves as the first minimal UI

## 5.2 Planned UI Layers

- Rich-powered color CLI  
- Jupyter widgets (Notebook Bell)  
- Web dashboards (Streamlit, Dash, FastAPI UI)  
- Visual timelines and live graphs  
- MAI-driven insights (adaptive monitoring)

---

# 6. End-to-End Data Flow (MVP)

```
+---------------------+
|      Rhopalia       |
|  (CPU, Memory ...)  |
+----------+----------+
           |
           v
+----------+----------+
|     CrabGuardian    |
| polls & buffers     |
+----------+----------+
           |
           v
+----------+----------+
|       Octopus       |
| global ring buffer  |
+----------+----------+
           |
           v
+---------------------+
|   GorgonBellCLI     |
|   status display    |
+---------------------+
```

---

# 7. Future Architecture Extensions

These components are part of the mid-term roadmap:

### 7.1 MAI Engine — Memory–Attention–Inference
A lightweight cognitive layer:

- anomaly detection  
- pattern memory  
- adaptive thresholds  
- behavioral prediction  

### 7.2 Distributed Crabs
Multiple machines → one Octopus hub.

### 7.3 Storage Engines
Swappable backends:

- SQLite (local persistence)  
- DuckDB (analytics)  
- Redis (shared memory)  
- Parquet (long-term logging)  

### 7.4 Web Bell
Full monitoring dashboard with graphs and event streams.

---

# 8. Summary

Gorgon System architecture is:

- **bio-inspired**  
- **modular and pluggable**  
- **lightweight and portable**  
- **ready for advanced AI-assisted monitoring**  

This layered design ensures:

```
simplicity at the bottom (sensors)
modularity in the middle (crabs + octopus)
intelligence at the top (Gorgon Bell + MAI)
```

This document will evolve as additional components are introduced.

