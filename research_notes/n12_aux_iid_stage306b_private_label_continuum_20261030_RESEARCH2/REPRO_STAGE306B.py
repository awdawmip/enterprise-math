#!/usr/bin/env python3
"""Exact certificate: Stage306-B 3F two-private-label locked Bernoulli rates.

External finite positive-mass BRC-style probability model only; not native X6.
Pure fractions.Fraction, complete branch-and-bound of the full real square.
"""
from fractions import Fraction as Q
from math import comb
from hashlib import sha256
from pathlib import Path
import json

A, B = Q(1, 4), Q(3, 4)
U, ALPHA = Q(1, 10), Q(1, 5)
WEIGHTS = [comb(3, k) for k in range(4)]
TARGET = [(1-U)*A**k*(1-A)**(3-k) + U*B**k*(1-B)**(3-k) for k in range(4)]
LOW = Q(1209322758, 100000000000)
X = Q(231083940855, 1000000000000)
Y = Q(555508857277, 1000000000000)

def wordprob(t, k):
    return t**k * (1-t)**(3-k)

def single_risk(x, y):
    residuals = [(1-ALPHA)*wordprob(x,k)+ALPHA*wordprob(y,k)-TARGET[k] for k in range(4)]
    return sum(WEIGHTS[k]*abs(residuals[k]) for k in range(4))/2

def bounds_f(k, lo, hi):
    z = [wordprob(lo,k), wordprob(hi,k)]
    peak = Q(k,3)
    if lo <= peak <= hi:
        z.append(wordprob(peak,k))
    return min(z),max(z)

def rectangle_lower(rect):
    xl,xh,yl,yh = rect
    lower = Q(0)
    for k in range(4):
        fxl,fxh = bounds_f(k,xl,xh)
        fyl,fyh = bounds_f(k,yl,yh)
        mn = (1-ALPHA)*fxl+ALPHA*fyl-TARGET[k]
        mx = (1-ALPHA)*fxh+ALPHA*fyh-TARGET[k]
        d = mn if mn>0 else (-mx if mx<0 else Q(0))
        lower += WEIGHTS[k]*d/2
    return lower

def split(rect):
    xl,xh,yl,yh=rect
    if xh-xl >= yh-yl:
        m=(xl+xh)/2
        return (xl,m,yl,yh),(m,xh,yl,yh)
    m=(yl+yh)/2
    return (xl,xh,yl,m),(xl,xh,m,yh)

def verify_coverage(leaf_paths):
    """Independently checks each exact leaf and prefix partition of unit square."""
    leafset=set(leaf_paths)
    assert len(leafset)==len(leaf_paths)
    assert all(set(path)<={"0","1"} for path in leaf_paths)
    stack=[("",(Q(0),Q(1),Q(0),Q(1)))]
    accepted=0
    while stack:
        path,rect=stack.pop()
        if path in leafset:
            assert rectangle_lower(rect)>=LOW, (path,rect)
            accepted+=1
            continue
        # Every missing branch must split; gaps or ancestors of a leaf fail.
        assert any(p.startswith(path) for p in leafset), "Incomplete cover at "+path
        l,r=split(rect)
        stack.extend([(path+"1",r),(path+"0",l)])
    assert accepted==len(leaf_paths)
    return accepted

def make_certificate():
    stack=[("",(Q(0),Q(1),Q(0),Q(1)))]
    leaves=[]
    visited=0
    maxdepth=0
    while stack:
        path,rect=stack.pop()
        visited+=1
        maxdepth=max(maxdepth,len(path))
        if rectangle_lower(rect)>=LOW:
            leaves.append(path)
            continue
        l,r=split(rect)
        stack.extend([(path+"1",r),(path+"0",l)])
    return leaves,visited,maxdepth

def one_f_joint_audit_minimum():
    # Source-tagged one-F risk includes S and J, as well as public W,Y1.
    misclass=Q(0)
    for j in (0,1):
        for w in (0,1):
            for first_y in (0,1):
                z=[]
                for s in (0,1):
                    ps=A if s==0 else B
                    pj=Q(1,8) if s==0 else Q(7,8)
                    jmass=pj if j else 1-pj
                    wmass=Q(3,4) if w==s else Q(1,4)
                    ymass=ps if first_y else 1-ps
                    z.append(Q(1,2)*jmass*wmass*ymass)
                misclass += min(z)
    return misclass*(B-A),misclass

def root_result():
    assert TARGET==[Q(61,160),Q(21,160),Q(9,160),Q(9,160)]
    assert sum(comb(3,k)*TARGET[k] for k in range(4))==1
    assert LOW<single_risk(X,Y)<Q(1209322759,100000000000)
    leaves,visited,maxdepth=make_certificate()
    assert verify_coverage(leaves)==len(leaves)
    certificate={
      "schema":"STAGE306B_EXACT_DYADIC_COVER_V1",
      "low_risk_per_outer_public_prefix":str(LOW),
      "splitting":"longer side; ties split x; left child 0, right child 1",
      "root":["0","1","0","1"],
      "leaf_paths":sorted(leaves),
    }
    out=Path(__file__).with_name("CERT_STAGE306B_DYADIC.json")
    out.write_text(json.dumps(certificate,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n",encoding="utf-8")
    loaded=json.loads(out.read_text(encoding="utf-8"))
    assert loaded["low_risk_per_outer_public_prefix"]==str(LOW)
    assert verify_coverage(loaded["leaf_paths"])==len(leaves)
    print("STAGE306B_THREE_VISIT_REAL_CONTINUUM_CERTIFICATE_PASS")
    print("exact_target_per_word_probability_k0_to_k3="+",".join(map(str,TARGET)))
    print("outer_prefix_probability_each=5/16; two_outer_total=5/8")
    print("center_prefix_total_probability=3/8; center_exact_risk=0")
    print("exact_lower_per_outer="+str(LOW))
    print("witness_rates_x_y="+str(X)+","+str(Y))
    print("exact_upper_per_outer="+str(single_risk(X,Y)))
    print("global_lower="+str(LOW*Q(5,8)))
    print("global_upper="+str(single_risk(X,Y)*Q(5,8)))
    print("prior_stage305_upper=63/6400")
    print("strict_improvement="+str(Q(63,6400)-single_risk(X,Y)*Q(5,8)))
    print("verified_cover_leaves="+str(len(leaves)))
    print("verified_visited_nodes="+str(visited))
    print("max_dyadic_depth="+str(maxdepth))
    print("certificate_bytes="+str(out.stat().st_size))
    print("certificate_sha256="+sha256(out.read_bytes()).hexdigest())
    risk_joint, misclass=one_f_joint_audit_minimum()
    assert misclass==Q(7,64) and risk_joint==Q(7,128)
    print("joint_source_and_J_audit_one_F_exact_minimax="+str(risk_joint))
    print("irreducible_one_F_Bayes_error="+str(misclass))
    print("STAGE306B_EXACT_PASS")

if __name__ == "__main__":
    root_result()
