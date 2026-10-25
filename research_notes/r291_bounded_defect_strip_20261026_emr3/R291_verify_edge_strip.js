'use strict';
// Exact, portable BigInt coefficient certificate for the bounded-defect BRC tail.
// A standalone local verifier; output JSON contains actual coverage and boundary.
const J = Number(process.argv[2] || '12000');
if (!Number.isSafeInteger(J) || J < 100 || J > 50000) throw Error('J must be 100..50000');
const pAdd=(a,b)=>{let c=Array(Math.max(a.length,b.length)).fill(0n);for(let i=0;i<c.length;i++) c[i]=(a[i]||0n)+(b[i]||0n);return c};
const pMul=(a,b)=>{let c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return c};
const pScale=(a,t)=>a.map(x=>x*t);
const pSub=(a,b)=>pAdd(a,pScale(b,-1n));
const A=[1n,0n,2n,-1n], C=[1n,0n,0n,-1n], E=[1n,-4n,4n,-1n];
// E=(1-y)(1-3y+y^2)=1-4y+4y^2-y^3.
let P=[[1n]],Q=[[0n]];
for(let k=0;k<18;k++) { P.push(pSub(pMul(A,P[k]),pMul(E,Q[k]))); Q.push(pSub(pMul(A,Q[k]),pMul(C,P[k]))); }
const T=[1n,-1n,1n];
const filters=[
  {label:'minus11',sign:-1,m:11,p:pSub(pScale(P[10],2n),P[11]),q:pSub(pScale(Q[10],2n),Q[11]),shift:10,scale:2n**11n},
  {label:'plus13',sign:1,m:13,p:pSub(pScale(pMul(T,P[14]),2n),P[15]),q:pSub(pScale(pMul(T,Q[14]),2n),Q[15]),shift:14,scale:2n**15n},
];
const maxshift=Math.max(...filters.map(o=>o.shift));
const limit=J+maxshift;
const f=Array(limit+1).fill(0n);f[0]=-1n;
for(let n=0;n<limit;n++){
  const at=(k)=>k>=0?f[k]:0n;
  const num=(2n*BigInt(n)-2n)*f[n]+(BigInt(n)-1n)*at(n-1)+(2n*BigInt(n)-2n)*at(n-2)-(BigInt(n)-3n)*at(n-3);
  const div=BigInt(n+1);
  if(num%div!==0n)throw Error('Noninteger f at '+(n+1));
  f[n+1]=num/div;
}
const output={schema:'EM_R291_BOUNDED_DEFECT_STRIP_V1',status:'PASS',base_coefficients_checked_through_j:J,model:'positive ordered 6-edge BRC clean-reset, exact full-affine fiber differences', algebra:'w=(1+y)(1+h), h=y^4+(y+2y^2+y^3+y^4)h+y(1+y)^2 h^2; w=(A-(1-y^3)g)/(2y)', method:'linear-order recurrence for rational-square-root g and exact polynomial filters; pairwise G_{m+1}=w G_m', proof_scope:'for all m>=11 minus and m>=13 plus, 0<=j<=J; no conclusion for j>J',negative_coefficients_found:0,bases:{}, native_owner_verified:false,driver_review:'NOT_DONE'};
for(const o of filters){
  let prev=0n, minvalue=null, first12=[], zeros=[], npos=0, rawDP_prefix=[];
  for(let j=0;j<=J;j++){
    const k=j+o.shift;
    let numerator=o.p[k]||0n;
    for(let i=0;i<o.q.length;i++) if(i<=k) numerator-=o.q[i]*f[k-i];
    if(numerator%o.scale!==0n)throw Error('nonintegral (1+y)G '+o.label+' j '+j);
    const H=numerator/o.scale;
    const val=H-prev;
    if(j<12)first12.push(val.toString());
    if(j<=80)rawDP_prefix.push(val);
    if(val<=0n){npos++; if(zeros.length<30)zeros.push({j,value:val.toString()});}
    if(minvalue===null || val<minvalue)minvalue=val;
    if(j===J){o.last=val;}
    prev=val;
  }
  if(npos)throw Error('strict positivity fails '+o.label+': '+JSON.stringify(zeros));
  output.bases[o.label]={m:o.m, first12, strict_positive_coefficients:J+1, min_coefficient:minvalue.toString(), last_coefficient_decimal_digits:o.last.toString().length,last_coefficient_prefix:o.last.toString().slice(0,48),last_coefficient_suffix:o.last.toString().slice(-48)};
  o.rawDP_prefix=rawDP_prefix;
}
// Recheck known exact 10-term coefficients from R290's remote immutable evidence.
const expected={minus11:['1','8','26','39','16','5','191','718','1583','3237'],plus13:['1','11','52','130','157','24','51','1270','4569','9992']};
for(const [k,v] of Object.entries(expected)){
  if(output.bases[k].first12.slice(0,10).join(',')!==v.join(','))throw Error('R290 seed mismatch '+k);
}
// Second implementation: raw ordered bits and complete affine effects, length <=160.
const EDGES=[[[2,-1,-1],[2,1,-1]],[[0,-1,-1],[0,1,-1]],[[1,1,1],[2,1,-1]]];
let states=new Map([['0,1,0,0',1n]]),matches=0;
for(let n=0;n<=160;n++){
  const count=new Map();
  for(const [key,cnt] of states){
    const [q,e,k]=key.split(',').map(Number);
    if(q===0){const key2=e+','+k;count.set(key2,(count.get(key2)||0n)+cnt);}
  }
  for(const o of filters){
    const j=(n-o.m-2)/2;
    if(Number.isInteger(j)&&j>=0&&j<=80){
      const effect=(o.sign===1?'1':'-1')+',';
      const actual=(count.get(effect+(-o.m))||0n)-(count.get(effect+(-o.m-2))||0n);
      if(actual!==o.rawDP_prefix[j])throw Error('independent raw DP failed: '+o.label+' n='+n);
      matches++;
    }
  }
  const next=new Map();
  for(const [key,cnt] of states){
    const [q,e,k,prevZero]=key.split(',').map(Number);
    for(let bit=0;bit<2;bit++){
      if(prevZero===1&&bit===0)continue;
      const [q1,eta,d]=EDGES[q][bit];
      const key2=[q1,eta*e,eta*k+d,bit===0?1:0].join(',');
      next.set(key2,(next.get(key2)||0n)+cnt);
    }
  }
  states=next;
}
output.independent_six_edge_dp_end=160;
output.independent_six_edge_dp_matches=matches;
console.log(JSON.stringify(output,null,2));
