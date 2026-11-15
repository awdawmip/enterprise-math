'use strict';
// R5 exact verification: Node.js, run node VERIFY_R5_CONGRUENCE_QUOTIENT.js
function verify(){
  const assert=(ok,m)=>{if(!ok)throw Error(m);};
  const pop=x=>{let n=0;while(x){x&=x-1;n++;}return n;};
  const set=(u,i,b)=>b?(u|(1<<i)):(u&~(1<<i));
  const cycle=k=>Array.from({length:k},(_,i)=>(1<<i)|(1<<((i+1)%k)));
  const q=(u,es,ws)=>es.reduce((a,e,i)=>a+(((u&e)===e)?ws[i]:0),0);
  const cost=(f,es,ws)=>es.reduce((a,e,i)=>a+((f&e)?ws[i]:0),0);
  const canon=p=>p.map(b=>b.slice().sort((a,b)=>a-b).join(',')).sort().join('|');
  let partitions=0,compatible=0;
  const stable=new Set();
  function traverse(i,blocks){
    if(i===8){
      partitions++;
      const good=blocks.every(B=>[0,1,2].every(j=>[0,1].every(b=>
        blocks.some(C=>B.every(u=>C.includes(set(u,j,b)))))));
      if(good){compatible++;stable.add(canon(blocks));}
      return;
    }
    for(const block of blocks){block.push(i);traverse(i+1,blocks);block.pop();}
    blocks.push([i]);traverse(i+1,blocks);blocks.pop();
  }
  traverse(0,[]);
  assert(partitions===4140,"Bell number");
  const projected=new Set();
  for(let f=0;f<8;f++){
    const cs={};
    for(let u=0;u<8;u++){const key=u&(7^f);(cs[key]??=[]).push(u);}
    projected.add(canon(Object.values(cs)));
  }
  assert(compatible===8 && stable.size===8 && [...stable].every(x=>projected.has(x)),"Congruence count");
  const cycleResults=[];
  for(let k=3;k<=8;k++){
    const es=cycle(k),ws=es.map(()=>1),limit=1<<k;
    for(let s=0;s<=k;s++){
      let best=-1,ex=null;
      for(let f=0;f<limit;f++){
        const c=cost(f,es,ws);
        let max=0;
        for(let outer=0;outer<limit;outer++){
          if(outer&f)continue;
          for(let v=f;;v=(v-1)&f){
            const dif=q(outer|f,es,ws)-q(outer|v,es,ws);
            if(dif>max)max=dif;
            if(!v)break;
          }
        }
        assert(max===c,"Wrong cycle cost k="+k+" F="+f);
        if(c<=s&&pop(f)>best){best=pop(f);ex=f;}
      }
      const expect=s<2?0:s<k?s-1:k;
      assert(best===expect,"Wrong cycle formula k="+k+" s="+s);
      cycleResults.push({k,slack:s,states:2**(k-best),forgotten_count:best,witness_mask:ex});
    }
  }
  let hyperWeightVectors=0,hyperFiberChecks=0;
  const es=Array.from({length:7},(_,i)=>i+1);
  for(let enc=0;enc<3**7;enc++){
    let rem=enc;const ws=[];
    for(let i=0;i<7;i++){ws.push(rem%3);rem=Math.floor(rem/3);}
    for(let f=0;f<8;f++){
      let max=0;
      for(let outer=0;outer<8;outer++){
        if(outer&f)continue;
        for(let v=f;;v=(v-1)&f){
          max=Math.max(max,q(outer|f,es,ws)-q(outer|v,es,ws));
          if(!v)break;
        }
      }
      assert(max===cost(f,es,ws),"Hyperedge cost fails");
      hyperFiberChecks++;
    }
    hyperWeightVectors++;
  }
  return {status:"PASS_R5_NAMED_SET_CONGRUENCE_AND_HYPEREDGE_COST",frozen_science_pin:"435e77af0d180eac32bd1f9c4c464bc4010b7551",coverage:{partitions_of_three_bit_cube:partitions,congruences_of_three_bit_cube:compatible,cycle_k_range:"3..8",cycle_k_slack_cases:cycleResults.length,hyperedge_weight_vectors:hyperWeightVectors,hyperedge_fiber_checks:hyperFiberChecks,arithmetic:"exact nonnegative integer operations"},cycle_results:cycleResults,math_claim:"Universal proofs are in the companion theorem note; finite verification is not theorem acceptance",independent_review:"NOT_REVIEWED"};
}
console.log(JSON.stringify(verify(), null, 2));
