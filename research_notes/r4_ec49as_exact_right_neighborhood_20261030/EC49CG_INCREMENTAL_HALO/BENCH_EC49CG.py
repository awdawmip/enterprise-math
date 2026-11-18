"""Cold-process benchmark: one predeclared future cone versus three independent cones."""
import json,sys,time
from pathlib import Path
from VERIFY_EC49CG import multi, fixed
m=sys.argv[1]
t0=time.perf_counter()
if m=='multi':
    data=multi(14,2)
elif m=='fixed':
    data=[fixed(n) for n in (14,16,18)]
else:raise SystemExit('mode must be multi or fixed')
print(json.dumps({'mode':m,'wall_seconds_internal':round(time.perf_counter()-t0,6),
                  'data':data},sort_keys=True))
