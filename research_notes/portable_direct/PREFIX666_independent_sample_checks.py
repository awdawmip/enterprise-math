#!/usr/bin/env python3
"""Independent exact BRC survivor-polynomial evaluator for PREFIX-666 sampled endpoints."""
from PREFIX666_experiment import build,eval_az,moments_at,Q,N
from fractions import Fraction as F
from PREFIX666_certificate import EPS,DELTA
from pathlib import Path
import json

def main():
    rows=build()
    results=[]
    for z in (Q-DELTA,Q,Q+DELTA):
        a,b,t=eval_az(rows,z)
        for p in (F(0), EPS/2, EPS):
            mu,mup,mupp,hpp,wpp=moments_at(rows,a,b,t,p)
            assert mu>86 and mupp>225 and hpp<15400 and wpp<-8000
            assert wpp==2*hpp-2*mup*mup-2*mu*mupp
            results.append({'p':str(p),'z':str(z),'mu':str(mu), 'mup':str(mup),
                            'mupp':str(mupp),'hpp':str(hpp),'wpp':str(wpp)})
    data={'type':'EXACT_FRACTION_SAMPLE_CROSSCHECK','points':len(results),
          'sampled_points':results,'caveat':'Samples are not the proof of the uniform inequalities; see coefficient certificate.'}
    with open('PREFIX666_sample_crosscheck.json','w') as f:json.dump(data,f,indent=2)
    print('ALL_SAMPLE_CHECKS_PASS',len(results))
    for x in results:
        print(x['p'],x['z'], float(F(x['wpp'])))
if __name__=='__main__': main()
