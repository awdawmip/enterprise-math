"""Count actual V30/V42 PASS bridges and certify orientation and excursion limits with Arb."""
import argparse
from collections import Counter, defaultdict, deque
from contextlib import redirect_stdout
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from io import StringIO
from math import comb
from pathlib import Path
import json
import runpy

import flint
from flint import acb, acb_mat, arb


FILES = {
    'experiments/x6_network_event_ledger_v29_20260906/check_event_order_holonomy.py':
        '184c5954d9211f8c2c1ee55972008d6b5b324b60e4c7c64a7ca3fef6046673d4',
    'experiments/x6_nonfcc_observer_switch_v42_20260906/check_nonfcc_observer_switch.py':
        'b00d3a283b84bf2082eeb0e69b4d750eaf18fd38b90c36f6e1d711eca15763d2',
}
TARGET = (0,3,4)
INITIAL = (3,4,5)
IDENTITY = tuple(range(6))


def native_model(repo):
    sources = []
    for path,digest in FILES.items():
        path = repo/path
        if sha256(path.read_bytes()).hexdigest()!=digest:
            raise ValueError(f'wrong frozen source: {path}')
        with redirect_stdout(StringIO()):
            sources.append(runpy.run_path(str(path)))
    v30,v42 = sources
    assert v30['S0']==INITIAL and v42['ID']==IDENTITY
    def counters(h):
        u = [a+h*b for a,b in zip(v30['u0'],v30['A'][1],strict=True)]
        om = [[a+h*b for a,b in zip(left,right,strict=True)]
              for left,right in zip(v30['Om0'],v30['A'][2],strict=True)]
        return u,om
    scores = {}
    raw_comparisons = 0
    spreads = []
    for s in v30['TRIADS']:
        neighbors = v30['NEIGH'][s]
        affine = []
        for t in neighbors:
            a = v30['score'](*counters(0),s,t)
            b = v30['score'](*counters(1),s,t)-a
            affine.append((a,b,t))
        spreads.append(max(a for a,b,t in affine)-min(a for a,b,t in affine))
        for h in range(-20,21):
            ranked = sorted((a+h*b,t) for a,b,t in affine)
            assert ranked==sorted((v30['score'](*counters(h),s,t),t) for t in neighbors)
            raw_comparisons += len(ranked)
            scores[h,s] = ranked[-1][1] if ranked[-1][0]>ranked[-2][0] else None
        assert all(scores[h,s]==scores[7,s] for h in range(7,21))
        assert all(scores[h,s]==scores[-6,s] for h in range(-20,-5))
        assert scores[7,s] is not None and scores[-6,s] is not None
    assert max(spreads)==16
    # Beyond 16 an integral slope difference dominates every intercept difference.
    lifts = {(s,t):v42['edge_lift'](s,t) for s in v30['TRIADS'] for t in v30['NEIGH'][s]}
    @lru_cache(None)
    def carried(p):
        return tuple(sorted(p[i] for i in INITIAL))
    @lru_cache(None)
    def move(h,p):
        s = carried(p)
        t = scores[min(7,max(-6,h)),s]
        return None if t is None else v42['compose'](lifts[s,t],p)
    def frame_from_word(word):
        frame = IDENTITY
        h = 0
        for c in word:
            h += 1 if c=='A' else -1
            frame = move(h,frame)
            if frame is None:
                break
        return frame
    assert carried(frame_from_word('AB'))==carried(frame_from_word('BA'))==TARGET
    assert frame_from_word('AAA') is None
    return move,carried,{'source_score_comparisons':raw_comparisons,
                         'distinct_edge_lifts':len(lifts),'largest_intercept_range':max(spreads)}


def central_graph(move):
    states = [(0,IDENTITY)]
    ids = {states[0]:0}
    rows = []
    for h,p in states:
        edges = []
        for direction in (-1,1):
            k = h+direction
            if abs(k)<=7:
                target = move(k,p)
                if target is not None:
                    edges.append(((k,target),1,'step'))
                continue
            target = p
            order = 6 if h>0 else 1
            for j in range(1,order+1):
                # At heights h and k the same tail transformation acts.
                target = move(h,move(k,target))
                edges.append(((h,target),j,'upper' if h>0 else 'lower'))
            assert target==p
        row = []
        for state,j,tag in edges:
            if state not in ids:
                ids[state]=len(states)
                states.append(state)
            row.append((ids[state],j,tag))
        rows.append(row)
    return states,rows


def reachable_reverse(seed,pred):
    visited = set(seed)
    todo = deque(sorted(visited))
    while todo:
        x = todo.popleft()
        for y in pred[x]-visited:
            todo.append(y)
            visited.add(y)
    return visited


def finite_core(states, rows, carried):
    end = {i for i,(h,p) in enumerate(states) if h==0 and i!=0}
    pred = defaultdict(set)
    short_pred = defaultdict(set)
    killed = []
    for i,row in enumerate(rows):
        n_interior = 0
        for j,n,tag in row:
            pred[j].add(i)
            if tag=='step': n_interior += 1
            if tag=='step' or n==1: short_pred[j].add(i)
        if n_interior+int(abs(states[i][0])==7)<2:
            killed.append(i)
    todo = deque((i,1) for i in killed)
    distance = {}
    while todo:
        i,d = todo.popleft()
        if i in distance: continue
        distance[i]=d
        todo.extend((k,d+1) for k in short_pred[i] if k not in distance)
    counts = Counter(distance.values())
    assert len(distance)==len(states)==937 and [counts[i] for i in range(1,7)]==[126,162,163,198,162,126]
    core = reachable_reverse(end,pred)
    chart = {(h,carried(p)) for h,p in states}
    core_charts = {(states[i][0],carried(states[i][1])) for i in core}
    assert (len(end),len(chart),len(core),len(core_charts))==(72,53,667,38)
    assert {s for h,s in core_charts if h<=-5}=={(0,4,5)} and min(h for h,s in core_charts)==-5
    assert len({i for i in core if states[i][0]==7})==54
    # An explicit upper bound on ordinary time for each positive-tail witness.
    # These are lengths of actual found paths; breadth here is in macro-edge count.
    todo = deque([(0,0,False,0)])
    seen = {(0,0,False)}
    found = {}
    while todo:
        i,r,hit,t = todo.popleft()
        if hit and i in end: found[i,r]=t
        for j,d,tag in rows[i]:
            if tag!='step' and d!=1: continue
            length = 1 if tag=='step' else 2
            key = (j,(r+length)%12,hit or states[j][0]==7)
            if key not in seen:
                seen.add(key)
                todo.append((*key,t+length))
    assert len(found)==432 and max(found.values())<=46
    return core,{'full_states':len(states),'chart_states':len(chart),'full_return_core':len(core),
                 'chart_return_core':len(core_charts),'stable_zero_endpoints':len(end),
                 'coaccessible_by_height':dict(sorted(Counter(states[i][0] for i in core).items())),
                 'core_charts_by_height':{h:sorted(''.join(map(str,s)) for k,s in core_charts if k==h)
                                         for h in sorted(set(h for h,s in core_charts))},
                 'steps_to_possible_killing_distribution':dict(sorted(counts.items())),
                 'positive_boundary_target_residues_verified':len(found),
                 'largest_found_positive_boundary_witness_length':max(found.values())}


def orientation(p):
    return sum(p[i]>p[j] for i in INITIAL for j in INITIAL if i<j)%2


def orientation_graph(states,rows,core,carried):
    def key(i):
        h,p = states[i]
        return h,carried(p),orientation(p)
    ids = {}
    for i in sorted(core):
        ids.setdefault(key(i),len(ids))
    proj = [None]*len(ids)
    for i in sorted(core):
        edges = [(ids[key(j)],d,tag) for j,d,tag in rows[i] if j in core]
        k = ids[key(i)]
        if proj[k] is None: proj[k]=edges
        assert proj[k]==edges
    assert len(proj)==75 and ids[key(0)]==0
    # The action of a positive length-six excursion reverses slot orientation.
    for i,(h,s,sign) in enumerate(ids):
        if h==7:
            mids = [j for j,d,tag in proj[i] if d==3 and tag=='upper']
            assert mids==[ids[h,s,1-sign]]
    return ids,proj


def multiplicity_edges(rows,T):
    cat = {j:comb(2*j-2,j-1)//j for j in range(1,T//2+1)}
    edges = []
    for row in rows:
        new = [(j,1,1) for j,n,tag in row if tag=='step']
        tal = {n:j for j,n,tag in row if tag!='step'}
        if tal:
            order = len(tal)
            new.extend((tal[(i-1)%order+1],2*i,weight) for i,weight in cat.items())
        edges.append(new)
    return edges


def counts_by_length(edges,T,starts):
    layers = [[0]*len(edges) for _ in range(T+1)]
    for i in starts: layers[0][i]=1
    for t in range(T):
        for i,count in enumerate(layers[t]):
            if not count:continue
            for j,n,weight in edges[i]:
                if t+n<=T:
                    layers[t+n][j] += count*weight
    return layers


def raw_checks(move,carried,states,rows):
    T=34
    folded = counts_by_length(multiplicity_edges(rows,T),T,[0])
    raw = {(0,IDENTITY):1}
    checks=0
    example=None
    for t in range(T+1):
        for i,key in enumerate(states):
            assert folded[t][i]==raw.get(key,0)
            checks+=1
        assert sum(1 for (h,p) in raw if abs(h)<=7)==sum(v!=0 for v in folded[t])
        if t==28:
            mass={''.join(map(str,p)):v for (h,p),v in raw.items() if h==0 and carried(p)==TARGET}
            par=Counter()
            for (h,p),v in raw.items():
                if h==0 and carried(p)==TARGET: par[orientation(p)]+=v
            assert len(mass)==18 and (min(mass.values()),max(mass.values()))==(1972,462668)
            assert (par[0],par[1])==(1027390,1036747)
            example={'by_frame':dict(sorted(mass.items())),'even':par[0],'odd':par[1],'total':sum(mass.values())}
        if t<T:
            nxt=defaultdict(int)
            for (h,p),v in raw.items():
                for k in (h-1,h+1):
                    z=move(k,p)
                    if z is not None:nxt[k,z]+=v
            raw=nxt
    return {'unrestricted_word_DP_vs_Catalan_per_state_and_length':checks,
            'last_compared_length':T,'length_28_terminal_034':example}


@lru_cache(None)
def unit(k,n):
    k%=n
    if k==0:return acb(1)
    if 2*k==n:return acb(-1)
    return (acb(2*k)/n).exp_pi_i()


def interval22(x):
    """A stable rational outward enclosure, recorded as integers over 10^22."""
    if not x.is_finite():
        raise ArithmeticError('nonfinite ball')
    scale=10**22
    low=(x*scale).floor().unique_fmpz()
    if low is None:
        raise ArithmeticError('increase precision for rational enclosure')
    n=int(low)
    assert arb(n)/scale<=x and x<=arb(n+1)/scale
    return [n,n+1]


def arb_resolvent(rows, ends):
    n=len(rows)
    response=[]
    for v in range(12):
        eta=unit(v,12)
        field=[(1-(1-unit(k+v,6)).sqrt())/2 for k in range(6)]
        classes=[sum(unit(-k*j,6)*field[k] for k in range(6))/6 for j in range(6)]
        sing=[unit(v*j,6)/6 for j in range(6)]
        inverse,H=acb_mat(n,n),acb_mat(n,n)
        for i,row in enumerate(rows):
            inverse[i,i]=1
            for j,idx,tag in row:
                if tag=='step':
                    inverse[i,j]-=eta/2
                else:
                    assert tag=='upper'
                    inverse[i,j]-=classes[idx%6]
                    H[i,j]+=sing[idx%6]
        matrix=inverse.transpose()
        b=acb_mat(n,1)
        b[0,0]=1
        one=matrix.solve(b)
        two=matrix.solve(H.transpose()*one)
        response.append([two[i,0] for i in ends])
    phase={}
    sums={}
    balls={}
    for t in range(0,12,2):
        av,bv=[sum(unit(-v*t,12)*response[v][s] for v in range(12)) for s in (0,1)]
        assert 0 in av.imag and 0 in bv.imag and av.real>0 and bv.real>0
        q=av/(av+bv)
        assert 0 in q.imag and q.real.rad()<arb(1)/10**29
        balls[t]=q.real
        sums[t]=(av+bv).real/2
        phase[t]=interval22(q.real)
    for i in balls:
        assert not (arb(1)/2 in balls[i]) and 1 in (balls[i]+balls[(i+6)%12])
        for j in balls:
            if i<j: assert not balls[i].overlaps(balls[j])
    return phase,sums


def residual_checks(rows,ends,denominators):
    # w_(s,r) is computed by reserving the long excursion; all prefixes/suffixes
    # use the original positive word counts. Normalize only at the end.
    T=64
    edges=multiplicity_edges(rows,T)
    rev=[[] for _ in rows]
    for i,row in enumerate(edges):
        for j,d,w in row:rev[j].append((i,d,w))
    left=counts_by_length(edges,T,[0])
    right=counts_by_length(rev,T,ends)
    boundary={i:{n%6:j for j,n,tag in row if tag=='upper'} for i,row in enumerate(rows)}
    boundary={i:tab for i,tab in boundary.items() if tab}
    result={}
    for r in range(0,12,2):
        cdf=Fraction(0)
        sample={}
        for s in range(0,T+1,2):
            q=(r-s)//2%6
            raw=sum(left[a][i]*right[s-a][tab[q]] for a in range(s+1) for i,tab in boundary.items())
            cdf+=Fraction(raw,2**s)
            if s in (24,40,64):
                limit=arb(cdf.numerator)/cdf.denominator/denominators[r]
                assert 0<limit<1
                sample[s]=interval22(limit)
        result[r]=sample
    return result


def main(repo):
    flint.ctx.prec=112
    move,carried,source=native_model(repo)
    states,rows=central_graph(move)
    core,system=finite_core(states,rows,carried)
    ids,proj=orientation_graph(states,rows,core,carried)
    ends=[ids[(0,TARGET,sign)] for sign in (0,1)]
    phase,den=arb_resolvent(proj,ends)
    return {'registration':'RS-X6-UPPER-STRUCTURE-INTEGRATION','source_sha256':FILES,
            'source_replay':source,'graph':system,'checks':raw_checks(move,carried,states,rows),
            'orientation_states':len(proj),'Arb_precision_bits':flint.ctx.prec,
            'python_flint_version':flint.__version__,'FLINT_version':flint.__FLINT_VERSION__,
            'rational_interval_common_denominator':str(10**22),
            'even_slot_probability_limits_by_t_mod_12':phase,
            'limit_residual_length_cdf_terminal_034_at_24_40_64':residual_checks(proj,ends,den)}


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,default=Path.cwd())
    print(json.dumps(main(ap.parse_args().repo),sort_keys=True,indent=2))
