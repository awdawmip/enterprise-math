/* X6 Unit258: exact finite conditional BRC guard experiment; run with Node.js */
function checker(){
  const initial=[0,2,0,0],goal="0,2,-12,12", ports=[[6,0],[8,2]];
  const key=s=>s.join(","), parse=k=>k.split(",").map(Number);
  const E4=[[2,0],[3,1],[4,2],[5,3]], E16=[...E4,[6,4],[7,5],[8,6],[12,6],[2,6],[3,7],[4,8],[5,9],[6,10],[7,11],[8,12],[12,12]];
  function next(s,i,j){
    const out=[];
    for(let t=0;t<2;t++){
      const x=s[t],other=s[1-t],m=x===12?[[j,0]]:[[(x+1)%12,1],[(x+11)%12,-1],...(x===i?[[12,0]]:[])];
      for(const [y,delta] of m){
        if(y===other)continue;
        const z=s.slice();z[t]=y;z[t+2]+=delta;out.push({t,x,y,z});
      }
    }
    return out;
  }
  function deny(s,mode){
    if(mode==="none")return false;
    if(mode==="initial")return key(s)==="0,2,0,0";
    const pairs=mode==="early4"?E4:E16;
    return s[0]===0&&s[2]===0&&pairs.some(([p,w])=>p===s[1]&&w===s[3]);
  }
  function countByLayers(i,j,mode){
    let layer=new Map([[key(initial),1]]);
    for(let depth=1;depth<=31;depth++){
      const nxt=new Map();
      for(const [k,n] of layer)for(const e of next(parse(k),i,j)){
        if(e.t===0&&e.x===0&&e.y===11&&deny(parse(k),mode))continue;
        const q=key(e.z);nxt.set(q,(nxt.get(q)||0)+n);
      }
      if(nxt.has(goal))return [depth,nxt.get(goal)];
      layer=nxt;
    }
    return [null,0];
  }
  function countByBFS(i,j,mode){
    const q=[initial],seen=new Map([[key(initial),0]]),ways=new Map([[key(initial),1]]);
    for(let h=0;h<q.length;h++){
      const s=q[h],k=key(s),d=seen.get(k);
      if(k===goal)break;
      if(d>=31)continue;
      for(const e of next(s,i,j)){
        if(e.t===0&&e.x===0&&e.y===11&&deny(s,mode))continue;
        const v=key(e.z);
        if(!seen.has(v)){seen.set(v,d+1);ways.set(v,ways.get(k));q.push(e.z);}
        else if(seen.get(v)===d+1)ways.set(v,ways.get(v)+ways.get(k));
      }
    }
    return [seen.get(goal)??null,ways.get(goal)||0];
  }
  function cover(i,j){
    const q=[initial],dist=new Map([[key(initial),0]]);
    for(let h=0;h<q.length;h++){
      const s=q[h],d=dist.get(key(s));if(d>=28)continue;
      for(const e of next(s,i,j))if(!dist.has(key(e.z))){dist.set(key(e.z),d+1);q.push(e.z);}
    }
    const viable=new Map([[goal,1]]);
    for(const [k,d] of [...dist].sort((a,b)=>b[1]-a[1])){
      if(k===goal||d>=28)continue;
      viable.set(k,next(parse(k),i,j).reduce((a,e)=>a+(dist.get(key(e.z))===d+1?(viable.get(key(e.z))||0):0),0));
    }
    const paths=[];
    function walk(s,C){
      const k=key(s),d=dist.get(k);
      if(k===goal){paths.push(C);return;}
      for(const e of next(s,i,j)){
        if(dist.get(key(e.z))!==d+1||!(viable.get(key(e.z))||0))continue;
        const added=e.t===0&&e.x===0&&e.y===11?[[d+1,...s]]:[];
        walk(e.z,C.concat(added));
      }
    }
    walk(initial,[]);
    const cn=new Map();
    for(const p of paths)for(const c of p){const k=key(c);cn.set(k,(cn.get(k)||0)+1);}
    const keys=[...cn.keys()].sort((a,b)=>parse(a)[0]-parse(b)[0]),masks=paths.map(p=>p.reduce((a,c)=>a|(1<<keys.indexOf(key(c))),0));
    let best=Infinity,opt=[];
    if(keys.length<=10){
      for(let mask=0;mask<1<<keys.length;mask++){
        const bits=mask.toString(2).replace(/0/g,"").length;
        if(bits>best)continue;
        if(!masks.every(x=>(x&mask)!==0))continue;
        if(bits<best){best=bits;opt=[];}
        opt.push(mask);
      }
    }else{
      if(!paths.every(p=>p.length===1))throw Error("unit258 singleton count failed");
      best=keys.length;opt=[(1<<keys.length)-1];
    }
    return {shortest_histories:paths.length,shortest_dag_states:dist.size,distinct_contexts:keys.length,context_occurrences:keys.map(k=>({prestate:parse(k),histories:cn.get(k)})),minimal_blocking_contexts:best,number_minimal_context_covers:opt.length,unique_cover:keys.filter((_,h)=>(opt[0]&(1<<h))!==0).map(parse)};
  }
  const cases={};
  for(const mode of ["none","initial","early4","early16"]){
    cases[mode]=ports.map(([i,j])=>{
      const a=countByLayers(i,j,mode),b=countByBFS(i,j,mode);
      if(a[0]!==b[0]||a[1]!==b[1])throw Error("independent DP/BFS mismatch");
      return {port:[i,j],minimum_events:a[0],number_optimal_histories:a[1]};
    });
  }
  const expected={none:[[28,2832],[28,2832]],initial:[[28,632],[28,2200]],early4:[[30,10712],[28,928]],early16:[[30,9212],[30,1036]]};
  for(const mode of Object.keys(expected))for(let j=0;j<2;j++){
    const z=cases[mode][j],e=expected[mode][j];
    if(z.minimum_events!==e[0]||z.number_optimal_histories!==e[1])throw Error("case certificate failure");
  }
  const c60=cover(6,0),c82=cover(8,2);
  if(c60.shortest_histories!==2832||c82.shortest_histories!==2832||c60.distinct_contexts!==10||c82.distinct_contexts!==16||c60.minimal_blocking_contexts!==4||c82.minimal_blocking_contexts!==16||c60.number_minimal_context_covers!==1||c82.number_minimal_context_covers!==1)throw Error("context cover mismatch");
  return {schema:"X6_TIME_UNIT258_CONTEXTUAL_GUARD_FALLBACK_V1",task_id:"RS-X6-NATIVE-TIME-DYNAMICS",frozen_input_commit:"a72226e2430ffa4786321ac86e7f0c599d5f0389",original_witness_commit:"f56840285cafeb9f5767ea91e903e1f53808186f",parent_unit:"Unit257",model:"CONDITIONAL_SIGNED_WHOLE_TRIAD_BRC",context_definition:"[1_based_event_index,pos_A,pos_B,winding_A,winding_B]; P=12",guard_definitions:{none:"none",initial:"reject A 0->11 only at prestate (0,2,0,0)",early4:"reject A 0->11 iff pos_A=0,w_A=0,(pos_B,w_B) in [(2,0),(3,1),(4,2),(5,3)]",early16:"same with all 16 early contexts listed in c82.unique_cover; block only if w_A=0"},cases,context_cover:{port60:c60,port82:c82},verification:"two exact independent counting algorithms (layer-by-layer DP and FIFO BFS); complete shortest-DAG history enumeration; exhaustive 1024 subsets for 10-context cover; singleton-path proof for 16-context cover",native_physical_execution:false,independent_review:false,admitted:false};
}
process.stdout.write(JSON.stringify(checker(),null,2)+'\n');
