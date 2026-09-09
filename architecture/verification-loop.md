# Verification Loop

```text
EXECUTE -> COLLECT -> ASSERT
                    |
             +------+------+
             |             |
            PASS          FAIL
             |             |
          RECEIPT        REPAIR
             |             |
          PROMOTE     DELTA PLAN
                           |
                    REAUTHORIZE
```

A repair cycle receives failed assertions and current evidence. It can propose a delta but cannot mutate the original authorization envelope. If new permissions are genuinely required, the run stops for explicit contract revision.

This keeps self-repair bounded and auditable.
