"""R262 exact minimum labelled zero-only certificate for four frozen cases.
Requires R260_labelled_modular_quotient.py in the same directory.
"""
import itertools,json
from pathlib import Path
from R260_labelled_modular_quotient import CASES,reconstruct,sequence

FORMULAS={'R257-p23':(42,17,17), 'R258-p23':(42,10,3), 'R258-p13':(9,5,7)}

def run():
 results=[]
 for name,s,p,J,T,K,P,zeros in CASES:
  c,q=reconstruct(s,J,T,K)
  if name in FORMULAS:
   m,base,r=FORMULAS[name]
   d=len(q[m]);cm=[v%p for v in c[m]]
   assert cm==[0]*(d-1)+[(-r)%p,1]
   assert [v%p for v in q[m]]==[base*pow(r,j,p)%p for j in range(d)]
   assert base%p and r%p
   values=sequence(c[m],q[m],p,P)
   assert all(v==base*pow(r,j,p)%p and v!=0 for j,v in enumerate(values))
   results.append({'case':name,'p':p,'period_used':P,'minimum_zero_only_labels':1,
                   'labels':[m],'geometric_base':base,'geometric_multiplier':r,
                   'nonzero_all_events_proved_by_monic_recurrence':True})
   print(name,'min=1 mask',m,'formula',base,r,flush=True)
  else:
   assert name=='R256-p13'
   # Prove full joint period via 249 shifted taps and the monic annihilator.
   all_rows=[sequence(cm,qm,p,249+P) for cm,qm in zip(c,q)]
   assert all(row[j]==row[j+P] for row in all_rows for j in range(249))
   bits=[]
   for row in all_rows:
    b=0
    for j,v in enumerate(row[:P]):
     if v:b|=1<<j
    bits.append(b)
   target=0
   for b in bits:target|=b
   found_zero=[j+3 for j in range(P) if not (target>>j)&1]
   assert found_zero==[1093,2185]
   candidate=[m for m,b in enumerate(bits) if b]
   assert len(candidate)==24
   selected=[9,10,13,26]
   assert set(selected).issubset(candidate)
   assert bits[selected[0]]|bits[selected[1]]|bits[selected[2]]|bits[selected[3]]==target
   total=0
   for combo in itertools.combinations(candidate,3):
    total+=1
    assert (bits[combo[0]]|bits[combo[1]]|bits[combo[2]])!=target
   assert total==2024
   results.append({'case':name,'p':p,'period':P,'minimum_zero_only_labels':4,
      'labels':selected,'common_zero_events_in_period':found_zero,
      'active_labels':len(candidate),'exhaustive_three_label_combinations_rejected':total,
      'all_label_periodicity_proved_by_249_shifted_taps':True})
   print(name,'min=4 masks',selected,'allzero',found_zero,'tested triples',total,flush=True)
 out={'schema':'EM_R262_ZERO_ONLY_OBSERVER_V1','frozen_science_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
      'model':'R256/R257/R258 auxiliary scalar','results':results}
 path=Path(__file__).with_name('R262_verification.json')
 path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print('PASS',path)

if __name__=='__main__':run()
