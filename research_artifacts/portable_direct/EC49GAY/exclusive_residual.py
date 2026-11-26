"""Exact surplus of joint Hall deficiency beyond bank-exclusive deficits."""
import json
from collections import Counter
from peel_hall import cut_reference


def main():
    hist=Counter();by_threshold=Counter();witness={};checks=0
    for r in json.load(open('witness_records.json')):
        opts={int(t):m for t,m in r['opts'].items()};n=len(opts);caps=r['caps'];q=len(caps)//2
        m=(1<<q)-1;u={};v={};x=0;z=0
        for t,w in opts.items():
            a=w&m;b=w>>q
            if a and b:x+=1
            elif a:u[t]=a
            elif b:v[t]=b
            else:z+=1
        ub=cut_reference(u,caps[:q])+cut_reference(v,caps[q:])+x
        h=cut_reference(opts,caps);j=ub-h
        assert j>=0 and (ub<=r['L'])==r['ans'] and (h<=r['L'])==r['ans']
        hist[j]+=1;by_threshold[j,r['ans']]+=1
        if j not in witness:witness[j]={'opts':r['opts'],'caps':caps,'L':r['L'],'z':z,'u':len(u),'v':len(v),'x':x,'H':h,'B':ub}
        checks+=1
    print(json.dumps({'checks':checks,'surplus':dict(hist),'surplus_by_threshold':[[j,a,c] for (j,a),c in sorted(by_threshold.items())],'first_witness':witness},sort_keys=True))
if __name__=='__main__':main()
