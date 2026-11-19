"use strict";
// Exact finite-state, source/Port-labelled Boolean-BRC verifier for conditional X6 R21.
// No external libraries, no floating-point arithmetic, no physical-law assumption.
const run=function run(){
  "use strict";
  function assignments(m,n){const result=[];function grow(a){if(a.length===n){result.push(a.slice());return;}for(let x=0;x<m;x++)if(!a.includes(x)){a.push(x);grow(a);a.pop();}}grow([]);return result;}
  function automaton(m,n,cap,edges){
    const poses=assignments(m,n);
    const states=[], lookup=new Map();
    for(const p of poses)for(let r=0;r<=cap;r++){const s={p,r};lookup.set(p.join(",")+":"+r,states.length);states.push(s);}
    const alphabet=[];
    for(let a=0;a<n;a++)for(const d of [-1,1])alphabet.push({a,d,name:String.fromCharCode(65+a)+(d>0?"+":"-")});
    const trans=states.map(s=>alphabet.map(({a,d})=>{
      const u=s.p[a],v=u+d; const e=edges.find(x=>x.u===u&&x.v===v);
      if(!e||v<0||v>=m||s.p.includes(v)||s.r<e.cost)return -1;
      const p=s.p.slice();p[a]=v;
      return lookup.get(p.join(",")+":"+Math.min(cap,s.r-e.cost+e.grant));
    }));
    return {states,alphabet,trans,lookup};
  }
  function refine(T,old){
    const seen=new Map();return T.map(row=>{
      const key=row.map(t=>t<0?"x":old[t]).join("/");
      if(!seen.has(key))seen.set(key,seen.size);return seen.get(key);
    });
  }
  function samePart(A,B){
    for(let i=0;i<A.length;i++)for(let j=0;j<i;j++)
      if((A[i]===A[j])!==(B[i]===B[j]))return false;
    return true;
  }
  function bruteNext(T,alphabet,prev){
    return T.map(row=>{
      const out=new Set([""]);
      for(let a=0;a<row.length;a++)if(row[a]>=0)for(const suf of prev[row[a]])out.add(alphabet[a].name+"|"+suf);
      return out;
    });
  }
  function sameSet(a,b){if(a.size!==b.size)return false;for(const x of a)if(!b.has(x))return false;return true;}
  const edgeCells=[[0,1],[1,0],[1,2],[2,1]];
  const options=[null,{cost:0,grant:0},{cost:1,grant:0},{cost:0,grant:1},{cost:1,grant:1}];
  let configurations=0,stateOccurrences=0,languagePairChecks=0,stabilizationChecks=0,highestFirstSplit=0,nontrivialEquivalent=0;
  const partitionExamples=[];
  for(let cap=1;cap<=2;cap++)for(let n=1;n<=2;n++)for(let code=0;code<625;code++){
    let c=code, edges=[];
    for(let k=0;k<4;k++){const opt=options[c%5];c=Math.floor(c/5);if(opt)edges.push({u:edgeCells[k][0],v:edgeCells[k][1],...opt});}
    const A=automaton(3,n,cap,edges),N=A.states.length;
    configurations++;stateOccurrences+=N;
    let part=Array(N).fill(0),brute=Array.from({length:N},()=>new Set([""]));
    for(let h=1;h<=N;h++){
      const next=refine(A.trans,part);
      if(h<=4){
        const nextBrute=bruteNext(A.trans,A.alphabet,brute);
        for(let i=0;i<N;i++)for(let j=0;j<i;j++){
          const eq=sameSet(nextBrute[i],nextBrute[j]);
          if(eq!==(next[i]===next[j]))throw Error("BRC mismatch "+[cap,n,code,h,i,j,eq,next[i]===next[j]]);
          languagePairChecks++;
        }
        brute=nextBrute;
      }
      if(!samePart(next,part)){
        if(h>highestFirstSplit)highestFirstSplit=h;
      }else{
        if(h>1&&h<=4&&new Set(next).size<N)nontrivialEquivalent++;
        part=next;
        break;
      }
      part=next;
      if(h===N)throw Error("not stabilized by N steps "+[cap,n,code,N]);
    }
    stabilizationChecks++;
    if(code===312&&n===2&&cap===1)partitionExamples.push({cap,n,code,classes:new Set(part).size,states:N});
  }
  const recharge=automaton(3,2,1,[{u:1,v:2,cost:0,grant:1},{u:0,v:1,cost:1,grant:0}]);
  const start=recharge.lookup.get("0,1:0");
  const aBplus=recharge.alphabet.findIndex(x=>x.name==="B+");
  const aAplus=recharge.alphabet.findIndex(x=>x.name==="A+");
  const mid=recharge.trans[start][aBplus];
  if(mid<0||recharge.states[mid].r!==1)throw Error("recharge step not verified");
  const end=recharge.trans[mid][aAplus];
  if(end<0||recharge.states[end].r!==0||recharge.states[end].p.join(",")!=="1,2")throw Error("recharge witness failed");
  if(recharge.trans[start][aAplus]!==-1)throw Error("unrecharged move should be blocked");
  const alias=automaton(2,1,2,[{u:0,v:1,cost:1,grant:0}]);
  let part=Array(alias.states.length).fill(0);
  for(let i=1;i<=alias.states.length;i++){const next=refine(alias.trans,part);if(samePart(next,part)){part=next;break;}part=next;}
  const id0=alias.lookup.get("0:0"), id1=alias.lookup.get("0:1"),id2=alias.lookup.get("0:2");
  if(part[id1]!==part[id2]||part[id0]===part[id1])throw Error("resource quotient witness failed");
  const chain=automaton(6,1,0,Array.from({length:5},(_,u)=>({u,v:u+1,cost:0,grant:0})));
  const p0=chain.lookup.get("0:0"),p1=chain.lookup.get("1:0");
  let cp=Array(chain.states.length).fill(0),first=null;
  for(let h=1;h<chain.states.length;h++){cp=refine(chain.trans,cp);if(cp[p0]!==cp[p1]){first=h;break;}}
  if(first!==5)throw Error("sharp horizon witness failed: "+first);
  return {schema:"X6_BRC_R21_EXACT_VERIFICATION_V1",status:"PASS",date:"2026-11-19",exhaustive_scope:{base_chart:"3 selected X6 positions on one signed primitive axis, other 5 relative coordinates 0",directed_edges:edgeCells.length,edge_options_per_edge:options.length,credit_caps:[1,2],source_counts:[1,2],all_patterns_per_cap_and_source:625,configurations,stateOccurrences},tests:{boolean_language_pair_equivalence_checks:languagePairChecks,stabilization_checks:stabilizationChecks,maximum_refinement_round_observed:highestFirstSplit,nontrivial_early_fixed_points:nontrivialEquivalent},witnesses:{replenishment:{initial_positions:[0,1],initial_credit:0,credit_cap:1,successful_word:["B+","A+"],initial_R20_resource_feasible_path:false,first_A_move_event:2,initial_A_plus_illegal:true},resource_alias:{positions:[0],credit_levels_merged:[1,2],credit_level_distinguished:0},sharpness:{line_sites:6,starting_sites:[0,1],first_language_difference_at:5,N:6}},example:partitionExamples};
};
const result=run();
console.log(JSON.stringify(result,null,2));
