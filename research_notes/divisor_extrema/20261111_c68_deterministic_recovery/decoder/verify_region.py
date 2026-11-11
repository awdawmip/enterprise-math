"""Generate a complete first-divergence certificate at bounded five-stock."""
from argparse import ArgumentParser
from concurrent.futures import ProcessPoolExecutor
from math import comb
from pathlib import Path
import json
from stock_decoder import verify

def run(c):
 rows=[]
 for r in range(2,c-1):
  if c<=r+1+r//51:continue
  internal,exact,depth=verify(r,c)
  rows.append(dict(r=r,prefix_pairs_split=internal,terminal_pairs_compared=exact,deepest_split=depth))
 return dict(c=c,rows=rows)

if __name__=='__main__':
 ap=ArgumentParser(description=__doc__)
 ap.add_argument('--last-c',type=int,default=28)
 ap.add_argument('--jobs',type=int,default=2)
 ap.add_argument('--output',type=Path,required=True)
 args=ap.parse_args()
 with ProcessPoolExecutor(max_workers=args.jobs) as pool:rec=list(pool.map(run,range(3,args.last_c+1)))
 tot=lambda what:sum(row[what] for line in rec for row in line['rows'])
 report=dict(maximum_c=args.last_c,first_divergence_stocks=sum(len(line['rows']) for line in rec),
             prefix_pairs_split=tot('prefix_pairs_split'),terminal_pairs_compared=tot('terminal_pairs_compared'),
             largest_aligned_q=args.last_c-1,largest_aligned_family=comb(2*args.last_c-3,args.last_c-1),stocks=rec)
 args.output.write_text(json.dumps(report,indent=2)+'\n')
