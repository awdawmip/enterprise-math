"""Run the shared-transform table on the inherited original five-cycle components."""
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from frontier9.native.replay_joint import run

if __name__=='__main__':
    table = list(map(int, (HERE/'common_12_certificate.txt').read_text().split()))
    result = run(table,1)
    assert sum(result['joint']['by_queries'].values()) == 31250
    print(json.dumps(result,indent=2,sort_keys=True))
