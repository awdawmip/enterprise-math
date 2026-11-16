// R762CQ — exact 203-partition source-matched candidate BRC census
// Requires a modern JavaScript runtime (node R762CQ_VERIFY.js); no dependencies.
// Static conditional candidate law only; NOT native TRIADIC_CLOSURE_E authorization.
// Edge order: 01,02,03,12,13,23. Source labels are equality classes, not signed native directions.
const EDGES=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
const ALL=[0,1,2,3,4,5];
function comb(n,k){let r=1;for(let j=1;j<=k;j++)r=r*(n-j+1)/j;return Math.round(r)}

function perms(a){if(a.length===0)return [[]];return a.flatMap((v,i)=>perms(a.filter((_,j)=>i!==j)).map(t=>[v,...t]))}

function rgs(n){let out=[];function go(a,m){if(a.length===n){out.push(a);return;}for(let x=0;x<=m+1;x++)go([...a,x],Math.max(m,x))}go([0],0);return out}

function canonical(A){let a=[...A].sort((x,y)=>x-y),b=ALL.filter(x=>!a.includes(x));return a.join(",")<b.join(",")?a:b}

function states(){let d=new Map();for(let a=0;a<6;a++)for(let b=a+1;b<6;b++)for(let c=b+1;c<6;c++){let s=canonical([a,b,c]);d.set(s.join(","),s)}return [...d.values()].sort((a,b)=>a.join(",").localeCompare(b.join(",")))}

function kinds(S){return S.map(A=>{let deg=[0,0,0,0];for(let i of A)for(let v of EDGES[i])deg[v]++;return deg.includes(0)||deg.includes(3)?"F":"P"})}

function matrix(p,S){let idx=new Map(S.map((s,i)=>[s.join(","),i]));let T=Array.from({length:10},()=>Array(10).fill(0));for(let i=0;i<10;i++){let a=S[i],b=ALL.filter(x=>!a.includes(x));for(let x of a)for(let y of b)if(p[x]===p[y]){let A=canonical([...a.filter(z=>z!==x),y]);T[i][idx.get(A.join(","))]++}}return T}

function makeBlocks(T,K){let d=new Map();for(let i=0;i<10;i++){let f=T[i].reduce((n,w,j)=>n+w*(K[j]==="F"),0),p=T[i].reduce((n,w,j)=>n+w*(K[j]==="P"),0);let key=`${K[i]}:${f}:${p}`;if(!d.has(key))d.set(key,[]);d.get(key).push(i)}return [...d.entries()].sort((a,b)=>a[0].localeCompare(b[0])).map(([key,indices])=>({key,indices}))}

function components(T){let unseen=new Set(ALL.concat([6,7,8,9])),out=[];while(unseen.size){let first=unseen.values().next().value;unseen.delete(first);let q=[first],g=[first];while(q.length){let i=q.pop();for(let j of [...unseen])if(T[i][j]){unseen.delete(j);q.push(j);g.push(j)}}out.push(g.sort((a,b)=>a-b))}return out.sort((a,b)=>a.length-b.length||a[0]-b[0])}

function examine(p,S,K){let T=matrix(p,S),blocks=makeBlocks(T,K),C=components(T);for(let i=0;i<10;i++)for(let j=0;j<10;j++)if(T[i][j]!==T[j][i]||T[i][j]>1||(i===j&&T[i][j]))throw Error("non-simple adjacency");
for(let b of blocks)for(let c of blocks){let target=c.indices;let sums=b.indices.map(i=>target.reduce((z,j)=>z+T[i][j],0));if(sums.some(v=>v!==sums[0]))throw Error("O1 not equitable for "+p.join("")+" "+b.key+"->"+c.key)}
let sizes=Array(Math.max(...p)+1).fill(0);for(let x of p)sizes[x]++;
let stats=[];for(let g of C){let k=Array(sizes.length).fill(0);for(let j of S[g[0]])k[p[j]]++;let symmetric=k.every((x,i)=>2*x===sizes[i]),v=k.reduce((n,x,i)=>n*comb(sizes[i],x),1)/(symmetric?2:1),d=k.reduce((n,x,i)=>n+x*(sizes[i]-x),0);if(v!==g.length||g.some(i=>T[i].reduce((a,b)=>a+b,0)!==d))throw Error("component mismatch "+p.join(""));stats.push({v,d})}
let byType={F:0,P:0};for(let b of blocks)byType[b.key[0]]++;let m=Math.max(byType.F,byType.P),bits=0;while(2**bits<m)bits++;return {T,blocks,components:stats,profile:[...sizes].sort((a,b)=>b-a).join("+"),K:blocks.length,bits,byType}}

function run(){
  const S=states(),K=kinds(S),parts=rgs(6),P4=perms([0,1,2,3]);
  if(S.length!==10||K.filter(x=>x==="F").length!==4||parts.length!==203||P4.length!==24)throw Error("coverage failed");
  let hK={},hBits={},byProfile={},cases=[],map=new Map();
  for(let p of parts){let z=examine(p,S,K),key=p.join("");map.set(key,z);hK[z.K]=(hK[z.K]??0)+1;hBits[z.bits]=(hBits[z.bits]??0)+1;if(!byProfile[z.profile])byProfile[z.profile]={total:0,histogram:{}};byProfile[z.profile].total++;byProfile[z.profile].histogram[z.K]=(byProfile[z.profile].histogram[z.K]??0)+1;
    cases.push({partition:key,profile:z.profile,classes:z.K,repair_bits:z.bits,blocks:z.blocks.map(b=>b.key+`[${b.indices.length}]`),components:z.components.map(c=>`${c.v}@${c.d}`)});
  }
  for(let perm of P4){let em=EDGES.map(e=>EDGES.findIndex(f=>f[0]===Math.min(perm[e[0]],perm[e[1]])&&f[1]===Math.max(perm[e[0]],perm[e[1]])));let si=S.map(a=>S.findIndex(s=>s.join(",")===canonical(a.map(x=>em[x])).join(",")));for(let p of parts){let q=Array(6);for(let i=0;i<6;i++)q[em[i]]=p[i];let T=map.get(p.join("")).T,U=matrix(q,S);for(let i=0;i<10;i++){if(K[i]!==K[si[i]])throw Error("kind covariance");for(let j=0;j<10;j++)if(T[i][j]!==U[si[i]][si[j]])throw Error("S4 covariance")}}}
  const norm=p=>{let c=new Map();return p.map(x=>{if(!c.has(x))c.set(x,c.size);return c.get(x)}).join("")};
  const coarse="001112",fine="012223";let pa=coarse.split("").map(Number),pb=fine.split("").map(Number);
  for(let i=0;i<6;i++)for(let j=0;j<6;j++)if(pb[i]===pb[j]&&pa[i]!==pa[j])throw Error("not a refinement");
  if(map.get(coarse).K!==7||map.get(fine).K!==4||map.get("000000").K!==2||map.get("000001").K!==3)throw Error("refinement witness");
  if(JSON.stringify(hK)!==JSON.stringify({"2":3,"3":30,"4":62,"5":36,"6":24,"7":48}))throw Error("hist classes unexpected "+JSON.stringify(hK));
  if(JSON.stringify(hBits)!==JSON.stringify({"0":3,"1":62,"2":114,"3":24}))throw Error("hist bits unexpected "+JSON.stringify(hBits));
  let binary=parts.filter(p=>Math.max(...p)<2);let h2={};for(let p of binary){let k=map.get(p.join("")).K;h2[k]=(h2[k]??0)+1}if(binary.length!==32||JSON.stringify(h2)!==JSON.stringify({"2":1,"3":13,"4":18}))throw Error("R762CP regression mismatch");
  return {schema:"R762CQ_EXACT_MULTICOLOR_PARTITION_BRC_V1",research_scope:"conditional equal-source cross-triad exchange on K4-labeled X6 six-axis carrier; not an authenticated native TRIADIC_CLOSURE_E event law",date:"2026-11-17",independent_review:"NOT_REVIEWED",edge_order:EDGES,states:S,observer:"O1=(F/P, T*1_F, T*1_P); equitable for all 203 partitions",partitions_checked:parts.length,source_relabelings_reduced_to_Bell6:true,S4_checks:parts.length*P4.length,transition_entry_checks:parts.length*P4.length*100,graph_component_check:"Johnson Cartesian product / complement antipodal quotient",all_one_step_quotients_equitable:true,distribution_by_classes:hK,distribution_by_optimal_repair_bits_known_FP:hBits,binary_regression:h2,by_profile:byProfile,nonmonotone_refinement:{coarse,coarse_classes:7,fine,fine_classes:4},cases};
}
const output=run();
console.log(JSON.stringify(output,null,2));
