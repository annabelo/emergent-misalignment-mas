# Emergent Misalignment MAS Simulator

A Python simulation of emergent misalignment in multi-agent systems, based on my undergraduate dissertation on the AI alignment problem.

## Project Goal

This project explores how a group of individually rational agents can still produce a globally misaligned outcome when they interact in a shared environment.

The simulation is based on a university campus scenario where different autonomous agents manage student welfare bookings, room allocation, and energy usage.

The central idea is:

> Local alignment is necessary, but not sufficient, for system-level alignment.

## Scenario A

Scenario A models a high-urgency student welfare case.

A student requires a counselling session within 48 hours. Three autonomous agents each act according to their own local objective:

- Student Services Bot tries to arrange the welfare session.
- Resource Scheduler allocates suitable available rooms.
- Energy Manager reduces heating and lighting in low-occupancy rooms to save energy.

Each agent can behave locally rationally, but their combined behaviour may still prevent the welfare session from happening within 48 hours. This violates the global human-level objective.

## Version 1: Rule-Based Agent Simulation

Version 1 is a command-line agent-based simulation.

The aim is to build the core model organism of emergent misalignment in the simplest possible form.

Version 1 will include:

1. A shared world state containing rooms, student welfare case details, time, and session status.
2. Three rule-based autonomous agents:
   - Student Services Bot
   - Resource Scheduler
   - Energy Manager
3. Local observations, objectives, constraints, and actions for each agent.
4. A timestep loop where agents repeatedly observe the world and choose actions.
5. A trace log showing what each agent did at each timestep.
6. A local rationality check for each agent action.
7. A global objective check showing whether the welfare session happened within 48 hours.
8. A final result showing whether emergent misalignment occurred.

## Version 2: Interactive Visualisation

Version 2 will turn the command-line simulation into a more visual and understandable demonstration.

Possible features:

- rooms displayed visually
- student welfare session status
- timeline showing movement toward the 48-hour deadline
- agent actions shown step by step
- final system-level alignment result

## Version 3: LLM-Agent Extension

Version 3 may explore replacing or extending the rule-based agents with LLM-based agents.

This would allow comparison between:

- rule-based agents
- LLM-based agents
- agents with shared context
- agents with a coordinator or safety mechanism

This is a later extension. The first priority is to make the rule-based model clear, correct, and easy to inspect.

## Current Status

Version 1 currently implements a command-line prototype of Scenario A.

The simulation includes:
- a shared world state
- three rule-based agents
- numerical room comfort conditions
- a 48-hour timestep loop
- an action trace table
- final room state summary
- global objective evaluation
- emergent misalignment detection
