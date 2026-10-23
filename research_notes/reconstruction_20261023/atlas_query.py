"""Search the recovered claim/tool atlas. Results are source leads, not proofs."""
import argparse
import json
from pathlib import Path


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query',nargs='+')
    parser.add_argument('--kind',choices=['claims','tools','packages'],default='claims')
    parser.add_argument('--limit',type=int,default=10)
    args=parser.parse_args()
    if args.limit<1:
        parser.error('limit must be positive')
    root=Path(__file__).resolve().parent/'atlas'
    if args.kind=='packages':
        records=json.loads((root/'packages.json').read_text())
    else:
        name='theorem_claims.jsonl' if args.kind=='claims' else 'tools.jsonl'
        records=(json.loads(line) for line in (root/name).open())
    words=[word.casefold() for word in args.query]
    selected=[]
    for row in records:
        text=json.dumps(row,ensure_ascii=False).casefold()
        if all(word in text for word in words):
            selected.append(row)
            if len(selected)>=args.limit:
                break
    print(json.dumps({'scope':'source leads; preserve original proof/admission status',
                      'returned':len(selected),'results':selected},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
