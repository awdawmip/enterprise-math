"use strict";
// Exact frozen R462 signed K(i) operator, theta=0; no floating point.
const C=(n,k)=>{if(k<0||k>n)return 0n;let x=1n;k=Math.min(k,n-k);for(let a=1;a<=k;a++)x=x*BigInt(n-a+1)/BigInt(a);return x;};
const mul=(a,b)=>{let c=Array(a.length+b.length-1).fill(0n);a.forEach((x,i)=>b.forEach((y,j)=>c[i+j]+=x*y));return c;};
const kern=i=>{
 const d=[-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3)];
 let z=Array(2*i+5).fill(0n);
 for(let j=1;j<=4;j++){const k=i+1-j;if(k<0)continue;for(let a=0;a<=k;a++)z[i-1+a]-=d[j-1]*C(k,a);}
 while(z.length>1&&z[z.length-1]===0n)z.pop();return z;
};
const ks=Array.from({length:12},(_,i)=>kern(i+1));
const alpha=ks.map((p,i)=>p[i]);
const nu=p=>p.findIndex(x=>x!==0n);
const assert=(x,m)=>{if(!x)throw Error(m);};
function run(){
 assert(alpha.map(String).join(",")==="2,-1,-8,-11,6,53,106,119,83,36,9,1","twelve leaders");
 for(let i=0;i<12;i++)assert(nu(ks[i])===i,"K valuation");
 let words=0;
 function walk(p,s,len,a){
   const v=nu(p);assert(v===s-len&&p[v]===a,"single-source valuation");
   for(let d=0;d<=Math.min(s,10);d++)assert(p.slice(0,d+1).every(x=>x===0n)===(v>d),"zero jet");
   words++;if(len===4)return;
   for(let i=1;i<=12;i++)walk(mul(p,ks[i-1]),s+i,len+1,a*alpha[i-1]);
 }
 walk([1n],0,0,1n);assert(words===22621,"word coverage");
 function attainable(s,v){
   return s>=0&&v>=0&&(s-v)%2===0&&(3*v-s)%8===0&&
          (3*v-s)>=0&&((3*v-s)/8)<=5*((s-v)/2);
 }
 const seen=new Set(["0,0"]);
 for(let j=1;j<=6;j++){
   let ds=4*j-1,dv=4*j-3;
   for(let s=ds;s<=180;s++)for(let v=dv;v<=180;v++){
     if(seen.has((s-ds)+","+(v-dv)))seen.add(s+","+v);
   }
 }
 for(let s=0;s<=180;s++)for(let v=0;v<=180;v++)
   assert(seen.has(s+","+v)===attainable(s,v),"closed criterion "+s+","+v);
 const closed=[];
 function enumerate(j,left,r=[]){
   if(j===6){if(left===0)closed.push(r);return;}
   const w=4*j+3;
   for(let n=0;n<=Math.floor(left/w);n++)enumerate(j+1,left-w*n,r.concat(n));
 }
 enumerate(0,21);
 function fact(n){let x=1n;for(let i=2;i<=n;i++)x*=BigInt(i);return x;}
 const buckets={};
 const rows=closed.map(r=>{
   const length=2*r.reduce((a,b)=>a+b,0);
   const v=21-length;
   let count=fact(length),lead=1n;
   for(let j=0;j<6;j++){count/=fact(r[j])*fact(r[j]);lead*=((alpha[2*j]*alpha[2*j+1])**BigInt(r[j]));}
   buckets[v]=(buckets[v]||0n)+count;
   return {r,valuation:v,count:String(count),leading:String(lead)};
 });
 assert(String(buckets[7])==="3432"&&String(buckets[15])==="920"&&rows.length===4,"level21");
 const family=[];
 for(let n=1;n<=5;n++){
   let A=[1n,1n],B=[1n,1n];
   for(let k=0;k<7*n;k++)A=mul(mul(A,ks[0]),ks[1]);
   for(let k=0;k<3*n;k++)B=mul(mul(B,ks[2]),ks[3]);
   assert(nu(A)===7*n&&nu(B)===15*n,"family valuations");
   assert(A[7*n]===(-2n)**BigInt(7*n),"family leading signed");
   family.push({n,level:21*n,first_split:7*n,other_first:15*n,leading_diff:String(A[7*n])});
 }
 return {schema:"EM_R620_SIGNED_BRC_VALUATION_CLOSED_FIBER_V1",science_pin:"R462@18783e01e3646c72b7aab3b16d3f565e83e6446f",source_blob:"7fa7a762f758b30c6090468ac43487daa34abad8",arithmetic:"exact JavaScript BigInt using original frozen K operator",leaders:alpha.map(String),short_words_checked:words,closed_semigroup_pairs_checked:181*181,closed_level21_rows:rows,closed_level21_total:String(buckets[7]+buckets[15]),closed_level21_valuation_counts:{"7":String(buckets[7]),"15":String(buckets[15])},family,pass:"R620_EXACT_VALUATION_CLOSED_FIBER_PASS"};
}
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module)
 console.log(JSON.stringify(run(),null,2));
