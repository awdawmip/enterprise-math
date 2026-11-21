"""Validate all three eleven-label optimum representatives with original program receipts."""
import argparse
import json
import sys
from pathlib import Path

def verify(previous):
    fifth=previous/'previous'
    fourth=fifth/'previous'
    third=fourth/'previous'
    sys.path.insert(0,str(third/'original'))
    from frontier9.native.replay_joint import run
    tables=json.loads((fourth/'eleven_six_counts/groups.json').read_text())
    tables.append(json.loads((fifth/'eleven_equal/groups.json').read_text()))
    results={}
    for name,rows in zip(('A','B','C'),tables):
        assert len(rows)==11 and sorted(sum(rows,[]))==list(range(125))
        ids=[0]*125
        for label,r in enumerate(rows):
            for x in r:
                ids[x]=label
        receipt=json.loads(json.dumps(run(ids,1)))
        assert receipt['joint']['total_queries']==11292
        results[name]=receipt
    return results

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',required=True,type=Path)
    print(json.dumps(verify(parser.parse_args().previous.resolve()),indent=2,sort_keys=True))
