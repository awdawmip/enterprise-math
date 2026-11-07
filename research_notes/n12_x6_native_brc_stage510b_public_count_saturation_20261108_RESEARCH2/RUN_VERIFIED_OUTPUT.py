"""Emit the exact archived Stage510-B JSON schema from the published checker.

Run next to REPRO_STAGE510B.py:
    python RUN_VERIFIED_OUTPUT.py > reproduced.json
Compare with STAGE510B_EXECUTED.json. The wrapper only canonicalizes the
internal frozen-science key name; all numerical checks run in the imported source.
"""
import json
from REPRO_STAGE510B import run

record = run()
record["frozen_science"]["global"] = record["frozen_science"].pop("global_")
print(json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True))
