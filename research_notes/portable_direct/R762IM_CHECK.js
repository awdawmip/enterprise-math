function R762IM_check() {
  "use strict";
  const choose = (items,k) => {
    const ans=[], q=[];
    function visit(start,need) {
      if (!need) {ans.push(q.slice());return;}
      for(let i=start;i<=items.length-need;i++){q.push(items[i]);visit(i+1,need-1);q.pop();}
    }
    visit(0,k);return ans;
  };
  const ids=Array.from({length:20},(_,i)=>i);
  const axes=[0,1,2,3,4,5];
  const ports=choose(axes,2), supports=choose(axes,3);
  const portId=new Map(ports.map((p,i)=>[p.join(","),i]));
  const supId=new Map(supports.map((s,i)=>[s.join(","),i]));
  const triangles=supports.map(s=>choose(s,2).map(p=>portId.get(p.join(","))));
  const edges=triangles.map(t=>choose(t,2));
  const edgeKey=(a,b)=>a<b?a+","+b:b+","+a;
  const edgeOwner=new Map();
  edges.forEach((ee,s)=>ee.forEach(([a,b])=>edgeOwner.set(edgeKey(a,b),s)));
  if(edgeOwner.size!==60)throw Error("source type error: 60 Port edges required");
  const permAxes=[];
  const makePerm=(arr,left)=>{
    if(!left.length){permAxes.push(arr);return;}
    left.forEach((v,i)=>makePerm([...arr,v],[...left.slice(0,i),...left.slice(i+1)]));
  };
  makePerm([],axes);
  const perms=permAxes.map(a=>({
    ps:ports.map(pair=>portId.get(pair.map(i=>a[i]).sort((x,y)=>x-y).join(","))),
    ss:supports.map(tri=>supId.get(tri.map(i=>a[i]).sort((x,y)=>x-y).join(",")))
  }));
  const code=triple=>triple.map(a=>a.join(".")).join("|");
  const hist=([odd,even,missing])=>{
    const h=Array(20).fill(3);
    odd.forEach(s=>h[s]=1);even.forEach(s=>h[s]=2);missing.forEach(s=>h[s]=0);
    return h;
  };
  const pass=(original,w,omit=-1)=>{
    if(!w || w.length!==52)return false;
    const h=Array(20).fill(0),degree=Array(15).fill(0),adj=Array(15).fill(0);
    for(const [s,a,b] of w){
      if(s<0||s>=20||!edges[s].some(e=>e[0]===Math.min(a,b)&&e[1]===Math.max(a,b)))return false;
      h[s]++;degree[a]++;degree[b]++;adj[a]|=1<<b;adj[b]|=1<<a;
    }
    for(let i=0;i<20;i++) {
      if(h[i]>original[i] || (h[i]===0)!==(original[i]===0) || (original[i]-h[i])%2)return false;
    }
    let active=0;
    for(let i=0;i<15;i++){if(degree[i]%2)return false;if(degree[i])active|=1<<i;}
    const target=omit<0?32767:32767^(1<<omit);
    if(active!==target)return false;
    let seen=1<<Math.floor(Math.log2(active & -active)), prev=-1;
    while(seen!==prev){
      prev=seen;
      for(let i=0;i<15;i++)if(seen&(1<<i))seen|=adj[i];
    }
    return seen===active;
  };
  const findWitness=(triple,omit=-1)=>{
    const [odd,even,missing]=triple,n=hist(triple);
    const full=ids.filter(s=>n[s]===3);
    const shorten=(n.reduce((a,b)=>a+b,0)-52)/2;
    if(!Number.isInteger(shorten)||shorten<1)return null;
    const selectedChoices=choose(full,shorten);
    for(const selected of selectedChoices){
      const selectedSet=new Set(selected),allowed=new Set(full.filter(s=>!selectedSet.has(s)));
      const defects=[...odd,...selected];
      const choices=defects.map(s=>edges[s].filter(e=>omit<0||!e.includes(omit)));
      if(choices.some(x=>!x.length))continue;
      const chosen=[];
      function tryChosen(i){
        if(i<defects.length){
          for(const e of choices[i]){chosen.push(e);const result=tryChosen(i+1);chosen.pop();if(result)return result;}
          return null;
        }
        const routeOptions=chosen.map(([a,b])=>{
          const opts=[];
          for(let v=0;v<15;v++){
            if(v===a||v===b||v===omit)continue;
            const sa=edgeOwner.get(edgeKey(a,v)),sb=edgeOwner.get(edgeKey(v,b));
            if(allowed.has(sa)&&allowed.has(sb))opts.push([[sa,a,v],[sb,v,b]]);
          }
          return opts;
        });
        if(routeOptions.some(x=>!x.length))return null;
        const changed=Array(20).fill(0);
        function tryRoute(j){
          if(j<defects.length){
            for(const route of routeOptions[j]){
              for(const [s,a,b] of route)changed[s]^=(1<<a)^(1<<b);
              const ans=tryRoute(j+1);
              for(const [s,a,b] of route)changed[s]^=(1<<a)^(1<<b);
              if(ans)return ans;
            }
            return null;
          }
          const w=[];
          for(const s of allowed){
            if(!changed[s]){
              for(const e of edges[s])w.push([s,...e]);
            }else{
              const matching=edges[s].find(([a,b])=>((1<<a)^(1<<b))===changed[s]);
              if(!matching)return null;
              const other=edges[s].find(e=>e!==matching && (omit<0||!e.includes(omit)));
              if(!other)return null;
              w.push([s,...matching],[s,...other],[s,...other]);
            }
          }
          for(const s of even) {
            const e=edges[s].find(e=>omit<0||!e.includes(omit));
            if(!e)return null;
            w.push([s,...e],[s,...e]);
          }
          for(let z=0;z<defects.length;z++)w.push([defects[z],...chosen[z]]);
          return pass(n,w,omit)?w:null;
        }
        return tryRoute(0);
      }
      const answer=tryChosen(0);
      if(answer)return answer;
    }
    return null;
  };
  const families=[
    ["T20",0,0,0],["E2",0,2,0],["U1",1,0,0],
    ["E4",0,4,0],["U1E2",1,2,0],["U2",2,0,0],["M1E1",0,1,1],
    ["E6",0,6,0],["U1E4",1,4,0],["U2E2",2,2,0],
    ["U3",3,0,0],["M1E3",0,3,1],["M1U1E1",1,1,1],["M2",0,0,2]
  ];
  const familyCases=(u,e,m)=>{
    const res=[];
    for(const odd of choose(ids,u)){
      const setO=new Set(odd), remaining1=ids.filter(s=>!setO.has(s));
      for(const even of choose(remaining1,e)){
        const setE=new Set(even),remaining2=remaining1.filter(s=>!setE.has(s));
        for(const missing of choose(remaining2,m))res.push([odd,even,missing]);
      }
    }
    return res;
  };
  const results=[],sample={}, total={histograms:0,orbits:0,omitted_port_cases:0,omitted_port_failures:0,full_port_failures:0};
  for(const [name,u,e,m] of families){
    const cases=familyCases(u,e,m);
    const pending=new Map(cases.map(t=>[code(t),t]));
    let orbits=0,covered=0;
    while(pending.size){
      const representative=pending.values().next().value;
      const witness=findWitness(representative);
      if(!witness)throw Error("missing representative witness "+name+" "+code(representative));
      if(name==="T20")sample.T20={
        initial_histogram:hist(representative),
        witness_edge_triples:witness
      };
      orbits++;
      for(const perm of perms){
        const image=representative.map(a=>a.map(i=>perm.ss[i]).sort((x,y)=>x-y));
        const key=code(image);
        if(!pending.has(key))continue;
        const mapped=witness.map(([s,a,b])=>[perm.ss[s],perm.ps[a],perm.ps[b]]);
        if(!pass(hist(image),mapped))throw Error("orbit lift invalid "+name+" "+key);
        covered++;pending.delete(key);
      }
    }
    if(covered!==cases.length)throw Error("orbit cover incomplete "+name);
    let omitted=0;
    for(const triple of cases){
      const n=hist(triple);
      for(let p=0;p<15;p++){
        const incident=ids.filter(s=>triangles[s].includes(p));
        if(incident.every(s=>n[s]<3)){
          const w=findWitness(triple,p);
          if(!pass(n,w,p))throw Error("omitted-Port witness invalid "+name+" "+code(triple)+" "+p);
          omitted++;
        }
      }
    }
    results.push({family:name,deficit:2*u+e+3*m,histograms:cases.length,orbits,omitted_port_cases:omitted});
    total.histograms+=cases.length;total.orbits+=orbits;total.omitted_port_cases+=omitted;
  }
  if(total.histograms!==181946||total.orbits!==435||total.omitted_port_cases!==3165)throw Error("unexpected census totals "+JSON.stringify(total));
  return {schema:"R762IM_EXACT_K0_EVEN_TAIL_V1",status:"PASS",model:"15 pair-Ports, 20 triple-supports, every named event chooses an edge of its Port triangle",observer:"Euler existence with same support presence/parity and exact active Port set; any active Port may start",frozen_input:"a72226e2430ffa4786321ac86e7f0c599d5f0389",target_events:52,verification:"Every even 54..60 event support histogram checked through complete S6 orbits; every possible 14-Port omission checked individually; each constructed witness independently checks count, parity, degree, connectivity, active Port set",total,results,sample};
}

if (typeof console !== 'undefined') console.log(JSON.stringify(R762IM_check(), null, 2));
