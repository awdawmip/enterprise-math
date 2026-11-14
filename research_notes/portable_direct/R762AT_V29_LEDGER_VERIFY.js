"use strict"; // R762AT: exact V29/V27 cumulative-ledger, positive Weighted-BRC audit; Node.js >=18; no dependencies.

const MATCHINGS=[[[0,1],[2,3],[4,5]],[[0,2],[1,4],[3,5]],[[0,3],[1,5],[2,4]],[[0,4],[1,3],[2,5]]], OMEGA=[[0,1,-1,0],[-1,0,1,0],[1,-1,0,0],[0,0,0,0]], U=[-2,-4,-3,10];

const TRIADS=[];for(let a=0;a<6;a++)for(let b=a+1;b<6;b++)for(let c=b+1;c<6;c++)TRIADS.push(`${a}${b}${c}`);

function code(s){return MATCHINGS.map(m=>{const bits=[];for(const [a,b] of m){let x=s.includes(String(a)),y=s.includes(String(b));if(x===y)return 0;bits.push(y?1:0)}return bits.reduce((x,y)=>x+y,0)%2===0?1:-1})}

function neighbor(s,t){return [...s].filter(x=>t.includes(x)).length===2}

function part(s,t){const a=code(s),b=code(t);let B=0,A=0;for(let i=0;i<4;i++){B+=U[i]*b[i];for(let j=0;j<4;j++)A+=a[i]*OMEGA[i][j]*b[j]}return [B,A]}

function score(s,t,n){const [b,a]=part(s,t);return b+n*a}

function ranking(n){let f={},ties={},margins={};for(const s of TRIADS){const opts=TRIADS.filter(t=>neighbor(s,t));let best=Math.max(...opts.map(t=>score(s,t,n)));let winners=opts.filter(t=>score(s,t,n)===best);let sorted=opts.map(t=>score(s,t,n)).sort((a,b)=>b-a);f[s]=winners[0];ties[s]=winners;margins[s]=sorted[0]-sorted[1]}return {f,ties,margins}}

function cycles(f){const seen=new Set(),out=[];for(const s of TRIADS){if(seen.has(s))continue;let path=[],at={},v=s;while(!(v in at)&&!seen.has(v)){at[v]=path.length;path.push(v);v=f[v]}if(v in at)out.push(path.slice(at[v]));for(const u of path)seen.add(u)}return out}

function holonomy(cyc){const base=cyc[0],slot={};for(let i=0;i<3;i++)slot[base[i]]=i;for(let i=0;i<cyc.length;i++){const s=cyc[i],t=cyc[(i+1)%cyc.length];const common=[...s].filter(x=>t.includes(x));const left=[...s].find(x=>!common.includes(x));const enter=[...t].find(x=>!common.includes(x));const prev={...slot};for(const k of Object.keys(slot))delete slot[k];for(const k of common)slot[k]=prev[k];slot[enter]=prev[left]}const p=[...base].map(x=>slot[x]);let inv=0;for(let i=0;i<3;i++)for(let j=i+1;j<3;j++)inv+=Number(p[i]>p[j]);return {permutation:p,parity:inv%2}}

function assert(x,msg){if(!x)throw Error(msg)}

function weight(p){return p>=0?[2n**BigInt(p),1n]:[1n,2n**BigInt(-p)]}

function compareW(a,b){return a[0]*b[1]>b[0]*a[1]?1:a[0]*b[1]<b[0]*a[1]?-1:0}

function audit(){
 assert(TRIADS.length===20,'triad count');
 assert(new Set(TRIADS.map(s=>code(s).join(','))).size===20,'V23 injection');
 const rows=[1,1,1,0],cols=[1,1,1,0],oldI=[0,0,0,10],oldO=[2,4,3,0],rin=[0,0,0,10],rout=[2,4,3,0];
 assert([0,1,2].every(i=>oldI[i]<rows[i]),'V27 snapshot violation');
 const fixI=rows.map((v,i)=>v+rin[i]),fixO=cols.map((v,i)=>v+rout[i]);
 assert(fixI.every((v,i)=>v>=rows[i])&&fixO.every((v,i)=>v>=cols[i]),'PF10 correction');
 assert(fixI.every((v,i)=>v-fixO[i]===U[i]),'u preserved');
 const d1=ranking(1),d15=ranking(15),d14=ranking(14);
 assert(Object.values(d1.ties).every(x=>x.length===1),'V27 uniqueness');
 const expectedOdd=['012','123','234','034','035','025'],expectedFlat=['145','245'];
 const cs1=cycles(d1.f), cs15=cycles(d15.f);
 assert(cs1.length===2&&cs1.some(c=>JSON.stringify(c)===JSON.stringify(expectedOdd))&&cs1.some(c=>JSON.stringify(c)===JSON.stringify(expectedFlat)),'V27 graph');
 assert(cs15.length===1&&JSON.stringify(cs15[0])===JSON.stringify(expectedOdd),'stable graph');
 assert(JSON.stringify(holonomy(cs15[0]))===JSON.stringify({permutation:[2,1,0],parity:1}),'V17 holonomy');
 assert(d14.ties['014'].length===2&&d14.ties['014'].join(',')==='013,145','sharp n14');
 const slopes={0:0,1:0,2:0};let minMargin=Infinity,comparisons=0;
 for(const s of TRIADS){const w=d15.f[s];for(const t of TRIADS.filter(t=>neighbor(s,t)&&t!==w)){const [bw,aw]=part(s,w),[bt,at]=part(s,t),ds=aw-at,m=(bw-bt)+15*ds;assert(ds>=0&&m>=1,'eventual unique dominance');slopes[ds]=(slopes[ds]||0)+1;minMargin=Math.min(minMargin,m);comparisons++}}
 assert(comparisons===160&&slopes[0]===52&&slopes[1]===54&&slopes[2]===54&&minMargin===1,'comparison certificate');
 for(const n of [16,17,18,21,50,100,1000]){const f=ranking(n).f;assert(TRIADS.every(s=>f[s]===d15.f[s]),'future map')}
 let maxDepth=0,depthWitness=[];
 for(const s of TRIADS){let v=s,k=0;while(!expectedOdd.includes(v)){assert(k<20,'nonrecurrent');v=d15.f[v];k++}if(k>maxDepth){maxDepth=k;depthWitness=[s]}else if(k===maxDepth)depthWitness.push(s)}
 assert(maxDepth===3&&depthWitness.includes('145'),'depth');
 let weightChecks=0;
 for(let n=0;n<=15;n++)for(const s of TRIADS){const adj=TRIADS.filter(t=>neighbor(s,t));for(let i=0;i<adj.length;i++)for(let j=i+1;j<adj.length;j++){let a=score(s,adj[i],n),b=score(s,adj[j],n);assert(compareW(weight(a),weight(b))===Math.sign(a-b),'BRC weight order');weightChecks++}}
 const tieCensus={};for(let n=0;n<=15;n++){let rr=ranking(n);tieCensus[n]=Object.fromEntries(Object.entries(rr.ties).filter(([s,w])=>w.length>1))}
 return {schema:"R762AT_V29_V27_LEDGER_BRC_EVIDENCE_V1",input:{V23_four_matchings:MATCHINGS,V27_U:U,unit_pass_cycle:["0->1","1->2","2->0"],V29_initial_Rin:rin,V29_initial_Rout:rout},correction:{V27_displayed_I:oldI,V27_displayed_O:oldO,row_M:rows,col_M:cols,corrected_I:fixI,corrected_O:fixO,original_fails_PF10_continuity:true},positive_BRC:{rho:2,exact_integer_exponent_order_checks:weightChecks},n_range_checked:"0..15, plus 16,17,18,21,50,100,1000",tie_census:tieCensus,affine_dominance_certificate:{n0:15,number_of_strict_neighbor_comparisons:comparisons,slopes_count:slopes,minimum_margin_at_15:minMargin,conclusion:"all n>=15 have same unique successor map"},eventual_successor_map:d15.f,eventual_cycles:cs15.map(c=>({states:c,holonomy:holonomy(c)})),max_steps_to_odd_cycle_from_any_triad:maxDepth,depth_witnesses:depthWitness,V27_at_n1_cycles:cs1.map(c=>({states:c,holonomy:holonomy(c)})),scope:"Conditional V23/V25/V27 four-field selector with actual V29 cumulative PASS updates and no native TRIADIC_CLOSURE_E admission; exact positive Weighted-BRC rho^Phi order"}
}

console.log(JSON.stringify(audit(),null,2));