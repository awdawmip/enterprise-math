"""One local PFN claim-intent preparation through the existing canonical bootstrap.

Do not replay after the immutable execution record has been created.
This control helper performs no mathematical execution and publishes no event.
"""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
invocation = json.loads(HERE.joinpath("prepare-invocation.json").read_bytes())
root = Path(invocation["cwd"])
record = root.joinpath(invocation["record_path"])
if record.exists():
    raise SystemExit("REFUSE_REPLAY_EXISTING_IMMUTABLE_EXECUTION_RECORD")
sys.path.insert(0, str(root))
from control_plane import research_control_bootstrap

research_control_bootstrap.install(root)
from tools import research_execution_records

sys.argv = invocation["argv"][4:]
raise SystemExit(research_execution_records.main())
