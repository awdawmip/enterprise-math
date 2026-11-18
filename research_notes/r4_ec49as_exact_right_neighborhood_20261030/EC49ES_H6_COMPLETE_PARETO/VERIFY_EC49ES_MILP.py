#!/usr/bin/env python3
"""Independent SciPy/HiGHS 0-1 MILP recheck of the exact M4,S4 and M5,S4 H=6 minimizers."""
import json
from VERIFY_EC49ER_M3_MILP import check
if __name__=='__main__':
 r=json.load(open('EC49ES_EXECUTED.json'))
 out={}
 for m in (4,5):
  choice={h:tuple(r['results'][str(m)]['best_p_h3_to_h6'][h-3]) for h in range(3,7)}
  result=check(choice)
  assert result['M']==m and result['E']==r['results'][str(m)]['min_E']
  out[str(m)]=result
 report={'unit':'EC49ES','status':'PASS','method':'independent SciPy/HiGHS 0-1 MILP model for each optimal-fiber representative; not all-case proof', 'optimal_fiber_checks':out}
 with open('EC49ES_MILP_EXECUTED.json','w') as f:json.dump(report,f,indent=2)
 print(json.dumps(report,indent=2))
