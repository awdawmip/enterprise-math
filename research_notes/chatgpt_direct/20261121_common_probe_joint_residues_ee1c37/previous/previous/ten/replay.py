"""Re-derive the exact feasibility threshold from the original common menus."""
import argparse
import json
import sys
from pathlib import Path

def verify(previous):
    original = previous/'previous/previous/previous/original'
    sys.path[:0]=[str(original/'next_repair/triple'),str(original)]
    from triple_verify import common_triples, no_ten
    edges=common_triples()
    assert len(edges)==47000
    result=no_ten(edges)
    assert result['size13_classes']==250 and result['size12_classes']==8875
    assert result['ten_messages_feasible'] is False
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--previous',type=Path,required=True)
    print(json.dumps(verify(p.parse_args().previous.resolve()),sort_keys=True,indent=2))
