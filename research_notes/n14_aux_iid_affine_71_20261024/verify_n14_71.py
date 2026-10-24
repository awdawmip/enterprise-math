#!/usr/bin/env python3
"""71st author Fraction proof checker, reusing the immutable 70th stop-model source."""
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
from fractions import Fraction as F
import json

def setup():
    src=Path(__file__).resolve().parents[1]/'n14_aux_iid_affine_70_20261024'/'verify_n14_70.py'
    if not src.is_file():
        src=Path(__file__).resolve().parent/'verify_n14_70.py' # local reproducibility package
    spec=spec_from_file_location('inherited70',src)
    m=module_from_spec(spec);spec.loader.exec_module(m)
    m.SQ.add((9,4,4))
    m.A=(11,1,2)
    m.AL=F(2585943605439642247,7450150876955541504)
    m.V=F(24633048191127045149,1862537719238885376)
    m.S=F(4173506760258937,6963200000000000)
    m.K=F(5184);m.LP=F(4680);m.LQ=m.K;m.G=m.LP+m.LQ
    return m

def check():
    m=setup()
    assert m.act(m.A)==m.act(m.B)=='C'
    pa,qa,live=m.firsthit(m.A);pb,qb,live_b=m.firsthit(m.B)
    ra=m.suffix(m.A);rb=m.suffix(m.B)
    X=pa*(1-ra[0]);Y=qa*ra[1]
    E=pb*(1-rb[0]);H=qb*rb[1]
    h=(X+Y)/(E+H);eta=X-E*h
    root,ties,strict,negative,comparisons,states,margin=m.dual()
    assert (states,comparisons,strict,len(negative))==(680,1240,1238,0)
    assert set(ties)=={(m.A,'C','Q'),(m.B,'C','Q')}
    assert root==m.V+m.G*m.AL==F(376562939953252048603,109561042308169728)
    assert (live,live_b)==(386,12)
    assert (pa,qa)==(F(75390625,3869835264),F(75390625,1451188224))
    assert ra==(F(511,512),F(1,1728),F(73,64),F(157,144))
    assert h==F(5597,163200) and eta==F(75390625,37893426905088)
    assert F(0)<m.S-h<m.S<F(1)
    assert m.AL+eta==F(2585958427839642247,7450150876955541504)
    assert m.V-m.G*eta==F(24596496152727045149,1862537719238885376)
    for j in range(4):
        assert m.forward(F(1),F(1))[j]-m.forward(F(1),F(0))[j]-m.forward(F(0),F(1))[j]+m.forward(F(0),F(0))[j]==0
    for u in (F(),F(1,7),F(1,4),F(1,2),F(3,4),F(6,7),F(1)):
        ep,eq,tp,tq=m.forward(u,m.S-h*u)
        assert ep==eq==m.AL+eta*u
        assert tp==m.V-m.G*eta*u and tp>tq
        assert tp+m.LP*ep+m.LQ*eq==root
    nxt,errors=m.next_dual()
    assert not errors and nxt==(F(10374480,2227),(9,4,0),'C','P')
    return {'status':'AUTHOR_EXACT_FRACTION_PASS_DRIVER_UNREVIEWED','states':states,'comparisons':comparisons,'strict':strict,'negative':len(negative),'ties':str(ties),'live_A':live,'nominal_A':495,'live_B':live_b,'firsthit_p':str(pa),'firsthit_q':str(qa),'h71':str(h),'eta71':str(eta),'s71':str(m.S-h),'alpha71':str(m.AL+eta),'V71':str(m.V-m.G*eta),'root':str(root),'next_dual_candidate':str(nxt)}

if __name__=='__main__':print(json.dumps(check(),indent=2))
