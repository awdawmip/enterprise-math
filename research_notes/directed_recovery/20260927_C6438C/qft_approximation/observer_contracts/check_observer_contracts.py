"""Exact rational validation of observer contracts on actual native prefixes.

This enumerates complete states for checking only; it is not an efficient
certificate construction algorithm. All numerical quadratic sums are
recorded by the existing PositivePathObserver.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import gzip
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parents[1] / 'sep27-qft-research'
sys.path.insert(0, str(BASE / 'gram_research'))
from check_single_walker import (load_bank, ExactCarrierCodec,
    SelectedStreamingProgram, LazyStreamingProgram, PointRowOracle,
    serializable, packed, CALLS, verify_vendor)
from single_walker import RawRow, normalize_row


def check_case(bank, codec):
    program = LazyStreamingProgram(21, 2, 4, bank, 61, codec=codec)
    explicit = SelectedStreamingProgram(21, 2, 4, bank, 61, codec=codec)
    state, den = explicit.initial()
    frontier = [((), state, den)]
    cases, raw_evidence = [], []
    cancellation = []
    for depth in range(4):
        following = []
        for history, state, den in frontier:
            oracle = PointRowOracle(program, history)
            obs = oracle.observe
            zero = RawRow((0,)*program.dim, 1)
            v = {key[1]: normalize_row(row, den) for key, row in state.items() if any(row)}
            def total(name, values):
                return obs(name, ((x,) for x in values))
            def dot(name, left, right):
                return obs(name, ((F(x,left.den), F(y,right.den))
                                 for x,y in zip(left.values,right.values)))
            def mass(rows):
                return total('field_mass', (oracle.norm_observation(row) for row in rows.values()))
            M = mass(v)
            if not M:
                continue
            P = program.tables[depth]
            inv = oracle.inverse_table(depth)
            labels = sorted(set(v) | {P[w] for w in v})
            pairs = []
            for z in labels:
                x = v.get(z,zero)
                y = oracle.apply_feedback(depth,v.get(inv[z],zero))
                S = total('two_arm_norm', (oracle.norm_observation(x),oracle.norm_observation(y)))
                cross = dot('exact_cross',x,y)
                if S:
                    pairs.append((z,S,cross,F(1,2)+cross/S))
            L = total('absolute_coherence', (abs(c) for _,_,c,_ in pairs))
            G = total('signed_coherence', (c for _,_,c,_ in pairs))
            fair = total('fair_joint_tv', (S/(2*M)*abs(p-F(1,2)) for _,S,_,p in pairs))
            marginal = abs(total('marginal_p0', (S*p/(2*M) for _,S,_,p in pairs))-F(1,2))
            assert fair == L/(2*M)
            assert marginal == abs(G)/(2*M)
            assert marginal <= fair <= F(1,2)
            if marginal < fair:
                cancellation.append({'history':history,'joint_tv':fair,'marginal_tv':marginal})
            trials = []
            variants = {
                'scaled8':{w:RawRow(tuple(x << 3 for x in row.values),row.den) for w,row in v.items()},
                'signed_by_label':{w:RawRow(tuple((-1 if w%2 else 1)*x for x in row.values),row.den) for w,row in v.items()},
                'keep_even_labels':{w:row for w,row in v.items() if w%2==0},
                'all_zero':{},
            }
            for name,u in variants.items():
                U = mass(u)
                cross = total('full_field_overlap',(dot('row_overlap',row,u.get(w,zero)) for w,row in v.items()))
                E = obs('raw_error_squared',((M,),(U,),(-2,cross)))
                Eproj = M-cross*cross/U if U else M
                assert 0 <= Eproj <= E
                errors = []
                for z,S,c,p in pairs:
                    x = u.get(z,zero)
                    y = oracle.apply_feedback(depth,u.get(inv[z],zero))
                    Su = total('approx_arm_norm',(oracle.norm_observation(x),oracle.norm_observation(y)))
                    pu = F(1,2)+dot('approx_cross',x,y)/Su if Su else F(1,2)
                    assert 0 <= pu <= 1
                    errors.append(S*abs(p-pu)/(2*M))
                local = total('projective_local_tv',errors)
                assert local*local*M <= Eproj
                if name=='scaled8':
                    assert E==49*M and Eproj==0 and local==0
                trials.append({'variant':name,'M':M,'U':U,'raw_E':E,'projective_E':Eproj,'local_joint_tv':local})
            leakage = []
            support = sorted(v)
            for size in range(len(support)+1):
                for subset in combinations(support,size):
                    A=set(subset)
                    if A & {P[w] for w in A}:
                        continue
                    eps=1-mass({w:v[w] for w in A})/M
                    if eps<=F(1,2):
                        assert (L/M)**2 <= 4*eps*(1-eps)
                        assert fair*fair <= eps*(1-eps)
                        leakage.append({'A':sorted(A),'epsilon':eps,'fair_joint_tv':fair})
            cases.append({'history':history,'M':M,'L':L,'G':G,'fair_joint_tv':fair,
                          'marginal_tv':marginal,'projective_trials':trials,'leakage_certificates':leakage})
            raw_evidence.append({'history':history,'exact_rows':v,'oracle':oracle.evidence()})
            if depth<3:
                for bit,(child,cd) in enumerate(explicit.branches(state,den,history)):
                    following.append((history+(bit,),child,cd))
        frontier=following
    return {'N':21,'a':2,'t':4,'dimension':program.dim,'positive_prefixes':len(cases),
            'cases':cases,'strict_marginal_cancellation_examples':cancellation,
            'raw_evidence':raw_evidence,'explicit_metrics':explicit.report_metrics(),
            'full_state_enumeration_for_validation_only':True}


def main():
    sources=[Path(__file__), ROOT/'PROJECTIVE_AND_COHERENCE_BOUNDS.md',
             BASE/'gram_research/single_walker.py',BASE/'gram_research/check_single_walker.py']
    hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    first=len(CALLS)
    vendor=verify_vendor()
    bank,binding=load_bank()
    cases=[check_case(bank,ExactCarrierCodec(61,tuple(range(6)))),check_case(bank,None)]
    assert cases[0]['cases']==cases[1]['cases']
    assert hashes=={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    payload={'status':'PASS','activity':'RA-CAAAC604CB513AEA8BBC1DFC','source_hashes':hashes,
             'bank_binding':binding,'vendor':vendor,'cases':cases,'actual_core_calls':CALLS[first:],
             'scope':'bounded native exact-rational validation; no polynomial certificate implementation'}
    raw=packed(serializable(payload))
    result=ROOT/'OBSERVER_CONTRACT_RESULTS.json.gz'
    result.write_bytes(gzip.compress(raw,mtime=0))
    summary={'status':'PASS','dimensions':[x['dimension'] for x in cases],
             'positive_prefixes_each':[x['positive_prefixes'] for x in cases],
             'projective_trials':sum(len(h['projective_trials']) for x in cases for h in x['cases']),
             'leakage_checks':sum(len(h['leakage_certificates']) for x in cases for h in x['cases']),
             'strict_cancellation_examples':sum(len(x['strict_marginal_cancellation_examples']) for x in cases),
             'actual_core_calls':len(CALLS)-first,'payload_sha256':hashlib.sha256(raw).hexdigest(),
             'gzip_sha256':hashlib.sha256(result.read_bytes()).hexdigest(), 'gzip_bytes':result.stat().st_size}
    (ROOT/'OBSERVER_CONTRACT_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    main()
