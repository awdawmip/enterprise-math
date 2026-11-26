# PREFIX-1119 — independent lacunarity audit, sharper cubic constant and close-pair extension

2026-11-27. RESEARCH_DRIVER EM-DVR-DEBB5E, own existing custody/session readback and historical DA-2C461358FCCA215C8753 receipt verified; no native disposition. Original author EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322, source 26bb7627e794f4081e3b4002ce78cb1743581224:research_notes/portable_direct/2026-11-27_r6_prefix1119_cubic_cluster_lacunarity.md; Activity association commit 8ae55266fc1090edcbe451400dc0032ca4ed4ff1. Shared context, independent arithmetic implementation and new deduction, not blind discovery. Retain the frozen Stage46 signed BRC carrier, P000 V5, observer/time companions, sign, phase, branch order and multiplicity as in author source. Integer relations below are auxiliary arithmetic, not a native plane or a change to native propagation. Inherit density/sign correspondence and the validity of the 8800 coefficient intervals; prior analytic command exits remain unconfirmed.

## 1. Audit and stronger cubic lacunarity

Write f(m)=rho*m+c+d/m, d>0, E>0; true hit (m,j) has |f(m)-j|<=E/m², m positive integer, j integer. Consider a fixed dyadic grid [L,2L), and the collinearity and uniqueness hypotheses d/10+2E/L<1, 2E/L²<1. A triple window has at least three true hits. Let its unique line have primitive slope p/q, q>0. Assume q>16E/d for the windows concerned, as certified for Stage46 below.

The author's proof is valid: for delta=rho-p/q, subtraction of two hit equations gives delta=d/(ab)+(e_b-e_a)/(b-a), e_m=f(m)-j_m. Since a,b in [L,2L) and b-a>=q, d/(8L²)<delta<9d/(8L²). Same slope in a later window forces L'<3L, so at most two dyadic starts per slope. For different slopes, 1/(qq')<=|delta-delta'|<=9d/(8L²). The author's q²<=16EL/d gives L'>=L³/(18E)². The small-q eventual argument is valid: for bounded q an unbounded subsequence of pair windows must have fixed slope rho=p/q and then fixed intercept c=h/q, leaving residual d/m>E/m². No irrationality hypothesis is needed. The author conclusion controls triples only.

**New improvement.** Reuse the independently proved PREFIX-1118 exact spacing envelope (0304624ff1f72c29996f5eaf0371213fc9ed8e1f:research_notes/driver/2026-11-27_prefix1118_determinant_and_sharp_triple_spacing_audit.md): for three true hits a<b<z<2L, q²<2Ez/d, in particular q²<4EL/d. The endpoint gap z-a>=2q. Consequently
 |delta-d/(az)|/(d/(az)) <= (E/(2qd))*(z/a+a/z) <5/64,
 since z/a<2, q>16E/d. Put K=69/64. Thus 0<delta<Kd/(az) and
 q² delta² < 2K² E d/(a² z) <=2K² E d/L³.
 For a distinct later slope on the same grid, L'>=2L and delta'<Kd/L'²; hence
 q² delta'² < (4EL/d)*K²*d²/(16L⁴)=K² E d/(4L³).
 Both slopes have positive delta. Thus q² |delta-delta'|² <=max(q² delta²,q² delta'²)<2K² E d/L³. Rational separation yields q'²>L³/(2K² E d). Applying q'²<4EL'/d proves
 **L' > L³/(8K² E²) = 512 L³/(4761 E²).**
 This improves the author's denominator constant 324E² by factor 324*512/4761=34.843100189... . No new assumption beyond the grid, prior exact triple-spacing envelope and the author's q cutoff. The earlier equal-slope bound and at most two windows per slope remain valid. For Stage46 E=400000, first possible triple start >=M=16225927682921336339157801028812800000000 (finite verification below), so the next distinct triple slope starts strictly above 2.87131212558156e108, rather than the author's 8.240690725003511e106. This is a conditional separation lower bound, not existence of a triple. Normalized y=L/sqrt(8K² E²) obeys y_next>y³. The author also correctly applies Legendre since q² delta<=18E/L<1/2; the new endpoint estimate gives q² delta<2K E/L.

## 2. New extension from triples to close pairs

For any dyadic window with at least two hits, retain its primitive slope p/q. If more than two occur, assume the same collinearity as above; with exactly two it is automatic. Fix A>0 and 0<theta<1. Call such a window thin in denominator if q<=A L^theta. Assume q>16E/d (eventual by the argument above, or certified).
 For two thin windows with distinct slopes at L<=L', the same positive slope estimates imply
 1/(q q') <= |delta-delta'| <= K0/L², K0=9d/8.
 Combining q<=A L^theta and q'<=A L'^theta gives
 **L' >= (L^(2-theta)/(K0 A²))^(1/theta).**
 Put S=(K0 A²)^(1/(2-2theta)), y=L/S and alpha=(2-theta)/theta>1. Then y_next>=y^alpha. Same slope appears at most twice on the grid (L'<3L). For starts at least L0>S satisfying the hypotheses, the number of distinct slopes up to X>=L0 is at most
 1+floor(log_alpha(log(X/S)/log(L0/S))),
 and the number of qualifying windows at most twice this. If X<L0 there are none. The count is O(log log X) for fixed A,theta,d,E. In particular a window containing a pair with scale gap <=A L^theta is thin because q divides the gap. This extends sparsity beyond triples to close pairs, even when the actual window contains exactly two hits. theta=1/2 gives cubic spacing with denominator (K0 A²)². This does not exclude unrestricted pairs, isolated hits, exact zeros or prove eventual separation. The cutoff for all bounded-denominator pairs is established independently of irrationality; no native-state equivalence inferred.

## 3. Exact Stage46 arithmetic audit

Input at 897771dcc60212121f1e222bf139da189cce0078:research_notes/portable_direct/2026-11-27_r6_prefix1117_root_8800_result.json; G=10^85. Exact BigInt calculations with new congruence-window enumeration choose the best convergent per window by a proved upper bound on candidate enumeration. For any candidate define h=q*j-p*m. For L<=m<=H, d>0, the lower bound is min((q*rl-p)*L,(q*rl-p)*H)+q*cl+q*dl/H-q*E/L² (here r,c,d are rational interval endpoints), and upper is max((q*ru-p)*L,(q*ru-p)*H)+q*cu+q*du/L+q*E/L². Round outward to the inclusive integer h interval by ceil/floor. For each h, m is in the unique congruence class -p^(-1)h mod q. The exact nonlinear filter uses cross multiplication by G*m². The cost criterion never discards any candidate; it only chooses q. This is an independent implementation, not a new asymptotic complexity claim.

Observed: all 107 dyadic windows from 10^8, 765 exact candidate checks, counts 0 for first 105 windows then 26,96; all 122 exact threshold intervals pairwise strictly disjoint (so at most one true hit for any fixed triple of coefficients). Independently reproduced Q0=660415, rational witness 127377638/5941111, small denominator margin 1.625764833215643e-7; dyadic determinant margin 0.022913734035845117. For q<=Q0, separation from P/Q (Q>Q0, gcd(P,Q)=1) yields q|rho-p/q|>=1/Q-Q0*eta, eta=max distance of rho endpoints to P/Q; a pair requires q|rho-p/q|<=(d_u Q0+2E)/L². Margins strictly positive for L>=10^8. Since q integer and Q0=floor(16E/d_l), all such pair denominators obey q>16E/d. Finite endpoint M as above. For X=10^106,10^107,10^108,10^109,10^200,10^1000, exact cubic recursion gives upper bounds 1,1,1,2,2,4 distinct groups from M (two windows per group). No individual sign resolved.

### Reproducer (JS BigInt; input object o from exact raw JSON)
```js
function audit(o){
const G=10n**85n,E=400000n,[rl,ru]=o.rho.map(BigInt),[cl,cu]=o.c.map(BigInt),[dl,du]=o.d.map(BigInt);
const floor=(a,b)=>{let q=a/b;return a<0n&&a%b!==0n?q-1n:q},ceil=(a,b)=>-floor(-a,b),min=(a,b)=>a<b?a:b,max=(a,b)=>a>b?a:b,abs=a=>a<0n?-a:a;
const mod=(a,b)=>(a%b+b)%b;
function inv(a,b){let x=1n,y=0n,c=b;while(b){let k=a/b;[a,b]=[b,a-k*b];[x,y]=[y,x-k*y]}if(a!==1n)throw Error("gcd");return mod(x,c)}
let a=rl+ru,b=2n*G,p0=0n,p1=1n,q0=1n,q1=0n,cv=[];while(b){let k=a/b;[a,b]=[b,a-k*b];[p0,p1]=[p1,k*p1+p0];[q0,q1]=[q1,k*q1+q0];if(q1>1n)cv.push([p1,q1])}
let pairs=[],counts=[],checks=0n;
for(let i=0;i<107;i++){
 let L=10n**8n*2n**BigInt(i),H=2n*L-1n,best=null;
 for(let [p,q] of cv){
  let l=rl*q-p*G,u=ru*q-p*G;
  let lo=ceil((min(l*L,l*H)+q*cl)*H*L*L+q*dl*L*L-q*E*G*H,G*H*L*L);
  let hi=floor((max(u*L,u*H)+q*cu)*L*L+q*du*L+q*E*G,G*L*L);
  let cost=max(0n,hi-lo+1n)*((H-L)/q+1n);
  if(!best||cost<best.cost)best={p,q,lo,hi,cost};
 }
 let {p,q,lo,hi,cost}=best;if(cost>1000000n)throw Error("cost");
 let pi=inv(p,q),n=0;
 for(let h=lo;h<=hi;h++){
   let r=mod(-pi*h,q);
   for(let m=L+mod(r-L,q);m<=H;m+=q){
    let j=(p*m+h)/q;checks++;let z=j*G*m*m;
    if((rl*m+cl)*m*m+dl*m-E*G<=z&&z<=(ru*m+cu)*m*m+du*m+E*G){pairs.push([m,j]);n++}
   }
 }
 counts.push(n)
}
const M=10n**8n*2n**107n;
function frac(n,d){return [n,d]}
function cmp(a,b){let x=a[0]*b[1]-b[0]*a[1];return x<0n?-1:x>0n?1:0}
let z=pairs.map(([m,j])=>[frac((j*G-cu)*m*m-du*m-E*G,G*m*m*m),frac((j*G-cl)*m*m-dl*m+E*G,G*m*m*m),m,j]).sort((a,b)=>cmp(a[0],b[0]));
if(z.length!==122||z.some((v,i)=>i&&cmp(z[i-1][1],v[0])>=0))throw Error("candidate separation");
let Q0=16n*E*G/dl,P=127377638n,Q=5941111n,eta=max(abs(rl*Q-P*G),abs(ru*Q-P*G));let L0=10n**8n;
let marg=(G-Q0*eta)*L0*L0-Q*(du*Q0+2n*E*G);let denom=G*Q*L0*L0;if(marg<=0n||Q<=Q0)throw Error("small-q margin");
let det=10n*G*L0-du*L0-20n*E*G;if(det<=0n)throw Error("det");
let nextNum=M**3n*512n,nextDen=4761n*E*E;if(nextNum<=10n**108n*nextDen)throw Error("next bound");
let maxGroups=(X,start)=>{if(X<start)return 0;let k=1,n=start,d=1n;while(n**3n*512n<=X*d**3n*4761n*E*E){n=n**3n*512n;d=d**3n*4761n*E*E;k++}return k};
return {checks:String(checks),counts,pairs:pairs.map(x=>x.map(String)),Q0:String(Q0),smallQMargin:Number(marg)/Number(denom),detMargin:Number(det)/Number(10n*G*L0),M:String(M),nextMin:Number(nextNum)/Number(nextDen),groups:[106,107,108,109,200,1000].map(k=>[k,maxGroups(10n**BigInt(k),M)]),factor:324*512/4761}
}
```
 All acceptance comparisons use integers; displayed decimal margins approximate the exact positives. No truncated computation. Earliest candidate from previous independent audit remains 4265326180744162387203315935318273935179 (the first pair visited in the new congruence scan need not be the earliest). Analytic anchors were not re-executed.

## 4. Next

Resolve rho interval precision or exploit spectral coupling; the close-pair theorem may reduce the remaining two-hit analysis by separating the thin-denominator case from q of order L. No shared Task publication, CLAIM, native Review, Result acceptance, Task or mother-objective closure. Preserve original authors and active researchers.
