"""Finite original BRC experiments for independent maps and three jointly decoded services."""
import argparse,copy,hashlib,json,sys
from collections import Counter
from functools import cache
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from adaptive.repair.joint_repair import first,MAPS
from adaptive.phase.phase_kernel import F,rewrite
from adaptive.graph.feedback_graph import V,E,audit,fcol
from projected.kernel.subset_kernel import prefix,initial,emit,marker_slot,least_one,core
C4=((0,0,1,1,2),(1,2,0,2,3),(1,3,0,3,2),(2,1,2,0,3),(3,1,3,0,2))
ORBITS=((12,20),(14,17),(0,9),(13,21),(15,18),(5,16),(23,24),(2,10),(3,11),(8,19),(4,21),(6,7),(1,22))
C16=(12, 3, 3, 3, 4, 2, 6, 8, 15, 10, 7, 1, 7, 7, 3, 0, 0, 0, 1, 1, 9, 1, 11, 13, 5, 1, 13, 8, 15, 4, 2, 7, 9, 12, 0, 13, 6, 13, 12, 13, 14, 13, 10, 12, 14, 3, 10, 11, 12, 5, 1, 11, 6, 10, 5, 3, 4, 9, 15, 0, 4, 8, 4, 4, 7, 6, 11, 14, 6, 6, 2, 4, 6, 13, 8, 2, 7, 9, 14, 12, 1, 6, 8, 14, 0, 2, 14, 9, 15, 10, 2, 7, 9, 15, 4, 3, 14, 11, 13, 5, 1, 12, 12, 10, 0, 3, 7, 5, 13, 11, 11, 6, 5, 11, 0, 8, 5, 14, 8, 4, 2, 9, 15, 9, 0)
C13_ind=(3, 10, 12, 2, 5, 2, 2, 2, 9, 4, 3, 1, 0, 0, 0, 3, 6, 11, 2, 7, 8, 8, 8, 2, 8, 12, 12, 11, 8, 12, 3, 5, 11, 9, 4, 0, 5, 11, 10, 2, 5, 6, 5, 5, 7, 1, 5, 1, 1, 1, 4, 4, 12, 4, 5, 3, 9, 9, 8, 9, 0, 1, 4, 8, 2, 10, 6, 4, 8, 7, 11, 11, 4, 11, 11, 7, 1, 12, 8, 5, 7, 1, 10, 9, 4, 0, 7, 7, 7, 2, 6, 1, 11, 6, 6, 7, 3, 3, 3, 3, 9, 0, 6, 8, 5, 3, 0, 6, 12, 4, 9, 1, 6, 12, 2, 9, 0, 11, 12, 7, 9, 0, 6, 12, 10)
def encode(h,policy):
    if policy=='optimal13':return C13_ind[25*h[0]+5*h[1]+h[2]]
    if policy=='table16':return C16[25*h[0]+5*h[1]+h[2]]
    if policy=='orbit13':
        q=5*((h[1]-h[0])%5)+(h[2]-2*h[0])%5
        return next(i for i,b in enumerate(ORBITS) if q in b)
    if policy=='early-site':return h[1]
    if policy in ('four','one-receipt'):return C4[h[0]][h[1]]
    if policy=='three':return ((h[0]+2*h[1])%5)//2
    raise ValueError(policy)
@cache
def worlds(n):return tuple(product(V,repeat=n))
@cache
def possible(policy,maps,es,fs,msg):
    outs=set()
    for h in worlds(len(es)):
        if encode(h,policy)!=msg:continue
        r=tuple(audit(e,F[m][v])for m,e,v in zip(maps,es,h))
        if tuple(q[0]for q in r)==fs:outs.add(tuple(q[1]for q in r))
    return tuple(sorted(outs))
@cache
def tree(outs):
    if len(outs)==1:return 0,outs[0],None
    cand=[]
    for i,col in enumerate(zip(*outs)):
        if len(set(col))==1:continue
        assert len(set(col))==2 and 11 in col
        sides=tuple(tuple(o for o in outs if (o[i]==11)==b)for b in (0,1))
        ds=[tree(x)[0]for x in sides]
        cand.append((1+max(ds),i,sides))
    return min(cand)
def decode(policy,maps,es,fs,msg,read,limit):
    outs=possible(policy,maps,es,fs,msg);assert outs
    d,ix,hyp=tree(outs);assert d<=limit
    trace=[]
    while hyp is not None:
        assert fs[ix]==11
        key=E[es[ix]][0]+1
        b=int(read(ix,key));assert b in (0,1);trace.append((ix,key,b))
        d,ix,hyp=tree(hyp[b])
    return ix,tuple(trace)
class Stats:
    def __init__(self):
        self.count=Counter();self.cost=Counter();self.maps={};self.ctr=0
        self.pathhash=hashlib.sha256();self.reps={}
    def add(self,h,m,e,msg,fs,ks,tr,fee):
        n=len(tr);self.count[n]+=1;self.cost[fee]+=1;self.ctr+=1
        self.maps.setdefault(' '.join(m),Counter())[n]+=1
        record=[h,m,e,msg,fs,ks,tr,fee]
        self.pathhash.update((json.dumps(record,separators=(',',':'))+'\n').encode())
        if n not in self.reps:self.reps[n]=record
    def result(self):
        return dict(paths=self.ctr,by_queries=dict(self.count),by_maps=self.maps,
            total_queries=sum(k*v for k,v in self.count.items()),fees=dict(sorted(self.cost.items())),
            min_total=min(self.cost),max_total=max(self.cost),sample_paths=list(self.reps.values()),
            sha256_ordered_paths=self.pathhash.hexdigest())
def fork(p):return copy.deepcopy(p,{id(p.C):p.C})
def old(C,h):
    p=prefix(C,initial(h),route=fcol)
    obs=sum(int(p.events[i]['present'])<<i for i in range(3))
    assert obs==h and p.cost==2346
    p.events=[];return p,obs
def update(p,m):
    w=rewrite(p,F[m]);assert w['cost']==1222 and p.cost==3568;p.events=[]
def real_path(ps,h,m,e,msg,policy,limit):
    reserved=0 if policy=='early-site' else None # selected before first business receipts
    banks=[p.codes()for p in ps];fresh=sum(p.cost for p in ps)
    first0=first(ps[0],e[0])
    if policy=='one-receipt':
        if first0['code']!=11:reserved=1
        else:
            pre=tuple(tuple(v for v in V if F[k][v] in E[j])for k,j in zip(m,e))
            reserved=int(any(all(C4[x][y]==msg for y in pre[1])for x in pre[0]))
    fr=(first0,)+tuple(first(p,j)for p,j in zip(ps[1:],e[1:]));fs=tuple(r['code']for r in fr)
    def read(i,k):
        if reserved is not None:assert i==reserved
        return ps[i].probe(marker_slot(k),least_one(k))
    if reserved is None:
        out,tr=decode(policy,m,e,fs,msg,read,limit)
    else:
        outs=possible(policy,m,e,fs,msg)
        assert 1<=len(outs)<=2;tr=()
        if len(outs)==2:
            i=reserved;k=e[i]+1;assert fs[i]==11 and outs[0][i]!=outs[1][i]
            b=int(read(i,k));tr=((i,k,b),);outs=tuple(o for o in outs if o[i]==(11 if b else k))
        assert len(outs)==1;out=outs[0]
    se=tuple(emit(p,[k])[0]for p,k in zip(ps,out));ks=tuple(s['bind_delivered']for s in se)
    assert ks==out and all((f,s)==audit(ed,F[m0][v])for f,s,ed,m0,v in zip(fs,ks,e,m,h))
    assert banks==[p.codes()for p in ps];fee=sum(p.cost for p in ps)
    assert fee==fresh+8*len(tr)+sum(x['paid']for x in fr)+sum(sum(x['words'])for x in se)
    return fs,ks,tr,fee
def direct_pairs(C,policy):
    # Joint computation consumes only real prefix observations and first receipts.
    st=Stats();prefixes=writers=0
    for h in worlds(2):
        orig=tuple(old(C,v)for v in h);prefixes+=2
        msg=encode(tuple(t[1]for t in orig),policy)
        for m in product(MAPS,repeat=2):
            base=tuple(fork(t[0])for t in orig)
            for p,m0 in zip(base,m):update(p,m0);writers+=1
            for e in worlds(2):
                fs,ks,tr,fee=real_path(tuple(fork(p)for p in base),h,m,e,msg,policy,1)
                st.add(h,m,e,msg,fs,ks,tr,fee)
    r=st.result();assert r['paths']==2500
    return dict(**r,physical_prefixes=prefixes,physical_writers=writers,
                physical_first_deliveries=5000,physical_second_deliveries=5000)
def component_table(C):
    # Fully execute both suffix alternatives when active; the missing-probe alternative is not emulated.
    table={};guard={};orig_prefix=orig_writes=orig_first=orig_second=orig_bits=0
    for v in V:
        base,guard[v]=old(C,v);orig_prefix+=1
        for m in MAPS:
            src=fork(base);update(src,m);orig_writes+=1
            for e in V:
                pre=fork(src);bank=pre.codes();fr=first(pre,e);orig_first+=1;fs=fr['code']
                for asked in range(2 if fs==11 else 1):
                    p=fork(pre);k=e+1
                    bit=int(p.probe(marker_slot(k),least_one(k))) if asked else None;orig_bits+=asked
                    # Generate demanded suffix from the independent oracle; only compare against decoder output at recovery time.
                    expected=audit(e,F[m][v]);assert expected[0]==fs
                    se=emit(p,[expected[1]])[0];orig_second+=1;code=se['bind_delivered'];assert code==expected[1]
                    if asked:assert (11 if bit else k)==code
                    assert bank==p.codes() and p.cost==3568+fr['paid']+sum(se['words'])+8*asked
                    table[v,m,e,asked]=(fs,bit,code,p.cost)
    return table,guard,dict(physical_prefixes=orig_prefix,physical_writers=orig_writes,physical_first_deliveries=orig_first,
                       physical_second_deliveries=orig_second,physical_probes=orig_bits)
def triple_group(C,T,G,policy,common,limit,sample=True):
    N=3;st=Stats();Nsample=0;sample_info=Counter();native_digest=hashlib.sha256()
    for h in worlds(N):
        msg=encode(tuple(G[v]for v in h),policy)
        for m in ((('identity',)*N,('doubling',)*N) if common else product(MAPS,repeat=N)):
            for e in worlds(N):
                keys=tuple(zip(h,m,e));records=tuple(T[*k,0]for k in keys);fs=tuple(r[0]for r in records)
                def read(i,k):assert k==e[i]+1;return T[*keys[i],1][1]
                out,tr=decode(policy,m,e,fs,msg,read,limit);queried={i for i,k,b in tr};assert len(queried)==len(tr)
                selected=[T[*k,int(i in queried)]for i,k in enumerate(keys)]
                ks=tuple(row[2]for row in selected);fee=sum(row[3]for row in selected)
                assert ks==out;st.add(h,m,e,msg,fs,ks,tr,fee)
                # First encountered joint scenario of each (map pattern, queried coordinates, active mask).
                tag=(m,tuple(i for i,_,_ in tr),tuple(f==11 for f in fs))
                if sample and tag not in sample_info:
                    sample_info[tag]=1;Nsample+=1
                    orig=tuple(old(C,v)for v in h);ps=tuple(t[0]for t in orig);mmsg=encode(tuple(t[1]for t in orig),policy)
                    for p,m0 in zip(ps,m):update(p,m0)
                    observed=real_path(ps,h,m,e,mmsg,policy,limit);assert observed==(fs,ks,tr,fee)
                    native_digest.update((json.dumps([h,m,e,msg,*observed],separators=(',',':'))+'\n').encode())
    return dict(**st.result(),full_raw_sample=Nsample,full_raw_prefixes=Nsample*N,full_raw_writers=Nsample*N,
        full_raw_first_deliveries=Nsample*N,full_raw_second_deliveries=Nsample*N,full_raw_sample_digest=native_digest.hexdigest())
def run(phase):
    C=core.prior.Compiler(slots=15)
    if phase in ('pair','early-site','one-receipt'):return dict(status='PASS',scope='Direct full pair executions with prefix and writer snapshots; no component-receipt replay.',independent_pair=direct_pairs(C,'four' if phase=='pair' else phase))
    T,G,count=component_table(C)
    common=phase in ('common-triple','common-one')
    policy={'independent-optimal-one':'optimal13','independent-one':'table16','common-one':'orbit13','common-triple':'three','independent-triple':'four'}[phase]
    R=triple_group(C,T,G,policy,common,1 if phase.endswith('-one') else 2)
    return dict(status='PASS',scope='All joint paths use exact compositional receipts from disjoint original components. Independently run sampled whole triple paths from fresh preparation. Prefix guards alone form summary; only public maps, edge menus, actual firsts and paid endpoint probes reach recovery.',component_construction=count,three_units=R)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--phase',required=True,choices=['independent-optimal-one','independent-one','one-receipt','common-one','early-site','pair','common-triple','independent-triple']);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    r=run(a.phase);a.out.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(a.phase,[(k,x.get('paths'),x.get('by_queries'),x.get('full_raw_sample'))for k,x in r.items()if isinstance(x,dict)])
