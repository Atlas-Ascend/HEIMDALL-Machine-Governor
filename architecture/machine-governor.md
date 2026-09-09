# Machine Governor

HEIMDALL's governor is the authority boundary. It owns contract issuance, policy evaluation, and the transition into verification.

The governor never executes raw model output. A model may propose a plan or tool call, but the runtime converts that proposal into a typed `ActionRequest`. The request is evaluated against the immutable execution contract and current policy set. Only an ALLOW decision may be handed to an executor adapter.

This separation enables provider-independent governance: Nemotron can be replaced or upgraded without changing the core authority semantics.
