"use strict";
function verifyPrefix284(){
 const c=(r,i=0)=>[BigInt(r),BigInt(i)];
 const add=(x,y)=>[x[0]+y[0],x[1]+y[1]];
 const conj=x=>[x[0],-x[1]];
 const mul=(x,y)=>[x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]];
 const equal=(x,y)=>x[0]===y[0]&&x[1]===y[1];
 const norm=x=>x[0]*x[0]+x[1]*x[1];
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b!==0n){const t=a%b;a=b;b=t;}return a;};
 const frac=(n,d)=>{if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g].join("/");};
 const phase=(m,p)=>p===0?c(m):p===1?c(0,m):p===2?c(-m):c(0,-m);
 function correlation(a,r){let total=c(0);for(let j=0;j+r<a.length;j++)total=add(total,mul(a[j],conj(a[j+r])));return total;}
 function signature(a){const Z=a.reduce((z,x)=>z+norm(x),0n),u=correlation(a,1),v=correlation(a,2);return [frac(u[0],Z),frac(u[1],Z),frac(v[0],Z),frac(v[1],Z),frac(norm(a[0]),Z)].join("|");}
 function ratio(a){return [frac(a[1][0],a[0][0]),frac(a[1][1],a[0][0]),frac(a[2][0],a[0][0]),frac(a[2][1],a[0][0])].join("|");}
 const check=(cond,msg)=>{if(!cond)throw Error(msg);};
 let grouped=new Map(),testedC4=0,realGroup=new Map(),testedReal=0;
 for(let m0=1;m0<=3;m0++)for(let m1=1;m1<=3;m1++)for(let m2=1;m2<=3;m2++)for(let p1=0;p1<4;p1++)for(let p2=0;p2<4;p2++){
   const a=[c(m0),phase(m1,p1),phase(m2,p2)],key=signature(a);
   if(!grouped.has(key))grouped.set(key,[]);grouped.get(key).push(a);testedC4++;
 }
 let ambiguous=0,maxClasses=0,ambiguousPairs=0,regular=0,singular=0;
 for(const [key,entries] of grouped){
   const unique=Array.from(new Map(entries.map(a=>[ratio(a),a])).values());
   const isSingular=norm(unique[0][0])===norm(unique[0][2]);
   maxClasses=Math.max(maxClasses,unique.length);
   if(isSingular)singular++;else regular++;
   check(unique.length<=(isSingular?2:1),"invalid class count "+key);
   if(unique.length>1){
     ambiguous++;
     check(isSingular,"nonsingular ambiguity");
     for(let i=0;i<unique.length;i++)for(let j=i+1;j<unique.length;j++){
       const a=unique[i],b=unique[j],a0=a[0][0],b0=b[0][0];
       const left=[b[1][0]*a0*a0,b[1][1]*a0*a0];
       const raw=mul(a[2],conj(a[1])),right=[raw[0]*b0,raw[1]*b0];
       check(equal(left,right),"twisted conjugation mismatch "+key);ambiguousPairs++;
     }
   }
 }
 for(let m0=1;m0<=8;m0++)for(let m1=1;m1<=8;m1++)for(let m2=1;m2<=8;m2++){
   const a=[c(m0),c(m1),c(m2)],key=signature(a);
   if(!realGroup.has(key))realGroup.set(key,new Set());realGroup.get(key).add(ratio(a));testedReal++;
 }
 for(const [key,ratios] of realGroup)check(ratios.size===1,"positive real nonuniqueness "+key);
 const a=[c(1),c(0,1),c(1)],b=[c(1),c(0,-1),c(1)];
 check(signature(a)===signature(b),"example observer mismatch");
 function orderedBRC(pkt){
   // 2 E = I - i |0><1| + i |1><0|, exact Hermitian candidate binary effect.
   const E2=[[c(1),c(0,-1),c(0)],[c(0,1),c(1),c(0)],[c(0),c(0),c(1)]];
   let sum=c(0);
   for(let j=0;j<3;j++)for(let k=0;k<3;k++)sum=add(sum,mul(mul(conj(pkt[j]),E2[j][k]),pkt[k]));
   check(sum[1]===0n,"complex probability");
   return frac(sum[0],2n*pkt.reduce((z,x)=>z+norm(x),0n));
 }
 const pA=orderedBRC(a),pB=orderedBRC(b);
 check(pA==="5/6" && pB==="1/6","binary BRC witness");
 for(let lag=0;lag<3;lag++)check(equal(correlation(a,lag),correlation(b,lag)),"C4 witness not homometric");
 return {
 schema:"PREFIX284_C4_ENDPOINT_RECONSTRUCTION_EXACT_CHECK_V1",
 status:"PASS_AUTHOR_SIDE_EXACT_TYPED_C4_BRC",
 source_pin:"awdawmip/enterprise-math@25cf910c09db04fec70f9de1a24467c06046faf3",
 operation:"source-labelled C4 ordered-pair BRC; no classical propagators or trigonometry",
 C4_weights:"1..3 inclusive",C4_first_phase:"fixed to 1 by global C4 gauge",C4_other_phases:"1,i,-1,-i",
 C4_packets_tested:testedC4,C4_distinct_observation_signatures:grouped.size,
 nonsingular_observation_signatures:regular,singular_observation_signatures:singular,
 ambiguous_signatures:ambiguous,ambiguous_normalized_class_pairs:ambiguousPairs,
 maximum_gauge_classes_per_signature:maxClasses,
 positive_real_weights:"1..8 inclusive",positive_real_packets_tested:testedReal,
 positive_real_distinct_signatures:realGroup.size,positive_real_nonunique_normalized_states:0,
 counterexample:{a:["1","i","1"],b:["1","-i","1"],C0:"3",C1:"0",C2:"1",p0:"1/3",
 hypothetical_binary_effect:"E=I/2+(-i|0><1|+i|1><0|)/2",
 exact_readout_a:pA,exact_readout_b:pB,gap:"2/3"},
 verification_scope:"Finite enumeration is not the proof of the general classification; no Stage50 or physical detector run this turn.",
 missing_native:["post-preparation X6 source-selective detector","model_law_id","heartbeat transition law"]
 };
}
const summary=verifyPrefix284();
console.log(JSON.stringify(summary,null,2));