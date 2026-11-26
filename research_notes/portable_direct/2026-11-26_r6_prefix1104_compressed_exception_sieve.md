# PREFIX-1104 — Compressed exact sieve for exceptional integer BRC edges

2026-11-26. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / FINITE_EXACT_INTEGER_AUXILIARY_COMPUTATION / NOT_REVIEWED. R6 continuation, RA-0ABD84561C86E53067DB0322, EM-DIRECT-780BBE / TASK_RESEARCH. Original own registration r6-20261123-2358-session-start-own-v1 verified SUCCEEDED. Prior LEASED query r6-20261126-1354-owner-read-v1 SUCCEEDED, empty as of 05:55:34 UTC; fresh r6-20261126-1453-owner-read-v1 queued, no shared claim or ownership authority inferred. Independent continuation only.

Frozen science unchanged: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json, X6 chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Use inherited native radial BRC observer D_m(k)=L[x^m(1-x)^k], preserving native signed/phase/ordered joint carrier. This auxiliary sieve acts solely on its integer edge and does not replace or rerun native propagation.

Parents:
- 0380a3e84a3c9d4031dba6d278c88490f4aa4385:research_notes/portable_direct/2026-11-26_r6_prefix1103_quantitative_sparse_integer_edge.md
- 4b000fd990a72817573fa4bb2c0a09c2dc8ded70:research_notes/portable_direct/2026-11-26_r6_prefix1102_sparse_integer_edge.md
- f0476c7795f31809302dae513504a06d1e9a9e4c:research_notes/portable_direct/2026-11-26_r6_prefix1101_adaptive_precision.md
- 0919218e87c1f6a094123bb19ff315c17846b778:research_notes/portable_direct/2026-11-26_r6_prefix1096_second_order_last_negative_edge.md

## 1. From counting to compressed enumeration

Inherit: every sufficiently large fast-oracle exception m has integer j with
|j-(rho*m+c+d/m)| <= C/m^2, 9<d<10, common finite C, m>=m0. C and m0 not yet numerical.
For each dyadic block [M,2M) choose rational r/D,s/D,t/D approximating rho,c,d, respectively, with absolute errors <=1/(24M^3),1/(12M^2),1/(6M); choose t/D in (9,10). Such rational approximations require O(log M) bits, available in asymptotic polynomial bit cost under 1101 and the derivative formulas of 1096 (the simple-root denominator is nonzero). Set A=a/D>=C+1, with A bounded independently of M. Then for every m in block,
m^2 |(rho-r/D)m+(c-s/D)+(d-t/D)/m|<=1.
Hence the true exceptional pairs lie in the rational band
|j-f(m)|<= A/m^2, f(m)=(r m+s+t/m)/D.
Exact enumeration of this band is a conservative candidate filter, not proof every candidate actually needs CT. No numerical C or finite starting threshold is claimed. If C and m0 become explicit, the sieve immediately has effective input.

Theorem. For M>=4, M>A and M>=m0, the rational band on [M,2M) can be represented exactly as a bounded number of arithmetic progressions of lattice pairs, with computation polynomial in log M and the bit lengths of rational input parameters. This includes singleton candidates, not merely nonsingleton lines. The output is compressed; expanding all points costs at least their number.

## 2. Enclosing strip is itself exactly collinear

Partition the integer block using endpoints floor(i*M/4) for i=0..4. A nonempty subblock has integer endpoints l,h and L=h-l<=M/4. Let H(x) be the chord of f at l,h, or its reciprocal-term tangent when l=h. Explicitly,
H(x)=(r/D-t/(D*l*h))*x + s/D+t*(l+h)/(D*l*h).
The exact chord defect for l<=x<=h is
H(x)-f(x)=(t/D)*(x-l)*(h-x)/(l*h*x),
between 0 and (t/D)*L^2/(4M^3). Consequently every band pair is contained in the strip
H(m)-(t/D)*L^2/(4M^3)-A/M^2 <= j <= H(m)+A/M^2.
Its vertical width W <= 10/(64M)+2A/M^2 < 1 under the stated conditions. For any three lattice pairs inside the strip, the determinant T of PREFIX-1103 cancels the affine H exactly. Their deviations from H belong to one interval of width W, so |T| <= (m3-m1)*W <= 10/256 + A/(2M) <1. Since integer, T=0. This proves collinearity of ALL lattice points in the outer strip, a stronger statement than collinearity only of exceptional pairs. At each m there is at most one j. Convexity of the strip means all lattice points between the first and last ones on the line are included: if there are n>=2 points, their step q=(m_last-m_first)/(n-1), p=(j_last-j_first)/(n-1) are integers and the lattice sequence has exactly these n points (primitive direction). n=1 is retained.

## 3. Count and locate strip without scanning

Write upper and lower as (u*m+U)/v and (u*m+L0)/v for common positive integer v. The exact number in [i,j] is
sum_{m=i}^j [floor((u*m+U)/v)+floor((-u*m-L0)/v)+1].
This follows from ceil(x)=-floor(-x). Evaluate each sum by Euclidean floor-sum recurrence, normalizing signed slope/intercept with floor division. Proof of the recurrence: after stripping integer multiples of v, 0<=a,b<v, interchange lattice rows and columns of the set 0<=i<n, 1<=y<=floor((a*i+b)/v). The standard reduction uses y=a*n+b, n'=floor(y/v), b'=y mod v and swaps v,a; when y<v the remaining sum is zero. Each nontrivial swap reduces the denominator as in Euclid. Thus O(log v) arithmetic steps; all intermediates have polynomial bit length. Two binary searches on subinterval counts recover the first and last lattice points, O(log M) counts. Even a strip with Theta(M) points is recovered in compressed form. No enumeration of m or scan of rational denominators.

## 4. Exact band filter along the line

For a strip progression m=x+qi, j=y+pi, 0<=i<n, define the integer cubic
P(i)=(D*j-r*m-s)*m^2-t*m.
The rational band is exactly -a<=P(i)<=a, including equality. Evaluate integer-polynomial nonnegative intervals by recursion on forward differences (degree falls by one). Each consecutive run of nonnegative differences gives a nondecreasing sequence; each complementary run is decreasing. Binary search the zero threshold on each monotone interval and merge adjacent intervals. Fixed degree 3 gives a bounded number of runs independent of M, O(log M) evaluations with polynomial bit length. Intersect runs for a+P>=0 and a-P>=0. Alternatively the two cubics have at most six real roots in total, unless one is identically zero, so a conservative bound is 13 runs per subblock, at most 52 per dyadic block. In fact the observed cases are much smaller. This proves compressed exact enumeration and the ability to identify every certainly nonexceptional m in a whole block without testing each m. The union is a superset of actual fallback locations, not a uniform separation result or an assertion of cheap CT. Whole-range [1,N] eventual output has O(log N) descriptors and polynomial(log N) preprocessing under the inherited precision supply and explicit startup constants. Actual enumeration of candidates and exact sign cost remain separate.

## 5. Executed exact auxiliary evidence

JavaScript BigInt, no floating decisions, no classical propagation or trigonometry. 42,237 signed floor-sum tests; 3,465 cubic sign interval tests; 512 full block comparisons against brute force (20 qualifying pairs across those cases); 5 tangent cases checked by independent exact inequality. Tangent parameters vary with M: D=2M^2,r=21D+19,s=-38M,t=19M^2,a=D. Thus rho=21+19/(2M^2), c=-19/M, d=19/2,A=1. At m=M+h, f(m)-21m=(19/2)h^2/(M^2*m). Test 19*h^2*(M+h)<=2*M^2.
M | strip points in first quarter | exact band candidates
10000 | 782 | 33
1000000 | 78126 | 325
100000000 | 7812501 | 3245
10000000000 | 781250001 | 32445
100000000000000000000 | 7812500000000000001 | 3244428423
All tangent candidate sets represented by one arithmetic progression with step 1. These are synthetic input tests, not a new computation of the frozen Stage46 observer. Existing 18 true row certificates unchanged.

Reproduction (Node-compatible JS; executed as equivalent function body with return; below uses console.log for standalone):
```javascript
function fd(x,y){if(y<=0n)throw Error("denominator");return x>=0n?x/y:-((-x+y-1n)/y)}
function fs(n,m,a,b){
  let q=fd(a,m),z=fd(b,m),v=q*n*(n-1n)/2n+z*n;
  a-=q*m;b-=z*m;
  while(true){
    if(a>=m){v+=(n-1n)*n*(a/m)/2n;a%=m}
    if(b>=m){v+=n*(b/m);b%=m}
    let y=a*n+b;if(y<m)return v;
    n=y/m;b=y%m;[m,a]=[a,m];
  }
}
function merge(xs){
  let out=[];for(let [l,h] of xs.sort((x,y)=>x[0]<y[0]?-1:x[0]>y[0]?1:0)){
    if(l>h)continue;let p=out[out.length-1];
    if(p&&l<=p[1]+1n){if(h>p[1])p[1]=h}else out.push([l,h]);
  }return out
}
function nonneg(n,f,deg){
  if(n===0n)return [];
  if(n===1n||deg===0)return f(0n)>=0n?[[0n,n-1n]]:[];
  let edges=nonneg(n-1n,i=>f(i+1n)-f(i),deg-1),out=[],pos=0n;
  function run(l,h,up){
    if(l>h)return;
    if(up){
      if(f(h)<0n)return;if(f(l)>=0n){out.push([l,h]);return}
      let a=l,b=h;while(b-a>1n){let m=(a+b)/2n;if(f(m)>=0n)b=m;else a=m}
      out.push([b,h])
    }else{
      if(f(l)<0n)return;if(f(h)>=0n){out.push([l,h]);return}
      let a=l,b=h;while(b-a>1n){let m=(a+b)/2n;if(f(m)>=0n)a=m;else b=m}
      out.push([l,a])
    }
  }
  for(let [l,h] of edges){if(pos<l)run(pos,l,false);run(l,h+1n,true);pos=h+1n}
  if(pos<n-1n)run(pos,n-1n,false);
  return merge(out)
}
function block(M,l,h,D,r,s,t,a){
  if(M<4n||M*D<=a||t<=9n*D||t>=10n*D||l<M||h>=2n*M||h-l>M/4n||l>h)throw Error("scope");
  let den=4n*D*l*h*M**3n, u=4n*M**3n*(r*l*h-t),
      v=4n*M**3n*(s*l*h+t*(l+h)),e=4n*a*l*h*M,
      U=v+e,L=v-e-t*(h-l)**2n*l*h;
  function cnt(i,j){
    if(i>j)return 0n;let n=j-i+1n;
    return fs(n,den,u,u*i+U)+fs(n,den,-u,-u*i-L)+n
  }
  let n=cnt(l,h);if(n===0n)return {strip:0n,runs:[]};
  let lo=l,hi=h;while(lo<hi){let m=(lo+hi)/2n;if(cnt(l,m)>0n)hi=m;else lo=m+1n}
  let x=lo,y=fd(u*x+U,den);
  lo=x;hi=h;while(lo<hi){let m=(lo+hi+1n)/2n;if(cnt(m,h)>0n)lo=m;else hi=m-1n}
  let q=1n,p=0n;
  if(n>1n){
    if((lo-x)%(n-1n)!==0n)throw Error("lattice spacing");
    q=(lo-x)/(n-1n);let dy=fd(u*lo+U,den)-y;
    if(dy%(n-1n)!==0n)throw Error("vertical spacing");
    p=dy/(n-1n)
  }
  function P(i){let m=x+q*i,j=y+p*i;return (D*j-r*m-s)*m*m-t*m}
  let A=nonneg(n,i=>a+P(i),3),B=nonneg(n,i=>a-P(i),3),runs=[];
  for(let [i,j] of A)for(let [k,w] of B){let f=i>k?i:k,g=j<w?j:w;if(f<=g)runs.push([f,g])}
  return {strip:n,runs:merge(runs).map(([i,j])=>({m:x+q*i,j:y+p*i,q,p,n:j-i+1n}))}
}
function all(M,D,r,s,t,a){
  let out=[];for(let i=0n;i<4n;i++){
    let l=M+i*M/4n,h=M+(i+1n)*M/4n-1n;
    if(l<=h)out.push(block(M,l,h,D,r,s,t,a))
  }return out
}
function check(M,D,r,s,t,a){
  let got=all(M,D,r,s,t,a),pts=[];
  for(let z of got)for(let w of z.runs)for(let i=0n;i<w.n;i++)pts.push([w.m+w.q*i,w.j+w.p*i].join(":"));
  let want=[];for(let m=M;m<2n*M;m++){
    let f=r*m*m+s*m+t, j=fd(f,D*m);
    for(let k of [j,j+1n]){let P=(D*k-r*m-s)*m*m-t*m;if(P>=-a&&P<=a)want.push([m,k].join(":"))}
  }
  if(pts.join(",")!==want.join(","))throw Error("brute mismatch "+[M,D,r,s,t,a]);
  return pts.length
}
let floorChecks=0, polyChecks=0, cases=0, pointChecks=0;
for(let n=0n;n<=12n;n++)for(let m=1n;m<=9n;m++)for(let a=-9n;a<=9n;a++)for(let b=-9n;b<=9n;b++){
 let z=0n;for(let i=0n;i<n;i++)z+=fd(a*i+b,m);
 if(fs(n,m,a,b)!==z)throw Error("floor sum");floorChecks++
}
for(let a=-2n;a<=2n;a++)for(let b=-3n;b<=3n;b++)for(let c=-4n;c<=4n;c++)for(let d=-5n;d<=5n;d++){
 let f=i=>((a*i+b)*i+c)*i+d,got=nonneg(30n,f,3),w=[];
 for(let [l,h] of got)for(let i=l;i<=h;i++)w.push(i);
 let v=[];for(let i=0n;i<30n;i++)if(f(i)>=0n)v.push(i);
 if(w.join(",")!==v.join(","))throw Error("poly");polyChecks++
}
for(let i=0n;i<512n;i++){
 let M=32n+i%97n,D=10000n,r=(i%7n-3n)*D+(i*7919n)%D,s=(i*1399n)% (4n*D)-2n*D,t=95000n,a=(1n+i%5n)*D;
 pointChecks+=check(M,D,r,s,t,a);cases++;
}
let tangent=[];
for(let M of [10000n,1000000n,100000000n,10000000000n,10n**20n]){
 let D=2n*M*M,r=21n*D+19n,s=-38n*M,t=19n*M*M,a=D;
 let z=block(M,M,M+M/4n-1n,D,r,s,t,a);
 let lo=0n,hi=M/4n;
 while(hi-lo>1n){let h=(lo+hi)/2n;if(19n*h*h*(M+h)<=2n*M*M)lo=h;else hi=h}
 if(z.runs.length!==1||z.runs[0].m!==M||z.runs[0].j!==21n*M||z.runs[0].q!==1n||z.runs[0].n!==lo+1n)throw Error("tangent");
 tangent.push({M:String(M),strip:String(z.strip),count:String(lo+1n)})
}
console.log({floorChecks,polyChecks,cases,pointChecks,tangent});
```

Next: make inherited C,m0 effective from the BRC edge and derivative bounds, then apply the sieve with actual certified coefficient enclosures. Verify independently and integrate with adaptive sign/CT fallback only at retained candidates. Mother target B_fix,odd(32), actual zero decisions, c2=0, other spectral zeros remain open. No shared mathematical acceptance.
