# Changelog

All notable changes to the **GORGON System** project will be documented in this file.

The format follows the recommendations of:
- **Keep a Changelog** — https://keepachangelog.com/en/1.1.0/
- **Semantic Versioning (SemVer)** — https://semver.org/

---

## [Unreleased]
Planned for future releases:
- AsyncCrabGuardian (async monitoring loop)
- Stethoscope Mode (short buffer + instant graphing)
- ETL Rhopalia family (timing, volume, quality)
- Octopus session/trace storage (SQLite / DuckDB)
- Jupyter integration (GorgonBell Notebook Mode)
- Gorgon CLI utilities (`gorgon quick`, `gorgon attach`, `gorgon bell`)
- MAI Engine 0.1 (Memory–Attention–Inference baseline)
- Design docs expansion (`architecture.md`, `design_philosophy.md`)
- Full sensor classification tree

---

## [0.0.1] – 2025-11-27
### Added
- **Core architecture vertical slice** (first working prototype):
  - *Rhopalia Sensors*:  
    - `RhopaliumCPU`  
    - `RhopaliumMemory`
  - *Crabs*:  
    - `CrabGuardian` – synchronous, multi-sensor monitoring agent
  - *Octopus Hub*:  
    - in-memory routing & record aggregation
  - *Gorgon Bell*:  
    - terminal-based `GorgonBellCLI` with OK/WARN/CRIT thresholds

- **Examples** under `gorgon/examples/`:
  - direct CPU/RAM monitoring
  - monitoring via Octopus hub
  - vertical demo using CLI

- **Repository structure**:
  - full package layout (`gorgon/…`)
  - minimal `pyproject.toml` (PEP 621 compatible)
  - `LICENSE` (Apache 2.0)
  - `NOTICE` (original architecture & naming rights)
  - `README` with logo and architecture overview

- **Documentation initialization**:
  - `/docs/MANUAL.md`
  - `/docs/ROADMAP.md`
  - `/docs/ARCHITECTURE.md` (placeholder)
  - project logo and branding elements

### Changed
- Repository reorganized into modular structure:
  - `rhopalia/`, `crabs/`, `core/`, `bell/`, `examples/`

### Notes
This version represents the first **MVP vertical slice**:
> *Rhopalia → Crabs → Octopus Hub → Gorgon Bell (CLI)*  
establishing the foundation for all upcoming features.

---

## [0.0.0] – 2025-11-26 (Internal Initialization)
### Added
- Initial repository created
- Base Git configuration + skeleton folders
- Early experimental notes (non-public)

