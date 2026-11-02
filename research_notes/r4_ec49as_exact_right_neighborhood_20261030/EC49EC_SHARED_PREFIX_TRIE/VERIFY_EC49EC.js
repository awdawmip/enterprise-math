// EC49EC exact signed native-X6 computation. Run: node VERIFY_EC49EC.js
const verifyEC49EC = function verifyEC49EC() {
 const OPS={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3]};
 const ST=[["N",0],["N",1],["N",2],["A",0],["A",2],["B",0],["B",1],["AB",0],["BA",0]],B=["N","A","B","AB","BA"],P=1000003;
 const HIST=[
 [2,-2,2,-1,1,-1,-1,1,-1,-2],
 [-1,-1,2,-1,1,-1,2,-2,-2,1],
 [-2,-1,1,-1,1,-1,2,-1,-2,2],
 [-1,-1,1,-1,2,-1,1,2,-2,-2],
 [1,-1,-1,-1,-2,2,-2,-1,1,2],
 [1,-1,-1,-1,-2,-1,2,1,-2,2],
 [-2,-2,2,1,-1,-1,-1,2,-1,1],
 [-2,2,-1,-1,-1,-1,-2,1,2,1],
 [-1,-1,-1,-1,-2,2,1,-2,1,2]];
 const must=(v,m)=>{if(!v)throw Error(m)};
 const steps=w=>[...w].flatMap(c=>OPS[c]);
 const disp=t=>Array.from({length:6},(_,i)=>t.reduce((s,v)=>s+(v===i+1)-(v===-i-1),0));
 const pc=t=>Array.from({length:6},(_,i)=>t.filter(v=>v===i+1).length);
 const obs=(st,t)=>{let [s,last]=st;for(const v of t){const e=last===1&&v===2?"A":last===2&&v===1?"B":null;
   if(e){if(s==="N")s=e;else if(s==="A"&&e==="B")s="AB";else if(s==="B"&&e==="A")s="BA"}last=v;}return s;};
 const atom=t=>{const s=obs(["N",0],t),v=t[t.length-1];return [s,s==="N"?(v===1||v===2?v:0):s==="A"&&v===2?2:s==="B"&&v===1?1:0]};
 const z9=([s,v])=>[+(s==="N"),+(s==="A"),+(s==="B"),+(s==="AB"),+(s==="BA"),+(s==="A"&&v===2),+(s==="B"&&v===1),+(s==="N"&&v===1),+(s==="N"&&v===2)];
 const mod=v=>(v%P+P)%P;
 const inv=a=>{let x=1,n=P-2;while(n){if(n%2)x=x*a%P;a=a*a%P;n=Math.floor(n/2)}return x};
 const rank=vs=>{const piv=new Map();for(const v0 of vs){let v=v0.slice();for(;;){const k=v.findIndex(x=>mod(x)!==0);if(k<0)break;
   const base=piv.get(k);if(!base){const q=inv(mod(v[k]));piv.set(k,v.map(x=>mod(x*q)));break}
   const q=v[k];v=v.map((x,j)=>mod(x-q*base[j]));}}return piv.size};
 const det=m0=>{const m=m0.map(row=>row.map(BigInt)),n=m.length;let d=1n,sgn=1n;
  for(let k=0;k<n-1;k++){if(m[k][k]===0n){let r=k+1;while(r<n&&m[r][k]===0n)r++;
    if(r===n)return 0n;[m[k],m[r]]=[m[r],m[k]];sgn=-sgn}
    const q=m[k][k];for(let i=k+1;i<n;i++){for(let j=k+1;j<n;j++){
      const t=q*m[i][j]-m[i][k]*m[k][j];must(t%d===0n,"Bareiss divisibility");m[i][j]=t/d}m[i][k]=0n}d=q}
  return sgn*m[n-1][n-1]};
 const cols=w=>B.map(b=>ST.map(st=>+(obs(st,steps(w))===b)));
 const allcols=ws=>ws.flatMap(cols);
 const sig=w=>cols(w).flat().join(",");
 const prefixes=w=>steps(w).map((_,i,t)=>t.slice(0,i+1).join(","));
 const triecost=ws=>new Set(ws.flatMap(prefixes)).size;
 const trie=ws=>{const paths=[...new Set(ws.flatMap(prefixes))].map(k=>k.split(",").map(Number))
   .sort((a,b)=>a.length-b.length||a.join(",").localeCompare(b.join(",")));
   const ix=new Map(paths.map((v,i)=>[v.join(","),i+1]));
   return paths.map((v,i)=>[i+1,ix.get(v.slice(0,-1).join(","))||0,v[v.length-1],v.length])};
 const witness=ws=>{const out=[],labs=[];for(const w of ws){for(let j=0;j<5;j++){const v=cols(w)[j];
   if(rank(out.concat([v]))>out.length){out.push(v);labs.push(w+":"+B[j])}if(out.length===9)break}if(out.length===9)break}
   must(out.length===9,"nine-column witness absent");const d=det(ST.map((_,i)=>out.map(v=>v[i])));must(d!==0n,"zero determinant");
   return {columns:labs,det:d.toString()}};
 const weight=(t,w)=>pc(t).reduce((s,p,i)=>s*BigInt(w[i])**BigInt(p),1n);
 const words=h=>{const out=[];const grow=s=>{if(s.length===h){if(disp(steps(s)).join(",")==="2,0,0,0,0,0")out.push(s);return}
   for(const c of "abcde")grow(s+c)};grow("");return out};
 must(det(ST.map(z9))===-1n,"history basis");
 for(let i=0;i<9;i++){const t=HIST[i];
   must(t.length===10&&disp(t).join(",")==="-2,0,0,0,0,0","history displacement");
   must(pc(t).join(",")==="2,2,0,0,0,0","history positive count");
   must(JSON.stringify(atom(t))===JSON.stringify(ST[i]),"history atom")};
 const solve=h=>{
  const ws=words(h),map=new Map();
  for(const w of ws){const s=sig(w);if(!map.has(s))map.set(s,[]);map.get(s).push(w)}
  const groups=[...map.values()].map(a=>a.sort()).sort((a,b)=>a[0].localeCompare(b[0]));
  const minimal=[];
  for(let mask=1;mask<(1<<groups.length);mask++){
    const ids=groups.map((_,i)=>i).filter(i=>mask&(1<<i));
    if(rank(allcols(ids.map(i=>groups[i][0])))!==9)continue;
    if(ids.some(i=>rank(allcols(ids.filter(j=>j!==i).map(j=>groups[j][0])))===9))continue;
    minimal.push(ids);
  }
  minimal.sort((a,b)=>a.length-b.length||a.join(",").localeCompare(b.join(",")));
  function optimize(equal){
   let best=Infinity,bestws=null,bestfiber=null,ties=0,total=0;const cases=[];
   for(const ids of minimal){
     const domains=ids.map(i=>groups[i]),families=[];
     if(!equal)families.push([null,domains]);
     else for(const fiber of [...new Set(domains[0].map(w=>pc(steps(w)).join(",")))].sort()){
       const sub=domains.map(g=>g.filter(w=>pc(steps(w)).join(",")===fiber));
       if(sub.every(g=>g.length))families.push([fiber,sub]);
     }
     for(const [fiber,domain] of families){
       let trials=0,low=Infinity;
       function search(i,chosen){
         if(i===domain.length){
           const c=triecost(chosen);trials++;total++;if(c<low)low=c;
           if(c<best){best=c;bestws=chosen.slice();bestfiber=fiber;ties=0}
           if(c===best){ties++;if(chosen.join(",")<bestws.join(",")){bestws=chosen.slice();bestfiber=fiber}}
           return;
         }
         for(const w of domain[i])search(i+1,chosen.concat([w]));
       }search(0,[]);
       cases.push({signature_ids:ids,fiber:fiber?fiber.split(",").map(Number):null,tuples:trials,minimum:low});
     }
   }
   must(Number.isFinite(best),"no full-rank subset");
   const T=trie(bestws),V=witness(bestws);
   must(T.length===best&&rank(allcols(bestws))===9,"invalid winner");
   for(const w of bestws){const t=steps(w);
     must(disp(t).join(",")==="2,0,0,0,0,0","future return");
     for(const hist of HIST){
       must(obs(atom(hist),t)===obs(["N",0],hist.concat(t)),"history seam");
       for(const weights of [[2,3,5,7,11,13],[17,19,23,29,31,37]])
         must(weight(hist.concat(t),weights)===weight(hist,weights)*weight(t,weights),"BRC factorization");
     }
   }
   return {optimum:best,optimal_representatives:ties,witness_words:bestws,
     future_positive_counts:bestws.map(w=>pc(steps(w))),
     independent_primitive_cost:bestws.reduce((s,w)=>s+steps(w).length,0),
     nine_columns:V.columns,determinant:V.det,
     native_primitive_trie_nodes_id_parent_signedAxis_depth:T,
     representative_tuples_evaluated:total,case_minima:cases};
  }
  return {h,returning_words:ws,signature_classes:groups,
    inclusion_minimal_fullrank_signature_sets:minimal,unrestricted:optimize(false),equal_counts:optimize(true)};
 };
 const cases=[2,3,4].map(solve);
 must(cases.map(z=>z.returning_words.length).join(",")==="4,15,56","returning inventory");
 must(cases.map(z=>z.unrestricted.optimum).join(",")==="28,34,46","unrestricted minima");
 must(cases.map(z=>z.equal_counts.optimum).join(",")==="28,44,46","same-count minima");
 must(cases.map(z=>z.inclusion_minimal_fullrank_signature_sets.map(a=>a.join(",")).sort().join("|")).join(";")==="0,1,2,3;0,1,4|1,4,5,8;0,1,2,4","minimal signature classification");
 return {schema:"EC49EC_EXACT_NATIVE_X6_TRIE_V1",status:"PASS",
   primitive_operators:OPS,observer_atoms:ST,actual_nine_length10_histories:HIST,
   historical_z9_determinant:"-1",
   rank_method:"0/1 Q-rank via mod 1000003; each subdeterminant has abs bound <= 9^(9/2) < prime; exact signed integer Bareiss witnesses",
   objective:"Unique signed native X6 primitive prefix edges; preserve full word and terminal-bucket provenance, both positive BRC instruments and count",
   cases};
};
const result = verifyEC49EC();
console.log(JSON.stringify(result,null,2));
