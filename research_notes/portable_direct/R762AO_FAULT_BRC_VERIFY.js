/* R762AO complete finite verifier. Usage: node R762AO_FAULT_BRC_VERIFY.js */
const result = (function verify(){
 const A=(b,s)=>{if(!b)throw Error(s)};
 const E="012",C="120",T="102",U="!";
 const mul=(p,q)=>[...q].map(i=>p[+i]).join("");
 let fs=[E];for(let i=0;i<fs.length;i++)for(let g of [C,T]){const v=mul(g,fs[i]);if(!fs.includes(v))fs.push(v)}
 A(fs.length===6,"frame group");
 let ss=[[0,E],[1,E],[2,E],...fs.filter(v=>v!==E).map(h=>[0,h])].sort((a,b)=>JSON.stringify(a).localeCompare(JSON.stringify(b)));ss.push(U);
 let si=new Map(ss.map((s,i)=>[JSON.stringify(s),i]));
 function step(s,a){
  if(s===U)return U;let [n,h]=s;
  if(a==="S"&&h===E)return [(n+1)%3,h];
  if(a==="C"&&n===0)return [0,mul(C,h)];
  if(a==="T"&&n===0)return [0,mul(T,h)];
  return U
 }
 let obs=s=>s===U?"U":(s[0]?"C":"E")+(s[1]===E?"E":(s[1]===C||s[1]===mul(C,C)?"C":"T"));
 let os=ss.map(obs),pairs=[];for(let i=0;i<ss.length;i++)for(let j=i+1;j<ss.length;j++)if(os[i]===os[j])pairs.push([i,j]);
 A(pairs.length===5,"baseline pairs");
 let I=ss.map((_,i)=>i),Q=[I],ws=new Map([[I.join(","),""]]);
 let act=(f,a)=>f.map(i=>si.get(JSON.stringify(step(ss[i],a))));
 for(let i=0;i<Q.length;i++)for(let a of "SCT"){let f=act(Q[i],a),key=f.join(",");if(!ws.has(key)){ws.set(key,ws.get(Q[i].join(","))+a);Q.push(f)}}
 A(Q.length===75,"monoid");
 let vs=new Map();for(let f of Q){let w=ws.get(f.join(",")),v=f.map(i=>os[i]).join("|");if(!vs.has(v)||w.length<vs.get(v).length)vs.set(v,w)}
 A(vs.size===43,"vectors");
 let pm=new Map();
 const mask=out=>pairs.reduce((m,[i,j],k)=>m|(out[i]===out[j]?0:1<<k),0);
 for(let [v,w] of vs){let m=mask(v.split("|"));if(m&&(!pm.has(m)||w.length<pm.get(m).length))pm.set(m,w)}
 A(pm.size===5,"mask count");
 let repr={};for(let w of ["S","C","T","CT","TC"]){let f=I;for(let a of w)f=act(f,a);repr[w]=mask(f.map(i=>os[i]));A(pm.has(repr[w])&&pm.get(repr[w]).length===w.length,"representative "+w)}
 A(new Set(Object.values(repr)).size===5,"distinct masks");
 const dp=(d,metric)=>{
  let memo=new Map();
  function solve(v){
   if(v.every(x=>x===d))return 0;
   let k=v.join(",");if(memo.has(k))return memo.get(k);
   let opt=Infinity;
   for(let [m,w] of pm){let z=v.map((x,i)=>Math.min(d,x+((m>>i)&1)));if(z.every((x,i)=>x===v[i]))continue;opt=Math.min(opt,(metric==="N"?1:w.length)+solve(z))}
   memo.set(k,opt);return opt
  }
  let value=solve(Array(5).fill(0));return {value,states:memo.size}
 };
 let checks=[];for(let d=1;d<=7;d++){let n=dp(d,"N"),l=dp(d,"L");A(n.value===2*d+Math.ceil(3*d/2),"N "+d);A(l.value===Math.ceil(9*d/2),"L "+d);checks.push({d,minimum_probes:n.value,minimum_letters:l.value,dp_states_N:n.states,dp_states_L:l.states})}
 return {schema:"R762AO_EXACT_FAULT_BRC_V1",scope:"AK4 conditional eight live states and absorbing undefined, reliable initial observation, independent reset per terminal word, fixed nonadaptive probes",
 states:ss.length,baseline_equal_pairs:pairs,transformation_monoid:Q.length,terminal_vectors:vs.size,
 masks:[...pm].map(([m,w])=>({bits:m.toString(2).padStart(5,"0"),representative:w,length:w.length})),
 representative_masks:repr,theorem:"d=e+2t+1; Nmin(d)=2d+ceil(3d/2); Lmin(d)=ceil(9d/2)",
 checks,claims:"AUTHOR_PROVED_CONDITIONAL_NOT_REVIEWED_NOT_NATIVE_ADMITTED"}
})();
console.log(JSON.stringify(result,null,2));
