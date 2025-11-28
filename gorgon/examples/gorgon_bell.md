# Gorgon Bell — Analysis & Presentation Layer

The **Gorgon Bell** is the **analysis + visualization tier** of the Gorgon System.  
It is responsible for turning raw snapshots into **signals, alerts, dashboards,  
interpretations, insights**, and future MAI-driven intelligence.

The Bell consists of **two sub-layers**:

```
Gorgon Bell
├── Subumbrella (inner analytic layer)
└── Exumbrella (outer UI/visual layer)
```

This structure is inspired by the anatomy of a real medusa  
and reflects the separation between cognition (analysis) and sensation (presentation).

---

# 1. Bell Architecture Overview

```
Rhopalia → Crabs → Octopus → Gorgon Bell → MAI
                    ▲
                    │
              (all data flows here)
```

The Bell reads **ONLY** from Octopus Hub, never directly from Crabs or sensors.

It provides:

- **status classification**
- **threshold-based warnings**
- **visual representation**
- **pre-MAI analysis**
- **CLI output** (current)
- web dashboards (planned)
- notebook widgets (planned)

---

# 2. Subumbrella — Analytic Core

Subumbrella is the **inner logic layer** of the Bell.  
Its responsibilities include:

### ✔ Snapshot interpretation  
Compute statuses such as:

- OK  
- WARN  
- CRIT  
- FUTURE: “PREDICTED CRIT”, “ANOMALY”, “PATTERN SHIFT”

### ✔ Threshold evaluation  
Current implementation:  
simple CPU/RAM heuristics.

Future versions will include:

- statistical baseline  
- rolling windows  
- outlier detection  
- MAI Engine integration  

### ✔ Status propagation  
Subumbrella produces a **unified structured state**:

```python
{
    "cpu": {"value": 34.1, "status": "OK"},
    "memory": {"value": 67.2, "status": "WARN"},
}
```

### ✔ Severity computation  
Multi-sensor rule aggregation:

```
if any status == CRIT → overall CRIT
elif any status == WARN → overall WARN
else → OK
```

---

# 3. Exumbrella — Presentation Layer

Exumbrella is the **outer visible shell** of the Bell.

It handles:

### ✔ CLI output (current)  
Simple, readable lines:

```
[1] CPU: 23.1% (OK  )   MEM: 67.4% (WARN)
```

### ✔ Visualization (planned)  
- real-time terminal dashboards  
- panels with sparklines  
- block charts  
- multi-crab overviews  

### ✔ Web UI (planned)  
Interactive dashboards using:

- Streamlit  
- Dash  
- FastAPI realtime events  
- Websocket Bell  

### ✔ Notebook UI (planned)  
- live charts  
- sliding window graphs  
- hoverable points  
- auto-updating metric cells  

---

# 4. Current Implementation: `GorgonBellCLI`

MVP Bell implemented:

```python
class GorgonBellCLI:
    def run(self, iterations=10, interval=None): ...
```

### Responsibilities:

- pull latest snapshot from Octopus  
- pass snapshot to Subumbrella  
- print formatted output via Exumbrella  
- classify values (OK/WARN/CRIT)

### Status thresholds:

| Metric | WARN | CRIT |
|--------|------|------|
| CPU | ≥ 70% | ≥ 90% |
| RAM | ≥ 80% | ≥ 95% |

(Values configurable by user.)

---

# 5. Example — Full Vertical Integration

```python
from gorgon.rhopalia.cpu import RhopaliumCPU
from gorgon.rhopalia.memory import RhopaliumMemory
from gorgon.crabs.guardian import CrabGuardian
from gorgon.core.octopus import Octopus
from gorgon.bell.cli import GorgonBellCLI

# Sensors
sensors = [RhopaliumCPU(), RhopaliumMemory()]

# Crab
crab = CrabGuardian(
    name="local_system",
    sensors=sensors,
    interval=2.0,
)

# Hub
octo = Octopus()
octo.register_crab(crab)

# Bell
bell = GorgonBellCLI(
    octopus=octo,
    crab_name="local_system",
    cpu_warn=70.0,
    cpu_crit=90.0,
    mem_warn=80.0,
    mem_crit=95.0,
)

bell.run(iterations=5)
```

---

# 6. Data Flow Through Both Umbrellas

### 6.1 Subumbrella workflow:

```
snapshot → threshold logic → per-sensor status → overall status
```

### 6.2 Exumbrella workflow:

```
structured status → chosen UI → final rendered output
```

### Combined:

```
Crab snapshot
    ↓
Octopus buffer
    ↓
Subumbrella (analysis)
    ↓
Exumbrella (visualization)
    ↓
User sees OK/WARN/CRIT or dashboards
```

---

# 7. Future Extensions of Gorgon Bell

### 7.1 Subumbrella Extensions

- MAI Engine integration  
- pattern memory  
- adaptive thresholds  
- anomaly windows  
- predictive alerts  
- cross-sensor correlation  
- time-derived metrics (deltas, derivatives)

### 7.2 Exumbrella Extensions

- terminal dashboards  
- notebook widgets  
- web dashboards  
- mobile-friendly views  
- alarms / notifications (Slack, email)

---

# 8. Format and Data Model

### Bell reads:

- snapshots (dict)
- history windows
- global status
- per-sensor breakdown

### Bell outputs:

- status objects
- formatted strings
- UI instructions (future)
- event structures (for MAI)

---

# 9. Why Two Umbrellas?

The 2-layer Bell is a unique invention in the Gorgon architecture.

### ✔ Subumbrella = *thinking*  
- logic  
- rules  
- analysis  
- insight  

### ✔ Exumbrella = *speaking*  
- UI  
- presentation  
- dashboards  

This separation enables:

- multiple UIs on same logic  
- multiple logic engines on same UI  
- easy replacement of both layers independently  

Other monitoring systems (Prometheus, OTel) mix these responsibilities.  
Gorgon System follows a **neuro-biological model**.

---

# 10. Best Practices

### ✔ Always use Octopus as the data source  
Bell should never talk directly to Crabs.

### ✔ Keep thresholds explicit  
Transparent > magical.

### ✔ Subumbrella should stay stateless (for now)  
State belongs in MAI or Octopus.

### ✔ Exumbrella should be portable  
CLI, web, notebook — all with minimal dependencies.

### ✔ Maintain separation  
Don’t mix UI code with analysis logic.

---

# 11. Roadmap for Gorgon Bell

| Version | Feature |
|---------|---------|
| **0.1.x** | GorgonBellCLI polishing |
| **0.2.x** | Subumbrella refactor + async support |
| **0.3.x** | Web Bell prototype |
| **0.4.x** | Notebook Bell (Jupyter widget) |
| **0.5.x** | Multi-crab dashboards |
| **0.6.x** | Alerting channels (Slack/email) |
| **1.0.0** | Production-ready dashboards + MAI integration |

---

# 12. Summary

The Gorgon Bell is the **voice and mind** of the system.

- **Subumbrella**: analysis, thresholds, logic  
- **Exumbrella**: visualization, UI, dashboards  

Together they transform raw machine data into:

- signals  
- warnings  
- insights  
- predictions  

Gorgon Bell completes the vertically integrated design:

```
Rhopalia → Crabs → Octopus → Gorgon Bell → MAI
```

This document will expand as more Bell layers are implemented.
