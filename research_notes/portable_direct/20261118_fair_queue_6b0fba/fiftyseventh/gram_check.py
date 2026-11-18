"""Exact real Q(sqrt(3)) reproduction. Run with --repo /path/to/enterprise-math."""
import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

CORE = "7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26"
stats = dict(calls=0, cancellations=0, max_states=0, observed_numerator_bits=0,
             observed_denominator_bits=0)
core = None


def record(q):
    stats["observed_numerator_bits"] = max(stats["observed_numerator_bits"], abs(q.numerator).bit_length())
    stats["observed_denominator_bits"] = max(stats["observed_denominator_bits"], q.denominator.bit_length())


@lru_cache(None)
def rails(terms):
    """A term (a,b) is a path of two nonnegative edges, sign read at its terminal."""
    if not terms:
        return F(0)
    width = len(terms) + 3
    graph = [[0] * width for _ in range(width)]
    for i, (a, b) in enumerate(terms, 1):
        graph[0][i] = abs(a)
        graph[i][-1 if (a < 0) != (b < 0) else -2] = abs(b)
        record(a)
        record(b)
    row = core.recurrent_mass_power(graph, 2)[0]
    pos, neg = row[-2:]
    stats["calls"] += 1
    stats["cancellations"] += bool(pos and neg)
    stats["max_states"] = max(stats["max_states"], width)
    for value in (pos, neg, pos-neg):
        record(value)
    return pos-neg


def dot(a, b):
    return rails(tuple(sorted((x,y) for x,y in zip(a,b,strict=True) if x and y)))


def rat(a=0, b=0):
    return F(a), F(b)


def fielddot(a, b):
    return (dot([x for x,y in a]+[3*y for x,y in a],
                [x for x,y in b]+[y for x,y in b]),
            dot([x for x,y in a]+[y for x,y in a],
                [y for x,y in b]+[x for x,y in b]))


def linear(coeff, values):
    return tuple(dot(coeff, v) for v in zip(*values))


def circle(t):
    return (1-t*t)/(1+t*t), 2*t/(1+t*t)


def rotate(v, c, s):
    return dot((c,-s),v), dot((s,c),v)


I = [rat(1),rat(0),rat(0),rat(1)]  # vec is column-major (input, output)
W = [rat(F(1,2)),rat(0,F(-1,2)),rat(0,F(1,2)),rat(F(1,2))]
A = [[z if i//2 == h else rat() for i,z in enumerate(op)]
     for op in (I,W) for h in (0,1)]
signs = (1,-1)
u,v = F(3,5),F(4,5)
e = (F(1),F(0))


def compile_joint(tags):
    g = [[dot(x,y) for y in tags] for x in tags]
    amplitude = {sig: [[linear([F(sig**(a//2),2)*tags[a][i] for a in range(4)],
                               [op[j] for op in A]) for j in range(4)]
                       for i in range(2)] for sig in signs}
    out = {}
    for sig in signs:
        for tau in signs:
            direct = [[fielddot([row[i] for row in amplitude[sig]],
                                [row[j] for row in amplitude[tau]]) for j in range(4)] for i in range(4)]
            for i in range(4):
                for j in range(4):
                    active = [(a,b) for a in range(4) for b in range(4) if A[a][i]!=rat() and A[b][j]!=rat()]
                    dyn = linear([F(sig**(a//2)*tau**(b//2),4)*g[a][b] for a,b in active],
                                 [fielddot([A[a][i]],[A[b][j]]) for a,b in active])
                    assert direct[i][j] == dyn
            out[sig,tau] = direct
    for h in (0,1):
        for k in (0,1):
            assert linear([1]*4,[out[sig,sig][2*h+i][2*k+i] for sig in signs for i in (0,1)]) == rat(h==k)
    return out


def probability(out, sig, h):
    a,b = linear([1,1], [out[sig,sig][2*h+i][2*h+i] for i in (0,1)])
    assert not b
    return a


def digest(blocks):
    rows = [[sig,tau,[[[str(a),str(b)] for a,b in row] for row in blocks[sig,tau]]]
            for sig in signs for tau in signs]
    return hashlib.sha256(json.dumps(rows,separators=(",",":")).encode()).hexdigest()


def test_orientation():
    # Several first-independent anchors, reflected and nonreflected rational tags.
    vectors = [circle(F(i,7)) for i in range(-5,6)]
    count = 0
    for i in range(11):
        for step in range(1,6):
            tags = [vectors[(i+j*step)%11] for j in range(4)]
            for mirror in (-1,1):
                pts = [(x,mirror*y) for x,y in tags]
                gram = [[dot(x,y) for y in pts] for x in pts]
                p,q = pts[:2]
                signed = p[0]*q[1]-q[0]*p[1]
                assert signed and signed**2 == gram[0][0]*gram[1][1]-gram[0][1]**2
                for a in (0,1):
                    for b in (2,3):
                        area = (gram[a][0]*gram[b][1]-gram[a][1]*gram[b][0])/signed
                        assert u*gram[a][b]-v*area == dot(pts[a],rotate(pts[b],u,v))
                        count += 1
    return count


def main():
    global core
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo",type=Path,default=Path("."))
    args = ap.parse_args()
    path = args.repo / "src/enterprise_math/brc_weighted_recurrent.py"
    assert hashlib.sha256(path.read_bytes()).hexdigest() == CORE
    spec = importlib.util.spec_from_file_location("em57_weighted_core",path)
    core = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = core
    spec.loader.exec_module(core)
    # Witness directly on the inherited positive coefficient kernel.
    basis = [(1,-1,0),(1,1,-2)]
    W3 = [[F(a,3) for a in row] for row in [[2,2,-1],[-1,2,2],[2,-1,2]]]
    raw = [[dot(x,[dot(row,y) for row in W3]) for y in basis] for x in basis]
    assert raw == [[1,3],[-3,3]]
    # B*B splits by input as [[1,1/2],[1/2,1]].
    for a in range(4):
        for b in range(4):
            assert fielddot(A[a],A[b]) == rat(1 if a==b else F(1,2) if a%2==b%2 else 0)
    histories = []
    for mirror in (1,-1):
        tags = [e,e,e,(F(4,5),mirror*F(3,5))]
        no_return = compile_joint(tags)
        after = compile_joint(tags[:2]+[rotate(x,u,v) for x in tags[2:]])
        old_p = [[str(probability(no_return,sig,h)) for sig in signs] for h in (0,1)]
        new_p = [[str(probability(after,sig,h)) for sig in signs] for h in (0,1)]
        assert old_p == [["3/4","1/4"],["7/10","3/10"]]
        assert new_p == [["13/20","7/20"],["1/2","1/2"] if mirror==1 else ["37/50","13/50"]]
        trace_cross = linear([1,1],[after[1,-1][2+i][2+i] for i in (0,1)])
        histories.append(dict(mirror=mirror,old=old_p,new=new_p,old_joint=digest(no_return),
                              returned_joint=digest(after),cross_11_diagonal=[list(map(str,after[1,-1][2+i][2+i])) for i in (0,1)],
                              cross_trace=list(map(str, trace_cross))))
    assert histories[0]['old_joint'] == histories[1]['old_joint']
    assert histories[0]['returned_joint'] != histories[1]['returned_joint']
    rare=[]
    for t in map(F,["1/3","1/10","1/100"]):
        c,s = circle(t)
        # Before return, arm 1 records R^t e, R^t(c,s).
        tags = [e,e,rotate(e,u,-v),rotate((c,s),u,-v)]
        tags = tags[:2]+[rotate(x,u,v) for x in tags[2:]]
        assert tags == [e,e,e,(c,s)]
        joint = compile_joint(tags)
        # Unnormalised test vector perpendicular to |1>+c W|1>, column major.
        w = [rat(1+c/2),rat(0,-c/2)]
        value = fielddot(w,[fielddot(joint[1,1][2+i][2:4],w) for i in (0,1)])
        norm = fielddot(w,w)
        assert norm[1]==0 and value[1]==0
        p = value[0]/norm[0]
        assert p == 3*s*s/(16*(1+c+c*c)) and p>0
        kept = fielddot(w,[rat(0,c/2),rat(1+c/2)])
        assert kept == rat()
        rare.append(dict(t=str(t),total_loss=str(s*s/2),event_probability=str(p),kept_event_probability="0"))
    orientations = test_orientation()
    print(json.dumps(dict(public_core_sha256=CORE,arithmetic="rational pairs a+b*sqrt(3)",
                          raw_W3_bridge=raw,full_joint_entries_compared=64*7,
                          orientation_cross_entries=orientations,histories=histories,
                          rare=rare,positive_kernel=stats),default=str,ensure_ascii=False,indent=2))


if __name__ == "__main__":
    main()
