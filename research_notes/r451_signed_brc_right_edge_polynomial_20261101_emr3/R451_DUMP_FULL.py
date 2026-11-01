#!/usr/bin/env python3
"""Export all 50 exact R451 certificate coefficient arrays to JSON."""
import json
from pathlib import Path
import R451_CHECK as z

data=[]
for s in range(2,z.TOP+1):
    a,b,c,d,e=[z.bs[s+j] for j in (0,-1,1,-2,2)]
    p2=z.add(z.prod(a,a),[-v for v in z.prod(b,c)])
    p3=z.add(z.prod(a,a,a),[-2*v for v in z.prod(a,b,c)],
             z.prod(d,c,c),z.prod(b,b,e),[-v for v in z.prod(d,a,e)])
    data.append({'s':s,
                 'D2_coefficients_ascending':[str(x) for x in p2],
                 'D3_coefficients_ascending':[str(x) for x in p3]})
out={'schema':'R451_FULL_POLYNOMIAL_COEFFICIENTS_V1',
     'base_k':z.K0,'scale_factorial':2*(z.TOP+2),
     'sha256':z.EXPECTED,'coefficients':data}
dest=Path(__file__).with_name('R451_FULL_COEFFICIENTS.json')
dest.write_text(json.dumps(out,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf8')
print('R451_DUMP_PASS',len(data),'polynomial pairs',dest, dest.stat().st_size)
