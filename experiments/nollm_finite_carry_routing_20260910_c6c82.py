#!/usr/bin/env python3
"""Exact finite-carry chart routing and congestion audit; research, not runtime.
Run: python experiment.py --output results
Requires numpy and the unchanged locality predecessor (including its tower script).
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,random,sys
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parent
PIN='3e09fb193258ad328fcad8d5e7678a69234d719e57ed02cfedbee77d26e3778b'
paths=[ROOT/'prior/nollm_chart_neighbor_locality/experiment.py',ROOT/'nollm_chart_neighbor_locality_20260910_c6c82.py']
path=next((p for p in paths if p.exists()),None)
if path is None:raise FileNotFoundError('pinned locality predecessor required')
if hashlib.sha256(path.read_bytes()).hexdigest()!=PIN:raise ValueError('source hash mismatch')
spec=importlib.util.spec_from_file_location('locality_predecessor',path)
old=importlib.util.module_from_spec(spec);sys.modules[spec.name]=old;spec.loader.exec_module(old)
t=old.t;D=tuple(tuple(map(int,x)) for x in old.D)
A=((1,-3),(3,4));AI=((4,3),(-3,1));C=((-4,1),(21,-5));CI=((5,1),(21,4))

def minimize(rows):
    blocks=[0]*len(rows);rounds=0
    while True:
        ids={};new=[]
        for row in rows:
            sig=tuple((out,blocks[nxt]) for out,nxt in row)
            if sig not in ids:ids[sig]=len(ids)
            new.append(ids[sig])
        rounds+=1
        if new==blocks:return blocks,rounds
        blocks=new
        if rounds>len(rows):raise AssertionError('partition convergence')

class Carry:
    """One coordinate-digit PAIR in and out at each step."""
    def __init__(self,A,d,p):
        if p not in (5,11) or d<1 or d%p==0 or t.det(A)%p==0:raise ValueError('nonunit')
        self.A,self.d,self.p=A,d,p;self.inv=pow(d,-1,p)
        self.lo=tuple(-sum(-a for a in row if a<0)-d for row in A)
        self.hi=tuple(sum(a for a in row if a>0) for row in A)
        self.states=[(0,0)];self.ids={(0,0):0};self.rows=[]
        for c in self.states:
            row=[]
            for x in product(range(p),repeat=2):
                y,cc=self.step(c,x)
                assert all(self.lo[i]<=cc[i]<=self.hi[i] for i in (0,1))
                if cc not in self.ids:self.ids[cc]=len(self.states);self.states.append(cc)
                row.append((y[0]*p+y[1],self.ids[cc]))
            assert len({o for o,_ in row})==p*p;self.rows.append(row)
        b,_=minimize(self.rows);assert len(set(b))==len(self.states)
    def step(self,c,x):
        z=t.plus(t.mv(self.A,x),c);y=tuple(v*self.inv%self.p for v in z)
        return y,tuple((z[i]-self.d*y[i])//self.p for i in (0,1))
    def vector(self,x,n):
        c=(0,0);out=[0,0];s=1;xx=list(x)
        for _ in range(n):
            digit=[]
            for i in (0,1):xx[i],a=divmod(xx[i],self.p);digit.append(a)
            y,c=self.step(c,digit);assert c in self.ids
            for i in (0,1):out[i]+=s*y[i]
            s*=self.p
        return tuple(out)

class Tower:
    """One p-ary refinement digit per step; at most one pending digit."""
    def __init__(self,carry,src,dst):
        self.carry,self.p,self.src,self.dst=carry,carry.p,src,dst
        self.states=[(0,(0,0),-1)];self.ids={self.states[0]:0};self.rows=[];self.causal=0
        for st in self.states:
            row=[]
            for a in range(self.p):
                out,ss=self.step(st,a,True)
                if ss not in self.ids:self.ids[ss]=len(self.states);self.states.append(ss)
                row.append((out,self.ids[ss]))
            assert len({o for o,_ in row})==self.p;self.rows.append(row)
        self.blocks,self.rounds=minimize(self.rows)
    def step(self,st,a,check=False):
        phase,c,first=st;p=self.p;sl=t.active_line(p,self.src,phase);dl=t.active_line(p,self.dst,phase)
        if first==-1:
            y,_=self.carry.step(c,t.unframe(a,0,sl,p));out=t.frame(y,dl,p)[0]
            if check:
                for b in range(p):
                    yy,_=self.carry.step(c,t.unframe(a,b,sl,p));assert t.frame(yy,dl,p)[0]==out;self.causal+=1
            return out,(phase,c,a)
        y,cc=self.carry.step(c,t.unframe(first,a,sl,p))
        return t.frame(y,dl,p)[1],((phase+1)%3,cc,-1)
    def word(self,ds):
        state=0;out=[]
        for a in ds:
            if type(a) is not int or not 0<=a<self.p:raise ValueError('digit')
            y,state=self.rows[state][a];out.append(y)
        return tuple(out)
    def summary(self):
        return dict(base=self.p,src=self.src,dst=self.dst,carry_states=len(self.carry.states),
          carry_transitions=len(self.carry.rows)*self.p**2,carry_bounds=[self.carry.lo,self.carry.hi],
          raw_tower_states=len(self.states),minimal_tower_states=len(set(self.blocks)),
          raw_tower_transitions=len(self.rows)*self.p,refinement_rounds=self.rounds,
          causal_completions_checked=self.causal)

def direct(x,p,k,mat,d,dst):
    mod=p**((k+1)//2);v=t.mv(mat,x)
    v=tuple(a*pow(d,-1,mod)%mod for a in v) if mod>1 else (0,0)
    return t.canon(v,p,k,dst)
def crt(a,b,m,n):return (a+m*((b-a)*pow(m,-1,n)%n))%(m*n)
def graph_hop(x,m):
    q,r=(int(v)%m for v in x)
    return min(max(abs(q+i*m),abs(r+j*m),abs(q+r+(i+j)*m)) for i,j in product((-1,0,1),repeat=2))
def interleave(w5,w11):
    out=[]
    for k in range(max(len(w5),len(w11))):
        if k<len(w5):out.append(format(w5[k],'03b'))
        if k<len(w11):out.append(format(w11[k],'04b'))
    return ''.join(out)
def route(a,b):
    if len(a)!=len(b):raise ValueError('same depth')
    h=0
    while h<len(a) and a[h]==b[h]:h+=1
    return [a[:k] for k in range(len(a),h,-1)]+[b[:k] for k in range(h+1,len(b)+1)],h

def tree_audit(tm5,tm11,out):
    m=55;points=list(product(range(m),repeat=2));codes=[];endpoint={}
    for x in points:
        z5=tm5.word(t.encode_digits(x,5,2,0));z11=tm11.word(t.encode_digits(x,11,2,0))
        codes.append(interleave(z5,z11))
        y5=t.decode_digits(z5,5,3);y11=t.decode_digits(z11,11,3)
        endpoint[x]=tuple(crt(y5[i],y11[i],5,11) for i in (0,1))
    assert len(set(codes))==3025 and len(set(endpoint.values()))==3025
    prefixes={''}
    for s in codes:prefixes.update(s[:j] for j in range(1,len(s)+1))
    degree=Counter()
    for v in prefixes:
        if v:degree[v]+=1;degree[v[:-1]]+=1
    assert max(degree.values())<=3
    loads=Counter();lengths=Counter();checks=0;examples=[]
    signal=[(i*37+19)%101 for i in range(3025)];sums=[0]*3025;expected=[0]*3025
    for i,x in enumerate(points):
        for d in D:
            nb=tuple((x[j]+d[j])%m for j in (0,1));ni=nb[0]*m+nb[1]
            edges,h=route(codes[i],codes[ni]);loads.update(edges);lengths[len(edges)]+=1
            assert all(e in prefixes for e in edges) and len(edges)<=28
            dy=tuple((endpoint[nb][j]-endpoint[x][j])%m for j in (0,1))
            assert all((dy[j]-t.mv(A,d)[j]*pow(13,-1,5))%5==0 for j in (0,1))
            assert all((dy[j]-t.mv(C,d)[j])%11==0 for j in (0,1))
            sums[ni]+=signal[i];expected[i]+=signal[ni];checks+=1
            if i==0:examples.append(dict(source=x,direction=d,destination=nb,
              source_address=codes[i],destination_address=codes[ni],router_hops=len(edges),edge_prefixes=edges))
    assert sums==expected and loads['1']==4840
    (out/'route_examples.json').write_text(json.dumps(examples,indent=2)+'\n')
    (out/'tree_loads.json').write_text(json.dumps(dict(sorted(loads.items())),indent=2)+'\n')
    return dict(states=3025,tree_nodes=len(prefixes),internal_nodes=len(prefixes)-3025,
      tree_max_degree=max(degree.values()),binary_depth=14,routed_directed_messages=checks,
      hops_histogram=dict(sorted(lengths.items())),max_hops=max(lengths),
      mean_hops=str(Fraction(sum(a*b for a,b in lengths.items()),checks)),
      cut_prefix='1',cut_messages=loads['1'],maximum_edge_load=max(loads.values()),aggregation_equal=True)

def run(out):
    out.mkdir(parents=True,exist_ok=True);rng=random.Random(20260910511)
    machines={};summaries=[];full=prefix=inverse=additive=deep=0
    configs=[('U5',5,A,13,0,3),('UI5',5,AI,1,3,0),('U11',11,A,13,0,3),
             ('UI11',11,AI,1,3,0),('C11',11,C,1,0,3),('CI11',11,CI,1,3,0)]
    for name,p,mat,d,src,dst in configs:
        cm=Carry(mat,d,p);tm=Tower(cm,src,dst);machines[name]=tm
        row=tm.summary();row['name']=name;summaries.append(row)
        assert row['carry_states']==(30 if name.startswith('C') else 22)
        for k in range(1,5):
            for x in t.reps(p,k,src):
                ds=t.encode_digits(x,p,k,src);ys=tm.word(ds);y=t.decode_digits(ys,p,dst)
                assert y==direct(x,p,k,mat,d,dst);full+=1
                assert ys[:-1]==tm.word(ds[:-1]);prefix+=1
                if not name.startswith('C'):assert y==t.transport(x,p,k,src,dst)
                for v in ((1,0),(0,1)):
                    xx=t.canon(t.plus(x,v),p,k,src)
                    z=t.decode_digits(tm.word(t.encode_digits(xx,p,k,src)),p,dst)
                    assert z==t.canon(t.plus(y,direct(v,p,k,mat,d,dst)),p,k,dst);additive+=1
        for k in (5,6,11,20,51,101,257):
            for _ in range(20):
                ds=tuple(rng.randrange(p) for _ in range(k));x=t.decode_digits(ds,p,src);ys=tm.word(ds)
                assert t.decode_digits(ys,p,dst)==direct(x,p,k,mat,d,dst);deep+=1
                assert ys[:-1]==tm.word(ds[:-1]);prefix+=1
        (out/(name+'_machine.json')).write_text(json.dumps(dict(parameters=dict(p=p,A=mat,d=d,src=src,dst=dst),
          carry_states=cm.states,carry_table=cm.rows,tower_states=tm.states,
          tower_table=tm.rows,minimal_partition=tm.blocks),separators=(',',':'))+'\n')
        print('machine',row,flush=True)
    for left,right in [('U5','UI5'),('U11','UI11'),('C11','CI11')]:
        f,g=machines[left],machines[right];p=f.p
        for k in range(1,5):
            for ds in product(range(p),repeat=k):assert g.word(f.word(ds))==ds;inverse+=1
    vector_checks=0
    for tm in machines.values():
        for n in (1,2,5,10,50,129):
            mod=tm.p**n
            for _ in range(30):
                x=(rng.randrange(-mod,mod),rng.randrange(-mod,mod));y=tm.carry.vector(x,n)
                assert y==tuple(v*pow(tm.carry.d,-1,mod)%mod for v in t.mv(tm.carry.A,x));vector_checks+=1
    product_checks=0
    for _ in range(1200):
        k5,k11=rng.randrange(1,20),rng.randrange(1,20)
        ds={5:tuple(rng.randrange(5) for _ in range(k5)),11:tuple(rng.randrange(11) for _ in range(k11))}
        tids={5:machines['U5'],11:machines['C11']};ref={p:tids[p].word(ds[p]) for p in ds}
        sched=[5]*k5+[11]*k11;rng.shuffle(sched);ix={5:0,11:0};st={5:0,11:0};vals={5:[],11:[]}
        for p in sched:
            y,st[p]=tids[p].rows[st[p]][ds[p][ix[p]]];vals[p].append(y);ix[p]+=1
        assert all(tuple(vals[p])==ref[p] for p in ds);product_checks+=1
    joint=[]
    for n in range(1,9):
        m5,m11=5**n,11**n;m=m5*m11
        G=tuple(tuple(crt(int(i==j),C[i][j],m5,m11) for j in (0,1)) for i in (0,1))
        cost=max(graph_hop(t.mv(G,x),m) for x in D);assert cost>=m5-1
        assert all(G[i][j]%m5==int(i==j) and G[i][j]%m11==C[i][j]%m11 for i,j in product(range(2),repeat=2))
        joint.append(dict(t=n,plane_period=m,plane_states=m*m,only11_changed_planar_max_hops=cost,
            proven_lower_bound=m5-1,hypothetical_product_binary_route_bound=28*n,
            both_components_conversion_symbol_steps=4*n))
    tree=tree_audit(machines['U5'],machines['C11'],out)
    result=dict(schema='NOLLM_FINITE_CARRY_ROUTING_V1',status='PASS_RESEARCH_NOT_PROMOTED',
      event_id='NOLLM-FINITE-CARRY-ROUTING-20260910-C6C82',predecessor_sha256=PIN,machines=summaries,
      full_word_class_checks=full,prefix_checks=prefix,inverse_word_checks=inverse,
      additive_generator_checks=additive,deep_samples=deep,deep_max_depth=257,
      vector_digit_checks=vector_checks,product_interleavings=product_checks,
      binary_symbol_codecs=[dict(p=p,width=(p-1).bit_length(),valid_leaves=p,unused_codes=2**((p-1).bit_length())-p) for p in (5,11)],
      joint_plane=joint,tree_audit=tree,
      limits=['logical tree links are not fine-grid physical links','26-hop bound does not extend to joint CRT plane',
        '22 counts coordinate-pair carry states, not all tower states','finite control is not depth-independent time or memory',
        'shared-root route has linear congestion for this workload','binary microlevels are not Hecke or Nollm layers',
        'no semantic corpus, runtime integration, or ordinary-label multiplication embedding'])
    (out/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','full_word_class_checks','prefix_checks','inverse_word_checks','deep_samples','tree_audit')},indent=2),flush=True)
    return result
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,default=ROOT/'results')
    run(parser.parse_args().output)
