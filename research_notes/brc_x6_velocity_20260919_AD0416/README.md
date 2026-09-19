# Six-axis heartbeat velocity research

Status: research candidate, not Foundation or Nollm production integration.

Run from an Enterprise Math checkout:

```sh
PYTHONPATH=src python research_notes/brc_x6_velocity_20260919_AD0416/verify_velocity.py
```

The original neighboring heartbeat source and existing BRC modules are reused, not replaced. `RESULTS.compact.json` contains the actual checked output; the verifier emits a semantically identical, pretty-printed `RESULTS.json`. The checkpoint records both byte forms appropriately. See `RESEARCH_NOTE.md` for complete scope, proofs, fine-step cost controls and observer limits. No network or hosted CI is required to run the checks.
