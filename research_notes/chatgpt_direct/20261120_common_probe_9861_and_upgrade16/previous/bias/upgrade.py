"""Price both orientations of the known twelve-label table on native menus."""
import argparse
import json
import sys
from pathlib import Path

def verify(previous):
    second=previous/'previous/previous/previous/previous'
    sys.path.insert(0,str(second/'bounds'))
    from cyclic11 import class_cost, observations
    _,menus=observations()
    blocks=[[[v&((1<<125)-1) for v in r] for r in menus],[[v>>125 for v in r] for r in menus]]
    original=json.loads((previous/'previous/c3/groups.json').read_text())
    def double(x):
        return 25*(2*(x//25)%5)+5*(2*(x//5%5)%5)+2*(x%5)%5
    pair=[[sum(class_cost(r,m) for r in t) for m in blocks] for t in [original,[[double(x) for x in r]for r in original]]]
    assert {tuple(x)for x in pair}=={(4915,5081),(5081,4915)}
    return {'incumbent_orientations':pair, 'difference_probability_lower_numerator':[648,29],'denominator':15625}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',type=Path,required=True)
    print(json.dumps(verify(parser.parse_args().previous.resolve()),sort_keys=True,indent=2))
