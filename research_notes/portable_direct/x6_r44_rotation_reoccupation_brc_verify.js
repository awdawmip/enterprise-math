/* X6 R44 reproducible exact positive-labelled-path BRC verifier; Node.js. */
const runR44 = function runR44(){
  const ensure=(condition,message)=>{if(!condition)throw new Error(message)};
  const cases=[];
  for(let p=1;p<=8;p++){
    const labels=["R","T"];
    for(let i=0;i<p;i++)labels.push("A"+i,"B"+i);
    const key=s=>s.join(",");
    function next(s,e){
      const [a,b,o,t]=s;
      if(e==="R")return o===0?null:[a,b,0,t];
      if(e==="T"){
        if(t!==0||o!==0||((a<0)===(b<0)))return null;
        const port=a>=0?a:b;
        return [a,b,port===0?(a>=0?1:2):0,1];
      }
      const side=e[0],i=Number(e.slice(1));
      if(side==="A"){
        if(a>=0||(i===0&&o!==0))return null;
        return [i,b,i===0?1:o,t];
      }
      if(b>=0||(i===0&&o!==0))return null;
      return [a,i,i===0?2:o,t];
    }
    const start=[-1,-1,0,0],states=[start],ids=new Map([[key(start),0]]),arcs=[];
    for(let j=0;j<states.length;j++){
      const edges={};
      for(const e of labels){
        const dest=next(states[j],e);
        if(dest===null)continue;
        const k=key(dest);
        if(!ids.has(k)){ids.set(k,states.length);states.push(dest);}
        edges[e]=ids.get(k);
      }
      arcs.push(edges);
    }
    let frontier=[{id:0,word:[]}],counts=[],withoutT=[],words=[];
    for(let h=0;h<10&&frontier.length;h++){
      counts.push(frontier.length);
      withoutT.push(frontier.filter(x=>!x.word.includes("T")).length);
      for(const x of frontier)words.push(x.word.join(" "));
      const nextFrontier=[];
      for(const x of frontier)for(const [e,to]of Object.entries(arcs[x.id])){
        nextFrontier.push({id:to,word:x.word.concat(e)});
      }
      frontier=nextFrontier;
    }
    ensure(frontier.length===0,"finite history p="+p);
    const expected=[1,2*p,2*p*p+2*(p-1),2*p*p+4*p-2,4*p,4*p-2,2];
    ensure(JSON.stringify(counts)===JSON.stringify(expected),"prefix counts p="+p+" actual="+counts);
    ensure(words.length===4*p*p+16*p-3&&new Set(words).size===words.length,"total or duplicate p="+p);
    ensure(states.length===2*p*p+8*p+5,"state count p="+p);
    ensure(states.filter(s=>s[3]===0).length===(p+1)*(p+3),"R43 state embedding p="+p);
    const baseline=[1,2*p,2*p*p,6*p-4,2];
    ensure(JSON.stringify(withoutT.slice(0,5))===JSON.stringify(baseline),"R43 word embedding p="+p);
    ensure(withoutT.slice(5).every(x=>x===0),"R43 word upper bound");
    let part=states.map(()=>0),blocks=[];
    for(let pass=0;pass<10;pass++){
      const sig=states.map((_,j)=>Object.keys(arcs[j]).sort().map(e=>e+":"+part[arcs[j][e]]).join(";"));
      const unique=[...new Set(sig)].sort(),map=new Map(unique.map((s,i)=>[s,i]));
      const np=sig.map(s=>map.get(s));
      blocks.push(unique.length);
      if(unique.length===new Set(part).size){part=np;break;}
      part=np;
    }
    const masks=new Set(arcs.map(e=>Object.keys(e).sort().join(",")));
    const expectClasses=p===1?11:13,expectMasks=p===1?7:9;
    ensure(new Set(part).size===expectClasses,"quotient p="+p);
    ensure(masks.size===expectMasks,"enabled masks p="+p);
    const memo=new Map();
    function suffix(j){
      if(memo.has(j))return memo.get(j);
      const set=new Set([""]);
      memo.set(j,set);
      for(const [e,to]of Object.entries(arcs[j]))for(const w of suffix(to)){
        set.add(e+(w?" "+w:""));
      }
      return set;
    }
    const languages=states.map((_,j)=>[...suffix(j)].sort().join("|"));
    ensure(new Set(languages).size===expectClasses,"full language quotient p="+p);
    for(let i=0;i<states.length;i++)for(let j=0;j<states.length;j++){
      ensure((part[i]===part[j])===(languages[i]===languages[j]),"partition vs complete future words p="+p);
    }
    if(p>=2){
      const left=ids.get("0,-1,0,0"),right=ids.get("1,-1,0,0");
      ensure(left!==undefined&&right!==undefined,"witness states");
      const enabled=j=>Object.keys(arcs[j]).sort().join(",");
      ensure(enabled(left)===enabled(right),"same one-step mask");
      const step=(id,seq)=>seq.reduce((q,e)=>q===null?null:(arcs[q][e]===undefined?null:arcs[q][e]),id);
      ensure(step(left,["T"])!==null&&step(right,["T"])!==null,"both allow T");
      ensure(step(left,["T","B0"])===null&&step(right,["T","B0"])!==null,"T B0 distinguishes p="+p);
    }
    cases.push({ports:p,reachable_states:states.length,successful_prefix_counts:counts,total_serial_BRC_words:words.length,one_step_enabled_masks:masks.size,complete_future_language_classes:new Set(part).size,refinement_class_counts:blocks,ordered_state_pairs_checked:states.length**2,original_R43_no_rotation_prefix_counts:baseline,pass:true});
  }
  return {schema:"X6_R44_ROTATION_REOCCUPATION_BRC_EXACT_V1",status:"PASS",scientific_scope:"conditional one-shot whole-triad Port transfers, public clearing R, and once-only provenance-sensitive candidate rotation T; positive named-word BRC",p_range:[1,8],assertions:"exact closed counts; R43 sublanguage; exhaustive successful suffix words; independent future-language partition; 3-Port same-mask witness T B0",closed_forms:{reachable_states:"2p^2+8p+5",BRC_serial_words_total:"4p^2+16p-3",prefix_counts:["1","2p","2p^2+2(p-1)","2p^2+4p-2","4p","4p-2","2"],complete_future_language_classes:"11 for p=1, 13 for p>=2",enabled_masks:"7 for p=1, 9 for p>=2"},cases};
};
const result = runR44();
process.stdout.write(JSON.stringify(result, null, 2) + '\n');
