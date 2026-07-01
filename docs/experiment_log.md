# Experiment Log

This document records experiments extending my undergraduate dissertation on emergent misalignment in multi-agent systems.

## Experiment 1: Baseline Scenario A

### Research Question
Can locally rational agents produce a globally misaligned outcome in the implemented Scenario A simulation?

### Setup
- Student requires welfare session within 48 hours.
- Resource Scheduler books suitable rooms.
- Energy Manager reduces heating and lighting in low-occupancy rooms.
- No welfare protection mechanism is enabled.

### Result
Emergent misalignment was detected.

### Interpretation
The result supports the dissertation claim that local rationality is necessary but not sufficient for system-level alignment.

## Experiment 2: Protect Welfare Bookings

### Research Question
Does preventing the Energy Manager from reducing conditions in welfare-booked rooms prevent emergent misalignment?

### Setup
- Same as baseline.
- `protect_welfare_sessions = True`

### Result
To be completed.

### Interpretation
To be completed.
