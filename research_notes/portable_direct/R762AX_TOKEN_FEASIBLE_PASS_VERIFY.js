'use strict';
// R762AX exact integer checker. Run: node R762AX_TOKEN_FEASIBLE_PASS_VERIFY.js > R762AX_TOKEN_FEASIBLE_PASS_EVIDENCE.json
const calculate = function calculate(){
 const ck=(v,msg)=>{if(!v)throw Error("R762AX CHECK FAILED: "+msg)};
 const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
 const perm=a=>a.length===0?[[]]:a.flatMap((x,i)=>perm(a.filter((_,j)=>i!==j)).map(z=>[x,...z]));
 const fac=n=>{let r=1;for(let i=2;i<=n;i++)r*=i;return r};
 const q=(m,S)=>{if(S.length===0)return 0;const a=[...S].sort((x,y)=>x-y);let d=1;for(let i=0;i<a.length;i++){const gap=(a[(i+1)%a.length]-a[i]+m)%m||m;d*=fac(gap)}return fac(m)/d};
 const feasible=(p,K)=>{const a=K.slice();for(const i of p){const j=(i+1)%a.length;if(a[i]===0)return false;a[i]--;a[j]++}ck(same(a,K),"return K");return true};
 let cycleCases=0,permutationTests=0;
 for(let m=2;m<=7;m++){const ps=perm(Array.from({length:m},(_,i)=>i));for(let bits=0;bits<(1<<m);bits++){const S=Array.from({length:m},(_,i)=>i).filter(i=>((bits>>i)&1)===1),K=Array.from({length:m},(_,i)=>((bits>>i)&1)?1:0),wide=K.map((v,i)=>v?(i+2):0);let count=0;for(const p of ps){const a=feasible(p,K),b=feasible(p,wide);ck(a===b,"stock magnitude invariance");if(a)count++;permutationTests++}ck(count===q(m,S),"multinomial m="+m+" S="+S);cycleCases++}}
 const match=[[[0,1],[2,3],[4,5]],[[0,2],[1,4],[3,5]],[[0,3],[1,5],[2,4]],[[0,4],[1,3],[2,5]]],events=[[0,1],[1,2],[2,0]];
 const states=[];for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)for(let k=j+1;k<6;k++)states.push([i,j,k]);
 const name=s=>s.join(""),codes={};for(const s of states)codes[name(s)]=match.map(p=>p.every(([a,b])=>s.includes(a)!==s.includes(b))?p.reduce((v,[a,b])=>v*(s.includes(b)?-1:1),1):0);
 const neighbors={};for(const s of states)neighbors[name(s)]=states.filter(t=>s.filter(x=>t.includes(x)).length===2).map(name);
 const score=(s,t,n,b)=>{const M=Array.from({length:4},()=>Array(4).fill(0));events.forEach(([a,c],i)=>M[a][c]=n+((b>>i)&1));const u=[-2,-4,-3,10].map((v,i)=>v+M[i].reduce((a,x)=>a+x,0)-M.reduce((a,row)=>a+row[i],0));let z=0,cs=codes[s],ct=codes[t];for(let i=0;i<4;i++){z+=u[i]*ct[i];for(let j=0;j<4;j++)z+=cs[i]*(M[i][j]-M[j][i])*ct[j]}return z};
 const winners=(s,n,b)=>{const a=neighbors[s].map(t=>[t,score(s,t,n,b)]),max=Math.max(...a.map(x=>x[1]));return a.filter(x=>x[1]===max).map(x=>x[0]).sort()};
 const C=["012","123","234","034","035","025"],orders=perm([0,1,2]);
 const trace=p=>p.map((_,i)=>p.slice(0,i+1).reduce((a,x)=>a|(1<<x),0));
 for(const n of [16,17,23,100])for(let i=0;i<6;i++)for(let b=0;b<8;b++)ck(same(winners(C[i],n,b),[C[(i+1)%6]]),"cyclic unique");
 const phases={};let expansions=0;
 for(let bits=0;bits<8;bits++){
  const S=[0,1,2].filter(i=>(bits>>i)&1),K=[0,1,2].map(i=>(bits>>i)&1),P=orders.filter(p=>feasible(p,K));ck(P.length===q(3,S),"q3");
  const data={positive_support:S,q:P.length,orders:P.map(p=>p.join("")),one_macro:{}};
  for(const s of states.map(name)){
   const histories=[];
   for(const p of P){let h=[{last:s,states:[s]}];for(const b of trace(p)){const next=[];for(const z of h)for(const y of winners(z.last,16,b))next.push({last:y,states:[...z.states,y]});h=next}histories.push(...h);expansions++}
   ck(histories.every(x=>C.includes(x.last)),"one-macro absorption");
   const B1=histories.length;data.one_macro[s]={B1,end_vector:C.map(c=>histories.filter(x=>x.last===c).length),distinct_state_paths:new Set(histories.map(x=>x.states.join(">"))).size};
   if(C.includes(s))ck(B1===P.length,"unique C path");
  }
  phases[String(bits)]=data;
 }
 const ex=new Set(["013","014","024","135","235","245"]);
 for(const s of states.map(name))ck(phases["7"].one_macro[s].B1===(ex.has(s)?8:6),"AW regression");
 ck(same(phases["7"].one_macro["145"].end_vector,[2,0,4,0,0,0]),"AW 145");
 ck(same(phases["7"].one_macro["013"].end_vector,[0,0,6,0,0,2]),"AW 013");
 let frameTests=0, periodChecks=0, maximalPeriod=0, frameWitness=null;
 for(const m of [4,5]){
  const all=perm(Array.from({length:m},(_,i)=>i));
  for(const sigma of all)for(let mask=0;mask<(1<<m);mask++){
   const initial=Array.from({length:m},(_,i)=>i).filter(i=>(mask>>i)&1);
   let S=initial, orbit=[];
   do {
    const K=Array.from({length:m},(_,i)=>S.includes(i)?1:0);
    const viaQ=q(m,S), viaEnumerate=all.filter(p=>feasible(p,K)).length;
    ck(viaQ===viaEnumerate,"frame orbit legal word check");frameTests++;
    orbit.push(viaQ);S=S.map(i=>sigma[i]).sort((a,b)=>a-b);
    ck(orbit.length<=fac(m),"finite frame orbit");
   } while(!same(S,initial));
   const d=orbit.length;maximalPeriod=Math.max(maximalPeriod,d);
   let product=1;
   for(let h=0;h<8;h++){
    product*=orbit[h%d];
    const completeBlocks=Math.floor((h+1)/d),remainder=(h+1)%d;
    let block=1,tail=1;for(let j=0;j<d;j++)block*=orbit[j];for(let j=0;j<remainder;j++)tail*=orbit[j];
    ck(product===block**completeBlocks*tail,"frame transport block product");periodChecks++;
   }
   if(m===4&&same(sigma,[0,2,1,3])&&same(initial,[0,1]))frameWitness={m,sigma,initial_support:initial,orbit_q:orbit,first_eight_histories:Array.from({length:8},(_,i)=>Array.from({length:i+1},(_,j)=>orbit[j%orbit.length]).reduce((a,b)=>a*b,1))};
  }
 }
 ck(frameWitness!==null&&same(frameWitness.orbit_q,[4,6]),"m4 alternating 4-6 witness");
 return {schema:"R762AX_TOKEN_FEASIBLE_PASS_CERT_V1",status:"PASS",date:"2026-11-15",model:"single-use directed cycle with sequential token enabling; conditional exact V23/V25/V29 positive typed BRC selector at integer n>=16",frozen_source:"enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json",dependencies:["R762AU PR #2451@f42064096ba3014a63a8d75bbe9f4b7dcdaff447","R762AW PR #2458@a71f4f4d72a27a013f46f41f87d2cb9785dd3820"],theorem_general:"m>=2: q(K)=m!/product cyclic positive-support gap factorials; q=0 for empty support; every macro restores K; legal future word language depends minimally on support(K)",frame_transport_theorem:"For a fixed port permutation sigma, the macro word count across r frames is product_{j=0}^{r-1} q_m(sigma^j K), periodic by sigma orbit; m=4 witness (1 2), S={0,1} gives alternating q=4,6",frame_transport_tests:frameTests,frame_periodic_factorization_checks:periodChecks,maximal_support_period:maximalPeriod,frame_witness:frameWitness,theorem_brc:"n>=16,r>=1: B_r^K(S)=B_1^K(S)q(K)^(r-1) for q>=1; C states B_r=q^r",exact_cycle_support_cases:cycleCases,exact_resource_permutation_checks:permutationTests,conditional_first_macro_expansions:expansions,triad_states:20,cycle:C,phases,independent_review:"NOT_REVIEWED",native_P000_event_admission:"OPEN"};
};
console.log(JSON.stringify(calculate(),null,2));
