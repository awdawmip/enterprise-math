"""Compute the capacity-constrained optimum when at most one class exceeds size ten."""
from pathlib import Path
from functools import cache
import json,os,sys
P=Path(__file__).resolve().parent.parent
prior=Path(os.environ.get('NATIVE_PROBE_PREVIOUS',str(P/'previous')))
sys.path.insert(0,str(prior/'curve'))
from verify import MINIMA
@cache
def minimum(n,k,mx):
    if k==0:return 0 if n==0 else 10**9
    return min((MINIMA[s]+minimum(n-s,k-1,s)for s in range(1,min(mx,n)+1)),default=10**9)
print(json.dumps({s:MINIMA[s]+minimum(125-s,12,10)for s in (10,11,12,13)}))
