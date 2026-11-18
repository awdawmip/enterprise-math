"""Verify that only the 8,000 five-full-class optima attain the unrestricted minimum."""
from pathlib import Path
import argparse,json
from replay import verify
HERE=Path(__file__).resolve().parent
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--previous',type=Path,required=True);p.add_argument('--jobs',type=int,default=3)
    p.add_argument('--native',action='store_true')
    a=p.parse_args();old=json.loads((HERE/'tie_result.json').read_text())
    data=verify(a.previous,old['budget'],a.jobs,a.native,old['checked_budgets'])
    assert data==old
    print(json.dumps(data,sort_keys=True,indent=2))
