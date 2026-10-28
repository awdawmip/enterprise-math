"""C42: factor-order rewards under weighted selection without replacement.

Weights are exact positive rational BRC path probabilities.  Reward signs are
observations, never negative probability mass.  Only equal (used counts,reward)
states are merged: their entire permitted future score laws agree.  The original
BRC histograms are retained, including individual path-weight multiplicities.
The power-CDF construction used in the proof is an auxiliary probability
representation; the executable generator uses only rational branching.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
from math import factorial, prod
import json
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'inherited'))
from c12_core import native, serialize
COUNTS = Counter()


def skew(k: int, entries):
    d = [[Q(0) for _ in range(k)] for _ in range(k)]
    for (i,j), value in zip(combinations(range(k),2), entries, strict=True):
        d[i][j] = Q(value)
        d[j][i] = -Q(value)
    return d


def validate(a, d, w):
    k=len(a)
    if len(w)!=k or len(d)!=k or any(len(row)!=k for row in d):
        raise ValueError('Counts, curvature, and priority weights must agree in size')
    if any(type(x) is not int or x<0 for x in a) or any(x<=0 for x in w):
        raise ValueError('Counts must be nonnegative integers; priorities positive')
    if any(d[i][j]!=-d[j][i] for i in range(k) for j in range(k)):
        raise ValueError('Curvature must be antisymmetric')


def theta(wi,wj):
    return wi/(wi+wj)


def kernel_cov(wp,wq,wr):
    """Cov(X**wq, X**wr) for P(X<=x)=x**wp."""
    return wp*wq*wr/((wp+wq+wr)*(wp+wq)*(wp+wr))


def pair_residual(wp,wq):
    return wp*wq*(wp*wp+wp*wq+wq*wq)/((wp+wq)**2*(wp+2*wq)*(2*wp+wq))


def exact_moments(a,d,w):
    """Exact finite expectation and orthogonal variance contributions."""
    w=tuple(map(Q,w));validate(a,d,w);k=len(a)
    mean=sum((a[p]*a[q]*d[p][q]*theta(w[p],w[q])
              for p,q in combinations(range(k),2)), Q(0))
    projection=Q(0)
    per_type=[]
    for p in range(k):
        var=sum((a[q]*a[r]*d[p][q]*d[p][r]*kernel_cov(w[p],w[q],w[r])
                 for q in range(k) for r in range(k)),Q(0))
        assert var>=0
        per_type.append(a[p]*var);projection+=a[p]*var
    residual=sum((a[p]*a[q]*d[p][q]**2*pair_residual(w[p],w[q])
                  for p,q in combinations(range(k),2)),Q(0))
    assert residual>=0
    return {'mean':mean,'projection':projection,'residual':residual,
            'variance':projection+residual,'projection_by_type':per_type}


def state_distribution(a: tuple[int,...],d,w,first_only: bool=False):
    """Full exact score law, using the existing positive BRC carrier."""
    w=tuple(map(Q,w));validate(a,d,w);k=len(a)
    empty=native.weight_histogram([])
    states={(0,)*k:{Q(0):native.weight_histogram([1])}}
    for _ in range(sum(a)):
        nxt={}
        for used,hist in states.items():
            remaining=[a[i]-used[i] for i in range(k)]
            active=(Q(1),)*k if first_only and sum(used)>0 else w
            den=sum((active[i]*remaining[i] for i in range(k)),Q(0))
            for p in range(k):
                if not remaining[p]:continue
                prob=active[p]*remaining[p]/den
                assert prob>0
                branch=native.weight_histogram([prob])
                newused=list(used);newused[p]+=1;newused=tuple(newused)
                inc=sum((d[q][p]*used[q] for q in range(p)),Q(0))
                target=nxt.setdefault(newused,{})
                for reward,mass in hist.items():
                    out=native.histogram_serial(mass,branch);COUNTS['brc_serial']+=1
                    newreward=reward+inc
                    target[newreward]=native.histogram_recoalesce(target.get(newreward,empty),out)
                    COUNTS['brc_recoalesce']+=1
        states=nxt
    hist=states[a]
    dist={reward:mass.total_mass for reward,mass in hist.items()}
    assert sum(dist.values())==1 and all(v>0 for v in dist.values())
    words=factorial(sum(a))//prod(factorial(x) for x in a)
    assert sum(mass.count for mass in hist.values())==words
    mean=sum((r*p for r,p in dist.items()),Q(0))
    var=sum(((r-mean)**2*p for r,p in dist.items()),Q(0))
    theory=first_only_moments(a,d,w) if first_only else exact_moments(a,d,w)
    assert mean==theory['mean'] and var==theory['variance']
    COUNTS['distribution_cases']+=1
    return dist, {'mean':mean,'variance':var,'word_count':words,
                  'score_support':len(dist),'distinct_weights_retained':sum(len(v.entries) for v in hist.values())}


def direct_words(a,d,w,first_only: bool=False):
    """Independent word-by-word recurrence; no moment formula used."""
    w=tuple(map(Q,w));out=Counter();count=0;rows=[]
    def visit(remaining, used, reward, probability, word):
        nonlocal count
        if not any(remaining):
            out[reward]+=probability;count+=1
            if sum(a)<=3:rows.append({'word':word,'reward':reward,'probability':probability})
            return
        active=(Q(1),)*len(a) if first_only and sum(used)>0 else w
        den=sum((active[i]*remaining[i] for i in range(len(a))),Q(0))
        for p,n in enumerate(remaining):
            if n:
                rem=list(remaining);rem[p]-=1
                nu=list(used);nu[p]+=1
                inc=sum((d[q][p]*used[q] for q in range(p)),Q(0))
                visit(tuple(rem),tuple(nu),reward+inc,probability*active[p]*n/den,word+(p,))
    visit(a,(0,)*len(a),Q(0),Q(1),())
    COUNTS['direct_words']+=count
    return dict(out),count,rows


def first_only_moments(a,d,w):
    """Exact conditioning on the first choice, uniform word law thereafter."""
    w=tuple(map(Q,w));k=len(a)
    if sum(a)==0:return {'mean':Q(0),'variance':Q(0)}
    den=sum(w[i]*a[i] for i in range(k));mean=Q(0);second=Q(0)
    for p in range(k):
        if not a[p]:continue
        probability=w[p]*a[p]/den
        rem=list(a);rem[p]-=1
        # Contributions involving the first token are deterministic.
        first_score=sum((d[p][q]*a[q] for q in range(p+1,k)),Q(0))
        child=exact_moments(tuple(rem),d,(Q(1),)*k)
        cm=first_score+child['mean']
        mean+=probability*cm
        second+=probability*(child['variance']+cm*cm)
    return {'mean':mean,'variance':second-mean*mean}


def balance_coefficients(u,d,w):
    """For a=t*u, variance = C*t**3+D*t**2 exactly."""
    m=exact_moments(u,d,w)
    return {'cubic':m['projection'],'quadratic':m['residual'],'mean_t_squared':m['mean']}


def group_constraints(u,d,w):
    vals=sorted(set(map(Q,w)))
    return {str(v):[sum((Q(u[q])*d[p][q] for q in range(len(u)) if w[q]==v),Q(0))
                    for p in range(len(u))] for v in vals}


def write(name,data):
    (ROOT/'results'/name).write_text(json.dumps(serialize(data),ensure_ascii=False,indent=2)+'\n')


if __name__=='__main__':
    cyc=skew(3,[1,-1,1]);weights=(Q(1),Q(1),Q(2))
    rows=[]
    for t in range(1,5):
        a=(t,t,t);dist,info=state_distribution(a,cyc,weights)
        assert info['variance']==Q(t*t,4)+Q(t*t*(t-1),90)
        rows.append({'t':t,**info,'distribution':dist})
    print(json.dumps(serialize(rows),indent=2))
    print(dict(COUNTS))
