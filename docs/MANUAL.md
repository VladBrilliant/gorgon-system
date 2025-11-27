# Gorgon System — Manual

This document describes how to install, configure and use Gorgon System
in typical workflows (local monitoring, ML training, notebooks, CLI usage).

---

## 1. Installation

### 1.1 Requirements

- Python 3.10+
- `psutil`
- Recommended: virtual environment

### 1.2 Setup (development mode)

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
2. Core Concepts
Gorgon System consists of four conceptual layers:

Rhopalia — atomic sensors

Crabs — monitoring units

Octopus — central hub

Gorgon Bell — analysis & UI layer

For deeper architectural details, see:
docs/ARCHITECTURE.md

3. Quick Start
3.1 Run CLI demo (full vertical slice)
bash
Copy code
python -m gorgon.examples.demo_bell_cli
You should see several lines with CPU and Memory values and status levels (OK / WARN / CRIT).

3.2 Run Octopus demo
bash
Copy code
python -m gorgon.examples.demo_octopus_cpu_mem
3.3 Run simple CrabGuardian demo
bash
Copy code
python -m gorgon.examples.demo_cpu_mem
4. Using Gorgon System in ML / Data workflows
Minimal integration example:

python
Copy code
from gorgon.rhopalia.cpu import RhopaliumCPU
from gorgon.rhopalia.memory import RhopaliumMemory
from gorgon.crabs.guardian import CrabGuardian
from gorgon.core.octopus import Octopus
from gorgon.bell.cli import GorgonBellCLI

# Create sensors
sensors = [RhopaliumCPU(), RhopaliumMemory()]

# Create monitoring unit (crab)
crab = CrabGuardian(
    name="training_resources",
    sensors=sensors,
    interval=2.0,
)

# Create hub and register crab
octo = Octopus()
octo.register_crab(crab)

# Attach CLI bell
bell = GorgonBellCLI(octopus=octo, crab_name="training_resources")
bell.run(iterations=5)
5. Configuration Options (current + planned)
5.1 CrabGuardian
interval — polling frequency

buffer_size — how many snapshots to store

sensors=[] — attached Rhopalia

5.2 GorgonBellCLI
cpu_warn, cpu_crit thresholds

mem_warn, mem_crit thresholds

iterations — number of cycles

interval override

5.3 Octopus
buffer_size — max global records

6. Advanced Usage (planned features)
These features are part of the planned roadmap:

async monitoring (async crabs & async hub)

multiple crabs and multi-component topologies

exporting monitoring data (JSON / NDJSON / DB)

GorgonBell web dashboards (Streamlit / Dash)

Jupyter notebook widgets

MAI (Memory–Attention–Inference) module

anomaly detection and resource prediction