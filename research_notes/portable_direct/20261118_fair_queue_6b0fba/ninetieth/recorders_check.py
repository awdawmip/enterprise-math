"""Named ternary recorder interleavings and exact weighted-BRC rows."""
import argparse
from collections import Counter, defaultdict, deque
from fractions import Fraction
from hashlib import sha1
from itertools import permutations, product
import json
from pathlib import Path
import sys

PINS = {
    'research_tasks/RS-EULER-RR-08-MULTIRECORDER-20261011.md': '6f6b3ed78b5c84a91ca11069f391c7e4d43f865f',
    'research_notes/chatgpt_direct/20261011_EULER_RELATIONAL_RECORDING.md': '03cfdf23f8f1a6208b4ac4eb862a1b7ad3811d8b',
    'research_notes/chatgpt_direct/20261010_EULER_CONTROLLER_RELATIONAL_MEMORY.md': '22a7d072e54f40c52a94e91dac7f68f63371436c',
    'research_notes/chatgpt_direct/20261011_EULER_READOUT_BACKACTION.md': '5e00414f752d97d69cee9bf602fd6b5e50da4b05',
    'src/enterprise_math/brc_weighted.py': '3f205696709e847909958a153f8fe10d3f6b70f0',
    'src/enterprise_math/brc_logarithm.py':'4732e5fc381ce613d240c4381ccbef03c27a69c7',
    'src/enterprise_math/exact_arithmetic.py':'35ea95b0916494b83a92386e3e313928362dd79e',
}
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'eightyfifth'))
from euler_check import gate as inherited_source_gate


def load(repo):
    for path,pin in PINS.items():
        data=(repo/path).read_bytes()
        assert sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==pin
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import brc_weighted
    return brc_weighted


def words(active):
    alphabet='1a2b'+('HUC' if active else '')
    return [''.join(w) for w in permutations(alphabet)
            if w.index('1')<w.index('a') and w.index('2')<w.index('b')
            and (not active or w.index('H')<w.index('U')<w.index('C'))]


def signed_unit_contact(labels,target,delta,sheets,w,kernel,count):
    sign=sheets[target-1]
    turns=(sign*delta)%3
    for _ in range(turns or 1):
        if turns:
            labels[target]=(labels[target]+sign)%3
        count['channel_contact' if turns else 'hold']+=1
        w=kernel.cwm_propagate(w,kernel.CWM_ONE)
    return w


def state_word(initial,order,source,sheets,kernel,cost):
    labels=list(initial)
    assert labels[0]==source[0]
    w=kernel.cwm_edge(Fraction(1,81))
    cost['initial_weights']+=1
    for cmd in order:
        j,a,y,z=labels
        if cmd in 'HUC':
            source=inherited_source_gate(source,cmd)
            labels[0]=source[0]
            cost['source_projection_commands']+=1
            w=kernel.cwm_propagate(w,kernel.CWM_ONE)
        else:
            delta,target={'1':(j-a,2),'2':(j-a,3),'a':(y-j,1),'b':(z-j,1)}[cmd]
            w=signed_unit_contact(labels,target,delta,sheets,w,kernel,cost)
    assert w.total==Fraction(1,81)
    return tuple(labels),source,w


def actual(kernel):
    points=list(product(range(3),repeat=4))
    samples={}
    for source in product(range(3),range(2),range(8),range(4),range(2)):
        after=source
        for step in 'HUC':
            after=inherited_source_gate(after,step)
        jump=(after[0]-source[0])%3
        assert jump in (1,2)
        samples.setdefault((source[0],jump),(source,after))
    assert len(samples)==6
    cost=Counter()
    modes={}
    for active in (False,True):
        schedules=words(active)
        classifications={}
        for jump in ((1,2) if active else (0,)):
            classes=defaultdict(list)
            for word in schedules:
                trace=[]
                sumweight=kernel.CWM_ZERO
                for j,a,y,z in points:
                    source,expected=samples[j,jump or 1]
                    target,old,w=state_word((j,a,y,z),word,source,(1,-1,1),kernel,cost)
                    assert old==(expected if active else source)
                    u=[j,a,y,z]
                    for cmd in word:
                        typ={'1':(0,1,2),'2':(0,1,3),'a':(2,0,1),'b':(3,0,1)}
                        if cmd in typ:
                            s,r,t=typ[cmd]
                            u[t]=(u[t]+u[s]-u[r])%3
                        elif cmd=='C':
                            u[0]=(u[0]+jump)%3
                    assert target==tuple(u)
                    trace.append(target)
                    sumweight=kernel.cwm_recoalesce(sumweight,w)
                    cost['final_recoalescences']+=1
                assert sumweight.total==1 and sumweight.count==81 and sumweight.dominant==Fraction(1,81)
                classes[tuple(trace)].append(word)
            classifications[jump]=sorted((min(v),len(v)) for v in classes.values())
        modes['source_HUC' if active else 'stationary']=dict(schedules=len(schedules),class_sizes_and_first_words=classifications)
    for init in points:
        source=samples[init[0],1][0]
        for sheet in product((1,-1),repeat=3):
            results={word:state_word(init,word,source,sheet,kernel,cost)[0]
                     for word in ('12','21','1a2b','2b1a','12ab','1a1a1a')}
            j,a,y,z=init
            assert results['12']==results['21']
            assert (results['1a2b']==results['2b1a'])==(a==y==z)
            assert (results['1a2b']==results['12ab'])==(y==a)
            assert (results['2b1a']==results['12ab'])==(z==a)
            assert (results['1a1a1a'][2]+y)%3==2*j%3
    return dict(schedules=modes,source_atoms=384,sheet_patterns=8,counts=dict(cost))


def operations(rows,m):
    a,b,c=rows
    sub=lambda u,v:tuple((x-y)%m for x,y in zip(u,v))
    return (b,sub(b,a),c),(c,b,sub(c,a))


def group(m):
    identity=((1,0,0),(0,1,0),(0,0,1))
    depth={identity:0}
    todo=deque([identity])
    while todo:
        g=todo.popleft()
        for h in operations(g,m):
            if h not in depth:
                depth[h]=depth[g]+1
                todo.append(h)
    return depth


def dot(row,v):
    return sum(a*b for a,b in zip(row,v))%3


def add(u,v,a=1,b=1):
    return tuple((a*x+b*y)%3 for x,y in zip(u,v))


def field_multiply(u,v):
    # F27 basis 1, eta, eta^2 with eta^3=eta+1.
    result=[0]*5
    for i,x in enumerate(u):
        for j,y in enumerate(v):
            result[i+j]+=x*y
    for h in (4,3):
        result[h-3]+=result[h]
        result[h-2]+=result[h]
    return tuple(x%3 for x in result[:3])


def observation(gs):
    vec=list(product(range(3),repeat=3));zero=vec[0]
    rows={s for g in gs for s in g[1:]}
    pair={g[1:] for g in gs}
    assert len(pair)==624 and len(rows)==26
    shell={v for v in rows if next(x for x in v if x)!=2}
    assert len(shell)==13
    assert all(sum(dot(row,v)==0 for row in shell)==(4 if any(v) else 13) for v in vec)
    weights={v:1+sum((i+1)*x for i,x in enumerate(v))**2 for v in vec}
    total=sum(weights.values())
    data={(row,b):sum(w for v,w in weights.items() if dot(row,v)==b)
          for row in shell for b in range(3)}
    assert all(sum(data[row,dot(row,v)] for row in shell)==4*total+9*w
               for v,w in weights.items())
    singles={(a,add(zero,r,0,a)) for r in rows for a in range(3)}
    doubles={((a+b)%3,add(r,s,a,b)) for r,s in pair for a,b in product(range(3),repeat=2)}
    assert len(singles)==53 and len(doubles)==79
    assert {k for k in product(range(3),vec) if k not in doubles}=={(1,zero),(2,zero)}
    squares={field_multiply(v,v) for v in rows}
    assert len(squares)==13 and (0,0,1) in squares and (1,0,1) not in squares
    sampled=set()
    designs=[]
    for d in sorted(squares):
        l=field_multiply(d,(0,0,1));r=field_multiply(d,(1,0,1))
        assert (l,r) in pair
        sampled.update(((i+j)%3,add(l,r,i,j)) for i,j in product(range(3),repeat=2))
        designs.append([l,r,min(depth for g,depth in gs.items() if g[1:]==(l,r))])
    assert sampled==doubles
    initial=((0,1,0),(0,0,1))
    length=min(l for g,l in gs.items() if any(add(v,w)==zero for v in initial for w in g[1:]))
    assert length==3
    return dict(absolute_pair_experiments=designs,relative_rows=len(rows),independent_receiver_row_pairs=len(pair),
                relative_scalar_experiments=len(shell),absolute_one_read_rank=len(singles),
                absolute_joint_read_rank=len(doubles),shortest_two_read_source_echo=length)


def uncertainty():
    # All 3x3 error couplings with denominator 5, grouped by both named margins.
    def comp(n,d):
        if d==1:
            yield (n,)
        else:
            for first in range(n+1):
                for tail in comp(n-first,d-1):
                    yield (first,)+tail
    families=defaultdict(list)
    for c in comp(5,9):
        left=tuple(sum(c[3*i+j] for j in range(3)) for i in range(3))
        right=tuple(sum(c[3*i+j] for i in range(3)) for j in range(3))
        families[left,right].append((5-sum(c[::4]),5-c[0]))
    for (p,q),scores in families.items():
        mismatch,paired=zip(*scores)
        assert min(mismatch)==5-sum(min(a,b) for a,b in zip(p,q))
        assert max(mismatch)==5-max(0,max(a+b-5 for a,b in zip(p,q)))
        assert min(paired)==max(5-p[0],5-q[0])
        assert max(paired)==min(5,10-p[0]-q[0])
    return dict(common_denominator=5,joint_tables=sum(map(len,families.values())),margin_pairs=len(families))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,required=True)
    kernel=load(parser.parse_args().repo)
    two=group(2);three=group(3)
    assert (len(two),len(three))==(168,5616)
    print(json.dumps(dict(positive_world_replay=actual(kernel),group_sizes=[len(two),len(three)],
                          word_length_distribution_F3=sorted(Counter(three.values()).items()),
                          readout=observation(three),calibration=uncertainty()),indent=2,sort_keys=True))
