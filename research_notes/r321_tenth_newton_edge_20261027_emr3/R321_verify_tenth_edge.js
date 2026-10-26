'use strict';
// R321: exact independent BigInt check of the original ordered six-edge BRC recurrence.
// Finite validation supplements the distinct all-s exact symbolic proof.
const N=192;
const choose=(n,k)=>{if(n<0||k<0||k>n)return 0n;let v=1n;for(let j=1;j<=k;j++)v=v*BigInt(n-j+1)/BigInt(j);return v;};
const trim=x=>{while(x.length>1&&x[x.length-1]===0n)x.pop();return x;};
const add=(x,y,sign=1n)=>{const z=Array(Math.max(x.length,y.length)).fill(0n);for(let i=0;i<x.length;i++)z[i]+=x[i];for(let i=0;i<y.length;i++)z[i]+=sign*y[i];return trim(z);};
const mul=(x,y)=>{const z=Array(x.length+y.length-1).fill(0n);for(let i=0;i<x.length;i++)for(let j=0;j<y.length;j++)z[i+j]+=x[i]*y[j];return trim(z);};
const minus=i=>Array.from({length:i+1},(_,j)=>(j%2?-1n:1n)*choose(i,j));
const num=i=>[0n,-choose(3,i-1),-choose(6,i-1),choose(8,i-2)];
const delta=i=>[0n,-choose(4,i)+choose(2,i-1),choose(5,i-1)-choose(5,i-2),choose(7,i-2),-choose(9,i-3)];
const moment=(p,r)=>{let v=0n;for(let j=r;j<p.length;j++){let ff=1n;for(let h=0;h<r;h++)ff*=BigInt(j-h);v+=p[j]*ff;}return v;};
const poly=(coeffs,s)=>coeffs.reduce((v,c)=>v*s+c,0n);
// m9(s) = 2^s h9(s)/262144, s>=9.
const h9=[19683n,-373977n,-5078214n,225467550n,-2791719189n,13314869127n,38834268264n,-860330966220n,4551847454736n,-9191974659840n];
// m9(s)-2m9(s-1) = 2^s d9(s)/262144, s>=10.
const d9=[177147n,-3700404n,-23422770n,1436025024n,-17489688237n,85841160804n,5218922340n,-1768561480944n,5434675948800n];
// a_(s,s-9) = 2^s q9(s)/19025362944, s>=9.
const q9=[390625n,-7734375n,78168750n,-476358750n,1425041625n,-3010947975n,9059710376n,13181542092n,-4890698640n,-67733293824n];
const shift9=[390625n,23906250n,660356250n,10827022500n,115842806625n,830967262650n,3922229318276n,11404006965144n,17815878242784n,11071720783872n];
const chk={degree:0,moment9:0,moment9_difference:0,newton9_direct:0,newton9_recovery:0,shifted_identity:0,positive_bound:0};
let P=[[1n]],lastMoment=null;const samples={};
for(let t=0;t<=N;t++){
 if(t){let f=mul(num(t),minus(t));for(let i=1;i<=Math.min(t,12);i++)f=add(f,mul(mul(delta(i),P[t-i]),minus(i-1)),-1n);P.push(f);}
 let x=P[t],s=BigInt(t),pow=2n**s;
 if(x.length-1>2*t+1)throw Error('degree t='+t);chk.degree++;
 if(t>=9){
   const ms=Array.from({length:10},(_,r)=>moment(x,r));
   if(262144n*ms[9]!==pow*poly(h9,s))throw Error('m9 formula t='+t);chk.moment9++;
   if(t>=10){if(262144n*(ms[9]-2n*lastMoment)!==pow*poly(d9,s))throw Error('m9 difference t='+t);chk.moment9_difference++;}
   let a=0n;for(let j=0;j<x.length;j++)a+=x[j]*choose(2*t+1-j,9);
   if(19025362944n*a!==pow*poly(q9,s))throw Error('q9 formula t='+t);chk.newton9_direct++;
   let recovered=0n;
   for(let r=0;r<=9;r++){
      let ff=1n;for(let j=0;j<9-r;j++)ff*=BigInt(2*t+1-r-j);
      recovered+=(r%2?-1n:1n)*choose(9,r)*ff*ms[r];
   }
   if(recovered!==362880n*a)throw Error('moment recovery t='+t);chk.newton9_recovery++;
   if(poly(shift9,s-9n)!==poly(q9,s))throw Error('shift t='+t);chk.shifted_identity++;
   if(128n*a<74489n*pow)throw Error('positive bound t='+t);chk.positive_bound++;
   if([9,10,11,12,13,20,32,128,192].includes(t))samples[t]={moment9:String(ms[9]),newton_q9:String(a)};
   lastMoment=ms[9];
 }
}
console.log(JSON.stringify({schema:'EM_R321_EXACT_EVIDENCE_V1',status:'PASS',model:'ordered positive six-edge BRC auxiliary polynomial',arithmetic:'Node.js BigInt integer only',range_s:[0,N],checks:chk,samples,claim:'For all integers s>=9, a_(s,s-9) >= (74489/128)*2^s > 0',proof_scope:'Universal claim follows from a separate symbolic recurrence induction and positive shift polynomial; finite computation covers s<=192.',native_acceptance:false},null,2));
