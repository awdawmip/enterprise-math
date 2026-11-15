// Exact BigInt rational verification of the two-endpoint BRC N4/S23 phase theorem.
// Source model frozen at enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
'use strict';
const absn = n => n < 0n ? -n : n;
function gcd(a,b) { a=absn(a); b=absn(b); while(b){const t=a%b;a=b;b=t;}return a||1n; }
function Q(a,b=1n) { a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b;}if(!b)throw Error('denominator zero');const g=gcd(a,b);return [a/g,b/g]; }
const Z=Q(0),O=Q(1),TWO=Q(2),HALF=Q(1,2),QUART=Q(1,4),EIGHTH=Q(1,8),THIRD=Q(1,3);
const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>Q(-a[0],a[1]);
const sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]);
const div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
const cmp=(a,b)=>{const v=a[0]*b[1]-b[0]*a[1];return v>0n?1:v<0n?-1:0;};
const aq=a=>cmp(a,Z)<0?neg(a):a;
const max=(a,b)=>cmp(a,b)>=0?a:b;
function must(ok,why){if(!ok)throw Error(why);}
function law(a,b,c){const oneA=sub(O,a),tail=mul(oneA,sub(O,b));return [a,mul(oneA,b),mul(tail,c),mul(tail,sub(O,c))];}
const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
function observe(a,b,c){
  const au=law(a,b,HALF),av=law(a,Z,c),bu=law(QUART,b,HALF),bv=law(QUART,THIRD,HALF);
  const src=[au,au,av,bu,bu,bv];
  return M.map(row=>[0,1,2,3].map(j=>div(row.reduce((t,w,i)=>add(t,mul(Q(w),src[i][j])),Z),Q(20))));
}
function tv(a,b){return div(a.reduce((t,v,j)=>add(t,aq(sub(v,b[j]))),Z),TWO);}
function distance(P,C){return P.reduce((t,row,i)=>max(t,tv(row,C[i])),Z);}
function mean(P,R){return P.map((row,i)=>row.map((v,j)=>div(add(v,R[i][j]),TWO)));}
function ceilSqrtFixed(x,bits){
  const scale=1n<<BigInt(bits),target=x[0]*scale*scale,denom=x[1];
  let low=0n,high=16n*scale;
  while(low<high){const mid=(low+high)>>1n;if(mid*mid*denom>=target)high=mid;else low=mid+1n;}
  const upper=Q(low,scale),lower=Q(low===0n?0n:low-1n,scale);
  must(cmp(mul(upper,upper),x)>=0 && cmp(mul(lower,lower),x)<=0,'sqrt enclosure');
  return {upper,lower};
}
function checkCase(h,k){
  const q=sub(EIGHTH,h),l=sub(EIGHTH,k),u=sub(O,q);
  const F=add(Q(3,16),div(h,TWO)),H=add(Q(3,16),div(add(h,k),Q(4)));
  const Rh=max(F,H);
  const disc=add(sub(add(Q(43),mul(Q(16),mul(h,h))),mul(Q(16),h)),mul(Q(24),k));
  const {upper,lower}=ceilSqrtFixed(disc,38);
  const Tupper=div(add(sub(upper,Q(5)),mul(Q(4),h)),Q(8));
  const Tlower=div(add(sub(lower,Q(5)),mul(Q(4),h)),Q(8));
  const r=max(F,Tupper),s=add(q,r),x=sub(u,r),y=sub(HALF,div(mul(Q(4),r),Q(3)));
  const w=add(Q(7,32),div(q,Q(4))),c=div(w,s);
  must(cmp(x,HALF)>=0&&cmp(x,u)<=0&&cmp(y,l)>=0&&cmp(y,HALF)<=0&&cmp(c,HALF)>=0&&cmp(c,Q(7,8))<=0,'lawful center bounds');
  const centerL=observe(x,y,c);
  const centerH=mean(observe(HALF,l,Q(7,8)),observe(u,HALF,HALF));
  let worstL=Z,worstH=Z;
  for(const a of [HALF,u])for(const b of [l,HALF])for(const cc of [HALF,Q(7,8)]){
    const p=observe(a,b,cc);
    worstL=max(worstL,distance(p,centerL));
    worstH=max(worstH,distance(p,centerH));
  }
  must(cmp(worstH,Rh)===0,'exact hull radius');
  must(cmp(worstL,r)<=0,'rational surrogate upper bound');
  must(cmp(sub(r,max(F,Tlower)),Q(1,1n<<36n))<=0,'root envelope accuracy');
  const K=sub(sub(div(mul(Q(2),h),Q(3)),div(mul(Q(2),mul(h,h)),Q(3))),Q(1,32));
  must(cmp(sub(disc,Q(169,4)),mul(Q(24),sub(k,K)))===0,'exact phase polynomial identity');
  const testRight=add(sub(Q(13,2),mul(Q(2),h)),mul(Q(2),k));
  must(cmp(sub(disc,mul(testRight,testRight)),Q(7,16))>=0,'positive T-H gap certificate');
  return {zero:cmp(k,K)<=0,strict:cmp(k,K)>0};
}
const cases=[];for(let i=0;i<=8;i++)for(let j=0;j<=8;j++)cases.push([Q(i,64),Q(j,64)]);
cases.push([Q(1,16),Q(1,128)],[Q(1,8),Q(1,24)]);
let strict=0,zero=0;for(const [h,k] of cases){const v=checkCase(h,k);if(v.zero)zero++;if(v.strict)strict++;}
must(strict+zero===cases.length,'phase partition');
const cornerD=add(sub(add(Q(43),mul(Q(16),mul(EIGHTH,EIGHTH))),mul(Q(16),EIGHTH)),mul(Q(24),EIGHTH));
must(cmp(cornerD,Q(177,4))===0,'endpoint radical');
must(cmp(cornerD,Q(169,4))>0,'gap reopens at h=k=1/8');
const output={status:'PASS_BRC_N4_S23_DOUBLE_ENDPOINT_EXACT_PHASE_20261102',cases:cases.length,corner_policies:8*cases.length,full_source_row_center_comparisons:8*6*2*cases.length,method:'BigInt exact rational 4-stop original 20M; certified sqrt 2^-38; continuous theorem by analytic proof',boundary_cases:['h=1/16,k=1/128','h=1/8,k=1/24'],zero_phase_cases:zero,positive_phase_cases:strict,gap_at_h_k_1_8:'(sqrt(177)-13)/16>0'};
console.log(JSON.stringify(output));
