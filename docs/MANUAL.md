# Gorgon System — Manual

This document describes how to install, configure, and use **Gorgon System**  
for local monitoring, ML training, notebook integration, and CLI workflows.

---

# 1. Installation

## 1.1 Requirements

- Python **3.10+**
- `psutil`
- Recommended: **virtual environment**

## 1.2 Install (development mode)

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/macOS

pip install -e .
```

This installs the library in **editable mode**, allowing you to develop locally.

---

# 2. Core Concepts

Gorgon System is built around **four layers**:

1. **Rhopalia** — atomic sensors  
2. **Crabs** — monitoring units that own sensors  
3. **Octopus** — central hub (coordination + storage)  
4. **Gorgon Bell** — analysis & user interface layer  

See full system architecture:

📄 `docs/ARCHITECTURE.md`

---

# 3. Quick Start — Running Demos

## 3.1 Full vertical pipeline (recommended)

```bash
python -m gorgon.examples.demo_bell_cli
```

You will see several lines showing CPU/RAM metrics  
with status levels:

- **OK**
- **WARN**
- **CRIT**

## 3.2 Octopus Hub demo

```bash
python -m gorgon.examples.demo_octopus_cpu_mem
```

## 3.3 Direct CrabGuardian demo

```bash
python -m gorgon.examples.demo_cpu_mem
```

---

# 4. Usage in ML / Data Workflows

A minimal integration in a real pipeline:

```python
from gorgon.rhopalia.cpu import RhopaliumCPU
from gorgon.rhopalia.memory import RhopaliumMemory
from gorgon.crabs.guardian import CrabGuardian
from gorgon.core.octopus import Octopus
from gorgon.bell.cli import GorgonBellCLI

# 1. Create sensors
sensors = [RhopaliumCPU(), RhopaliumMemory()]

# 2. Create monitoring unit (Crab)
crab = CrabGuardian(
    name="training_resources",
    sensors=sensors,
    interval=2.0,
)

# 3. Create hub and register Crab
octo = Octopus()
octo.register_crab(crab)

# 4. Create CLI Bell
bell = GorgonBellCLI(
    octopus=octo,
    crab_name="training_resources"
)

# 5. Run short monitoring session
bell.run(iterations=5)
```

Use cases:

- monitor ML training  
- monitor ETL pipelines  
- monitor ingestion & preprocessing  
- diagnose bottlenecks during heavy operations  

---

# 5. Configuration Options

## 5.1 CrabGuardian

| Parameter | Description |
|----------|-------------|
| `interval` | polling frequency (seconds) |
| `buffer_size` | local ring buffer size |
| `sensors` | list of attached Rhopalia |

## 5.2 GorgonBellCLI

| Parameter | Description |
|----------|-------------|
| `cpu_warn`, `cpu_crit` | thresholds for CPU |
| `mem_warn`, `mem_crit` | thresholds for RAM |
| `iterations` | number of print cycles |
| `interval` | optional override |

## 5.3 Octopus Hub

| Parameter | Description |
|----------|-------------|
| `buffer_size` | max global records |

---

# 6. Advanced Usage (Planned Features)

These features are part of ongoing development  
and are referenced in the project roadmap.

## 6.1 Async Monitoring

- async Crabs  
- async Octopus  
- async I/O for sensors  

## 6.2 Multiple Crabs & Complex Topologies

- multiple monitoring chains  
- cross-crab correlation  

## 6.3 Exporting Data

- JSON / NDJSON  
- SQLite  
- DuckDB  
- Redis  
- Parquet  

## 6.4 Web Dashboards

- Streamlit  
- Dash  
- FastAPI UI  

## 6.5 Notebook Widgets

- live graphs  
- sliding windows  
- event visualization  

## 6.6 MAI Engine (Memory–Attention–Inference)

- anomaly detection  
- temporal patterns  
- adaptive thresholds  
- predictive insights  

---

# 7. Summary

This manual covers:

- installation  
- basic demos  
- key concepts  
- how to integrate Gorgon into real workloads  
- configuration options  
- advanced upcoming features  

Gorgon System is designed to be:

- **modular**  
- **lightweight**  
- **bio-inspired**  
- **extendable**  
- **future-ready**  

For deeper details see:

📄 `docs/ARCHITECTURE.md`  
📄 `docs/ROADMAP.md`

