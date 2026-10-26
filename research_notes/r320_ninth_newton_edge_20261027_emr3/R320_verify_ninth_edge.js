'use strict';
// R320: exact BigInt cross-check of the original ordered six-edge BRC recurrence.
// All arithmetic is integer; no float or numerical interpolation is used as a proof.
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
// m8(s) = 2^s H8(s), H8(s) = h8(s)/65536 for s>=8.
const h8=[6561n,-90396n,-1371006n,41693400n,-395382351n,1509433716n,1771638636n,-36493134960n,99723415680n];
// m8(s)-2m8(s-1) = 2^s d8(s)/8192 for s>=9.
const d8=[6561n,-102060n,-745038n,28176120n,-252794031n,917001540n,-347820132n,-4539623760n];
// a_(s,s-8) = 2^s q8(s)/528482304 for s>=8.
const q8=[78125n,-1187500n,8916250n,-41125000n,72310525n,-81437020n,509008124n,808645200n,-308472192n];
const shift8=[78125n,3812500n,82416250n,1030855000n,8106910525n,40334899780n,119864161244n,183822902544n,103334805504n];
const chk={degree:0,moment8:0,moment8_difference:0,newton8_direct:0,newton8_recovery:0,shifted_identity:0,positive_bound:0};
let P=[[1n]],lastMoment=null;const samples={};
for(let t=0;t<=N;t++){
 if(t){let f=mul(num(t),minus(t));for(let i=1;i<=Math.min(t,12);i++)f=add(f,mul(mul(delta(i),P[t-i]),minus(i-1)),-1n);P.push(f);}
 let x=P[t],s=BigInt(t),pow=2n**s;
 if(x.length-1>2*t+1)throw Error('degree t='+t);chk.degree++;
 if(t>=8){
   const ms=Array.from({length:9},(_,r)=>moment(x,r));
   if(65536n*ms[8]!==pow*poly(h8,s))throw Error('m8 formula t='+t);chk.moment8++;
   if(t>=9){if(8192n*(ms[8]-2n*lastMoment)!==pow*poly(d8,s))throw Error('m8 difference t='+t);chk.moment8_difference++;}
   let a=0n;for(let j=0;j<x.length;j++)a+=x[j]*choose(2*t+1-j,8);
   if(528482304n*a!==pow*poly(q8,s))throw Error('q8 formula t='+t);chk.newton8_direct++;
   let recovered=0n;
   for(let r=0;r<=8;r++){
      let ff=1n;for(let j=0;j<8-r;j++)ff*=BigInt(2*t+1-r-j);
      recovered+=(r%2?-1n:1n)*choose(8,r)*ff*ms[r];
   }
   if(recovered!==40320n*a)throw Error('moment recovery t='+t);chk.newton8_recovery++;
   if(poly(shift8,s-8n)!==poly(q8,s))throw Error('shift t='+t);chk.shifted_identity++;
   if(32n*a<6257n*pow)throw Error('positive bound t='+t);chk.positive_bound++;
   if([8,9,10,11,12,20,32,128,192].includes(t))samples[t]={moment8:String(ms[8]),newton_q8:String(a)};
   lastMoment=ms[8];
 }
}
console.log(JSON.stringify({schema:'EM_R320_EXACT_EVIDENCE_V1',status:'PASS',model:'ordered positive six-edge BRC auxiliary polynomial',arithmetic:'Node.js BigInt integer only',range_s:[0,N],checks:chk,samples,claim:'For all integers s>=8, a_(s,s-8) >= (6257/32)*2^s > 0',proof_scope:'Universal claim follows from separate symbolic recurrence induction and positive shift polynomial; finite computation covers only s<=192.',native_acceptance:false},null,2));
