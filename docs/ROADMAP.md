# Gorgon System — Roadmap

This roadmap describes the planned development stages of Gorgon System,
from MVP to long-term advanced features.

---

## 1. Version 0.0.x — MVP Line (current stage)

### Completed ✔
- CPU sensor (`RhopaliumCPU`)
- Memory sensor (`RhopaliumMemory`)
- `CrabGuardian` (synchronous)
- `Octopus` core hub
- `GorgonBellCLI`
- Example files
- Initial documentation (`README`, `MANUAL`, `ARCHITECTURE`, `ROADMAP`, `CHANGELOG`)

### Ongoing
- Clean API refinements
- Improving documentation structure
- Preparing for async support

---

## 2. Version 0.1.0 — UX and Demo Improvements

### Goals
- Helper API imports in `gorgon.__init__`
- Better CLI output (colors, tables, banners)
- More example scripts for ML / data workflows
- First basic unit tests  

---

## 3. Version 0.2.0 — Async & More Sensors

### Goals
- `AsyncCrabGuardian` (non-blocking monitoring)
- Additional sensors:
  - Disk usage
  - Network IO
  - GPU metrics (if available)
- Configurable intervals per sensor
- Improved buffer implementations

---

## 4. Version 0.3.0 — MAI & Storage Layer

### Goals
- Initial **MAI (Memory–Attention–Inference)** interface
- Anomaly detection rules
- Prediction hooks (CPU/RAM trends)
- Storage backends (choose one first):
  - SQLite
  - DuckDB
  - or Redis (optional)
- Export metrics as JSON/NDJSON

---

## 5. Version 0.4.0 — UI Expansion

### Goals
- Gorgon Bell Web (Streamlit or Dash)
- Jupyter notebook widgets
- Interactive HTML dashboards
- CLI auto-refresh mode

---

## 6. Version 0.5.0 — Packaging & Distribution

### Goals
- Prepare package for PyPI
- Full installation guide
- API-reference documentation
- Release automation (GitHub Actions)

---

## 7. Version 1.0.0 — Stable Release Vision

### High-Level Goals
- All sensor types stable and modular
- Async infrastructure complete
- Stable storage backend
- MAI V1 operational
- CLI, Web and Notebook UI functioning
- Proper test suite & benchmarks
- Production-ready configuration system

---

## Long-Term Ideas (not version-bound)

- Distributed monitoring mode  
- Remote sensor orchestration  
- Device-level rhopalia (IoT integration)  
- Graph-based dependency visualization  
- Self-healing mode based on MAI insights  