# R5: global minimum is three positive Blackwell coupling edges, with an exact one-parameter minimizer locus

Date: 2026-11-10 (Asia/Shanghai). Status: author-side exact proof and local rational/SymPy verification; independent Source mathematical review pending.

## Frozen sources and theorem domain

The *same auxiliary seven-likelihood-ratio P/Q–BRC Blackwell model* used in PR #1939, commit `9f39dc7f2145548c2a9a04e387d9f33fdec1ce4e`, is fixed throughout. Preserve account frozen science pin `a01383f825ef9d43b4b754254303298c64041568` and EM frozen pin `86149263e38c22292c9def1e0f69092efa1be77e`. These are provenance pins, not refreshed scientific assumptions. The ratios are
[
r=(1/10,,1/2,,3/4,,1,,5/4,,3/2,,19/10).
]
A coupling `E_(i,j)>=0` has source columns `j in {0,1,2,3,5,6}` (column 4 has zero source mass), target rows `i=0,...,6`, with only `(0,0)` and `(6,6)` allowed in source columns 0 and 6. It satisfies exactly
[
sum_jE_{ij}=mu_i,quad sum_iE_{ij}=
u_j,quad
sum_i r_iE_{ij}=r_j
u_j.
]
The source physical parameters are `x=(g,a,b,u,v,w,z)`, target `y=(G,A,B,U,V,W,Z)`. Both obey the 13 capacity inequalities of PR #1939. The source has `g=b`, target `G=1, Z=A/10`, and the two stopping-time expectations agree. The physical-to-statistical mass functions and stopping-time formulas are **unchanged** from the frozen PR #1939 verifier.

## Main result: global sharp bound and complete equality case

**Theorem.** Over *all* physically lawful source/target pairs in this frozen model admitting a Blackwell coupling, the minimum number of positive coupling edges is **three**. Every pair with a three-edge coupling is, in physical parameters, exactly
[
oxed{x=y=(1,1,1,27/80,v,27/80,1/10),quad 1/10le vle13/40.}
]
For such a pair the **unique** coupling with three positive edges is diagonal, supported on
[
oxed{{(0,0),(3,3),(6,6)}.}
]
Its exact edge masses are
[
oxed{E_{00}=E_{66}=s(v)=rac{7933}{36000}+rac{67}{162}(v-1/10),quad E_{33}=1-2s(v).}
]
Both endpoints are included; all three masses remain strictly positive on the entire interval. In particular at `v=1/10` the weights are
[
(E_{00},E_{33},E_{66})=(7933/36000,,10067/18000,,7933/36000).
]
This is a **global minimum of the number of positive edges**, not a claim that all physical strategies can use three edges. PR #1939 independently identifies a local 14/15-edge transition; the present theorem classifies the opposite extreme.

### Proof 1: at least three source columns carry positive mass

Write `d=v-z`. The source capacity inequalities and `g=b` imply
[
0le ale ble1,quad 0le ule13a/40+b/80,quad
0le wle3a/40+21b/80,quad
0le zle a/10,quad 0le dle9b/40.
]
Necessarily `b>0`: if `b=0`, these inequalities force `a=u=v=w=z=0` and source second stopping time is exactly 1. The target has `G=1` and nonnegative physical variables, so its second stopping time is at least 2, contradicting the required equality.

The source mass in column 3 is
[

u_3=(1-b)+(a/10-z)+(9b/40-d)+191(u+w)/450+43z/90+14d/81.
]
All terms are nonnegative. Since `0le dle9b/40`,
[
oxed{
u_3ge1-b+7b/180>0}.
]
The source masses of columns 0 and 6 are
[

u_0=509u/900+47z/180+67d/162+w/100,qquad

u_6=u/100+47z/180+67d/162+509w/900.
]
Both are strictly positive simultaneously whenever at least one of `u,w,z,d` is positive. Then columns `0,3,6` are all positive. If instead `u=w=z=d=0`, the masses `
u_1=13a/40+b/80>0`, `
u_5=3a/40+21b/80>0` accompany `
u_3>0`. Thus every lawful source has **at least three** strictly positive source columns, regardless of which target is Blackwell-feasible. Every coupling consequently has at least three positive edges.

### Proof 2: three edges force identical statistical margins

If there are exactly three coupling edges, Step 1 implies exactly three source columns are positive and each contains **one** edge. For a positive column `j` with sole edge `(i,j)`, the exact moment equation yields `r_i=r_j`. The seven displayed likelihood ratios are pairwise distinct. Therefore `i=j` for each active source column, the coupling is diagonal and `mu=
u`.

### Proof 3: physical capacities upgrade equal statistical margins to x=y

Solve the five physical equalities (including the two stopping times) together with the seven linear equations `mu=
u`. Their exact rational coefficient matrix has rank **9** in the 14 physical coordinates, leaving five affine parameters. Writing `Z=y_z`, `z=x_z`, `Delta=Z-z` and retaining target `U,V,W`, the *entire* affine solution is
[
egin{aligned}
y&=(1,10Z,1,U,V,W,Z),\
x&=igl(1+kappaDelta, 10Z+kappaDelta, 1+kappaDelta, 
U+lambdaDelta, V-gammaDelta, W+lambdaDelta, zigr),
end{aligned}
]
where
[
kappa=49400/295513,quad
lambda=33345/591026,quad
gamma=132145/295513.
]
Direct substitution proves all equations; the five columns in this parameterization are independent, and rank 9 proves completeness. Two *original* physical source-capacity slacks are
[
1-x_g=-kappaDeltage0,qquad
x_a/10-x_z=(300453/295513)Deltage0.
]
The coefficients are positive, forcing `Delta=0`. Therefore `x=y`, not merely equality of current statistics. This is an exact example where the physical inequalities eliminate a one-dimensional affine observation fiber that the moment readout alone cannot distinguish.

On this lawful equality locus the parameters are necessarily
[
x=y=(1,a,1,u,v,w,a/10)
]
with `0le ale1`, `0le ule13a/40+1/80`, `0le wle3a/40+21/80`, and `a/10le vle a/10+9/40`. The two stopping-time equalities hold identically. This is a four-dimensional relative physical family.

### Proof 4: classify precisely when its source has three positive columns

On the equality locus, `
u_3>0`, and `
u_0,
u_6` are either both positive or both zero.

If both vanish, the positive-coefficient formulas force `u=w=z=v-z=0`, hence `a=0`; this leaves the **four** positive columns `1,2,3,5`. If both are positive, having just three positive columns means `
u_1=
u_2=
u_5=0`. The mass formulas
[

u_1=13a/40+1/80-u,quad

u_2=(1-a)/2,quad

u_5=3a/40+21/80-w
]
imply successively `a=1`, `u=27/80`, `w=27/80`, `z=1/10`, and the capacity interval `1/10le vle13/40`. All other margins vanish, and the three displayed masses are positive. Their diagonal coupling obeys all 21 Blackwell equations and has exactly three positive edges. Steps 1–4 prove the theorem.

## Additional reusable six-edge interior family

In the strict four-dimensional subregion
[
0<a<1,quad
0<u<13a/40+1/80,quad
0<w<3a/40+21/80,quad
a/10<v<a/10+9/40,
]
all six permitted source columns `0,1,2,3,5,6` are positive; the unique minimum-support coupling has six diagonal edges. One exact example is
[
x=y=(1,1/2,1,1/20,1/10,1/16,1/20),
]
whose positive masses, in source-column order `(0,1,2,3,5,6)`, are
[
(40589/648000, 1/8, 1/4, 82711/324000, 19/80, 45089/648000).
]
The same one-edge-per-column/martingale argument proves six is minimal for this source.

## Evidence, model scope and next inquiry

`VERIFY.py` uses exact rational SymPy algebra, verifies rank 9, the five-dimensional parameterization, the pair of sign-forcing physical slacks, the complete explicit three-edge family at two endpoints and one interior point, all 21 Blackwell identities, and the six-edge example. `EXACT_OUTPUT.txt` is its *actual local execution output*. The human proof supplies the universal nonnegative inequalities and support argument; finite tested parameter values are witnesses, not the universal proof.

BRC/observer reading: a five-dimensional equal-statistics **affine** fiber is reduced by the stated capacities to a four-dimensional physical equality locus. The seven likelihood ratios are auxiliary statistical states, not the locked six P000 spatial axes or native heartbeat arithmetic. P000 and frozen science pins are unchanged.

**Next scientific unit:** classify physical seven-, eight- and nine-edge realizations near the four-dimensional diagonal family using exact tangent-cone feasibility, then connect these lower-support strata to the established 14/15 local bifurcation. Separately check whether the three-edge diagonal segment has a nontrivial transverse admissible Blackwell tangent, and give a rational certificate for any such branch.

Control: author-side research evidence only; formal R5 Owner/CLAIM, Source Result and independent mathematical review are separate. Native researcher `EM-DIRECT-C534A2 / TASK_RESEARCH`, activity `RA-A797EAA416A7AF97A8A79E39`.
