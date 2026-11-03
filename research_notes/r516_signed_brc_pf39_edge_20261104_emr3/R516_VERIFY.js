'use strict';
/* R516: signed BRC auxiliary scalar; R462 frozen input. Exact BigInt certificate. */
const evidence=(function computeR516(){
const R=39,LIMIT=6*R+1;
const gcd=(aa,bb)=>{let a=aa<0n?-aa:aa,b=bb<0n?-bb:bb;while(b)[a,b]=[b,a%b];return a};
const lcm=(a,b)=>a/gcd(a,b)*b;
const cache=new Map();
function bin(n,k){if(n<0||k<0||k>n)return 0n;if(!k||k===n)return 1n;k=Math.min(k,n-k);const key=n+':'+k;if(cache.has(key))return cache.get(key);let z=1n;for(let i=1;i<=k;i++)z=z*BigInt(n+1-i)/BigInt(i);cache.set(key,z);return z}
const C=k=>bin(2*k,k)/BigInt(k+1);
function H(k,t){let r=2*k+1;if(t<2||t>r)return 0n;let s=0n;for(let q=0;q<=r-t;q++)s+=bin(r-t,q)*(bin(2*t,r-2*q)-bin(2*t,r-2*q-1));return bin(r+t,2*t)*s}
function H2(k,t){let r=2*k+1;if(t<2||t>r)return 0n;let s=0n;for(let q=0;q<=Math.min(Math.floor((t-1)/2),k);q++)s+=bin(t-1,2*q)*4n**BigInt(q)*C(k-q);return bin(r+t,2*t)*s}
function D(k,m){let p=H(k,2),h=Array.from({length:m},(_,i)=>H(k,i+3)),ds=[1n];for(let n=1;n<=m;n++){let s=0n,pp=1n;for(let e=1;e<=n;e++){s+=(e%2?1n:-1n)*h[e-1]*pp*ds[n-e];pp*=p}ds.push(s)}return ds[m]}
function G(k,m){let z=BigInt(k);return (z*(z+1n)*(2n*z+1n)*(2n*z+3n))**BigInt(m)*(z+2n)}
function diff(a){let o=[],v=a.slice();while(v.length){o.push(v[0]);v=v.slice(1).map((x,i)=>x-v[i])}return o}
function N(delta,k,k0){let s=0n;for(let j=0;j<delta.length;j++)s+=delta[j]*bin(k-k0,j);return s}
function bareiss(A){let a=A.map(r=>r.slice()),n=a.length,prev=1n,sgn=1n;for(let i=0;i<n-1;i++){if(!a[i][i]){let j=i+1;while(j<n&&!a[j][i])j++;if(j===n)return 0n;[a[i],a[j]]=[a[j],a[i]];sgn=-sgn}let p=a[i][i];for(let j=i+1;j<n;j++){for(let h=i+1;h<n;h++){let v=p*a[j][h]-a[j][i]*a[i][h];if(v%prev)throw Error('Bad Bareiss division');a[j][h]=v/prev}a[j][i]=0n}prev=p}return sgn*a[n-1][n-1]}
let L=1n,fractions=[];
for(let k=1;k<=2*R;k++){let a=D(k,R),b=C(k)**BigInt(R)*G(k,R),g=gcd(a,b);if(b<=0n)throw Error('G sign');fractions.push([a/g,b/g]);L=lcm(L,b/g)}
let delta=diff(fractions.map(([n,d])=>n*(L/d)));if(delta.length!==2*R)throw Error('Newton length');
let checks=0;for(let k=1;k<=LIMIT;k++){if(L*D(k,R)!==C(k)**BigInt(R)*G(k,R)*N(delta,k,1))throw Error('identity k='+k);checks++}
let tailOrigin=null,tail=null,tailSign=null;
for(let k0=1;k0<=1200;k0++){let a=diff(Array.from({length:2*R},(_,j)=>N(delta,k0+j,1)));if(a.every(x=>x>0n)||a.every(x=>x<0n)){tailOrigin=k0;tail=a;tailSign=a[0]>0n?'+':'-';break}}
const pre=Array.from({length:(tailOrigin??1)-1},(_,i)=>N(delta,i+1,1));
let blocks=[];for(let i=0;i<pre.length;i++){let s=pre[i]>0n?'+':pre[i]<0n?'-':'0';if(blocks.length&&blocks.at(-1).sign===s)blocks.at(-1).to=i+1;else blocks.push({from:i+1,to:i+1,sign:s})}if(tailOrigin!==null)blocks.push({from:tailOrigin,to:'infinity',sign:tailSign});
let direct=0;for(let k=1;k<=20;k++){let M=Array.from({length:R},(_,i)=>Array.from({length:R},(_,j)=>H(k,3+i-j)));if(bareiss(M)!==D(k,R))throw Error('direct det k='+k);direct++}
let branch=0;for(let k=1;k<=20;k++)for(let t=2;t<=R+1;t++){if(H(k,t)!==H2(k,t))throw Error('signed BRC identity k='+k+' t='+t);branch++}
return {status:tailOrigin===null?'R516_EXACT_IDENTITY_PASS_TAIL_CERTIFICATE_PENDING':'R516_EXACT_JS_PASS',date:'2026-11-04',scientific_pin:'18783e01e3646c72b7aab3b16d3f565e83e6446f',predecessor:'R515@65d735583db9fe66a9a44d3695c969f381420f50',definition:'r=2k+1; C_k=binom(2k,k)/(k+1); H_k(t)=binom(r+t,2t)[x^r](1-x)(1+x)^(2t)(1+x^2)^(r-t) for 2<=t<=r, otherwise zero; D_39=det H_k(3+i-j)',polynomial_prerequisite:'R452/R462 p_t(k)=H_k(t)/C_k in Q[k], deg p_t<=2t',degree_bound:6*R,G:'[k(k+1)(2k+1)(2k+3)]^39*(k+2)',G_degree:4*R+1,interpolant_degree_max:2*R-1,normalization_L:String(L),newton_delta_at_k1:delta.map(String),identity_grid:'k=1..'+LIMIT,identity_checks:checks,tail_shift_origin_k:tailOrigin,tail_sign:tailSign,tail_newton_coefficients:tail?.map(String),finite_values_k1_to_before_tail:pre.map(String),sign_blocks:blocks,independent_direct_Bareiss_checks:direct,original_BRC_to_ballot_checks:branch,exact_arithmetic:'BigInt exact integer operations; no floating point',status_scope:'AUTHOR_SIDE_EXACT_COMPUTER_CERTIFICATE; DRIVER_UNREVIEWED; NOT_ADMITTED'};
})();
console.log(JSON.stringify(evidence,null,2));
