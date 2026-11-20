"""Check the minimizing translation table against the original three-service program."""
import argparse
import json
import sys
from pathlib import Path

def verify(original):
    sys.path.insert(0, str(original))
    from frontier9.native.replay_joint import run
    rows = json.loads(Path(__file__).with_name('groups4.json').read_text())
    assert len(rows) == 12 and sorted(sum(rows, [])) == list(range(125))
    labels = [None] * 125
    for index, row in enumerate(rows):
        for point in row:
            labels[point] = index
    receipt = json.loads(json.dumps(run(labels, 1)))
    assert receipt['joint']['by_queries'] == {'0': 20120, '1': 11130}
    return receipt

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--original', type=Path, required=True)
    print(json.dumps(verify(parser.parse_args().original.resolve()), sort_keys=True, indent=2))
