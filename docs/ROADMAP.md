# Gorgon System — Roadmap

This roadmap outlines the evolution of **Gorgon System** from early MVP  
toward a stable, extensible, bio-inspired monitoring and adaptive intelligence framework.

It is divided into **version milestones** plus a long-term vision section.

---

# 1. Version 0.0.x — MVP Line (Current Stage)

### ✔ Completed
- CPU sensor (`RhopaliumCPU`)
- Memory sensor (`RhopaliumMemory`)
- `CrabGuardian` (synchronous version)
- `Octopus` core hub with unified buffer
- `GorgonBellCLI` basic console UI
- Working examples:
  - CPU/RAM demo
  - Crab + Octopus integration
  - Full vertical CLI demo
- Initial documentation:
  - `README.md`
  - `MANUAL.md`
  - `ARCHITECTURE.md`
  - `ROADMAP.md`
  - `CHANGELOG.md`

### 🔄 In Progress
- API cleanup & code style polishing  
- Improved directory structure  
- Better documentation hierarchy  
- Preparing foundation for async execution

---

# 2. Version 0.1.0 — UX & Developer Experience

### 🎯 Goals
- Cleaner top-level import API (`from gorgon import Crab, Octopus, ...`)
- Improved CLI output:
  - basic colors
  - aligned tables
  - smoother refresh
- Additional examples for:
  - ML training monitoring  
  - ETL/ELT monitoring  
  - archive extraction/compression profiling  
- First wave of **unit tests**

### 🧩 Stretch Goals
- Basic CI (lint + tests)
- Configurable “pretty print” modes for CLI

---

# 3. Version 0.2.0 — Async Engine & More Sensors

### 🎯 Goals
- `AsyncCrabGuardian`  
- Async snapshot pipeline  
- Sensor-level async support

### 📡 New Rhopalia (Sensors)
- Disk usage sensor  
- Network IO sensor  
- GPU sensor (NVML / torch)  
- SQL latency sensor  
- File-system watchers (optional)

### 📦 Internal Improvements
- Per-sensor polling intervals  
- More efficient ring buffer  
- Sensor categories (system / process / data / ML)

---

# 4. Version 0.3.0 — Storage Layer & MAI Engine (Phase 1)

### 🧠 MAI (Memory–Attention–Inference) — Initial Interface
- Time-window anomaly detection  
- Adaptive thresholds  
- Early pattern recognition hooks  
- Behavior signatures (CPU/RAM “profiles”)

### 🗄 Storage Backends (choose one first)
- SQLite — simplest stable storage  
- DuckDB — analytical column store  
- Redis — real-time shared memory (optional)

### 📤 Export Formats
- JSON / NDJSON  
- Parquet (optional)  
- SQLite table dumps  

---

# 5. Version 0.4.0 — UI Expansion (Gorgon Bell)

### 🌐 Web Bell (first UI)
- Streamlit prototype  
- Dash/Plotly alternative  
- Timeline graphs  
- Sliding window performance charts  

### 📘 Notebook Bell
- Jupyter widget  
- Hover metrics  
- Sparkline graphs  

### 🖥 CLI 2.0
- Full-screen mode  
- Auto-refresh loop  
- Alerts + blinking states  

---

# 6. Version 0.5.0 — Packaging & Distribution

### 🎯 Goals
- Publish to PyPI  
- Wheel + Source distribution  
- Full `pyproject.toml` with extras:
  - `[visual]`
  - `[cli]`
  - `[async]`
  - `[all]`
- Full API documentation under `/docs/api_reference/`
- Release automation (GitHub Actions)

---

# 7. Version 1.0.0 — Stable Release Vision

### 🎯 High-Level Goals
- All major sensor classes implemented  
- Async infrastructure complete  
- Storage backend stable  
- MAI Engine v1 operational  
- CLI, Jupyter, and Web Bell fully functional  
- Full test suite with 85%+ coverage  
- Monitoring profiles for:
  - ML training  
  - ETL/ELT workflows  
  - batch jobs  
  - long-running services  

### 🔐 Optional (if time/resources allow)
- Plugin system  
- Remote Crabs  
- Secure ingestion endpoints  

---

# Long-Term Ideas (Beyond 1.0)

These items are not tied to specific versions but define the broader vision.

### 🧬 Bio-inspired intelligence
- Reinforcement-like feedback for thresholds  
- Multi-sensor “attention weights”  
- Adaptive pattern memory  
- Self-adjusting poll frequency  

### 🌍 Distributed Monitoring
- Multi-node fleet  
- Central Octopus cluster  
- Remote Rhopalia  
- Federated view dashboard  

### 🛰 DevOps & Infra Extensions
- Container metrics (Docker API)  
- Kubernetes pod-level sensors  
- System logs ingestion  
- Crash pattern detection  

### 🔄 Self-Healing Concepts
- Automated recommendations  
- Auto-throttle processes  
- Early-warning predictions  
- MAI-guided recovery actions  

---

# Summary

Gorgon System roadmap is structured into clear phases:

```
MVP → Async Engine → Storage Layer → MAI → UI → Packaging → Stable Release
```

Each step extends the bio-inspired architecture while keeping the system:

- lightweight  
- modular  
- fast  
- deeply extensible  
- and ready for AI-assisted monitoring  

This roadmap evolves dynamically as new components are introduced.

