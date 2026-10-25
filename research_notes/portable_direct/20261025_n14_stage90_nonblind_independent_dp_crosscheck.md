# N=14 Stage90：第二实现的精确 Bellman 与占有量交叉核验（非盲）

Date: 2026-10-25. Evidence class: **PORTABLE_NONBLIND_CROSSCHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_DRIVER_REVIEW**.

## Origin and independence boundary

The current ChatGPT conversation read the author-side stage90 proof at `awdawmip/enterprise-math@9508fe3ad5d9961fb264d16a85d9957bf7c65141:research_notes/n14_aux_iid_affine_90_20261025/PROOF.en.md` **before** this check. Consequently this implementation is nonblind, may share the author's choice of dual multiplier and the two candidate tie states, and does **not** qualify as an independently authorized native Driver review. No Researcher CLAIM, Driver DA, formal Result admission or P000/X6 theorem is asserted. Native service returned `CONTROL_QUOTA` for canonical task listing and the Site credential was verified as static read-only. This note is a neutral evidence artifact, not a new Task, review, activity registration or checkpoint; registration/native synchronization remain pending.

## Recalculation, without importing stage88/stage89 scripts or their action table

Exact model: `P=(1/8,1/24,5/6)`, `Q=(1/12,1/12,5/6)`; `N=14`. Each state is `(n,a,b)`, with `a,b` denoting counts of symbols 0 and 1; `Q/P=2^(a+b)/3^a`. Recompute the 680-state Bellman recursion directly, not by copying the author's inherited stop map. Set `K=3166224876/1665893`, `lambdaP=72+8K/9=2934366408/1665893`. The P- and Q-terminal costs are respectively `K*Q/P` and `lambdaP`, and continuation cost is `1+sum(P_i*D_child)`.

Exact output:
- `D(0,0,0)=468802934844745618084160341/365033946907767585374208`.
- Exactly two tied states, `A=(7,2,3)` and `B=(12,0,1)`, each with choices immediate-Q versus continue.
- Of all alternative-action comparisons against an arbitrarily selected Bellman minimizer, 1238 have strictly positive differences, 2 are zero and none negative; smallest positive difference `40045614911/35373012221952`.
- At `A` the P/Q first-hit masses are `175/1769472` and `175/497664`; at `B` they are `48828125/725594112` and `48828125/362797056`.

Forward occupancy propagation was implemented separately from backward Bellman evaluation. Non-tied states take the newly recomputed minimizing action; at A the probability of deciding Q is `u`, and at B it is `s`, with probability otherwise assigned to continue. At the three exact points `(u,s)=(0,s89),(1/2,(s89+s90)/2),(1,s90)`, the error probabilities are equal, the P mean sample size dominates, and:

| u | both errors | max mean sample size |
|---|---|---|
| 0 | 5172392071501613543/14900301753911083008 | 24307502088163349729/1862537719238885376 |
| 1/2 | 5172392323384635143/14900301753911083008 | 24307386786988082129/1862537719238885376 |
| 1 | 5172392575267656743/14900301753911083008 | 24307271485812814529/1862537719238885376 |

Here `s89=29743962535332427/41779200000000000` and `s90=29733408254700427/41779200000000000`. The two endpoint differences `tP-tQ` are respectively `2166717554273724305/3725075438477770752` and `2167774451913429905/3725075438477770752`, both positive. The recovered affine slope agrees exactly with `-(lambdaP+K)=-6100591284/1665893` and the segment width is `291531275/8622859811291136`.

Reproduction sketch below is self-contained and uses only Python's exact `Fraction` and `defaultdict`. It neither imports the predecessor scripts nor assumes the predecessor's action table.

~~~python
from fractions import Fraction as F
from collections import defaultdict

N=14
P=(F(1,8), F(1,24), F(5,6))
Q=(F(1,12), F(1,12), F(5,6))
K=F(3166224876,1665893)
LP=F(72)+F(8,9)*K
A,B=(7,2,3),(12,0,1)

def child(st,i):
    n,a,b=st
    return (n+1,a+(i==0),b+(i==1))

D={};action={};ties=[];positive=[];zero=0
for n in range(N,-1,-1):
    for a in range(n+1):
        for b in range(n-a+1):
            st=(n,a,b)
            costs={'P':K*F(2**(a+b),3**a),'Q':LP}
            if n<N:
                costs['C']=F(1)+sum((P[i]*D[child(st,i)] for i in range(3)),F())
            val=min(costs.values())
            D[st]=val
            winners=[z for z,c in costs.items() if c==val]
            action[st]=winners[0]
            if len(winners)>1:ties.append((st,tuple(winners)))
            for z,c in costs.items():
                if z==action[st]:continue
                if c==val:zero+=1
                else:
                    assert c>val
                    positive.append(c-val)

assert len(D)==680 and len(positive)==1238 and zero==2
assert {st for st,_ in ties}=={A,B}
assert min(positive)==F(40045614911,35373012221952)
assert D[(0,0,0)]==F(468802934844745618084160341,365033946907767585374208)

def forward(u,s):
    states={(0,0,0):(F(1),F(1))}
    ep=eq=tp=tq=F()
    firsthit={}
    for n in range(N+1):
        nxt=defaultdict(lambda:(F(),F()))
        for st,(pm,qm) in states.items():
            if st==A or st==B:
                if st==A:firsthit['A']=(pm,qm);fraction=u
                else:firsthit['B']=(pm,qm);fraction=s
                ep+=pm*fraction
                pm*=1-fraction
                qm*=1-fraction
                z='C'
            else:z=action[st]
            if z=='P':eq+=qm
            elif z=='Q':ep+=pm
            else:
                assert n<N
                tp+=pm;tq+=qm
                for i in range(3):
                    ch=child(st,i)
                    ap,aq=nxt[ch]
                    nxt[ch]=(ap+P[i]*pm,aq+Q[i]*qm)
        states=nxt
    assert not states
    return ep,eq,tp,tq,firsthit

s89=F(29743962535332427,41779200000000000)
s90=F(29733408254700427,41779200000000000)
alpha89=F(5172392071501613543,14900301753911083008)
eta=F(291531275,8622859811291136)
V89=F(24307502088163349729,1862537719238885376)
for u,s in ((F(),s89),(F(1,2),(s89+s90)/2),(F(1),s90)):
    ep,eq,tp,tq,fh=forward(u,s)
    assert ep==eq==alpha89+eta*u
    assert tp>=tq
    assert tp==V89-(LP+K)*eta*u
    assert fh['A']==(F(175,1769472),F(175,497664))
    assert fh['B']==(F(48828125,725594112),F(48828125,362797056))
print('NONBLIND_EXACT_CHECK_PASS')
~~~

## Scope and next action

This is a fresh exact-rational computational corroboration of the author's finite iid stage90 claims, **not** independent original discovery. It does not check manuscript novelty, the author's raw terminal-suffix enumeration, stage91, full native X6/Heartbeat transfer, or independent Driver eligibility. Author inputs were visible first; there is no clean-blind review. For formal consumption, a genuinely authorized Driver must read the exact frozen Result and existing review set, disclose source exposure, check contribution overlap, and use the native review/reference/synthesis/follow-up contracts. No additional Task is proposed from this corroboration alone.

Global knowledge read snapshot: `awdawmip/chatgpt-global-knowledge@496bf491114433250b753d57d1294de0ecda0382`. Source math snapshot: `awdawmip/enterprise-math@9508fe3ad5d9961fb264d16a85d9957bf7c65141`. No P000 modification.
