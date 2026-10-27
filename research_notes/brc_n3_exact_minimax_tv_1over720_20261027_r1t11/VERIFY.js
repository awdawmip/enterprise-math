'use strict';
const A=require('node:assert/strict');
const N={
root:[0,240,240,['a','b']],a:[1,180,120,['ax','ay']],b:[1,60,120,['bu','bv']],
ax:[2,60,60,['axL','axM','axH']],ay:[2,120,60,['ayT']],
bu:[2,30,30,['buL','buM','buH']],bv:[2,30,90,['bvT']],
axL:[3,12,24,[]],axM:[3,12,12,[]],axH:[3,36,24,[]],
ayT:[3,120,60,[]],buL:[3,5,10,[]],buM:[3,10,10,[]],
buH:[3,15,10,[]],bvT:[3,30,90,[]]};
A.equal(Object.keys(N).length,15);
A.equal(Object.values(N).filter(v=>!v[3].length).length,8);
for(const [h,[t,p,q,ch]] of Object.entries(N)){
 A(p>0&&q>0);
 if(ch.length){A.equal(ch.reduce((s,k)=>s+N[k][1],0),p);
  A.equal(ch.reduce((s,k)=>s+N[k][2],0),q);
  for(const k of ch)A.equal(N[k][0],t+1);}
}
// Joint law grid: T0P,T0Q,T1P,T1Q,T2P,T2Q,T3P,T3Q; exact units 1/720.
const fullP=[0,0,0,0,360,90,108,162],fullQ=[0,0,0,0,180,90,72,378];
const compP=[0,0,0,0,360,90,107,163],compQ=[0,0,0,0,180,90,73,377];
const sum=a=>a.reduce((s,v)=>s+v,0);
for(const v of [fullP,fullQ,compP,compQ])A.equal(sum(v),720);
A.equal(fullP[4],3*120);A.equal(fullP[5],3*30);
A.equal(fullQ[4],3*60);A.equal(fullQ[5],3*30);
A.equal(fullP[6],3*36);A.equal(fullP[7],3*(12+12+30));
A.equal(fullQ[6],3*24);A.equal(fullQ[7],3*(24+12+90));
// Compression stops at common collision state with 1/3 and continues with 2/3.
// Terminal L=Q,H=P; terminal M chooses P with 5/44 and Q with 39/44.
A.equal(compP[4],3*120);A.equal(compP[5],60+30);
A.equal(compQ[4],3*60);A.equal(compQ[5],60+30);
A.equal(compP[6],2*51+5);A.equal(compP[7],2*17+39+3*30);
A.equal(compQ[6],2*34+5);A.equal(compQ[7],2*34+39+3*90);
const J=(p,q)=>90*(p[4]+p[5]+p[6])+17*(q[4]+q[5])+90*q[7];
const collStop=90*107,collCont=60*108+30*105;
A.equal(collStop,collCont);
const support=60*197+90*90+collStop,fullSupport=60*197+90*90+60*108+30*107;
A.equal(support,29550);A.equal(fullSupport,29610);
A.equal(J(compP,compQ),support*3);
A.equal(J(fullP,fullQ),fullSupport*3);
const tv720=(p,q)=>sum(p.map((v,i)=>Math.abs(v-q[i])))/2;
A.equal(tv720(fullP,compP),1);A.equal(tv720(fullQ,compQ),1);
for(let t=0;t<4;t++){
 A.equal(fullP[2*t]+fullP[2*t+1],compP[2*t]+compP[2*t+1]);
 A.equal(fullQ[2*t]+fullQ[2*t+1],compQ[2*t]+compQ[2*t+1]);
}
A.equal((fullSupport-support)/240,1/4);A.equal(15/720,1/48);
console.log(JSON.stringify({status:'PASS_EXACT_INTEGER_720',ordered_prefixes:15,terminals:8,
parameters:['2/5','1/3'],max_compressed_J:'985/8',full_history_J:'987/8',J_gap:'1/4',
full_P_720:fullP,full_Q_720:fullQ,compressed_P_720:compP,compressed_Q_720:compQ,
TV_P:'1/720',TV_Q:'1/720',exact_fixed_history_inf_maxTV:'1/720',
improved_global_K_lower:'1/48',prior_K_lower:'15/2527',known_global_K_upper:'1/6',
stop_time_marginals_preserved:true,scope:'AUTHOR_UNREVIEWED_NOT_ADMITTED'},null,2));
