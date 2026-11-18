"""Run one declared recovery policy on an actual U27F-03 interrupted snapshot."""
import argparse
import json
from pathlib import Path

from priority_check import authority, resume


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('snapshot', type=Path)
    parser.add_argument('--route', required=True, choices=['reverse', 'forward'])
    parser.add_argument('--grow-port', type=int, choices=range(4, 12),
                        help='durable command at a FREE_NATIVE_HOP stop without a label')
    args = parser.parse_args()
    raw = json.loads(args.snapshot.read_bytes())
    stop = raw.get('data', raw)
    if args.grow_port is not None:
        stop = authority(stop,args.grow_port)
    print(json.dumps(resume(stop,args.route), indent=2))


if __name__ == '__main__':
    main()
