# R284JO — Full second-branch joint block transfer (all offsets, both parities)

2026-11-27. Independent continuation of own Activity RA-B82240E8488EF5A1DA5186C4, EM-DIRECT-0C386E, TASK_RESEARCH; NOT_REVIEWED. Own public recovery r1-20261127-1655-recovery confirms original open registration and no formal runs; owner inventory r1-20261127-1655-owner RUNNING at initial check. No shared task/claim mutation. Global entry snapshot eb27d657f4c8d3bc743932e0fe93abf21e2210f8; P000 V5, ACTIVE worldview, joint and residual contracts, portable research and current research method consulted. This is an auxiliary exact arithmetic observer, not native spatial dynamics.

Frozen scientific inputs: R284JN 7266b6aa921d79d17724c3032935e1b9c8dac781:research_notes/portable_direct/R284JN_JOINT_ENDPOINT_HARMONIC_PRODUCT_20261127.md; R284JL e700b37ddcbcd90bf7ae887bea7d3f2795c6df9c:research_notes/portable_direct/R284JL_RESONANT_MOMENTS_AND_ENDPOINT_CHARACTER_CERTIFICATES_20261127.md, including its JK/JI/JG dependencies. JN accelerated T,H only; JL's Newton coefficient construction may still dominate in deep resonance. New route evaluates all original signed observers together directly, avoiding the affine coefficient expansion and retaining full observer information.

## 1. Exact seven-output block carrier (eight polynomial coordinates)

For integer 3<=r<=d, prime p>4d+6, write j=d-r, w=(r-2)/2, h=r-k, l=d-k. JL's direct carrier is c_h=(-1)^h binom(2j+h+1,h), U_0=1, B_0=(r+2)/(4(r-1)), U_(k+1)=U_k(w-k)/(w+k+3), B_(k+1)=B_k(w-k-1)/(w+k+2). Put X_k=U_k c_h, Y_k=B_k c_h. The signed carrier identity c_(h-1)/c_h=-h/(2j+h+1) holds for h>=1; for h=0 set the next carrier to zero. Put a=r+2k+4, b=r+2k+2, c=2j+h+1, D=abc. Define polynomial coordinates
 x=-(r-2-2k)hb, y=-(r-4-2k)ha,
 v=D(k+1)(l+1), z=-ab(k+1)lh, s=v+z,
 n=2j+k+2, f=k+1.
The exact step, in auxiliary field coordinates, is
 X'=xX/D, Y'=yY/D,
 V'=V+vX/D, Q'=Q+zX/D, A'=A+sY/D.
Proof: insert the c-ratio in the U and B recurrences and in the original signed observations V+=U(k+1)(l+1)c_h, Q+=U(k+1)l c_(h-1), A+=B[(k+1)(l+1)c_h+(k+1)l c_(h-1)]. In particular the Q term at k=r is exactly zero; no divide-by-zero or even-offset zero fibre is discarded. This proves the identity over Q and F_p because all denominators in the declared range are units.

The eight-coordinate block L=(D,x,y,v,z,s,n,f) acts by the same normalized transition, and retains the two scalar products n,f for the initial carrier. Concatenate earlier block L and later block H by
 D'=D_H D_L, x'=x_H x_L, y'=y_H y_L,
 v'=D_H v_L+v_H x_L, z'=D_H z_L+z_H x_L,
 s'=D_H s_L+s_H y_L, n'=n_H n_L, f'=f_H f_L.
Associativity follows either by direct substitution or the faithful representation of the first six coordinates as a structured triangular 5x5 matrix numerator with diagonal (x,y,D,D,D) and nonzero lower entries v,z on the X column and s on the Y column, together with scalar products n,f. No independent-marginal approximation. The identity is (1,1,1,0,0,0,1,1). Individual historical branch values or the standalone formal coefficients T,H are not claimed recoverable from the aggregated block; they remain in the pinned source and can be computed by JN/JL as needed. The block is lossless for the stated full joint observers and composition of such intervals.

After k=0,...,r, recover the true initial signed binomial from the jointly retained scalar products:
 c_r=(-1)^r (r+1) n / ((2j+r+2) f),
 since n/f=binom(2j+r+2,r+1). Starting X=c_r, Y=B_0 c_r, V=Q=A=0 yields
 V*=c_r v/D, Q*=c_r z/D, A*=B_0 c_r s/D.
Then q0=w-d, Z*=q0 A*+Q*+V*, G=3q0(4q0+3d+1)^2 A*Q*-32(3q0+d+1)(Z*)^2.
All factors needed for divisions are positive integers <p (including seed factorial factors), except fixed powers of 2 which are units. Thus this works for every offset 3<=r<=d and both parities, including deep resonance and r=d. By the frozen pole/edge congruences, when q>=64, d^2<=4q, p divides 2q+2d-r+2 and p>4d+6, G!=0 mod p certifies qK(q,d)!=32/3. The test does not assert nonzero when G=0.

## 2. Complete observer evaluation in sublinear field operations

Each step coordinate has degree <=5 in k. Choose m=ceil(sqrt(r+1)); form the block P(X)=compose step(X),...,step(X+m-1) in chronological order via a balanced polynomial product tree. Each of the eight polynomial coordinates has degree <=5m (each composition is a fixed number of multiplications/additions; degrees add at most). Evaluate the same P at x=0,m,2m,...,(floor((r+1)/m)-1)m by a single monic point-product tree and recursive polynomial remainders. Compose the scalar blocks and handle <m tail steps directly. Unlike JN alone, this evaluates V,Q,A,Z,G themselves, without constructing the O(j^2) Newton coefficient table or evaluating T,H separately. The n,f scalar products are included, so initial binomial evaluation is also accounted for. Field inversions for final scalar recovery can be done by binary powers; only a constant number is necessary.

Let M(n) be polynomial multiplication cost with M(n)/n nondecreasing up to a constant. Product/remainder trees with reversal and truncated Newton inversion of monic polynomial divisors cost safely O(M(m) log^2(m+1)); number of fixed-size coordinates is 8. Remainder tree uses reversed monic constant 1, so no repeated field exponentiation at nodes. Scalar compositions/tail cost O(m). Hence total cost O(M(ceil(sqrt(r+1))) log^2(r+2)+log p) field operations, i.e. Karatsuba O(r^(log_2(3)/2) log^2(r+2)+log p); near-linear multiplication gives soft-O(sqrt(r)+log p). Bound includes seed, all observers, residual and modular test given p. It is an arithmetic complexity theorem, not wall-clock or bit-complexity superiority at every size; prime discovery and q,d input bit reduction are separate. This does not require polynomial approximation or a sign theorem. All exact coefficients of the combined observer map are retained for the specified block composition.

## 3. Exact replay

Executed JS BigInt modular arithmetic. All d=3..32, r=3..d, first two primes >4d+6; compare blocked and unblocked joint transfer with independently evaluated original direct signed observer recurrence. Extra large cases compare blocked with direct. Prime checks by trial division. Result:
```json
{
  "cases": 930,
  "odd": 480,
  "even": 450,
  "zeros": 9,
  "large": [
    {
      "d": 1001,
      "r": 1001,
      "p": 4013,
      "m": 32,
      "V": "1803",
      "Q": "3817",
      "A": "3355",
      "Z": "2528",
      "G": "3222"
    },
    {
      "d": 2000,
      "r": 1000,
      "p": 8009,
      "m": 32,
      "V": "4588",
      "Q": "7167",
      "A": "406",
      "Z": "3024",
      "G": "7714"
    },
    {
      "d": 10001,
      "r": 10001,
      "p": 40013,
      "m": 101,
      "V": "36799",
      "Q": "27696",
      "A": "29316",
      "Z": "8140",
      "G": "38582"
    },
    {
      "d": 20000,
      "r": 10000,
      "p": 80021,
      "m": 101,
      "V": "2465",
      "Q": "11739",
      "A": "64847",
      "Z": "59654",
      "G": "42413"
    },
    {
      "d": 1000000,
      "r": 1001,
      "p": 4000037,
      "m": 32,
      "V": "3606597",
      "Q": "2583017",
      "A": "1531648",
      "Z": "1408282",
      "G": "3178098"
    }
  ]
}
```
Each zero is a modular noncertificate, not an exact equality. All comparisons include V,Q,A,Z,G individually, not only G.
```javascript
function replay(){
function compute(d,r,p,m,blocked){
  d=BigInt(d);p=BigInt(p); const R=BigInt(r),j=d-R;
  const mod=x=>(x%p+p)%p;
  function pow(a,n){let z=1n;a=mod(a);for(;n;n>>=1n,a=mod(a*a))if(n&1n)z=mod(z*a);return z}
  function inv(a){a=mod(a);if(!a)throw Error("zero inverse");return pow(a,p-2n)}
  function trim(a){while(a.length&&a.at(-1)===0n)a.pop();return a}
  function add(a,b){return trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>mod((a[i]??0n)+(b[i]??0n))))}
  function neg(a){return a.map(x=>mod(-x))}
  function sub(a,b){return add(a,neg(b))}
  function mul(a,b){
    if(!a.length||!b.length)return [];
    if(Math.min(a.length,b.length)<=16){let c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let k=0;k<b.length;k++)c[i+k]=mod(c[i+k]+a[i]*b[k]);return trim(c)}
    let s=Math.ceil(Math.max(a.length,b.length)/2),a0=a.slice(0,s),a1=a.slice(s),b0=b.slice(0,s),b1=b.slice(s);
    let lo=mul(a0,b0),hi=mul(a1,b1),mid=sub(sub(mul(add(a0,a1),add(b0,b1)),lo),hi);
    let c=Array(a.length+b.length-1).fill(0n);
    for(let [v,k] of [[lo,0],[mid,s],[hi,2*s]])for(let i=0;i<v.length;i++)c[i+k]=mod(c[i+k]+v[i]);
    return trim(c)
  }
  function seriesInv(f,n){if(f[0]!==1n)throw Error("nonmonic divisor");let g=[1n],k=1;while(k<n){k=Math.min(2*k,n);let z=neg(mul(f.slice(0,k),g).slice(0,k));z[0]=mod((z[0]??0n)+2n);g=mul(g,z).slice(0,k)}return g}
  function rem(f,g){if(f.length<g.length)return f;let k=f.length-g.length+1;let qr=mul(f.slice().reverse().slice(0,k),seriesInv(g.slice().reverse(),k)).slice(0,k);while(qr.length<k)qr.push(0n);return sub(f,mul(qr.reverse(),g)).slice(0,g.length-1)}
  function tree(xs){if(xs.length===1)return {f:[mod(-xs[0]),1n]};let n=xs.length>>1,l=tree(xs.slice(0,n)),h=tree(xs.slice(n));return {f:mul(l.f,h.f),l,h}}
  function evals(f,t,out=[]){let g=rem(f,t.f);if(!t.l)out.push(g[0]??0n);else{evals(g,t.l,out);evals(g,t.h,out)}return out}
  // Carrier [D,X,Y,V,Q,A,N,F]; concatenate earlier L with later H.
  function compose(L,H){
    return [mul(L[0],H[0]),mul(L[1],H[1]),mul(L[2],H[2]),
      add(mul(H[0],L[3]),mul(H[3],L[1])),
      add(mul(H[0],L[4]),mul(H[4],L[1])),
      add(mul(H[0],L[5]),mul(H[5],L[2])),
      mul(L[6],H[6]),mul(L[7],H[7])]
  }
  function step(k,slope){
    const f=(a,b=0n)=>trim([mod(a),mod(b*slope)]);
    let a=f(R+2n*k+4n,2n),b=f(R+2n*k+2n,2n),c=f(2n*j+R-k+1n,-1n),
        h=f(R-k,-1n),l=f(d-k,-1n),kp=f(k+1n,1n);
    let ab=mul(a,b),D=mul(ab,c),X=neg(mul(mul(f(R-2n-2n*k,-2n),h),b)),
        Y=neg(mul(mul(f(R-4n-2n*k,-2n),h),a)),
        V=mul(mul(D,kp),f(d-k+1n,-1n)),Q=neg(mul(mul(mul(ab,kp),l),h));
    return [D,X,Y,V,Q,add(V,Q),f(2n*j+k+2n,1n),kp]
  }
  function product(lo,hi){if(hi-lo===1)return step(BigInt(lo),1n);let mid=(lo+hi)>>1;return compose(product(lo,mid),product(mid,hi))}
  const one=[1n],zero=[];
  let acc=[one,one,one,zero,zero,zero,one,one];
  if(blocked){
    const n=Math.floor((r+1)/m),P=product(0,m),tr=tree(Array.from({length:n},(_,i)=>BigInt(i*m)));
    const vals=P.map(f=>evals(f,tr));
    for(let i=0;i<n;i++)acc=compose(acc,vals.map(row=>trim([row[i]])));
    for(let k=n*m;k<=r;k++)acc=compose(acc,step(BigInt(k),0n));
  }else for(let k=0;k<=r;k++)acc=compose(acc,step(BigInt(k),0n));
  const [D,X,Y,V,Q,A,N,F]=acc.map(z=>z[0]??0n);
  const seed=mod((r%2?-1n:1n)*N*(R+1n)*inv(F*(2n*j+R+2n)));
  const B0=mod((R+2n)*inv(4n*(R-1n)));
  const scale=mod(seed*inv(D));
  const v=mod(scale*V),q=mod(scale*Q),a=mod(scale*B0*A);
  const q0=mod((R-2n)*inv(2n)-d),z=mod(q0*a+q+v);
  const g=mod(3n*q0*(4n*q0+3n*d+1n)**2n*a*q-32n*(3n*q0+d+1n)*z*z);
  return [v,q,a,z,g].map(String)
}
function direct(d,r,p){
  d=BigInt(d);p=BigInt(p);const R=BigInt(r),j=d-R;
  const mod=x=>(x%p+p)%p;
  function pow(a,n){let z=1n;a=mod(a);for(;n;n>>=1n,a=mod(a*a))if(n&1n)z=mod(z*a);return z}
  const inv=a=>{a=mod(a);if(!a)throw Error("zero inverse");return pow(a,p-2n)};
  let n=1n,f=1n;
  for(let k=1n;k<=R;k++){n=mod(n*(2n*j+1n+k));f=mod(f*k)}
  let c=mod((r%2?-1n:1n)*n*inv(f)),U=1n,B=mod((R+2n)*inv(4n*(R-1n))),v=0n,q=0n,a=0n;
  for(let k=0n;k<=R;k++){
    const h=R-k,l=d-k;
    const cq=mod(-c*h*inv(2n*j+h+1n));
    let vv=mod((k+1n)*(l+1n)*c),qq=mod((k+1n)*l*cq);
    v=mod(v+U*vv);q=mod(q+U*qq);a=mod(a+B*(vv+qq));
    c=cq;U=mod(U*(R-2n-2n*k)*inv(R+2n*k+4n));B=mod(B*(R-4n-2n*k)*inv(R+2n*k+2n));
  }
  let q0=mod((R-2n)*inv(2n)-d),z=mod(q0*a+q+v);
  let g=mod(3n*q0*(4n*q0+3n*d+1n)**2n*a*q-32n*(3n*q0+d+1n)*z*z);
  return [v,q,a,z,g].map(String)
}
function next(n){for(;;n++){let ok=n>=2;for(let k=2;k*k<=n;k++)if(n%k===0){ok=false;break}if(ok)return n}}
let cases=0,odd=0,even=0,zeros=0;
for(let d=3;d<=32;d++)for(let r=3;r<=d;r++){
  for(let p of [next(4*d+7),next(next(4*d+7)+1)]){
    let ref=direct(d,r,p),m=Math.ceil(Math.sqrt(r+1)),a=compute(d,r,p,m,true),b=compute(d,r,p,m,false);
    if(JSON.stringify(a)!==JSON.stringify(ref)||JSON.stringify(b)!==JSON.stringify(ref))throw Error(`mismatch ${d},${r},${p}`);
    cases++;if(r%2)odd++;else even++;if(a[4]==="0")zeros++;
  }
}
let large=[];
for(let [d,r] of [[1001,1001],[2000,1000],[10001,10001],[20000,10000],[1000000,1001]]){
  let p=next(4*d+7),m=Math.ceil(Math.sqrt(r+1)),a=compute(d,r,p,m,true),b=direct(d,r,p);
  if(JSON.stringify(a)!==JSON.stringify(b))throw Error(`large mismatch ${d},${r},${p}`);
  large.push({d,r,p,m,V:a[0],Q:a[1],A:a[2],Z:a[3],G:a[4]})
}
return {cases,odd,even,zeros,large};
}
console.log(JSON.stringify(replay(),null,2));
```

## Next
Use the full evaluator to scan actual legal primal budgets (not only formal p,d,r pairs); compare exception intersections of the three windows, and investigate a genuinely new deterministic constraint on shared exceptions. For H-only root exclusion or exact affine sensitivity, retain JL/JM/JN separately; the new evaluator gives actual values rather than symbolic H-discriminant coefficients. All-budget non-equality and inverse-polynomial real separation remain open. No formal Result or independent Review.
