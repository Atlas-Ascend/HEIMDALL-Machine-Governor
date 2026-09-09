# 02 — Problem

Coding agents increasingly write files, execute tests, call tools, access networks, and modify infrastructure. Their capability is improving faster than the governance layer around them.

A binary permission model is insufficient. Giving an agent shell access is not the same as authorizing a specific command for a specific objective inside a specific path with a specific risk budget. Human approval on every action destroys autonomy; unrestricted tool access destroys control.

HEIMDALL addresses the missing middle: a runtime governor that turns broad intent into bounded authority and makes authorization, execution, evidence, failure, repair, and promotion distinct states.

The demo problem is concrete: an agent is asked to repair a broken codebase. It should be allowed to inspect source, edit scoped files, install approved dependencies, and run tests. It should not be allowed to exfiltrate credentials, delete arbitrary machine paths, modify unrelated repositories, or deploy to production. Those differences must be enforced by software, not by prompt wording alone.
