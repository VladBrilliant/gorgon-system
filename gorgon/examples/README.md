# Gorgon System — Examples (First Prototypes)

This document provides **hands-on examples** of using Gorgon System  
for quick monitoring prototypes in scripts, notebooks, and ML / ETL workflows.

These examples focus on:

- simple, readable CPU/RAM monitoring
- full vertical pipeline usage (Rhopalia → Crabs → Octopus → Gorgon Bell)
- how to embed Gorgon into real code, not only demos

---

# 1. Running Built-In Demo Scripts

### 1.1 Prerequisites

From the project root:

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/macOS

pip install -e .
```

Now you can run the built-in examples.

---

## 1.2 Example 1 — Direct CrabGuardian (CPU + Memory)

File: `gorgon/examples/demo_cpu_mem.py`

Run:

```bash
python -m gorgon.examples.demo_cpu_mem
```

What happens:

- creates `RhopaliumCPU` and `RhopaliumMemory`;
- attaches them to a `CrabGuardian`;
- runs a short loop, printing CPU and RAM values.

Output looks like:

```text
Starting Gorgon demo (CPU + Memory)...

[1] CPU:  53.1%   MEM:  66.9%
[2] CPU:  14.3%   MEM:  67.0%
[3] CPU:  27.5%   MEM:  66.1%
...

Demo finished.
```

Use this when:

- you want the **simplest possible** monitoring prototype;
- you’re testing sensors and crab behavior;
- you debug your environment (psutil, permissions, etc.).

---

## 1.3 Example 2 — Octopus Hub + Crab

File: `gorgon/examples/demo_octopus_cpu_mem.py`

Run:

```bash
python -m gorgon.examples.demo_octopus_cpu_mem
```

This adds a **central hub**:

- a `CrabGuardian` still polls CPU/RAM;
- an `Octopus` instance collects and buffers snapshots;
- at the end, you see how many records were stored.

Typical output:

```text
Starting Gorgon demo with Octopus (CPU + Memory)...

[1] CPU:   1.9%   MEM:  65.8%
[2] CPU:   0.0%   MEM:  65.8%
[3] CPU:   3.7%   MEM:  65.8%
...

Demo finished.
Octopus buffered records: 5
```

Use this when:

- you want to experiment with **buffering** and **multi-crab** scenarios;
- you plan to add storage backends later (SQLite, DuckDB, etc.);
- you want a single place to read metrics from.

---

## 1.4 Example 3 — Full Vertical GorgonBellCLI

File: `gorgon/examples/demo_bell_cli.py`

Run:

```bash
python -m gorgon.examples.demo_bell_cli
```

This demonstrates **the full vertical path**:

```text
Rhopalia → Crabs → Octopus → Gorgon Bell (CLI)
```

Typical output:

```text
Starting GorgonBellCLI for crab 'local_system'...

[1] CPU:   2.1% (OK  )   MEM:  67.5% (OK  )
[2] CPU:  72.5% (WARN)   MEM:  67.5% (OK  )
[3] CPU:   2.1% (OK  )   MEM:  67.5% (OK  )
...

GorgonBellCLI session finished.
```

Use this when:

- you want to **see statuses (OK/WARN/CRIT)** in the console;
- you test threshold logic;
- you want a “stethoscope-style” view on your machine.

---

# 2. Using Gorgon in Your Own Script

Below is a minimal example of integrating Gorgon into real code.

### 2.1 Basic CPU/RAM monitor around a heavy function

```python
from time import sleep

from gorgon.rhopalia.cpu import RhopaliumCPU
from gorgon.rhopalia.memory import RhopaliumMemory
from gorgon.crabs.guardian import CrabGuardian
from gorgon.core.octopus import Octopus
from gorgon.bell.cli import GorgonBellCLI

def heavy_job():
    data = [x ** 2 for x in range(10_000_00)]
    sleep(2)
    return sum(data)

# 1) Sensors
sensors = [RhopaliumCPU(), RhopaliumMemory()]

# 2) Crab
crab = CrabGuardian(
    name="heavy_job_monitor",
    sensors=sensors,
    interval=1.0,
    buffer_size=20,
)

# 3) Octopus hub
octo = Octopus()
octo.register_crab(crab)

# 4) Bell
bell = GorgonBellCLI(
    octopus=octo,
    crab_name="heavy_job_monitor",
    cpu_warn=70.0,
    cpu_crit=90.0,
    mem_warn=80.0,
    mem_crit=95.0,
)

# 5) Run monitoring + job
print("Starting monitoring + heavy job...")
bell.run(iterations=5)   # simple synchronous loop
result = heavy_job()
print("Job result:", result)
```

You can adapt this pattern to:

- data loading code;  
- preprocessing pipelines;  
- model training;  
- ETL tasks;  
- file compression/decompression;  
- any CPU/RAM-intensive block.

---

# 3. Example — Around an ML Training Loop (Concept Sketch)

Below is a conceptual example for a future tutorial  
(you can adapt it to your ML framework):

```python
from gorgon.rhopalia.cpu import RhopaliumCPU
from gorgon.rhopalia.memory import RhopaliumMemory
from gorgon.crabs.guardian import CrabGuardian
from gorgon.core.octopus import Octopus
from gorgon.bell.cli import GorgonBellCLI

# Sensors for training
sensors = [RhopaliumCPU(), RhopaliumMemory()]

crab = CrabGuardian(
    name="training_resources",
    sensors=sensors,
    interval=2.0,
    buffer_size=50,
)

octo = Octopus()
octo.register_crab(crab)

bell = GorgonBellCLI(
    octopus=octo,
    crab_name="training_resources",
)

def train_model(model, loader, epochs=5):
    for epoch in range(epochs):
        for batch in loader:
            # your train step here
            # loss = model(batch)
            # loss.backward()
            # optimizer.step()
            pass

        # After each epoch, you may print a short monitoring snapshot:
        snapshot = octo.collect_once("training_resources")
        print(f"[epoch {epoch+1}] snapshot:", snapshot)

# later: integrate bell.run(...) or async monitoring loop
```

This pattern will later be extended into:

- proper Jupyter examples;  
- integration with specific ML frameworks;  
- MAI-based anomaly and bottleneck detection.

---

# 4. Next Steps

Planned additions to `docs/examples/`:

- `ml_training.md` — detailed ML monitoring tutorial;  
- `etl_pipeline.md` — ETL/ELT resource profiling;  
- `kubernetes_sidecar.md` — prototype for K8s integration;  
- `prometheus_bridge.md` — example of exporting metrics to Prometheus.

For now, this **Examples index** serves as the first entry point  
to see Gorgon System in action and start building your own prototypes.
