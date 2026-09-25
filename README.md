# Engine-Coolant-Gauge
An interactive Graphical User Interface (GUI) engine coolant temperature gauge application built with Python and guizero. Implements data-driven state logic to dynamically update visual display tracking elements across variable operational bounds.
markdown# 🌡️ Captain Jack's Engine Coolant Gauge GUI (ITN160)

An event-driven Graphical User Interface (GUI) dashboard widget designed to simulate marine engine coolant temperature regulation monitoring. Built using the Python `guizero` desktop application framework.

---

## 🛠️ Technical Design & Engineering Highlights

*   **GUI Component Staging:** Integrates structural visual tracking widgets—including reactive input controls (`Slider`), single-cell programmatic status light arrays (`Waffle`), and dynamic message strings (`Text`).
*   **State-Driven Conditional Logic:** Employs an explicit numeric routing evaluation function (`update_temp`) to divide temperature vectors cleanly across 4 operational states:
    *   **Power Off (0°F):** Discharges warning arrays (`Black`).
    *   **Warming Up (1°F - 194°F):** Triggers standard ignition warmup tracking indicators (`Blue`).
    *   **Normal (195°F - 220°F):** Illuminates optimal baseline running arrays (`Green`).
    *   **Overheating (221°F - 300°F):** Signals high-risk engine thermal alerts (`Red`).
*   **Encapsulated Functional Context Scope:** Sets functional execution context pointers explicitly mapping layout element memory addresses onto the operational callback loop variables without mutating global memory pools.
*   **Asynchronous Event Refresh Loop:** Implements a localized loop interval tracker (`app.repeat`) ticking every 50 milliseconds to continuously scrape input values and refresh layout states asynchronously.

---

## 🚀 Deployment Instructions

### Prerequisites
*   Python 3.8+
*   The `guizero` user interface library interface:
    ```bash
    pip install guizero
    ```

### Execution Steps
1. Run the local script component:
   ```bash
   python gauge.py
   ```
2. Interact with the application slider manually to watch the graphical matrix upd
