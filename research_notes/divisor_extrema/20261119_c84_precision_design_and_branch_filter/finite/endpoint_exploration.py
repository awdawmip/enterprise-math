"""Exploratory check of the proved a->1/2 overlap expansion."""
from pathlib import Path
import json
import mpmath as mp
from one_dimensional import correction
mp.mp.dps=60
rows=[]
for power in [2,3,4,5,6]:
    e=mp.mpf(10)**(-power)
    value=correction((1-e)/2)/e**4
    leading=3/(4*mp.pi**2)*mp.log(1/e)+25/(16*mp.pi**2)+64/(105*mp.pi**2)*mp.sqrt(e)
    row={'epsilon':str(e),'correction_over_epsilon_fourth':str(value),'three_term_prediction':str(leading),'residual_over_epsilon_log':str((value-leading)/(e*mp.log(1/e)))}
    rows.append(row)
    print(row,flush=True)
Path(__file__).with_name('endpoint_values.json').write_text(json.dumps({'scope':'Exploratory high precision evaluation; the asymptotic proof is analytic, not inferred from these values.','working_decimal_digits':60,'rows':rows},indent=2)+'\n')
