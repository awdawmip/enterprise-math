"use strict";
// Stage410-B exact native-X6 signed-direction Path-formal certificate.
// A=+E1, B=-E1; all other ten native direction labels remain available in APP.
function J(w) {const c={AA:0,AB:0,BA:0,BB:0};for(let i=1;i<w.length;i++)c[w[i-1]+w[i]]++;return c;}
function K(p,q){let k=0;for(let i=0;i<Math.min(p.length,q.length);i++)k+=(p[i]===q[i]);return k;}
function z(w){return [...w].reduce((s,x)=>s+(x==="A"?1:-1),0);}
function O(p,q){return JSON.stringify([p.length,q.length,z(p),z(q),J(p),J(q),K(p,q)]);}
const classes=[
  [["ABAAAA","ABABAA"],["AAABAA","ABABAA"]],
  [["ABAAAA","ABAABA"],["AABAAA","AABABA"]],
  [["AAAABA","ABAABA"]],
  [["AAAABA","AABABA"]]
];
function enumerate() {
 const P=[],Q=[];
 for(let i=1;i<=4;i++)P.push("A".repeat(i)+"B"+"A".repeat(5-i));
 for(let u=1;u<=2;u++)for(let v=1;v<=3-u;v++){
   const w=4-u-v;if(w>0)Q.push("A".repeat(u)+"B"+"A".repeat(v)+"B"+"A".repeat(w));
 }
 return P.flatMap(p=>Q.filter(q=>K(p,q)===5).map(q=>[p,q]))
    .sort((x,y)=>(x.join("|")).localeCompare(y.join("|")));
}
function eulerK(){
 const ix={AA:0,AB:1,BA:2,BB:3};
 const s={rp:[3,1,1,0],rq:[1,2,2,0],p:"A",q:"A",sp:"A",sq:"A",k:1};
 let states=new Map([[JSON.stringify(s),[s,1n]]]),sizes=[1];
 for(let t=1;t<6;t++){
   const next=new Map();
   for(const [st,m] of states.values())for(const a of "AB")for(const b of "AB"){
     const i=ix[st.p+a],j=ix[st.q+b];if(!st.rp[i]||!st.rq[j])continue;
     const rp=st.rp.slice(),rq=st.rq.slice();rp[i]--;rq[j]--;
     const v={rp,rq,p:a,q:b,sp:(st.sp+a).slice(-3),sq:(st.sq+b).slice(-4),k:st.k+(a===b?1:0)};
     const key=JSON.stringify(v),old=next.get(key);
     if(old)old[1]+=m;else next.set(key,[v,m]);
   }
   states=next;sizes.push(states.size);
 }
 const counts={};let total=0n;
 for(const [s,m] of states.values())if(s.k===5){
   if(s.rp.some(Boolean)||s.rq.some(Boolean))throw Error("nonzero residual edges");
   const key=s.sp+"|"+s.sq;counts[key]=(BigInt(counts[key]||"0")+m).toString();total+=m;
 }
 return {total:total.toString(),suffix_keys:Object.fromEntries(Object.entries(counts).sort()),states_per_depth:sizes};
}
// A complete typed boundary certificate for each claimed equivalent pair.
// All possible numbers of removed ORIGINAL letters: dP<=1,dQ<=2.
// Once dP=1, CANCEL is spent; once dQ=2 both erasers are spent.
// Thus last-2 P tags are needed only for dP=0; Q last-2 tags only when dQ<=1.
function bisimCertificate(pair){
 const [[p,q],[p2,q2]]=pair;let checked=0;
 for(let dp=0;dp<=1;dp++)for(let dq=0;dq<=2;dq++){
   const a=p.slice(0,6-dp),b=q.slice(0,6-dq),c=p2.slice(0,6-dp),d=q2.slice(0,6-dq);
   if(O(a,b)!==O(c,d))throw Error("truncated original observable mismatch");
   if(a.slice(-(dp===0?2:1))!==c.slice(-(dp===0?2:1)))throw Error("P boundary mismatch");
   if(b.slice(-(dq<2?2:1))!==d.slice(-(dq<2?2:1)))throw Error("Q boundary mismatch");
   if(dp<dq && a.slice(6-dq)!==c.slice(6-dq))throw Error("P overlap mismatch");
   if(dq<dp && b.slice(6-dp)!==d.slice(6-dp))throw Error("Q overlap mismatch");
   checked++;
 }
 return checked;
}
function canC(p,q){return p.length>=2&&q.length>=2&&p[p.length-2]!==p[p.length-1]&&q[q.length-2]!==q[q.length-1];}
function afterC(p,q){return canC(p,q)?[p.slice(0,-2),q.slice(0,-2)]:null;}
function witness(i,j){
 const a=classes[i][0],b=classes[j][0];
 if(canC(...a)!==canC(...b))return "CANCEL enabledness";
 const popa=[a[0],a[1].slice(0,-1)],popb=[b[0],b[1].slice(0,-1)];
 if(O(...popa)!==O(...popb))return "POP_Q observed J,K,endpoints";
 const ca=afterC(...popa),cb=afterC(...popb);
 if((ca===null)!==(cb===null))return "POP_Q; CANCEL enabledness";
 if(ca && O(...ca)!==O(...cb))return "POP_Q; CANCEL observed J,K,endpoints";
 throw Error("missing class distinguisher: "+i+","+j);
}
function nativeBRC(){
 // Full 12 signed X6 directions, weighted path recurrence; integer arithmetic only.
 const dirs=[];for(let i=0;i<6;i++)for(const sign of [1,-1])dirs.push([i,sign,(i===0?(sign===1?2n:3n):1n)]);
 let dp=new Map([["0,0,0,0,0,0",[1n,1n]]]);
 for(let t=0;t<6;t++){
   const next=new Map();
   for(const [key,[N,W]] of dp){
     const v=key.split(",").map(Number);
     for(const [i,sign,weight] of dirs){
       const u=v.slice();u[i]+=sign;const k=u.join(",");const old=next.get(k)||[0n,0n];
       next.set(k,[old[0]+N,old[1]+weight*W]);
     }
   }
   dp=next;
 }
 const get=x=>{const [n,w]=dp.get([x,0,0,0,0,0].join(","))||[0n,0n];return {N:n.toString(),W:w.toString()};};
 return {P_4E1:get(4),Q_2E1:get(2)};
}
function main(){
 const F=enumerate(),listed=classes.flat(),seen=new Set(F.map(x=>x.join("|")));
 if(F.length!==6||seen.size!==6||listed.length!==6||listed.some(x=>!seen.has(x.join("|"))))throw Error("incomplete exact observation fiber");
 const initial=O(...F[0]);
 if(F.some(x=>O(...x)!==initial))throw Error("current observation not constant");
 const dp=eulerK(),safe=new Set(F.map(([p,q])=>p.slice(-3)+"|"+q.slice(-4)));
 if(dp.total!=="6"||safe.size!==6||Object.keys(dp.suffix_keys).length!==6||
    Object.keys(dp.suffix_keys).some(k=>!safe.has(k)||dp.suffix_keys[k]!=="1"))
   throw Error("independent residual Euler/K calculation disagrees");
 const prefix_cases=bisimCertificate(classes[0])+bisimCertificate(classes[1]);
 const witnesses=[];
 for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)witnesses.push({classes:[i,j],trace:witness(i,j)});
 const brc=nativeBRC();
 if(brc.P_4E1.N!=="156"||brc.Q_2E1.N!=="4665"||brc.P_4E1.W!=="2976"||brc.Q_2E1.W!=="32760")
   throw Error("full native X6 BRC recurrence mismatch");
 return {status:"STAGE410B_ONE_DEFECT_FOUR_CLASS_PASS",initial_observation:JSON.parse(initial),
   full_fiber:F,equivalence_classes:classes,multiplicities:classes.map(x=>x.length),
   exact_minimum_states:4,raw_suffix_keys:6,original_prefix_certificate_cases:prefix_cases,
   distinguishers:witnesses,residual_Euler_K:dp,full_X6_native_BRC:brc,
   theorem_scope:"All 12 signed native APP pairs; <=1 POP_Q; <=1 synchronous inverse-pair CANCEL; all finite action traces (bisimulation proof)"};
}
const output=main();
if(typeof console!=="undefined")console.log(JSON.stringify(output,null,2));
