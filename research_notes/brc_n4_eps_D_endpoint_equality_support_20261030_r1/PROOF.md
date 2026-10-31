# BRC N=4: exact endpoint gaps and smallest lawful terminal support

Author analytical proof, 2026-10-30. Status: UNREVIEWED / NOT_ADMITTED. Direct continuation of PR #1756, immutable source 24fa3d1259bec2362060f70d3b58b80a99526280, research_notes/brc_n4_fixed_eps_D_joint_TV_sharp_20261030_r1/PROOF.md.

## Frozen finite BRC source / lawful actions

For s=AU,AV,BU,BV and j,k in {0,1}, the strictly positive normalized sixteen-leaf source has Q(s,j,k)=q_s/4 and P(s,j,k)=q_s*r_sj/4, where q=(1/6,1/3,1/4,1/4), r_AU=(9/10,11/10), r_AV=(1/4,1/4), r_BU=(1/5,9/5), r_BV=(2,2). The coarse C=(E,A,B) has equal P/Q masses (7/12,1/6,1/4). On BU, source J is observed through Z=J XOR Bernoulli(epsilon), 0<=epsilon<=1/2, common to both laws. BU continuation rates u0,u1 lie in [0,1]. Stopping at stage 3 gives B3; continuing reads the actual fair unchanged K, then produces B4Pk or B4Qk by the lawful behavioral decision probability d_jk. Let F_j be the conditional law on Y=(B3,B4P0,B4Q0,B4P1,B4Q1):
F_j(B3)=1-u_j;
F_j(B4Pk)=u_j*d_jk/2;
F_j(B4Qk)=u_j*(1-d_jk)/2.
S23 further requires d_j0=d_j1. No hidden leaves or physical K writes are added.

Set a_y=F0(y), b_y=F1(y), x_y=|b_y-a_y|, m_y=min(a_y,b_y), s_y=a_y+b_y=x_y+2m_y, D=TV(F0,F1), t=1-2epsilon. Then sum_y x_y=2D, sum_y m_y=1-D, sum_y s_y=2. The already-proved exact *between-law full-joint* TV, not common-decoder deficiency, is
T = TV(P_(C,Z,Y),Q_(C,Z,Y))
  = (1/20)*sum_y max(x_y,t*s_y).
Its sharp fixed-(epsilon,D) bounds are
L=max(D,t)/10; U=[D+t*(1-D)]/10.

## Theorem 1 (all-real equality cases and exact residual deficits)

For every finite pair (F0,F1) and every t in [0,1],
20*(U-T) = sum_y min((1-t)*x_y, 2*t*m_y).             (A)

If D>=t, 20*(T-L)=sum_y (t*s_y-x_y)_+.              (B1)
If D<=t, 20*(T-L)=sum_y (x_y-t*s_y)_+.              (B2)
Here h_+=max(h,0). These are exact nonnegative residual gap certificates, not approximations.

For 0<t<1, 0<D<1, the upper bound is attained exactly iff for every y either a_y=b_y or one of a_y,b_y equals zero. In words, each active output atom must carry either *identical common mass* or *one-source-exclusive mass*. The equivalent condition is x_y*m_y=0 for all y. The lower bound is attained exactly iff all atoms satisfy x_y>=t*s_y when D>t, or all satisfy x_y<=t*s_y when D<t, or x_y=t*s_y for all y when D=t. At t=0, t=1, D=0, or D=1, L=U and every admissible pair attains both endpoints; interior equality classification is not applied at these degenerate boundaries.

Proof: per atom, x+2tm-max(x,t(x+2m))=min(2tm,(1-t)x). Sum and divide by 20 for (A). Since sum x=2D and sum ts=2t, subtracting the larger sum from sum max gives (B1) or (B2), respectively. Every summand is nonnegative. For 0<t<1, a summand of (A) vanishes exactly when x=0 or m=0; (B1),(B2) similarly give all lower equality cases. The collapsed boundary intervals follow by substitution. QED.

## Theorem 2 (minimum active terminal outputs at the upper bound)

An *active atom* is a symbol y with F0(y)+F1(y)>0. The declared legal Y alphabet always has five symbols; this theorem counts the actually positive support N within it. Assume 0<t<1 and 0<D<1.

* For unrestricted abstract finite F0,F1, N_min=3 for every D: one common atom with mass 1-D under each law, one F0-only atom with mass D, and one F1-only atom with mass D. Fewer than three cannot supply common and both exclusive source masses.
* For lawful S2, N_min=4 if 0<D<1/2, N_min=3 if D=1/2, and N_min=5 if 1/2<D<1.
* For lawful S23 (k-independent decisions), N_min=5 for every 0<D<1.

Lower-bound proof. At B3 the pair of masses is (1-u0,1-u1). Upper equality forces them to be equal or one to vanish.

Case u0=u1=w: each of the k=0,1 output blocks has the same total branch mass w/2. Since each block has only two decision symbols and every shared positive atom must have *equal* mass, equality of block totals forces either (i) identical componentwise output laws for that block or (ii) disjoint deterministic P/Q decisions. An identical block contributes zero to D and needs >=1 active symbol; a disjoint block contributes w/2 to D and needs exactly two active symbols. With 0<w<1, B3 is positive common, and one disjoint block yields D=w/2<1/2 and N>=1+1+2=4; two disjoint blocks yield D=w and N>=1+2+2=5. When w=1, B3 vanishes and 0<D<1 forces precisely one disjoint block, hence D=1/2 and N>=1+2=3. w=0 gives D=0.

Case u0!=u1: unequal positive B3 masses are excluded by upper equality; hence some uj=1. If the other uj=0, the two branches have disjoint support and D=1; otherwise it lies in (0,1). Each k block then has strictly positive but unequal source total masses 1/2 versus uj/2. One active output symbol in that block would carry unequal shared mass and violate Theorem 1, so both k blocks require at least two symbols. The exclusive B3 supplies a fifth: N>=1+2+2=5. The symmetric case is identical. These exhaust S2.

Under S23, both k blocks have the same source-specific decision probabilities. Thus in the equal-continuation case they must be *both* identical (D=0) or *both* disjoint (five active symbols if 0<w<1); the single-disjoint-block S2 economy is unavailable. Unequal continuation already requires five. QED.

Sharp lawful constructions:
- If 0<D<1/2: S2 u0=u1=2D; d00=d01=d10=1, d11=0. B3 common, k=0 identical P, k=1 source-exclusive P/Q. Exactly four active atoms; TV(F0,F1)=D.
- If D=1/2: same S2 construction with u0=u1=1, so B3 disappears. Exactly three active atoms; TV(F0,F1)=D.
- If 1/2<D<1: S2 u0=u1=D, d00=d01=1 and d10=d11=0. B3 common, both k-blocks source-exclusive; five active atoms, TV(F0,F1)=D.
The last construction is also lawful S23 and works for *all* 0<D<1, proving the S23 bound. By Theorem 1 each witness attains T=U for every 0<t<1. In particular at epsilon=1/4, D=1/4,1/2,3/4, the S2 active support sizes and T are respectively (4,1/16),(3,3/40),(5,7/80).

## Verification / scientific boundary

VERIFY.js executed directly under V8 using exact normalized BigInt fractions: reconstructed the 16 strictly positive original P/Q leaves and their normalization, directly pushed BU leaves to (Z,Y), checked the formula and sharp interval over 3^6*5=3645 legal rational six-parameter/noise cases, checked the lower and strict-interior upper equality iff tests, and tested the support witnesses. RUN_EVIDENCE.txt preserves the exact execution output. An independent Python fractions.Fraction checker on the same model also passed 3645 grid checks; finite checks corroborate the analytic identities, while the continuous domain follows from the proofs above.

BRC reuse is the exact positive-weight provenance-preserving J, K and joint (C,Z,Y) observer with declared stage-4 future operators. The signed/phase interpretation is not inferred from positive mass. Native P000 six-axis Cell paths, triadic closure, separately typed time and physical dynamics are different types and need independent observation/composition bridges. No project mathematical admission, native CLAIM/Result or independent Driver review is implied.