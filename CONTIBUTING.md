# Contributing to Gorgon System

Thank you for your interest in **Gorgon System**.

This project is both a personal research environment and a real monitoring framework.
Contributions are welcome as long as they respect the original architectural vision:

**Rhopalia → Crabs → Octopus Hub → Gorgon Bell → MAI Engine**

Please read the guidelines below before submitting changes.

---

# 🧱 General Principles

- Keep the codebase **clean, readable and modular**.
- Maintain compatibility with the **bio-inspired architecture**.
- New features must **extend**, not replace, existing concepts.
- Small, atomic changes are preferred over large “god-commits”.
- Architectural names (**Rhopalia, Crabs, Octopus, Bell, MAI**) must not be renamed.

---

# 🔀 Workflow: How to Propose Changes

### 1. Fork the repository

```bash
git clone https://github.com/VladBrilliant/gorgon-system
git checkout -b feature/my-new-feature
2. Make your changes in small commits
Use clear commit messages:

makefile
Copy code
feat: add disk I/O rhopalium
fix: correct octopus buffer logic
docs: update sensors guide
3. Ensure the project installs correctly
bash
Copy code
pip install -e .
4. Run tests (when the test suite is added)
bash
Copy code
pytest
5. Submit a Pull Request
Include:

short summary in the title

detailed explanation of the change

screenshots / logs if UI or CLI changed

references to issues (if any)

📝 Code Style
Python 3.10+

Follow PEP 8 (formatting)

Follow PEP 484 (type hints)

Use docstrings for all public classes and methods

Keep functions logically small and focused

Keep imports clean and grouped

Every file must start with the official project header:
python
Copy code
"""
GORGON System — https://github.com/VladBrilliant/gorgon-system
© 2025 Vladimir Brilliantov

Creator of the GORGON System architecture:
Rhopalia Sensors, Crabs Monitoring Agents, Octopus Hub,
Gorgon Bell, MAI Engine.

All concepts, terminology, and architectural patterns introduced in this project
originated with the author.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
"""
🧪 Tests
New features should be accompanied by tests inside tests/.

Test types to include:

Normal behaviour

Edge cases

Failure modes (if applicable)

Integration tests (Crab ↔ Octopus, Rhopalia ↔ Crab)

📚 Documentation Requirements
When changing or adding behaviour, update the corresponding documentation:

docs/sensors.md — new Rhopalia

docs/crabs.md — changes to Crab logic

docs/octopus.md — hub behaviour, routing, storage

docs/gorgon_bell.md — CLI / Jupyter modes

docs/mai_engine.md — intelligence layer

Also update:

CHANGELOG.md (top-level version entry)

Examples under docs/examples/ if relevant

🐙 Respecting the Architecture
Gorgon System is not a typical monitoring library.
It is a bio-inspired layered architecture with original terminology and behaviour.

Please:

do not rename core components

do not collapse layers

do not introduce terms that contradict the established naming model

keep new features aligned with the metaphors (Rhopalia, Crabs, Octopus, Bell, MAI)

If you propose a structural change — open a discussion first.

🧭 Branch Naming Convention
Use one of:

bash
Copy code
feature/my-feature
fix/bug-description
docs/update-manual
refactor/crabs-buffer
test/add-octopus-tests
🗂 Issue Guidelines
When opening an issue:

describe the problem clearly

include environment details

provide reproduction steps (if possible)

attach logs, screenshots or short code samples

specify the component (Rhopalia, Crab, Octopus, Bell, MAI)

🤝 Thank You
By contributing, you help Gorgon System evolve into a powerful diagnostic and monitoring framework.

Attach a Crab. Listen. Diagnose.
GORGON System 🐙