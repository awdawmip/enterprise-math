#!/usr/bin/env node
'use strict';
/* PREFIX287 C4-BRC: all four ordered source pairs, exact Gaussian BigInt. */
const z=(r=0n,i=0n)=>({r,i});
const add=(a,b)=>z(a.r+b.r,a.i+b.i),neg=a=>z(-a.r,-a.i);
const mul=(a,b)=>z(a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r);
const cj=a=>z(a.r,-a.i),norm=a=>mul(a,cj(a)).r;
const eq=(a,b)=>a.r===b.r&&a.i===b.i;
const sum=x=>x.reduce((s,v)=>s+v,0n),abs=x=>x<0n?-x:x;
const ZERO=z(),PH=[z(1n),z(0n,1n),z(-1n),z(0n,-1n)];
const gcd=(a,b)=>{a=abs(a);b=abs(b);while(b){[a,b]=[b,a%b]}return a||1n};
const F=(n,d)=>{if(!d)throw Error('zero denominator');if(d<0n){n=-n;d=-d}let g=gcd(n,d);return String(n/g)+'/'+String(d/g)};
const Z=a=>sum(a.map(norm));
const C=(a,r)=>{let s=ZERO;for(let j=0;j+r<a.length;j++)s=add(s,mul(a[j],cj(a[j+r])));return s};
function branches(a,p,si,j){const v=j<a.length?a[j]:ZERO,w=j>0&&j-1<a.length?a[j-1]:ZERO;return [mul(PH[p],v),si===1?w:neg(w)]}
function cross(Ba,Bb){let s=ZERO;for(const x of Ba)for(const y of Bb)s=add(s,mul(x,cj(y)));return s}
function outputs(a,p){let raw=[];for(const si of [1,-1])for(let j=0;j<=a.length;j++){
 const v=cross(branches(a,p,si,j),branches(a,p,si,j));
 if(v.i!==0n||v.r<0n)throw Error('invalid BRC mass');raw.push(v.r)
 }if(sum(raw)!==4n*Z(a))throw Error('mass conservation');return raw}
function inner(a,b){let s=ZERO;for(let j=0;j<a.length;j++)s=add(s,mul(a[j],cj(b[j])));return s}
function outInner(a,b,p){let s=ZERO;for(const si of [1,-1])for(let j=0;j<=a.length;j++)s=add(s,cross(branches(a,p,si,j),branches(b,p,si,j)));return s}
function sig(a){let n=Z(a),x=C(a,1),y=C(a,2);return [F(x.r,n),F(x.i,n),F(y.r,n),F(y.i,n),F(norm(a[0]),n)].join('|')}
function rel(a){return [F(a[1].r,a[0].r),F(a[1].i,a[0].r),F(a[2].r,a[0].r),F(a[2].i,a[0].r)].join('|')}
const groups=new Map();let packets=0,reads=0,completions=0,isometry=0;
for(let m0=1n;m0<=4n;m0++)for(let m1=1n;m1<=4n;m1++)for(let m2=1n;m2<=4n;m2++)
for(let k1=0;k1<4;k1++)for(let k2=0;k2<4;k2++){
 const a=[z(m0),mul(z(m1),PH[k1]),mul(z(m2),PH[k2])];
 const b=[add(a[0],a[1]),add(a[1],neg(a[2])),add(a[2],z(1n,1n))];
 for(let p=0;p<4;p++){
  const raw=outputs(a,p);reads+=8;completions++;
  if(!eq(outInner(a,b,p),mul(z(4n),inner(a,b))))throw Error('full isometry failed');isometry++;
  if(sum(raw.slice(0,4))!==2n*Z(a)+2n*mul(cj(PH[p]),C(a,1)).r)throw Error('port no-go formula failed');
 }
 let key=sig(a),v=groups.get(key)||[];v.push({a,rel:rel(a),n:Z(a)});groups.set(key,v);packets++;
}
let ambiguous=0,singular=0,binary=0,phase0=0;
for(const list of groups.values()){
 const uniq=[...new Map(list.map(x=>[x.rel,x])).values()];
 if(uniq.length>2)throw Error('more than two normalized candidates');
 let A=uniq[0];if(norm(A.a[0])===norm(A.a[2]))singular++;
 if(uniq.length===2){
  ambiguous++;if(norm(A.a[0])!==norm(A.a[2]))throw Error('non-singular ambiguity');
  let B=uniq[1],t=PH.findIndex(w=>eq(mul(A.a[0],w),A.a[2]));
  if(t<0)throw Error('t outside C4');let p=t===0?1:0;
  let x=outputs(A.a,p),y=outputs(B.a,p),n=A.n,m=B.n;
  let d=x.map((v,j)=>v*m-y[j]*n),e=d[1]+d[6];
  if(!d[1]||e!==2n*d[1])throw Error('binary gap missing');
  if(2n*abs(e)!==sum(d.map(abs)))throw Error('TV bound not saturated');
  const mag=abs(A.a[1].r)+abs(A.a[1].i),fac=(t===0||t===2)?2n:1n;
  if(abs(e)!==4n*m*A.a[0].r*mag*fac)throw Error('exact gap formula failed');
  let x0=outputs(A.a,0),y0=outputs(B.a,0);
  if(x0.every((v,j)=>v*m===y0[j]*n))phase0++;
  binary++;
 }
}
let a=[z(1n),z(0n,1n),z(1n)],b=[z(1n),z(0n,-1n),z(1n)];
let x=outputs(a,1),y=outputs(b,1);
if(x[1]+x[6]!==0n||y[1]+y[6]!==8n||Z(a)!==3n||Z(b)!==3n)throw Error('witness mismatch');
let result={status:'PREFIX287_BRC_BINARY_ISOMETRY_EXACT_PASS',arithmetic:'Gaussian BigInt; four ordered BRC source pairs per Port-bin',source_packets:packets,phase_settings:4,exact_brc_mass_readouts:reads,exact_mass_checks:completions,exact_full_inner_product_isometry_checks:isometry,distinct_signatures:groups.size,singular_signatures:singular,ambiguous_signatures:ambiguous,optimal_binary_discriminator_checks:binary,total_variation_equalities:binary,phase_zero_indistinguishable_pairs:phase0,binary_event:['(+,1)','(-,2)'],witness:{a:'(1,i,1)',b:'(1,-i,1)',p:1,raw_a:x.map(String),raw_b:y.map(String),mass_denominator:'12',event_E:['0','2/3'],port_totals:'1/2 each'},scope:'formal C4 BRC; native H_n detector pending'};
console.log(JSON.stringify(result,null,2));
