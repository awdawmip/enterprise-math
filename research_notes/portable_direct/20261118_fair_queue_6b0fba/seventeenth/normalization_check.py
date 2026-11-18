"""Exact three-port event and Dirichlet-observer checks. Python stdlib.

Run with --repo /path/to/enterprise-math on the named pinned files.
"""
import argparse
import contextlib
import hashlib
import io
import json
import runpy
import sys
from collections import Counter
from itertools import product
from pathlib import Path

PIN='c0f816e2ab6be0145a3edd1a77488bddfd42a2f6'
FILES={
    'signed_path':('experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py',
              '6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4'),
    'frame':('experiments/x6_cell_internal_state_v1_20260906/check_triadic_port_frame.py',
              '34058e33af5d8e325e3804bdbcf92f06918d48817b3ba5f8ded02e34c337a964'),
    'cwm':('src/enterprise_math/brc_weighted.py',
              '4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f')}

def vector(port):
    return tuple((1 if port>0 else -1) if i==abs(port) else 0 for i in range(1,7))

def minus(p,q):
    return tuple(a-b for a,b in zip(p,q))

def plus(p,q):
    return tuple(a+b for a,b in zip(p,q))

def accepted_event(frame, R, path):
    target=R(frame)
    starts=list(map(vector,frame))
    ends=list(map(vector,target))
    origin=(0,)*6
    options=[]
    for u,v in zip(starts,ends):
        delta=minus(v,u)
        assert path['shortest_event_count'](delta)==2
        assert path['shortest_path_multiplicity'](delta)==2
        # Independently enumerate the two ways to swap these signed coordinates.
        mids={plus(u,vector(p)) for i in range(1,7) for p in (i,-i)
              if path['shortest_event_count'](minus(v,plus(u,vector(p))))==1}
        assert mids=={origin,plus(u,v)}
        options.append((origin,plus(u,v)))
    accepted=[ms for ms in product(*options) if ms[0]==ms[1]==ms[2]]
    assert accepted==[(origin,)*3]
    return target,[(t,u,origin,v) for t,(u,v) in enumerate(zip(starts,ends))]

def native_checks(frames, R, F, path):
    hist=set()
    for frame in frames:
        target,token_paths=accepted_event(frame,R,path)
        assert len({t for t,*rest in token_paths})==3
        assert F(F((frame,0)))==(target,0)
        if (frame,0) in hist:
            continue
        state=(frame,0)
        orbit=[]
        for _ in range(12):
            orbit.append(state)
            state=F(state)
        assert state==orbit[0] and len(set(orbit))==12 and not (set(orbit)&hist)
        hist.update(orbit)
    assert len(hist)==1920
    return {'all_ordered_signed_frames':len(frames),'joint_branch_candidates':8*len(frames),
            'atomic_accepted':len(frames),'decorated_states':len(hist),'C12_orbits':160}

def token_history(initial,n,R):
    # Pull back the actual shell/closure sequence, keeping the history position.
    origin=(0,)*6
    frame=initial
    history=[]
    for k in range(n):
        target=R(frame)
        for mode in ('in','out'):
            movement=[]
            for t,(p,q) in enumerate(zip(frame,target)):
                u,v=(vector(p),origin) if mode=='in' else (origin,vector(q))
                movement.append((t,p,q,u,v))
            history.append((k,mode,tuple(movement)))
        frame=target
    return history

def typed_corners(history):
    ports={}
    for i,(k,mode,marks) in enumerate(history):
        for token,p,q,u,v in marks:
            # At a shared pivot, incoming and outgoing records refer to the same
            # joint (p,q) event, with the original named token in both records.
            left=(i,token,u,('shell',p) if mode=='in' else ('closure',p,q))
            right=(i+1,token,v,('closure',p,q) if mode=='in' else ('shell',q))
            for state in (left,right):
                key=(state[0],state[1])
                assert ports.setdefault(key,state)==state
    return ports

def gram(history,a,b,brc):
    # Group equal end-point tests only after signing and recording the token edge.
    m=len(history)
    entries={}
    for i,(_,mode,marks) in enumerate(history):
        for token,port_in,port_out,u,v in marks:
            assert sum(abs(k) for k in minus(u,v))==1
            assert token in range(3) and port_in!=port_out
            # Assign full a/b to every occurrence. On synchronous tests the
            # resulting K is three times the layer-weighted observer matrix.
            edge=brc.cwm_edge(a if mode=='in' else b)
            incidence=((i,-1),(i+1,1))
            for j,s in incidence:
                for k,t in incidence:
                    if j in (0,m) or k in (0,m):
                        continue
                    key=(j-1,k-1,s*t)
                    entries[key]=brc.cwm_recoalesce(entries.get(key,brc.CWM_ZERO),edge)
    ans=[]
    for j in range(m-1):
        row=[]
        for k in range(m-1):
            pos=entries.get((j,k,1),brc.CWM_ZERO).total
            neg=entries.get((j,k,-1),brc.CWM_ZERO).total
            signed=pos-neg
            assert signed.denominator==1
            row.append(signed.numerator)
        ans.append(row)
    return ans

def det_signed_permutations(matrix):
    # Independent signed expansion through nonzero columns, no division.
    def extend(row,prev,weight):
        if row==len(matrix):
            return weight
        answer=0
        for j,x in enumerate(matrix[row]):
            if not x or j in prev:
                continue
            sign=-1 if sum(k>j for k in prev)%2 else 1
            answer+=extend(row+1,prev+(j,),weight*x*sign)
        return answer
    return extend(0,(),1)

def dimer_checks(R,brc):
    cases=Counter()
    for n in range(2,8):
        history=token_history((1,-2,3),n,R)
        m=2*n-1
        ports=typed_corners(history)
        assert len(ports)==3*(2*n+1)
        # Boundary equality of all synchronous-token test columns and their gradients.
        for j in range(1,m+1):
            f=[int(i==j) for i in range(2*n+1)]
            lifted={state:f[state[0]] for state in ports.values()}
            for k,(_,_,marks) in enumerate(history):
                differences=[lifted[ports[k+1,t]]-lifted[ports[k,t]] for t,*_ in marks]
                assert differences==[f[k+1]-f[k]]*3
            cases['pinned_unit_tests']+=1
        for a,b in ((1,1),(2,2),(4,4),(3,6),(6,3),(2,5)):
            s=a+b
            G=gram(history,a,b,brc)
            K=[[s if i==j else
                (-(a,b)[max(i,j)%2] if abs(i-j)==1 else 0)
                for j in range(m)] for i in range(m)]
            assert all(G[i][j]==3*K[i][j] for i in range(m) for j in range(m))
            cases['signed_three_port_grams']+=1
            for lam in sorted(set(range(-2,m+2))|{s}):
                mat=[[K[i][j]-(lam if i==j else 0) for j in range(m)] for i in range(m)]
                actual=det_signed_permutations(mat)
                diagonal=2*a*b-lam*(2*s-lam)
                u,v=1,diagonal
                for _ in range(2,n):
                    u,v=v,diagonal*v-(a*b)**2*u
                assert actual==(s-lam)*v
                cases['signed_determinant_evaluations']+=1
    return dict(cases)

def main(repo):
    pins={}
    for name,(p,sha) in FILES.items():
        fn=repo/p
        assert hashlib.sha256(fn.read_bytes()).hexdigest()==sha
        pins[name]=sha
    path=runpy.run_path(str(repo/FILES['signed_path'][0]))
    with contextlib.redirect_stdout(io.StringIO()):
        frame=runpy.run_path(str(repo/FILES['frame'][0]))
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import brc_weighted as brc
    assert Path(brc.__file__).resolve()==repo/FILES['cwm'][0]
    actual=native_checks(frame['frames'],frame['R'],frame['F'],path)
    checks=dimer_checks(frame['R'],brc)
    a=[4,4]; b=[3,6]
    # Reciprocal duration, in external twelfths: both protocols total six ticks.
    assert all(w*t==12 for w,t in zip(a+b,[3,3,4,2]))
    assert all(x*y==2*(x+y) for x,y in [a,b])
    h=token_history((1,-2,3),6,frame['R'])
    assert h[0][2][0][1:3]==(1,-2)
    assert [sum(times) for times in ((3,3),(4,2))]==[6,6]
    return {'source_commit':PIN,'source_sha256':pins,
            'actual_source_entrypoints':['R','F','shortest_event_count','shortest_path_multiplicity','cwm_edge','cwm_recoalesce'],
            'native':actual,'observer_checks':checks,
            'one_orbit':{'initial_signed_ports':[1,-2,3],'relation_layers':len(h),
                        'ordered_primitive_occurrences':sum(len(marks) for _,_,marks in h),
                        'shared_action_cells_per_macrostep':1},
            'equal_coarse_conductance_examples':[
                {'in_out':[4,4],'durations_in_external_twelfths':[3,3],'coarse_weight':2,
                 'pinned_interpolation_numerator_denominator':[1,2],'middle_eigenvalue':8},
                {'in_out':[3,6],'durations_in_external_twelfths':[4,2],'coarse_weight':2,
                 'pinned_interpolation_numerator_denominator':[1,3],'middle_eigenvalue':9}]}

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--repo',type=Path,default=Path.cwd())
    print(json.dumps(main(p.parse_args().repo.resolve()),indent=2,sort_keys=True))
