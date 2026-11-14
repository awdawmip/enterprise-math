#!/usr/bin/env python3
"""EC49FOM exact one-hot Möbius kernel (integer arithmetic).

Usage:
 python VERIFY_EC49FOM_MOBIUS.py native_profiles.csv original_edges.txt \
    EC49FOL_CANCELLATION_84.csv EC49FOM_MOBIUS_84.csv

The native_profiles.csv is independently exported from the frozen signed-prefix
words by VERIFY_EC49FOM_EXTRACT.cpp; the FOL census is only a cross-check.
"""
import csv,collections,itertools,sys,json
from pathlib import Path
ROOTS=(3,5,6,7)
def load_profiles(path):
    data={}
    for row in csv.DictReader(open(path)):
        k=int(row["config"]);r=int(row["root"])
        must=int(row["must"]);opt=int(row["opt"]);sub=int(row["subset"]);cost=int(row["cost"])
        v=data.setdefault(k,{}).setdefault(r,{"must":must,"opt":opt,"cost":{}})
        assert (v["must"],v["opt"])==(must,opt)
        assert sub&~opt==0 and sub not in v["cost"]
        v["cost"][sub]=cost
    for k,p in data.items():
        assert set(p)==set(ROOTS)
        for r,d in p.items():assert len(d["cost"])==1<<d["opt"].bit_count()
    return data
def domain(p):
    d={}
    for l in range(24):
        d[l]=tuple(r for r in ROOTS if (p[r]["opt"]|p[r]["must"])>>l&1)
        assert d[l]
    return d
def evaluate(a,b,choice):
    total=0
    for r in ROOTS:
        chosen=sum(1<<l for l in range(24) if choice[l]==r and a[r]["opt"]>>l&1)
        total+=b[r]["cost"][chosen]-a[r]["cost"][chosen]
    return total
def polynomial(a,b,dom):
    baseline={l:min(dom[l]) for l in range(24)}
    coeff=collections.defaultdict(int)
    raw_nz=0
    for r in ROOTS:
        x=a[r];assert (x["must"],x["opt"])==(b[r]["must"],b[r]["opt"])
        labels=[l for l in range(24) if x["opt"]>>l&1]
        vals=[0]*(1<<len(labels))
        for subset in range(len(vals)):
            mask=sum(1<<l for j,l in enumerate(labels) if subset>>j&1)
            vals[subset]=b[r]["cost"][mask]-x["cost"][mask]
        for j in range(len(labels)):
            for subset in range(len(vals)):
                if subset>>j&1:vals[subset]-=vals[subset^(1<<j)]
        for subset,c in enumerate(vals):
            if not c:continue
            raw_nz+=1
            terms={():c}
            for j,l in enumerate(labels):
                if not subset>>j&1:continue
                after=collections.defaultdict(int)
                for mon,v in terms.items():
                    if baseline[l]==r:
                        after[mon]+=v
                        for other in dom[l]:
                            if other!=r:after[mon+((l,other),)]-=v
                    else:
                        after[mon+((l,r),)]+=v
                terms=after
            for mon,v in terms.items():coeff[mon]+=v
    coeff={k:v for k,v in coeff.items() if v}
    return coeff,baseline,raw_nz
def main(profiles,edges,reference,out):
    p=load_profiles(profiles)
    old={(int(x["src"]),int(x["dst"])):x for x in csv.DictReader(open(reference))}
    inventory=[tuple(map(int,s.split())) for s in open(edges) if s.strip()]
    assert len(inventory)==84 and len(p)==51 and len(old)==84
    rows=[];summ=collections.Counter()
    for src,dst in inventory:
        a=p[src];b=p[dst];dom=domain(a)
        if dom!=domain(b):
            rows.append(dict(src=src,dst=dst,same_domain=0,polynomial_terms="NA",lowest_degree="NA",highest_degree="NA",raw_mobius_nonzero="NA",constant_delta="NA",shortest_witness="NA",witness_delta="NA",degree_hist="NA"))
            summ["domain_change"]+=1;continue
        coeff,baseline,raw_nz=polynomial(a,b,dom)
        degrees=collections.Counter(map(len,coeff))
        if coeff:
            d=min(degrees);h=max(degrees)
            witness=min((m for m in coeff if len(m)==d))
            choice=dict(baseline);choice.update(dict(witness))
            assert evaluate(a,b,choice)==coeff[witness]!=0
        else:
            d=h=-1;witness=()
        # Verify the exact normalized one-hot polynomial on all 648 named assignments.
        count=0
        for tup in itertools.product(*(dom[l] for l in range(24))):
            choice=dict(enumerate(tup))
            chosen={(l,r) for l,r in choice.items() if baseline[l]!=r}
            symbolic=sum(c for mon,c in coeff.items() if set(mon)<=chosen)
            assert symbolic==evaluate(a,b,choice)
            count+=1
        assert count==648
        assert (not coeff)==(int(old[(src,dst)]["changed_total"])==0)
        summ["shared"]+=1;summ["identical" if not coeff else "changed"]+=1
        if coeff:summ[("degree",d)]+=1;summ["terms"]+=len(coeff)
        rows.append(dict(src=src,dst=dst,same_domain=1,polynomial_terms=len(coeff),lowest_degree=d,highest_degree=h,raw_mobius_nonzero=raw_nz,constant_delta=coeff.get((),0),shortest_witness=";".join(f"{l}:{r}" for l,r in witness) if witness else ("BASE" if coeff else "NA"),witness_delta=coeff.get(witness,0) if coeff else 0,degree_hist=";".join(f"{k}:{v}" for k,v in sorted(degrees.items()))))
    assert (summ["shared"],summ["identical"],summ["changed"],summ["domain_change"],summ["terms"])==(82,32,50,2,2773)
    with open(out,"w",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]))
        writer.writeheader();writer.writerows(rows)
    triple=[r for r in rows if r["src"]==32315 and r["dst"]==32303]
    assert len(triple)==1 and triple[0]["polynomial_terms"]==1
    assert triple[0]["lowest_degree"]==3 and triple[0]["shortest_witness"]=="13:7;17:7;21:7" and triple[0]["witness_delta"]==-1
    print("EC49FOM_EXACT_PASS",dict(summ),"triple",triple[0],file=sys.stderr)
if __name__=="__main__":main(*sys.argv[1:])
