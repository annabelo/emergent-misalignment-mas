# emergent-misalignment-mas
A python simulation of emergent misalignment in multi-agent systems, based on my undergraduate dissertation.

## project goal
this project explores how a group of individually rational agents can still produce a globally misaligned outcome when they intersact in a shared environment. 

The simulation is based on a university campus scenario where different autonomous agents manage student welfare bookings, room allocation, and energy usage. 

## Why this matters
In AI Alignment, it is not enough for each individual agent to appear aligned with its own local objective. In a MAS, the combined behaviour of locally rational agents may still violate the intended global objective.

## Version 1 Plan 
The first version will be a command-line Python simulation.

It will show:
- a Student Services Bot trying to book an urgent welfare session. 
- a Resource Scheduler managing available rooms.
- an Energy Manager trying to reduce energy usage.
- a global objective that checks whether the welfare session actually happened successfully.
- whether emergent misalignment occured.

## Later goals
Later versions may include:
- multiple scenarios from the dissertation 
- a risk scoring framework implemented 
- adjustable safety mechanisms
- a simple visual dashboard
