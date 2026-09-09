# 12 — Failure Modes

1. **Model unavailable** — fail closed for new autonomous actions; preserve existing evidence.
2. **Policy engine exception** — deny action and emit governor error evidence.
3. **Sandbox timeout** — mark execution failed; route evidence to repair or operator review.
4. **Test failure** — never promote; generate REPAIR result.
5. **Missing proof** — verification returns REPAIR with explicit missing evidence.
6. **Out-of-scope filesystem target** — DENY.
7. **Credential-like command** — DENY.
8. **Unknown high-risk command** — REVIEW or DENY depending on configured mode.
9. **Receipt persistence failure** — completion remains unproven and not promotion eligible.
10. **Model/provider changes** — discover current models at runtime; pin the chosen NVIDIA model in submission proof.

Recovery must shrink uncertainty; it must not silently widen permissions.
