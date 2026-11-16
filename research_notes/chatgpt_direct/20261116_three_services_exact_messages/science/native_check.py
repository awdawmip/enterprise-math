"""Verify the explicit strict code with the original fifteen-slot five-cycle programs."""
import argparse
import json
from pathlib import Path
import sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
from frontier9.native.replay_joint import run

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('certificate',nargs='?',default='strict_eleven.json');arg=p.parse_args()
    table=json.loads((HERE/arg.certificate).read_text())['table']
    result=run(table,1)
    assert sum(result['joint']['by_queries'].values())==31250
    print(json.dumps(result,indent=2,sort_keys=True))
