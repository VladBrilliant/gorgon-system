# Gorgon System

![Gorgon Placeholder Logo](https://via.placeholder.com/800x200?text=GORGON+SYSTEM)

**Gorgon System** is an experimental modular monitoring library inspired by biological architectures  
(jellyfish nervous system, octopus coordination, sensory rhopalia).  
It provides a lightweight, plug-and-play framework for collecting system metrics,  
monitoring ML workloads, and building adaptive observability tools.

This project is currently in early MVP stage — but already includes a full working vertical slice.

## 🧬 Core Architecture

Gorgon System is composed of four layers:

### 1. Rhopalia — Sensors
Small, atomic units that collect raw metrics.

Current sensors:
- RhopaliumCPU — CPU usage (%)
- RhopaliumMemory — RAM usage (%)

### 2. Crabs — Monitoring Units
A crab owns one or more sensors and polls them.

Current implementation:
- CrabGuardian
  - polls sensors
  - stores lightweight in-memory buffer
  - exposes .collect_once()
  - has an optional poll loop .run_forever()

### 3. Octopus — Central Hub
Responsibilities:
- register crabs
- poll all crabs
- store unified metric records
- provide .get_buffer() for analysis

### 4. Gorgon Bell — Analysis & Presentation Layer
Current implementation:
- GorgonBellCLI — prints human-readable status lines

## 🚀 MVP Vertical Slice

Rhopalia → CrabGuardian → Octopus → GorgonBellCLI

## 📦 Installation

```bash
pip install -e .
```

Use virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

## 🧪 Examples

```bash
python -m gorgon.examples.demo_bell_cli
```

## 📄 License

Apache License 2.0
