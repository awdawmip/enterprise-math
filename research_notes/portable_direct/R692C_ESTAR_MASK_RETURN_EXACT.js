const R692_MASK_RESULT = (function R692MaskExact(){
  "use strict";
  const n={
    0:[{"012":6,"021":9},{"012":6,"021":6,"120":3},{"012":6,"021":3,"201":6},{"012":6,"120":3,"201":6}],
    1:[{"012":6,"120":6,"201":3},{"012":9,"120":6},{"012":12,"201":3},{"012":15}],
    2:[{"012":15},{"012":12,"021":3},{"012":9,"021":6},{"012":6,"021":9}]
  };
  function assert(ok,msg){if(!ok)throw Error(msg);}
  function mul(g,p){return [...p].map(i=>g[+i]).join("");}
  function gcd(x,y){while(y){[x,y]=[y,x%y]}return x;}
  function reduce(x,y){let d=gcd(x,y);return x/d+"/"+y/d;}
  const cases=[],classifications=[];
  for(let a=0;a<3;a++){
    let signatures=[];
    for(let mask=1;mask<16;mask++){
      let count={},pop=0;
      for(let j=0;j<4;j++)if(mask&(1<<j)){
        pop++;
        for(let [g,w] of Object.entries(n[a][j]))count[g]=(count[g]||0)+w;
      }
      let D=15*pop;
      assert(Object.values(count).reduce((u,v)=>u+v,0)===D,"kernel mass");
      let v={"012":1},p=["1/1"];
      for(let k=1;k<=6;k++){
        let w={};
        for(let [s,u] of Object.entries(v))for(let [g,mass] of Object.entries(count)){
          let dest=mul(g,s);w[dest]=(w[dest]||0)+u*mass;
        }
        assert(Object.values(w).reduce((u,x)=>u+x,0)===D**k,"convolution mass");
        v=w;
        p.push(reduce(v["012"]||0,D**k));
      }
      cases.push({root_phase_a:a,allowed_direction_mask:mask,denominator_per_macro:D,group_counts:count,return_probabilities_k0_to_k6:p});
      signatures.push({mask,sequence:p.slice(1)});
    }
    let map=new Map();
    for(let s of signatures){
      const key=s.sequence.join("|");
      if(!map.has(key))map.set(key,[]);
      map.get(key).push(s.mask);
    }
    let expected=(a===2?9:12);
    assert(map.size===expected,"future class count");
    let horizons=[];
    for(let h=1;h<=6;h++){
      horizons.push(new Set(signatures.map(s=>s.sequence.slice(0,h).join("|"))).size);
    }
    assert(horizons.join(",")===[[1,11,12,12,12,12],[9,12,12,12,12,12],[9,9,9,9,9,9]][a].join(","),"horizon counts");
    let multiples=[...map.values()].filter(x=>x.length>1).sort((x,y)=>x[0]-y[0]);
    let expectMult=[[[2,5],[6,9,15]],[[4,10],[6,9,15]],[[2,5,7],[4,10,14],[6,9,15]]][a];
    assert(JSON.stringify(multiples)===JSON.stringify(expectMult),"class mask membership");
    classifications.push({root_phase_a:a,return_observer_future_equivalence_classes:[...map.values()].sort((x,y)=>x[0]-y[0]),
      non_singleton_classes:multiples,class_count:map.size,distinct_class_counts_by_horizon_k1_to_k6:horizons,
      least_complete_horizon:horizons.indexOf(map.size)+1});
  }
  const a0m2=cases.find(x=>x.root_phase_a===0&&x.allowed_direction_mask===2);
  const a0m5=cases.find(x=>x.root_phase_a===0&&x.allowed_direction_mask===5);
  assert(JSON.stringify(a0m2.group_counts)!==JSON.stringify(a0m5.group_counts),"full group distributions distinct");
  assert(JSON.stringify(a0m2.return_probabilities_k0_to_k6)===JSON.stringify(a0m5.return_probabilities_k0_to_k6),"return traces same");
  return {status:"ALL_EXACT_ASSERTIONS_PASS",model:"frozen R691 E* X6 group kernels, persistent nonempty allowed-direction subset M with equal mass for 15*|M| labeled square paths",numeric_semantics:"integers exact; max denominator^6 = 60^6 < 2^53",enumerated_mask_models:45,cases,classifications,
    explicit_full_group_lossy_pair:"a=0, masks 2 and 5: distributions differ by conjugation by tau (c vs c^2), but all return probabilities coincide",limits:"author E* candidate; not native V29/Link/Port permitted-mask dynamics"};
})();
if(typeof console!=='undefined')console.log(JSON.stringify(R692_MASK_RESULT,null,2));
