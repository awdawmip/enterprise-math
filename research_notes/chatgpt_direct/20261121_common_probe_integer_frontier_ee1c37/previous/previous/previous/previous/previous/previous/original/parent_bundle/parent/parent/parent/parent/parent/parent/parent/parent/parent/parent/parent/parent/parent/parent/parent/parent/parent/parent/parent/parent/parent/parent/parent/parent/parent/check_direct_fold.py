"""Consume two full private triadic registers through one declared bridge.

Research model only. All matching updates use the pinned primitive/BRC kernel.
This imports parent builders, never executes the parent's main test suites.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from itertools import product
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'parent'))
import check_streaming as f
b,p,a,e,m,r=f.b,f.p,f.a,f.e,f.m,f.r
ONE,ZERO=f.ONE,f.ZERO
CHECKS=0

def ck(ok,label):
    global CHECKS
    CHECKS+=1
    if not ok: raise AssertionError(label)

def direct_gate(left,sample,out,kind='AND'):
    domains=[set(range(o+1,o+7)) for o in (left,sample,out)]
    if any(domains[i]&domains[j] for i in range(3) for j in range(i)):
        raise ValueError('Three private registers must have disjoint members')
    if kind not in ('AND','OR'):raise ValueError('AND or OR required')
    H=set(p.library(left))|set(p.library(sample))|set(p.library(out))
    # The tested bridge forms only on 11 for AND, and only on 00 for OR.
    d=4 if kind=='AND' else 3
    bridge=tuple(sorted((left+d,sample+d,out+d)))
    H.add(bridge)
    Lh,Lt=p.reg(out,0);Rh,Rt=p.reg(out,1)
    tails=(Lt,Rt) if kind=='AND' else (Rt,Lt)
    W=[p.one(left+1),p.one(sample+1),p.add(bridge),
       p.add(tails[0]),p.add(tails[1]),p.one(left+d),
       p.add(Rh),p.add(Lh),p.one(left+5),p.one(sample+5)]
    return H,W

def collector(k,overwrite=False,indices=None):
    if not 2<=k<=6:raise ValueError('Concrete allocator supports 2..6 lanes')
    S=[b.spec(i) for i in range(k)];H=set();W=[];stages=[]
    if overwrite:W+=p.clear_word(500)+p.clear_word(700)
    W += [p.add(s[key]) for key in ('pos','neg') for s in S]
    H |= {s[key] for s in S for key in ('pos','neg')}
    indices=list(range(k)) if indices is None else list(indices)
    if len(indices)!=k or any(not 0<=i<k for i in indices):raise ValueError('Bad scan list')
    h,w,_=a.reader(300,500,800);H|=h;W+=w
    cur=700 if k%2 else 720
    h,w,_=a.reader(310+indices[0],cur,800);H|=h;W+=w
    stages.append(dict(index=indices[0],end=len(W),acc=cur,read_end=len(W),sample=cur))
    for index in indices[1:]:
        out=720 if cur==700 else 700
        h,w,_=a.reader(310+index,740,800);H|=h;W+=w;read_end=len(W)
        h,w=direct_gate(cur,740,out);H|=h
        start=len(W);W+=w
        stages.append(dict(index=index,end=len(W),acc=out,read_end=read_end,sample=740,gate_start=start,old_acc=cur))
        cur=out
    ck(cur==700,'fixed final output from compile-time parity')
    return H,W,stages

def private_members():
    return set().union(*(set(range(o+1,o+7)) for o in (500,700,720,740)))|{800}

def setup(source,k,overwrite=False):
    S=[b.spec(i) for i in range(k)];HC,WC,stages=collector(k,overwrite)
    H=a.SOURCE_H|HC|set().union(*(s['H'] for s in S))
    J=m.canon(source+tuple(s['guard'] for s in S))
    return H,J,S,WC,stages

def execute(*args,**kwargs):return f.execute(*args,**kwargs)
def code(J):return f.result_code(J)

def gates():
    rows=[]
    for kind in ('AND','OR'):
        H,W=direct_gate(700,740,720,kind)
        ck(len(W)==10,'ten primitive calls')
        ck(len(set().union(*H))==18,'three registers only')
        for x,y in product((0,1),repeat=2):
            J=m.canon(p.reg(700,x)+p.reg(740,y))
            z=execute(J,W,H,keep=True)
            wanted=x&y if kind=='AND' else x|y
            ck(z['end']==p.reg(720,wanted),'all inputs consumed, output exact, no residual bridge')
            rows.append(dict(kind=kind,bits=[x,y],run=z))
    return rows

def static_and_integration():
    static=[];whole=[];representatives=[]
    for k in range(2,7):
        H,W,_=collector(k);W=W[2*k:]
        signals=[(port,20000+2*j,20001+2*j) for j,port in enumerate([300]+list(range(310,310+k)))]
        H|=set(signals)
        n=0
        for bits in product((0,1),repeat=k+1):
            J=m.canon(tuple(h for h,bit in zip(signals,bits) if bit))
            z=execute(J,W,H)
            expected=m.canon(J+p.reg(500,bits[0])+p.reg(700,int(all(bits[1:]))))
            ck(z['end']==expected,'every synthetic signal input has exact clean collector output')
            n+=1
        static.append(dict(k=k,cases=n))
    _,domain=e.catalog(a.SOURCE_H)
    for k in (2,3,6):
        for source in sorted(domain):
            if a.signed(source)<0:continue
            H,J,S,W,_=setup(source,k)
            ck(len(W)==18*k-4,'new collector command count')
            ck(len(set().union(*H))==11*k+36,'full source/producer/collector member inventory')
            for overlap in (False,True):
                z=execute(J,[p.one(4)]+f.producing(S,overlap)+W,H,
                          keep=(k==6 and source==(a.P,a.HN) and overlap))
                expected=(1,0) if a.signed(source) else (0,1)
                ck(code(z['end'])==expected,'genuine source-to-result')
                base=tuple(h for h in z['end'] if set(h).isdisjoint(private_members()))
                ck(z['end']==m.canon(base+p.reg(500,expected[0])+p.reg(700,expected[1])), 'no constant, scratch, or consumed operands remain')
                ck(b.old.protected(J,z['end']),'source E/P/tails preserved')
                hr,wr,_=collector(k,True)
                nxt=execute(z['end'],wr,H|hr)
                ck(nxt['end']==z['end'],'same-generation reset and reread exact endpoint')
                whole.append(dict(k=k,source=source,overlap=overlap,length=z['commands'],inventory=len(set().union(*H)),code=expected))
                if z['trace']:representatives.append(z)
    return dict(static=static,integration=whole,traces=representatives)

def omissions():
    rows=[];witnesses=[]
    H,W=direct_gate(700,740,720)
    for x,y in product((0,1),repeat=2):
        J=m.canon(p.reg(700,x)+p.reg(740,y))
        for budget in (1,2):
            word=a.rep(W,budget);d={(J,0):e.prep(J)}
            for op in word:
                nd={}
                for (K,j),mass in d.items():
                    L,_=f.step(K,op,H);f.put(nd,(L,j),r.serial(mass,ONE))
                    if j<budget:f.put(nd,(K,j+1),r.serial(mass,ONE))
                d=nd
            layers={}
            for (K,j),mass in d.items():
                ck(K==p.reg(720,x&y),'protected direct gate exact consumption and output')
                f.put(layers,j,mass)
            ck(layers==a.layers(len(word),budget),'exact weighted deletion histories')
            rows.append(dict(type='gate',bits=[x,y],budget=budget,length=len(word),layers=[dict(omitted=j,CWM=e.cw(w)) for j,w in sorted(layers.items())]))
    for pos in range(10):
        found=None
        for x,y in product((0,1),repeat=2):
            J=m.canon(p.reg(700,x)+p.reg(740,y))
            z=execute(J,W,H,omitted=(pos,))
            if z['end']!=p.reg(720,x&y):found=dict(slot=pos+1,bits=[x,y],end=z['end']);break
        ck(found is not None,'each of ten original positions has a single-omission witness')
        witnesses.append(found)
    for k in (2,3,6):
        for bit in (0,1):
            for overlap in (False,True):
                for budget in (1,2):
                    H,J,S,W,_=setup(p.reg(3,bit),k)
                    basic=[p.one(4)]+f.producing(S,overlap)+W;word=a.rep(basic,budget)
                    reference=execute(J,basic,H)['end'];d={(J,0):e.prep(J)}
                    for op in word:
                        nd={}
                        for (K,j),mass in d.items():
                            L,_=f.step(K,op,H);f.put(nd,(L,j),r.serial(mass,ONE))
                            if j<budget:f.put(nd,(K,j+1),r.serial(mass,ONE))
                        d=nd
                    layers={}
                    for (K,j),mass in d.items():
                        ck(K==reference,'global budget end-to-end clean endpoint')
                        f.put(layers,j,mass)
                    ck(layers==a.layers(len(word),budget),'global omission histories retain total CWM')
                    rows.append(dict(type='whole',k=k,bit=bit,overlap=overlap,budget=budget,length=len(word),layers=[dict(omitted=j,CWM=e.cw(w)) for j,w in sorted(layers.items())]))
    return dict(families=rows,necessary_positions=witnesses)

def shuffle(bit,k=2):
    source=p.reg(3,bit)
    H,J,S,W,stages=setup(source,k);J=execute(J,[p.one(4)],H)['end']
    words=[s['W'] for s in S]+[W];lengths=tuple(map(len,words))
    reads={st['read_end']:(j,st['sample']) for j,st in enumerate(stages)}
    ends={st['end']:(j,st['acc']) for j,st in enumerate(stages)}
    d={((0,)*(k+1),J,()):e.prep(J)};peak=1
    for _ in range(sum(lengths)):
        nd={}
        for (pcs,K,seen),mass in d.items():
            for i,pos in enumerate(pcs):
                if pos==lengths[i]:continue
                pp=list(pcs);pp[i]+=1;pp=tuple(pp)
                L,_=f.step(K,words[i][pos],H);ss=seen
                ck(b.old.protected(J,L),'original source evidence preserved under shuffle')
                if i==k and pp[i] in reads:
                    j,o=reads[pp[i]];v=p.read(L,o)
                    ck(v in (0,1) and p.restrict(L,o)==p.reg(o,v),'new sample complete')
                    ck(len(ss)==j,'actual coverage at compile-time index')
                    ss=ss+(v,)
                if i==k and pp[i] in ends:
                    _,o=ends[pp[i]]
                    ck(p.restrict(L,o)==p.reg(o,int(all(ss))),'stream invariant after every consuming gate')
                f.put(nd,(pp,L,ss),r.serial(mass,ONE))
        d=nd;peak=max(peak,len(d))
    results={}
    for (pcs,K,seen),mass in d.items():
        z=code(K)
        ck(z in ((0,0),(1,0),(0,1)),'no contradictory output')
        ck(not z[0] or bit==1,'YES correct')
        ck(not z[1] or bit==0,'NO correct')
        hr,wr,_=collector(k,True);L=execute(K,wr,H|hr)['end']
        ck(code(L)==((1,0) if bit else (0,1)),'next complete round after all producers resolves')
        f.put(results,z,mass)
    total=f.total(d.values());expected=b.old.positional_mass(lengths,0,0)[0]
    ck(total==expected,'all possible interleavings retained')
    return dict(bit=bit,lengths=lengths,peak_states=peak,terminals=len(d),CWM=e.cw(total),outcomes=[dict(code=z,CWM=e.cw(w)) for z,w in sorted(results.items())])

def failures():
    rows={}
    H,J,S,W,_=setup(p.reg(3,1),2)
    ready=execute(J,[p.one(4)]+f.producing(S,True),H)['end']
    hd,wd,_=collector(2,indices=[1,1]);z=execute(ready,wd,H|hd,keep=True)
    ck(code(z['end'])==(1,1),'faster value gate does not repair duplicated named coverage')
    rows['duplicate_index']=z
    H,W=direct_gate(700,740,720)
    J=m.canon(p.reg(700,1)+p.reg(740,1))
    first=execute(J,W,H,keep=True);again=execute(first['end'],W,H,keep=True)
    rows['macro_replay']=dict(first=first,again=again)
    # A shared operand can be consumed by one gate before another uses it.
    h2,w2=direct_gate(700,760,780);H|=h2
    J=m.canon(p.reg(700,0)+p.reg(740,1)+p.reg(760,1))
    first=execute(J,W,H,keep=True);second=execute(first['end'],w2,H,keep=True)
    ck(p.read(second['end'],780)==1,'using the already-consumed false operand creates a false conjunction')
    rows['shared_operand']=dict(first=first,second=second)
    # An unconsumed (11) bridge must be gone before either input is reusable.
    J=m.canon(p.reg(700,1)+p.reg(740,1));z=execute(J,W,H,keep=True,omitted=(5,))
    ck(z['end']!=p.reg(720,1),'one missed bridge release violates ready-for-next-operation')
    rows['bridge_not_released']=z
    return rows

def preserving_gate(left,sample,out):
    H,_=direct_gate(left,sample,out)
    bridge=tuple(sorted((left+4,sample+4,out+4)))
    Lh,Lt=p.reg(out,0);Rh,Rt=p.reg(out,1)
    W=[p.one(left+1),p.one(sample+1),p.add(bridge),p.add(Lt),p.add(Rt),
       p.one(out+4),p.add(Lt),p.add(Rh),p.add(Lh)]
    W += [p.add(p.reg(o,v)[0]) for o in (left,sample) for v in (0,1)]
    return H,W

def restoration_and_coverage():
    preserved=[];H,W=preserving_gate(700,740,720)
    ck(len(W)==13,'thirteen-call input-preserving companion')
    for x,y in product((0,1),repeat=2):
        J=m.canon(p.reg(700,x)+p.reg(740,y))
        z=execute(J,W,H,keep=True)
        ck(z['end']==m.canon(J+p.reg(720,x&y)),'both input states restored and independent result complete')
        preserved.append(dict(bits=[x,y],run=z))
    h2,w2=direct_gate(700,760,780);H|=h2
    J=m.canon(p.reg(700,0)+p.reg(740,1)+p.reg(760,1))
    z=execute(J,W+w2,H,keep=True)
    ck(p.read(z['end'],720)==0 and p.read(z['end'],780)==0,'restoring first operand repairs the sequential second user')
    coverage=[]
    for k in range(1,7):
        tokens=[(30000+3*i,30001+3*i,30002+3*i) for i in range(k)]
        HH=set(tokens);_,domain=e.catalog(HH);full=m.canon(tokens)
        ck(len(domain)==2**k,'all named covered subsets realized in the original matching kernel')
        pairs=0
        states=sorted(domain)
        for ii,A in enumerate(states):
            for B in states[ii+1:]:
                if not(set(A)-set(B)):A1,B1=B,A
                else:A1,B1=A,B
                suffix=[p.add(t) for t in tokens if t not in A1]
                aa=execute(A1,suffix,HH)['end'];bb=execute(B1,suffix,HH)['end']
                ck(aa==full and bb!=full,'common allowed future distinguishes every pair of coverage states')
                pairs+=1
        # Exact unit-weight receipt histories; duplicates never invent a token.
        d={():ONE}
        for depth in range(k+2):
            nd={}
            for K,mass in d.items():
                for t in tokens:
                    L,_=f.step(K,p.add(t),HH);f.put(nd,L,r.serial(mass,ONE))
            d=nd
        coverage.append(dict(k=k,states=len(domain),distinguishing_pairs=pairs,receipt_length=k+2,terminal_states=len(d),CWM=e.cw(f.total(d.values()))))
    return dict(preserved=preserved,sequential_reuse_control=z,coverage=coverage)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=['cases','faults','shuffle0','shuffle1'],required=True);parser.add_argument('--output',required=True);args=parser.parse_args()
    if args.mode=='cases':data=dict(gates=gates(),cases=static_and_integration(),failures=failures(),interfaces=restoration_and_coverage())
    elif args.mode=='faults':data=omissions()
    else:data=shuffle(int(args.mode[-1]))
    result=dict(mode=args.mode,new_checks=CHECKS,kernel_calls=f.CALLS,transition_uses=f.USES,data=data)
    Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='data'}))
if __name__=='__main__':main()
