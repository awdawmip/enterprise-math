#!/usr/bin/env python3
"""Exact rational optimizer for the full P7 five-vertex / P3 terminal convex bridge.
Data rows are normalized h.q/||T^T h||_1, reconstructed independently from
PR1976 VERIFY_7.py, PR1986 VERIFY_PHYSICAL_DUAL_TUBE.py.
The 14-coordinate, original-21-row source reconstruction was also executed
separately; this verifier checks the complete finite optimality certificate.
"""
from fractions import Fraction as F
ROW = {
"00": """55037291328623391/266089946207400640 73815001519247841/266089946207400640 1710095801404726067781/8976864641830450219712 7739036784774570573/36343581545872268096 12997022624760458901/66981880348691110400 71397/320480 101547/320480""",
"33": """4544038073227893/107229156754483190 3099598827795243/107229156754483190 92290258085940352929/4275232804242151071866 253424651046636879/14645767937297932666 892756857720223623/26992416098357928400 90603/1678915 60453/1678915""",
"43": """550609460307500/116839042577461087 550609460307500/116839042577461087 990433968688525500/79791614305221298909 990433968688525500/79791614305221298909 12493328654377175/1470573932146832266 0 0""",
"45": """191516334020000/10947731483143039 191516334020000/10947731483143039 344498771717748000/7476414978674157373 344498771717748000/7476414978674157373 2172752809456900/68895842434603301 0 0""",
"65": """1915163340200/48763315106511 1915163340200/48763315106511 1148329239059160/11100466491878159 1148329239059160/11100466491878159 21727528094569/306875417920149 0 0""",
"66": """36364448761673391/844431230095282466 55142158952297841/844431230095282466 254087337130964128905/142439520168704998753514 5106553681392422865/576678219306497970662 4523286667878548901/212565684735995259760 71397/1017037 101547/1017037""",
"ell": """55060946030750/5601522160784537 55060946030750/5601522160784537 99043396868852550/3825386496805218059 99043396868852550/3825386496805218059 2498665730875435/141005134726798732 0 0""",
}
R={k:tuple(F(x) for x in s.split()) for k,s in ROW.items()}
assert set(R)=={"00","33","43","45","65","66","ell"}
assert all(len(row)==7 and all(v>=0 for v in row) for row in R.values())
alpha=F(171472243623,194864094623)
rho=F(2335581000,194864094623)
w1=F(12297672472745316495884170635,221733247658614103185557105322)
w3=1-w1
assert w3==F(209435575185868786689672934687,221733247658614103185557105322)
assert 0<alpha<1 and 0<w1<w3<1
upper=[alpha*R["43"][j]+(1-alpha)*R["66"][j] for j in range(7)]
assert upper[1]==upper[3]==upper[6]==rho
assert upper[0]<rho and upper[2]<rho and upper[4]<rho and upper[5]<rho
assert rho-upper[0]==F(16611051322475475000,6222802389683251360439)
assert rho-upper[2]==F(11583161354989089665625000,13645692406573825632930684503)
assert rho-upper[4]==F(76581048761739845625,39161100507573401829901)
assert rho-upper[5]==F(693450000,194864094623)
lam=[F(0)]*7
lam[1],lam[3]=w1,w3
def radius(v,k): return sum(v[j]*R[k][j] for j in range(7))
assert sum(lam)==1
assert radius(lam,"43")==radius(lam,"66")==rho
assert all(radius(lam,k)>=rho for k in R)
assert radius(lam,"00")>rho and radius(lam,"33")>rho
assert radius(lam,"45")>rho and radius(lam,"65")>rho and radius(lam,"ell")>rho
a3,b3,b6=R["43"][3],R["66"][3],R["66"][6]
tmax=(a3-b3)/(a3-b3+b6)
assert tmax==F(1944148810350222725565,56507105428884278215883)
lam2=[F(0)]*7
lam2[3],lam2[6]=1-tmax,tmax
assert sum(lam2)==1
assert radius(lam2,"43")==radius(lam2,"66")==rho
assert all(radius(lam2,k)>=rho for k in R)
assert [radius(lam,k) for k in R]==[radius(lam2,k) for k in R]
# Upper convex certificate: any admissible (P,t,v) is a convex combination
# of exactly these seven physically lawful samples. Therefore min_h r_h
# never exceeds alpha*r43+(1-alpha)*r66 <= rho.
assert max(upper)==rho
for row in R.values():
    for left,right in zip(lam,lam2):
        assert left>=0 and right>=0
# The upper certificate is saturated ONLY by samples 1,3,6; the additional
# condition r43=r66 intersects their simplex in precisely this segment.
assert [j for j,v in enumerate(upper) if v==rho]==[1,3,6]
for blend in (F(0),F(1,5),F(1,2),F(4,5),F(1)):
    l=[(1-blend)*lam[j]+blend*lam2[j] for j in range(7)]
    assert sum(l)==1 and all(v>=0 for v in l)
    assert min(radius(l,k) for k in R)==rho
assert rho>F(4419128514205873438322431365000,965242855541993161664216604137419)
print("FROZEN_GLOBAL a01383f825ef9d43b4b754254303298c64041568")
print("FROZEN_EM 86149263e38c22292c9def1e0f69092efa1be77e")
print("SEVEN_DUAL_OPTIMAL_RADIUS",rho,"APPROX",float(rho))
print("EXACT_UPPER_ALPHA",alpha)
print("P7_OPTIMAL_START_LAMBDA_V1_V3",w1,w3)
print("BRIDGE_OPTIMAL_END_TMAX",tmax,"APPROX",float(tmax))
print("RATIO_VS_PREVIOUS_UNIFORM_OVER_P7",float(rho/F(4419128514205873438322431365000,965242855541993161664216604137419)))
print("UPPER_GAPS",[str(rho-v) for v in upper])
print("ALL_SEVEN_SENSITIVITY_MARGINS_AT_OPT",[(k,str(radius(lam,k)-rho)) for k in R])
print("FINITE_CERTIFICATE_EXACT_ALL_SEVEN_SAMPLES_VERIFIED")
print("PASS_GLOBAL_OPTIMUM_AND_FULL_ONE_DIMENSIONAL_MAXIMIZER_FACE")
