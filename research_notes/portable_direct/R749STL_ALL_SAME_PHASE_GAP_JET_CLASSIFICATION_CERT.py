#!/usr/bin/env python3
"""R749STL: exact classification for all same-residue cutoff gaps 6h.

Requires Python 3 and SymPy. Depends on the pinned R749STK standalone
certificate, which reconstructs source generating functions exactly.
No floating point is used in the proof or test.
"""
import json
from pathlib import Path
import sympy as s
from R749STK_SIX_PHASE_ADJACENT_JET_CERT import (e,d,E,D, universal_jet, shift_jet, independent_integer_counts)

H = s.Symbol('H', integer=True, positive=True)
AB = [(54027,118312),(74412,119707),(69363,105532),
      (60588,110455),(62019,127564),(70092,132667)]
BASE = [78,73,74,75,76,77]

def check():
    count_check=independent_integer_counts(240)
    outcome=[]
    for r,(A,B) in enumerate(AB):
        q=BASE[r]
        left=shift_jet(universal_jet(r,e,d),q)
        right=shift_jet(universal_jet(r,E,D),q+6*H)
        assert left[0]==right[0]
        a=[s.factor(left[i]-right[i]) for i in range(1,4)]
        assert s.factor(a[0]-720*(D-d))==0
        assert s.factor(a[1].subs(d,D)-4320*(e-E-H*(D-s.Rational(A,34992))))==0
        sol=s.solve(a,(e,d,E),dict=True)
        assert len(sol)==1
        sol=sol[0]
        formula={d:D,
            e:((34992*H-139968)*D-A*H-B)/69984,
            E:(-(34992*H+139968)*D+A*H-B)/69984}
        assert all(s.factor(sol[v]-formula[v])==0 for v in (e,d,E))
        assert s.factor(formula[e]+formula[E]+4*D+s.Rational(B,34992))==0
        assert s.factor(formula[e]-formula[E]-H*(D-s.Rational(A,34992)))==0
        witness1={D:s.Integer(-1),H:s.Integer(1)}
        legal3={v:s.factor(formula[v].subs(witness1)) for v in (e,d,E)}
        legal3[D]=s.Integer(-1)
        assert all(-2<legal3[v]<2 for v in (e,d,E,D))
        assert all(s.factor(ai.subs(legal3).subs(H,1))==0 for ai in a)
        # The h=2 obstruction uses e>=-2 and E<=2 from the exact 3-jet family.
        # It requires 8*A+2*B <= 559872. All six reverse strictly.
        ob=8*A+2*B
        assert ob>559872
        twojet_limit=None
        if A<=69984:
            c=s.Rational(A,34992)
            witness2={e:s.Integer(0),E:s.Integer(0),d:c,D:c}
            assert all(-2<=witness2[v]<=2 for v in (e,d,E,D))
            assert all(s.factor(ai.subs(witness2))==0 for ai in a[:2])
            depth2='all h>=2'
            witnessdesc={'e':'0','d':str(c),'E':'0','D':str(c)}
        else:
            twojet_limit=139968//(A-69984)
            assert (A-69984)*twojet_limit<=139968<(A-69984)*(twojet_limit+1)
            assert twojet_limit==({1:31,5:1296}[r])
            for h in (2,twojet_limit):
                witness2={d:s.Integer(2),D:s.Integer(2),
                          e:-s.Rational(h*(A-69984),69984),
                          E:s.Rational(h*(A-69984),69984)}
                assert all(-2<=witness2[v]<=2 for v in (e,d,E,D))
                assert all(s.factor(ai.subs(witness2).subs(H,h))==0 for ai in a[:2])
            for h in (twojet_limit+1, 2*twojet_limit+1):
                # Exact interval obstruction: smallest feasible |e-E| is
                # h*(A-69984)/34992 >4.
                assert h*(A-69984)>139968
            depth2=f'2<=h<={twojet_limit}'
            witnessdesc={'e':'-h*(A-69984)/69984','d':'2',
                         'E':'h*(A-69984)/69984','D':'2'}
        outcome.append({'residue':r,'base_cutoff':q,'A':A,'B':B,
            'common_constant_jet':str(left[0]),
            'a1':'720*(D-d)',
            'a2_after_d_eq_D':f'4320*(e-E-h*(D-{s.Rational(A,34992)}))',
            'all_three_jet_solutions':{
              'd':'D',
              'e':f'((34992*h-139968)*D-{A}*h-{B})/69984',
              'E':f'(-(34992*h+139968)*D+{A}*h-{B})/69984'},
            'h1_interior_three_jet_witness':{str(v):str(legal3[v]) for v in (e,d,E,D)},
            'h2_three_jet_necessary_LHS':ob,
            'h2_three_jet_necessary_RHS':559872,
            'h_ge_2_depth2_range':depth2,
            'h_ge_2_depth2_witness':witnessdesc,
            'h_ge_2_depth1_begin':twojet_limit+1 if twojet_limit is not None else None})
    payload={
      'unit':'R749STL',
      'frozen_scientific_source':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'source_dependency':'R749STK six-phase h=1 four-jet obstruction and three-jet witnesses',
      'population':'five labeled sources (1,1,2,3,6)',
      'cutoff_family':'all q=b_r+6k, p=q+6h, six residues r, all integers k>=0, h>=1',
      'fixed_nuisances':'e,d,E,D in [-2,2]',
      'expansion_variable':'x=1/(6j), simultaneous observation index j',
      'classification':{
          'h=1':'depth 3 for every residue',
          'h>=2,residue in {0,2,3,4}':'depth 2 for every h',
          'h>=2,residue=1':'depth 2 for 2<=h<=31; depth 1 for h>=32',
          'h>=2,residue=5':'depth 2 for 2<=h<=1296; depth 1 for h>=1297'},
      'independent_integer_count_check':count_check,
      'rows':outcome,
      'proof':'Symbolic quasi-polynomial Laurent coefficients; all h three-jet family affine in D; h=2 box obstruction; h>=2 contraction to h=2; exact two-jet feasible interval; h=1 reuse R749STK',
      'status':'AUTHOR_EXACT_NOT_REVIEWED',
      'unresolved':'finite-time/readout separation and native X6/BRC source-preserving Port transfer'
    }
    target=Path(__file__).with_name('R749STL_ALL_SAME_PHASE_GAP_JET_CLASSIFICATION_RESULTS.json')
    target.write_text(json.dumps(payload,sort_keys=True,ensure_ascii=False,indent=2)+'\n')
    print('PASS six residue phases, all positive gaps, exact sharp threshold h=31 / h=1296')
    for row in outcome:print(row['residue'],row['A'],row['B'],row['h_ge_2_depth2_range'],row['h_ge_2_depth1_begin'])
    print(target.name,target.stat().st_size)
    return payload

if __name__=='__main__':check()
