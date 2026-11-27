import json, random, hashlib, time

def greedy(c, items):
    # items (mask,weight), descending order, prefix retained ranks
    n=len(c); occ=[[] for _ in c]; masks=[]; ranks=[]; r=0
    def add(x,seen):
        for j in range(n):
            if masks[x]>>j&1 and j not in seen:
                seen.add(j)
                if len(occ[j])<c[j]:
                    occ[j].append(x); return True
                for k,y in enumerate(occ[j]):
                    if add(y,seen):
                        occ[j][k]=x; return True
        return False
    for mask,w in items:
        if not mask:
            r+=1; ranks.append(r); continue
        x=len(masks); masks.extend([mask,mask])
        assert add(x,set())
        if add(x+1,set()):
            for a in occ:
                if x+1 in a: a.remove(x+1); break
            r+=1
        else:
            for a in occ:
                if x in a: a.remove(x); break
        ranks.append(r)
    return ranks

def value(items,ranks):
    return sum(w*(r-(ranks[k-1] if k else 0)) for k,((_,w),r) in enumerate(zip(items,ranks)))

def adjacent(c,items,i):
    # ignore empty masks, retaining them for zero cost; i remains a positive-capacity port
    items=sorted([(e,w) for e,w in items if e],key=lambda x:-x[1]); bit=1<<i
    singles=[w for e,w in items if e==bit]
    groups=[1<<j for j in range(len(c)) if j!=i]
    for e,w in items:
        p=e&~bit
        if not p: continue
        hit=[g for g in groups if g&p]
        g=0
        for h in hit: g|=h; groups.remove(h)
        groups.append(g)
    base=0; new=0; slots=singles[:]; total=sum(w for e,w in items)
    for g in groups:
        local=[(e,w) for e,w in items if e&g]
        if not local: continue
        js=[j for j in range(len(c)) if g>>j&1]
        def remap(e): return sum(1<<k for k,j in enumerate(js) if e>>j&1)
        p=[(remap(e),w) for e,w in local]; cc=[c[j] for j in js]
        old=[(p[k][0]|((1<<len(js)) if e&bit else 0),w) for k,(e,w) in enumerate(local)]
        r0=greedy(cc+[1],old); ri=greedy(cc+[len(old)+1],old); rn=greedy(cc,p)
        base+=value(old,r0); new+=value(p,rn)
        d=[b-a for a,b in zip(r0,ri)]
        for k in range(1,max(d,default=0)+1):
            slots.append(sum((w-(old[t+1][1] if t+1<len(old) else 0)) for t,(_,w) in enumerate(old) if d[t]>=k))
    top=sum(sorted(slots,reverse=True)[:c[i]-1]); oldcost=total-base-top
    newcost=total-sum(singles)-new
    return oldcost,newcost,sum(any(e&g and e&bit for e,w in items) for g in groups),base-new,top,sum(singles)

def direct(c,items):
    items=sorted(items,key=lambda x:-x[1]); return sum(w for e,w in items)-value(items,greedy(c,items))

def brute(c,items):
    n=len(c); best=0
    for keep in range(1<<len(items)):
        selected=[(e,w) for j,(e,w) in enumerate(items) if keep>>j&1 and e]
        if all(sum(e&v==e for e,w in selected)<sum(c[j] for j in range(n) if v>>j&1) for v in range(1,1<<n)):
            best=max(best,sum(w for e,w in selected))
    return sum(w for e,w in items if e)-best

def check(c,items,i,exhaust=False):
    a,b,k,z,t,s=adjacent(c,items,i)
    c2=c[:i]+c[i+1:]; lower=(1<<i)-1
    p=[((e&lower)|((e>>(i+1))<<i),w) for e,w in items]
    assert (a,b)==(direct(c,items),direct(c2,p)),(c,items,i,a,b)
    if exhaust: assert (a,b)==(brute(c,items),brute(c2,p))
    assert b-a==z+t-s and z>=0
    return k,b-a

def main():
    start=time.monotonic(); rng=random.Random(20261127); rcount=0
    for _ in range(300):
        n=rng.randrange(1,6); c=[rng.randrange(1,4) for j in range(n)]; items=[(rng.randrange(1<<n),rng.randrange(17)) for j in range(rng.randrange(8))]
        for i in range(n): check(c,items,i,True); rcount+=1
    print('random_brute_pairs',rcount,flush=True)
    raw=open('witness_records.json','rb').read(); assert hashlib.sha256(raw).hexdigest()=='c75076272328a0d67c4a991cdb02045099e79ddccba71aea32d4824a97b495e7'
    records=json.loads(raw); count=multi=pos=neg=zero=0; min_delta=0; max_delta=0
    for mode in ('root','one_sampled_cut'):
        count=multi=pos=neg=zero=0; min_delta=0; max_delta=0
        for ri,r in enumerate(records):
            c=r['caps']; items=[(e,(13*ri+7*j)%17) for j,e in enumerate(r['opts'].values())]
            if mode!='root':
                # Deterministic proper, nonempty cut; preserve original label order and weights.
                n=len(c); W=1+((ri*2654435761)%((1<<n)-2)); js=[j for j in range(n) if not (W>>j&1)]
                items=[(sum(1<<k for k,j in enumerate(js) if e>>j&1),w) for e,w in items]; c=[c[j] for j in js]
            for i in range(len(c)):
                k,d=check(c,items,i); count+=1; multi+=k>1; pos+=d>0; neg+=d<0; zero+=d==0; min_delta=min(min_delta,d); max_delta=max(max_delta,d)
        print(mode,'records',len(records),'pairs',count,'multiple_affected_components',multi,'positive',pos,'negative',neg,'zero',zero,'min_delta',min_delta,'max_delta',max_delta,flush=True)
    print('seconds',time.monotonic()-start,flush=True)
if __name__=='__main__': main()
