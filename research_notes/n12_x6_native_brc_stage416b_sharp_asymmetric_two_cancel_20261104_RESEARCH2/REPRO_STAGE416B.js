'use strict';
// Stage416-B exact X6 witnesses and source-labeled suffix-key counts.
// All output is integer/finite. All-horizon sufficiency is proved in PROOF_STAGE416B.md.
const D=Array.from({length:6},(_,i)=>[i+1,-(i+1)]).flat();
function letters(s){return [...s].map(ch=>ch==='A'?1:-1)}
function observer(p,q){
  function src(w){
    const z=Array.from({length:6},(_,i)=>w.filter(x=>x===i+1).length-w.filter(x=>x===-(i+1)).length);
    const J={};
    for(let i=0;i<w.length-1;i++){const k=w[i]+','+w[i+1];J[k]=(J[k]||0)+1}
    return [w.length,z,Object.entries(J).sort((a,b)=>a[0].localeCompare(b[0]))]
  }
  return [src(p),src(q),p.reduce((k,x,i)=>k+(i<q.length&&x===q[i]?1:0),0)]
}
function equal(x,y){return JSON.stringify(x)===JSON.stringify(y)}
const trace=[['POP'],['POP'],['CANCEL'],['CANCEL']];
function run(p0,q0,actions){
  let p=p0.slice(),q=q0.slice(),pop=2,cancel=2,records=[observer(p,q)];
  for(const a of actions){
    if(a[0]==='POP'){if(!pop||!q.length)return {status:'DENIED_POP',records};q.pop();pop--}
    else if(a[0]==='CANCEL'){
      if(!cancel||p.length<2||q.length<2||p.at(-1)!==-p.at(-2)||q.at(-1)!==-q.at(-2))return {status:'DENIED_CANCEL',records};
      p.splice(-2);q.splice(-2);cancel--
    }else if(a[0]==='APP'){if(!D.includes(a[1])||!D.includes(a[2]))throw Error('direction');p.push(a[1]);q.push(a[2])}
    else throw Error('action');
    records.push(observer(p,q))
  }
  return {status:'OK',records}
}
function demand(b,msg){if(!b)throw Error(msg)}
const cases={
 P_five_tail_failure:['AABAABAB','AAABABAA','ABAAABAB','AAABABAA',5,7],
 Q_six_tail_failure:['AAAAAABAB','AABABABAA','AAAAAABAB','ABAABABAA',6,6]
};
const witnesses={};
for(const [key,[sp,sq,tp,tq,kp,kq]] of Object.entries(cases)){
  const [p,q,r,s]=[sp,sq,tp,tq].map(letters);
  demand(equal(observer(p,q),observer(r,s)),'initial O '+key);
  demand(equal(p.slice(-kp),r.slice(-kp))&&equal(q.slice(-kq),s.slice(-kq)),'suffix '+key);
  const h=run(p,q,trace),i=run(r,s,trace);
  demand(h.status==='OK'&&i.status==='OK'&&!equal(h.records.at(-1),i.records.at(-1)),'witness '+key);
  for(const a of D)for(const b of D) demand(equal(observer([...p,a],[...q,b]),observer([...r,a],[...s,b])),'first APP '+key);
  witnesses[key]={inputs:[sp,sq,tp,tq],matching_suffix:[kp,kq],initial_observation_equal:true,
    final_K:[h.records.at(-1)[2],i.records.at(-1)[2]],
    final_observers_differ:true,first_APP_full_144_checks:'PASS'};
}
function fiber(n){
 const f=[];
 for(let r=2;r<n-2;r++)for(let s=r+2;s<n;s++)for(const i of [r,s]){
  const p='A'.repeat(i-1)+'B'+'A'.repeat(n-i);
  const q='A'.repeat(r-1)+'B'+'A'.repeat(s-r-1)+'B'+'A'.repeat(n-s);
  f.push([p,q]);
 }
 return f
}
const counts={};
for(let n=5;n<=25;n++){
 const f=fiber(n), k67=new Set(f.map(([p,q])=>p.slice(-6)+'|'+q.slice(-7))),
 k77=new Set(f.map(([p,q])=>p.slice(-7)+'|'+q.slice(-7)));
 demand(f.length===(n-3)*(n-4),'fiber count '+n);
 if(n>=11)demand(k67.size===32&&k77.size===33,'stable key count '+n);
 counts[n]=[f.length,k67.size,k77.size]
}
return {marker:'STAGE416B_SHARP_6_7_EXACT_PASS',
  scope:'All-horizon theorem is symbolic; executable checks exact witnesses, 144 one-APP direction pairs each, and complete F_n for 5<=n<=25.',
  science_pins:{global:'bf84bd7c61a2444b59b1da96be57df0e9ae47e53',enterprise_math:'2af3fc484eb11060b69e0afc1b562bcaf5ad1419',p000_blob:'bcc2590d3168a28f72e8b9f0f9b1f76faadcd488'},
  trace,witnesses,counts};
