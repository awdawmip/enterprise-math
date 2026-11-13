// R719q: finite-directed-permission certificate for cyclic non-backtracking X6/V17 holonomy.
// Integer-only Node.js 18+.
const verify=function verify(){
 const S="012",labels=["012","021","102","120","201","210"];
 const arcs=["012>013","012>023","012>123","012>124","013>014","013>123","014>012","014>024","023>024","023>123","024>012","024>014","123>124","123>234","124>012","124>014","124>024","234>024"];
 const E=arcs.map(x=>x.split(">")),A={};for(const [u,v] of E){if(!A[u])A[u]=[];A[u].push(v);if([...u].filter(c=>v.includes(c)).length!==2)throw Error("not Johnson adjacent "+u+">"+v)}
 const move=(frame,w)=>{const out=[...frame].find(c=>!w.includes(c)),inn=[...w].find(c=>!frame.includes(c));if(!out||!inn)throw Error("slot transfer");return frame.replace(out,inn)};
 const histogram=(h)=>Object.fromEntries(labels.map(k=>[k,String(h.get(k)||0n)]));
 for(const a of "012"){const x=[..."012"].filter(c=>c!==a).concat("3").sort().join("");const y=[..."012"].filter(c=>c!==a).concat("4").sort().join("");for(const [u,v] of [[S,x],[x,y],[y,S]])if(!arcs.includes(u+">"+v))throw Error("missing root repair triangle "+u+">"+v)}
 function dp(maxm){let d=new Map();for(const w of A[S])d.set([S,w,move(S,w),w].join("|"),1n);const res={};for(let m=2;m<=maxm;m++){const h=new Map(),next=new Map();for(const [id,num] of d){const [prev,v,frame,first]=id.split("|");for(const w of A[v]||[]){if(w===prev)continue;const f=move(frame,w);if(w===S&&v!==first)h.set(f,(h.get(f)||0n)+num);const nk=[v,w,f,first].join("|");next.set(nk,(next.get(nk)||0n)+num)}}res[m]=histogram(h);d=next}return res}
 function dfs(m){const h=new Map();function walk(prev,v,first,frame,d){if(d===m){if(v===S&&prev!==first)h.set(frame,(h.get(frame)||0n)+1n);return}for(const w of A[v]||[])if(w!==prev)walk(v,w,first??w,move(frame,w),d+1)}walk(null,S,null,S,0);return histogram(h)}
 const h=dp(17);
 for(let m=3;m<=7;m++)if(JSON.stringify(h[m])!==JSON.stringify(dfs(m)))throw Error("DP-vs-DFS m="+m);
 for(let m=4;m<=17;m++)if(labels.some(k=>BigInt(h[m][k])===0n))throw Error("missing holonomy m="+m);
 const expected={"4":{"012":"1","021":"2","102":"2","120":"1","201":"1","210":"2"},"5":{"012":"2","021":"1","102":"1","120":"2","201":"2","210":"1"},"6":{"012":"11","021":"2","102":"5","120":"2","201":"2","210":"5"}};
 for(const m of [4,5,6])for(const k of labels)if(h[m][k]!==expected[m][k])throw Error("sample mismatch m="+m+" k="+k);
 return {schema:"R719Q_DIRECTED_PORT_CERTIFICATE_V1",status:"R719Q_18_DIRECTED_ARCS_SIX_STATE_PASS",root:S,accessible_axes:"01234",full_johnson_directed_arcs:60,used_directed_arcs:arcs.length,arc_list:arcs,root_repair_triangles_verified:3,reference_counts:expected,dp_histograms:h,exhaustive_dfs_matches_dp_lengths:[3,4,5,6,7],verified_six_state_support_lengths:"4..17",unbounded_extension:"three-step root identity triangle proof"};
};
console.log(JSON.stringify(verify(),null,2));
