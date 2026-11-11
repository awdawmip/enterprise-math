"""Closed intervals and copy tariffs in a prescribed schedule.
No original BRC steps simulated here. Lifted costs come from the compiler;
the independent literal path directly tracks current numeric request keys.
Python 3.10+, standard library only.
"""
from dataclasses import dataclass
from itertools import product
from pathlib import Path
import argparse, json


def w(r,k):
    return 2*k.bit_count()+4*(1-((k>>(r.bit_length()-1))&1))

def cp(r,k,targets=3):
    q=(targets*(r+1)).bit_length()
    return 9*q+1 if not k else 9*q+2+k.bit_count()+4*(1-((k>>(q-1))&1))

# Ops: W(target,dst) = create from free, bind, release. C(dst,src), D(dst).
@dataclass
class Graph:
    r:int
    schedule:tuple
    births:list                   # root i<r old; newly born roots ordered by create index
    ends:list                     # largest creation number preceding its extinction
    copies:list                   # count all nonself copies of each source, including copies of aliases
    copy_roots:list               # source root or -1 explicit empty, sequential copy occurrence
    bool_roots:list               # self copy / drop: previous nonempty Boolean
    targets:list
    first_full:list               # number of completed creates at first free full observation
    first_presence:list           # same for first observable nonempty Boolean
    empty_copies:int

def compile_graph(r,sched):
    slot=list(range(r));n=[1]*r
    birth=[0]*r;end=[None]*r;cop=[0]*r;cr=[];pr=[];tar=[];ff=[None]*r;fp=[None]*r
    j=0; cp0=0
    def assign(i,o):
        a=slot[i]
        if a==o:return
        if a>=0:
            n[a]-=1
            if n[a]==0:end[a]=j
        slot[i]=o
        if o>=0:n[o]+=1
    for op in sched:
        k,i=op[:2]
        if k=='W':
            j+=1;tar.append(i);d=op[2];o=len(birth)
            birth.append(j);end.append(None);n.append(0);cop.append(0);ff.append(None);fp.append(None)
            assign(d,o)
        elif k=='D':
            a=slot[i];pr.append(a)
            if a>=0 and fp[a] is None:fp[a]=j
            assign(i,-1)
        elif k=='C':
            s=op[2];a=slot[s]
            if s==i:
                pr.append(a)
                if a>=0 and fp[a] is None:fp[a]=j
            else:
                cr.append(a)
                if a>=0:
                    cop[a]+=1
                    if ff[a] is None:ff[a]=j
                else:cp0+=1
                assign(i,a)
        else:raise ValueError(op)
    return Graph(r,tuple(sched),birth,[j if z is None else z for z in end],cop,cr,pr,tar,ff,fp,cp0)

def projected(g,x,keys):
    r=g.r;codes=tuple(x)+tuple(keys)
    # Initial sources do not conflict with each other; a selected key only
    # conflicts with another creation active at its birth or a still-live old root.
    for j,k in enumerate(keys,1):
        if any(codes[o]==k and g.ends[o]>=j for o in range(r+j-1)):return None
    paid=sum(w(r,k) for k in keys)+sum(nn*cp(r,k) for nn,k in zip(g.copies,codes))+g.empty_copies*cp(r,0)
    cv=lambda o:0 if o==-1 else codes[o]
    return paid,tuple(cv(o) for o in g.copy_roots),tuple(bool(cv(o)) for o in g.bool_roots)

def literal(r,sched,x,keys):
    tab=list(x);j=0;paid=0;codes=[];presence=[]
    for op in sched:
        kind,i=op[:2]
        if kind=='W':
            key=keys[j];j+=1
            if key in tab:return None
            paid+=w(r,key);tab[op[2]]=key
        elif kind=='D':
            presence.append(bool(tab[i]));tab[i]=0
        else:
            k=tab[op[2]]
            if i==op[2]:presence.append(bool(k))
            else:codes.append(k);paid+=cp(r,k);tab[i]=k
    return paid,tuple(codes),tuple(presence)

def shifted_one_create(r,t,x,m):
    q=(3*(r+1)).bit_length();keys=range(1+t*(r+1),1+(t+1)*(r+1))
    if r!=2:raise ValueError('known target-specific constants in these examples only')
    D=[62,65,62][t]
    rows=[dict(key=k,base_word=D,w=w(r,k),copy_word=cp(r,k),extra_probe_commands=8*r,total=D+8*r+w(r,k)+m*cp(r,k)) for k in keys if k not in x]
    return dict(copy_count=m,paths=rows,min_keys=[e['key'] for e in rows if e['total']==min(z['total'] for z in rows)],minimum=min(z['total'] for z in rows))

def crossover_classification(limit=116):
    # Delta w>0, Delta L>0 force -1<=d<=3. Derived, not an empirical bound.
    triples=[]
    for h,u,d in product((-1,0,1),(-1,0,1),range(-1,4)):
        dw=2*d+4*h;dl=4*u-d
        if dw>0 and dl>0:
            triples.append(dict(h=h,u=u,d=d,dw=dw,dl=dl,first_strict=dw//dl+1))
    assert len(triples)==10
    thresholds=sorted({v['first_strict'] for v in triples})
    assert thresholds==[1,2,3,5,7,11]
    examples={}
    for r in range(2,limit+1):
        b=r.bit_length();m=r+1;q=(3*m).bit_length()
        for t in range(3):
            group={}
            for k in range(1+t*m,1+(t+1)*m):
                group.setdefault((k.bit_count(),(k>>(b-1))&1,(k>>(q-1))&1),k)
            for k,l in product(group.values(),repeat=2):
                dw=w(r,l)-w(r,k);dl=cp(r,k)-cp(r,l)
                if dw<=0 or dl<=0:continue
                mm=dw//dl+1
                assert mm in thresholds
                if mm in examples:continue
                # One lawful actual preparation leaves exactly k and l free.
                x=[v for v in range(1+t*m,1+(t+1)*m) if v not in (k,l)]+[0]
                assert len(x)==r and len(set(x))==r
                assert w(r,k)+(mm-1)*cp(r,k)<=w(r,l)+(mm-1)*cp(r,l)
                assert w(r,k)+mm*cp(r,k)>w(r,l)+mm*cp(r,l)
                examples[mm]=dict(r=r,target=t,k=k,l=l,delta_base=dw,delta_copy=dl,
                                  weak_tie_at_m_minus_1=dw==(mm-1)*dl)
    assert sorted(examples)==thresholds
    return dict(thresholds=thresholds,admissible_triples=triples,
                all_six_attained_by_actual_legal_pairs=examples,
                unbounded_proof="dw>0 and dl>0 imply -1<=d<=3; r>=2 for distinct-address copies",
                scope="number m of required nonself copies of this creation; not arbitrary-horizon whole-schedule minimax")

def run():
    r=2
    # Complete specified universe: independent values 0..9, every 3-event
    # word over two targets, both physical directions and both drops, plus self copy.
    alphabet=(('W',0,0),('W',1,1),('C',0,1),('C',1,0),('C',0,0),('D',0),('D',1))
    stats=dict(schedules=0,table_schedule_trace_comparisons=0,feasible=0,infeasible=0)
    for sched in product(alphabet,repeat=3):
        g=compile_graph(r,sched);stats['schedules']+=1
        for keys in product(*(range(1+t*(r+1),1+(t+1)*(r+1)) for t in g.targets)):
            for x in product(range(3*(r+1)+1),repeat=r):
                a=projected(g,x,keys);b=literal(r,sched,x,keys)
                if a!=b:raise AssertionError((x,keys,sched,a,b))
                stats['table_schedule_trace_comparisons']+=1
                stats['feasible' if a is not None else 'infeasible']+=1
    # An alias of an alias survives both earlier storage slots.
    s=(('C',1,0),('D',0),('C',2,1),('D',1),('W',0,0),('D',2),('W',0,1))
    g=compile_graph(3,s)
    assert g.ends[:3]==[1,0,0] and g.copies[:3]==[2,0,0]
    assert projected(g,(1,2,3),(1,2)) is None and projected(g,(1,2,3),(2,1))==literal(3,s,(1,2,3),(2,1))
    # Same blocked-complete-key profiles at every creation, different compulsory outputs and costs.
    ss=(('C',2,0),('W',0,2));gg=compile_graph(3,ss)
    def maxes(x):
        return {k:max(gg.ends[i] for i,a in enumerate(x) if a==k) for k in x if k}
    aa=(1,3,0);bb=(3,1,0)
    assert maxes(aa)==maxes(bb) and gg.copies[:3]==[1,0,0]
    va=projected(gg,aa,(2,));vb=projected(gg,bb,(2,))
    assert (va[0],vb[0])==(45,46) and va[1]==(1,) and vb[1]==(3,)
    frontier=tuple(shifted_one_create(2,2,(8,8),m) for m in (0,1))
    assert [e['minimum'] for e in frontier]==[84,126]
    assert [e['min_keys'] for e in frontier]==[[7],[9]]
    crosses=[shifted_one_create(2,0,(2,2),m) for m in range(5)]
    assert [z['min_keys'] for z in crosses]==[[3],[3],[1,3],[1],[1]]
    # A full numeric copy/last-death front + paid-uncertainty fronts are genuinely distinct.
    s2=(('W',1,2),('C',2,0),('C',1,2),('D',0),('W',0,2),('D',1),('W',0,1))
    g2=compile_graph(3,s2)
    assert [g2.ends[0],g2.first_full[0],g2.copies[0]]==[2,1,2]
    return dict(status='PASS',unit='Control: w plus entire mandatory nonself copy words; fixed W business constant, self copy and drop lengths separate (included in the one-create table where applicable).',exhaustive=stats,
       alias_chain=dict(schedule=s,initial_root_0=dict(last_live_creation=g.ends[0],copies=g.copies[0]),forbidden=[1,2],permitted=[2,1]),
       two_fronts=dict(schedule=s2,old0_first_full_after_n_creates=g2.first_full[0],old0_last_live_create=g2.ends[0],old0_copy_count=g2.copies[0]),
       deadline_only_counterexample=dict(schedule=ss,old=[aa,bb],last_profiles=[maxes(aa),maxes(bb)],chosen=[2],variable_costs=[va[0],vb[0]],compulsory_outputs=[va[1],vb[1]]),
       single_create_single_copy_reversal=frontier,low_family_crossover=crosses,six_crossover_thresholds=crossover_classification())

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).with_name('origin_results.json'));a=p.parse_args()
    ans=run();a.out.write_text(json.dumps(ans,indent=2,sort_keys=True)+'\n');print(ans['exhaustive'])
