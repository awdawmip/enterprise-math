const R692_RESULT = (function R692Exact() {
  "use strict";
  const T={"0,0":"012","1,0":"013","2,0":"014","0,1":"023","1,1":"123","2,1":"013"};
  const signs={"--":[-1,-1],"-+":[-1,1],"+-":[1,-1],"++":[1,1]};
  const expected={
    0:{"--":{"012":6,"021":9},"-+":{"012":6,"021":6,"120":3},"+-":{"012":6,"021":3,"201":6},"++":{"012":6,"120":3,"201":6}},
    1:{"--":{"012":6,"120":6,"201":3},"-+":{"012":9,"120":6},"+-":{"012":12,"201":3},"++":{"012":15}},
    2:{"--":{"012":15},"-+":{"012":12,"021":3},"+-":{"012":9,"021":6},"++":{"012":6,"021":9}}
  };
  function assert(x,msg){if(!x)throw Error(msg);}
  function phase(z){return String(((z[0]+z[2]+z[4])%3+3)%3)+","+String(((z[1]+z[3]+z[5])%2+2)%2);}
  function square(a,b,i,j,si,sj){
    let z=[a,b,0,0,0,0],root=T[phase(z)],frame=root.split("");
    for(let [axis,dir] of [[i,si],[j,sj],[i,-si],[j,-sj]]){
      let old=T[phase(z)];z[axis]+=dir;let fresh=T[phase(z)];
      let exiting=[...old].filter(c=>!fresh.includes(c));
      let entering=[...fresh].filter(c=>!old.includes(c));
      assert(exiting.length===1&&entering.length===1,"triad transition");
      let pos=frame.indexOf(exiting[0]);assert(pos>=0&&!frame.includes(entering[0]),"frame update");
      frame[pos]=entering[0];
    }
    assert(z[0]===a&&z[1]===b&&z.slice(2).every(x=>x===0),"cell return");
    return frame.map(x=>String(root.indexOf(x))).join("");
  }
  function mul(g,p){return [...p].map(i=>g[Number(i)]).join("");}
  function powerCounts(count,K=6){
    let v={"012":1},p=[1];
    for(let k=1;k<=K;k++){
      let w={};
      for(let [state,mass] of Object.entries(v))
        for(let [g,n] of Object.entries(count)){
          let q=mul(g,state);
          w[q]=(w[q]||0)+mass*n;
        }
      assert(Object.values(w).reduce((s,t)=>s+t,0)===15**k,"mass check");
      p.push(w["012"]||0);v=w;
    }
    return p;
  }
  const cases=[],profiles=[],sig={};
  let checked=0;
  for(let a=0;a<3;a++)for(let b=0;b<2;b++)
  for(let [sigma,[si,sj]] of Object.entries(signs)){
    let cnt={};
    for(let i=0;i<6;i++)for(let j=i+1;j<6;j++){
      let g=square(a,b,i,j,si,sj);cnt[g]=(cnt[g]||0)+1;checked++;
    }
    assert(JSON.stringify(Object.entries(cnt).sort())===JSON.stringify(Object.entries(expected[a][sigma]).sort()),"R691 kernel mismatch");
    if(b===0){
      let p=powerCounts(cnt);
      cases.push({root_phase_a:a,sigma,group_counts:cnt,return_numerators_k0_k6:p});
      sig[a+":"+sigma]=p;
    }
  }
  assert(checked===360,"path count");
  for(let a=0;a<3;a++){
    let h=1;
    for(;h<=6;h++){
      let s=new Set(Object.keys(signs).map(sigma=>{
        let p=sig[a+":"+sigma];
        return Array.from({length:h},(_,j)=>p[j+1]*15**(h-j-1)).join(",");
      }));
      if(s.size===4)break;
    }
    assert(h===([3,1,1][a]),"minimal distinguishing horizon");
    profiles.push({root_phase_a:a,least_horizon_for_four_distinct_return_signatures:h});
  }
  assert(["--","-+","+-","++"].map(s=>sig["0:"+s][2]).join(",")==="117,72,45,72","k2 certificate");
  assert(["--","-+","+-","++"].map(s=>sig["0:"+s][3]).join(",")==="1674,891,594,1107","k3 certificate");
  return {status:"ALL_EXACT_ASSERTIONS_PASS",run:"2026-11-10",frozen_task_source:"a72226e2430ffa4786321ac86e7f0c599d5f0389",
  model:"R691 E* X6 native labeled four-step square, direction sigma repeated each macro, 15 equally weighted unordered axis pairs",
  observer:"return to input S3 frame after k macros", raw_four_step_paths:checked,
  numerical_semantics:"exact safe integers: k<=6 and all counts <=15^6",
  cases,profiles,limits:"Author E* model; no unverified Link/Port, V29 or V39 interpretation"};
})();

if (typeof console !== 'undefined') console.log(JSON.stringify(R692_RESULT,null,2));
