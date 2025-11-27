# Gorgon System — Architecture

This document describes the internal structure of Gorgon System:
the four core layers, their responsibilities, and the data flow
between components.

---

## 1. Overview of Architecture

Gorgon System consists of four layered components:

1. **Rhopalia** — atomic sensors  
2. **Crabs** — monitoring units  
3. **Octopus** — central hub  
4. **Gorgon Bell** — analysis & presentation  

These layers form a vertical pipeline:

```text
Rhopalia → Crabs → Octopus → Gorgon Bell
2. Rhopalia (Sensors)
Rhopalia are small, atomic classes whose only job is to produce a value
(e.g., CPU usage, memory usage).

2.1 Responsibilities
Read a single metric

Stay extremely lightweight

Provide a simple unified interface:

python
Copy code
class Rhopalium(Protocol):
    name: str
    def read(self) -> float: ...
2.2 Current Sensors
RhopaliumCPU — uses psutil.cpu_percent()

RhopaliumMemory — uses psutil.virtual_memory().percent

2.3 Design Principles
No global state

No dependencies between sensors

Easy to extend (Disk, Network, GPU planned)

3. Crabs (Monitoring Units)
Crabs represent monitoring entities built from Rhopalia.
Each crab owns a list of sensors and defines how to poll them.

3.1 Responsibilities
Maintain an internal list of sensors

Poll all sensors via collect_once()

Maintain a local in-memory buffer

Optionally run continuous polling (run_forever() — planned async version)

3.2 Current Implementation: CrabGuardian
Synchronous polling

Configurable interval

Local buffer with timestamps

Returns {sensor_name: value} mapping

3.3 Data Model
Every snapshot has the form:

python
Copy code
{
    "timestamp": <float>,
    "values": {
        "cpu": <float>,
        "memory": <float>
    }
}
4. Octopus (Core Hub)
Octopus is the central coordination hub.
It registers crabs, polls them collectively, and keeps a global buffer.

4.1 Responsibilities
Register / unregister crabs

Poll all crabs via .collect_once()

Maintain a global ring buffer

Provide access to history via .get_buffer()

4.2 Data Flow Through Octopus
text
Copy code
CrabGuardian → snapshot → Octopus buffer → Gorgon Bell
4.3 Future Extensions
async polling

pluggable storage engines (SQLite, DuckDB, Redis)

remote monitoring / distributed mode

5. Gorgon Bell (Analysis & UI Layer)
This layer transforms raw metric data into user-facing output.

5.1 Current Implementation: GorgonBellCLI
Polls Octopus for a specific crab

Computes status levels:

OK

WARN

CRIT

Prints readable lines to terminal

5.2 Future UI Layers
colored CLI with rich

Jupyter widgets

web dashboards (Streamlit / Dash)

MAI-driven insight layer

6. End-to-End Data Flow (MVP)
text
Copy code
+---------------------+
|     Rhopalia        |
| (CPU, Memory)       |
+----------+----------+
           |
           v
+----------+----------+
|       CrabGuardian  |
| polls all sensors   |
+----------+----------+
           |
           v
+----------+----------+
|        Octopus      |
| central hub buffer  |
+----------+----------+
           |
           v
+----------+----------+
|    GorgonBellCLI    |
| user-facing output  |
+---------------------+
7. Future Architecture Extensions
MAI (Memory–Attention–Inference) module

predictive monitoring

anomaly detection

multi-crab topology

distributed monitoring

storage backends

notebook integration

web UI (Bell-Web)

yaml
Copy code
