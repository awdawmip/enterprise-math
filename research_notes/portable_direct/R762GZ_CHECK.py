"""R762GZ reproducible positive BRC incidence-histogram and signed Port checker.

Model: R762GY signed X6 K4 STAR endpoint-choice candidate, chirality +1,
initial named Port 01. No physical heartbeat/time calibration or native
TRIADIC_CLOSURE_E legality asserted. Branches and positive multiplicity
are preserved; compressed histograms do not preserve original word order.
"""

from collections import defaultdict
from math import comb
import json

V = (0, 1, 2, 3)
LAYERS = (("01", "23"), ("02", "13"), ("03", "12"))
ZERO = (0, 0, 0, 0)

def vertex(a, b):
    common = set(a) & set(b)
    assert len(common) == 1
    return int(next(iter(common)))

def unit(v):
    return tuple(int(i == v) for i in V)

def brc_recoalesce(a, b):
    """Typed positive BRC alternative: ADD ordered-source multiplicities."""
    out = dict(a)
    for dest, mass in b.items():
        assert type(mass) == int and mass > 0
        out[dest] = out.get(dest, 0) + mass
    return out

def brc_serial(a, b):
    """Typed positive BRC serial path composition, with occurrence addition."""
    out = defaultdict(int)
    for av, ac in a.items():
        for bv, bc in b.items():
            out[tuple(x+y for x,y in zip(av, bv))] += ac*bc
    return dict(out)

def matmul(a, b):
    out = [[{} for j in range(2)] for i in range(2)]
    for i in range(2):
        for k in range(2):
            for j in range(2):
                if a[i][k] and b[k][j]:
                    out[i][j] = brc_recoalesce(out[i][j], brc_serial(a[i][k], b[k][j]))
    return out

def transfer(left, right):
    return [[{unit(vertex(left[i],right[j])):1} for j in range(2)] for i in range(2)]

def three_block():
    A,B,C=(transfer(LAYERS[i], LAYERS[(i+1)%3]) for i in range(3))
    return matmul(matmul(A,B),C)

def terminal_signed_lift(histogram):
    """Exact zero-six-axis Cell observer; signed choices are independent."""
    mass=0
    for occurrences, count in histogram.items():
        if any(n%2 for n in occurrences):
            continue
        choices=1
        for n in occurrences:
            choices *= comb(n,n//2)
        mass += count*choices
    return mass

def represent(poly):
    return {"".join(map(str,k)):v for k,v in sorted(poly.items())}

def block_counts(kmax=12):
    T=three_block()
    identity=[[{ZERO:1} if i==j else {} for j in range(2)] for i in range(2)]
    curr=identity
    rows=[]
    for k in range(kmax+1):
        observed=curr[0][0]
        port_words=sum(observed.values())
        assert port_words == (1 if k==0 else 2**(3*k-1))
        z=terminal_signed_lift(observed)
        assert (z==0) if k%2 else (z>0)
        rows.append({
            "m":3*k,
            "port_endpoint_source_words":port_words,
            "joint_x6_cell_port_positive_brc_paths":z,
            "whole_signed_source_population":4**(3*k),
            "state_histogram_terms":sum(len(curr[i][j]) for i in range(2) for j in range(2))
        })
        if k<kmax:
            curr=matmul(curr,T)
    return rows

def parity(xs):
    inv=sum(xs[i]>xs[j] for i in range(4) for j in range(i+1,4))
    return -1 if inv%2 else 1

def outgoing(port, chi):
    result=[]
    for v in map(int,port):
        u=next(x for x in map(int,port) if x!=v)
        rest=[x for x in V if x not in (v,u)]
        nxt=rest[0] if parity([v,u,rest[0],rest[1]])==chi else rest[1]
        result.append(("".join(map(str,sorted((v,nxt)))),v))
    return result

def direct_signed_dp(chi, maximum=12):
    """Independent signed source-state recurrence; no histogram reduction."""
    curr={("01",ZERO):1}
    totals={}
    for m in range(maximum+1):
        totals[m]=curr.get(("01",ZERO),0)
        if m==maximum: break
        nxt=defaultdict(int)
        for (port,signed),count in curr.items():
            for newport,v in outgoing(port,chi):
                for sign in (-1,1):
                    new=tuple(signed[i]+sign*(i==v) for i in V)
                    nxt[(newport,new)]+=count
        curr=dict(nxt)
        assert sum(curr.values())==4**(m+1)
    return totals

def verify():
    T=three_block()
    assert sum(sum(sum(p.values()) for p in row) for row in T)==16
    assert T[0][0]=={
        (3,0,0,0):1,(1,1,1,0):1,(1,1,0,1):1,(0,3,0,0):1
    }
    assert T[1][1]=={
        (0,0,3,0):1,(0,0,0,3):1,(1,0,1,1):1,(0,1,1,1):1
    }
    rows=block_counts(12)
    got={row["m"]:row["joint_x6_cell_port_positive_brc_paths"] for row in rows}
    expected={0:1,6:88,12:61160,18:96403768,24:211907632744,
              30:544635063751488,36:1532744178320344712}
    for m,n in expected.items(): assert got[m]==n,(m,got[m],n)
    for chi in (-1,1):
        actual=direct_signed_dp(chi)
        for m,n in actual.items():
            if m%3==0: assert got[m]==n,(chi,m,got[m],n)
            else: assert n==0,(chi,m,n)
    return {
        "schema":"R762GZ_POSITIVE_BRC_THREE_BLOCK_EVIDENCE_V1",
        "model":"R762GY_K4_SIGNED_STAR_ENDPOINT_CHOICE_CANDIDATE",
        "interface":"POSITIVE_BRC_SERIAL_RECOALESCENCE_ON_NAMED_PORT_OCCURRENCE_HISTOGRAM",
        "signs":"TERMINAL_INDEPENDENT_SIGN_REFINEMENT_NOT_SIGNED_BRC_MASS",
        "observer":"FULL_SIGNED_X6_CELL_AND_NAMED_PORT_01_AT_FIXED_EVENT_LENGTH",
        "source_provenance":"ORDERED_MULTIPLICITY_RETAINED; PER_WORD_ORDER_NOT_RECONSTRUCTED",
        "future_gate_scope":"PORT_AND_NEW_INDEPENDENT_SIGN; NO_LINK_OR_HISTORY_DEPENDENT_GATES",
        "frozen_science":"taskbook@857280d1012943290d141d1317179c40ec3cbdf8;P000@a72226e2430ffa4786321ac86e7f0c599d5f0389",
        "three_block_entries":[[represent(T[i][j]) for j in range(2)] for i in range(2)],
        "direct_signed_dp_checked_through_m":12,
        "three_event_block_checked_through_m":36,
        "counts":[row for row in rows if row["m"]%6==0],
        "author_checker":"PASS",
        "independent_review":"NOT_REVIEWED"
    }

if __name__=="__main__":
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
