"""Reconstruct the published evidence at every supplied stratum."""
from pathlib import Path
import json
from replay import check
root=Path(__file__).resolve().parent
for k,t in ((4,11364),(3,11291),(2,10985)):
    if (root/f'weights{k}.json').is_file():
        result=check(k,t)
        print(k,result['affine_types'],result['lower_bound'],result['total_nodes'],flush=True)
        reference=root/f'result{k}.json'
        if reference.exists():
            assert json.loads(reference.read_text())==result
