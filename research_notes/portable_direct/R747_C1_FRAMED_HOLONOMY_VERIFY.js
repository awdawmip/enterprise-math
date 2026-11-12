'use strict';
const verify=function verify(){
  const ok=(p,m)=>{if(!p)throw new Error(m||"FAILED")};
  const perms=a=>a.length===0?[[]]:a.flatMap((x,i)=>perms(a.filter((_,j)=>j!==i)).map(p=>[x,...p]));
  const S3=perms([0,1,2]),S6=perms([0,1,2,3,4,5]);
  const port=(a,s)=>String(a)+(s>0?"+":"-");
  const ax=p=>+p[0], sg=p=>p[1]==="+"?1:-1;
  const rot=f=>[f[1],f[2],f[0]];
  const orient=f=>[f.join(","),rot(f).join(","),rot(rot(f)).join(",")].sort()[0];
  const permFrame=(f,sigma)=>f.map(p=>port(sigma[ax(p)],sg(p)));
  const replace=(f,a,b,s)=>{const i=f.findIndex(p=>ax(p)===a);ok(i>=0&&f.every(p=>ax(p)!==b));const r=f.slice();r[i]=port(b,s);return r};
  const triple=[];for(let a=0;a<6;a++)for(let b=a+1;b<6;b++)for(let c=b+1;c<6;c++)triple.push([a,b,c]);
  const frames=[];
  for(const t of triple)for(let bits=0;bits<8;bits++)for(const p of S3)frames.push(p.map(i=>port(t[i],(bits&(1<<i))?1:-1)));
  ok(frames.length===960&&new Set(frames.map(f=>f.join())).size===960);
  const orbit={};for(const f of frames){const k=f.map(sg).join();orbit[k]=(orbit[k]||0)+1}
  ok(Object.keys(orbit).length===8&&Object.values(orbit).every(x=>x===120));
  ok(new Set(S6.map(s=>permFrame(frames[0],s).join())).size===120);
  let q=0,succ=0;
  for(const f of frames)for(const p of f)for(let b=0;b<6;b++)if(!f.some(x=>ax(x)===b))for(const sign of [-1,1]){
    const g=replace(f,ax(p),b,sign);
    for(let j=0,h=f;j<3;j++,h=rot(h)){ok(orient(replace(h,ax(p),b,sign))===orient(g));q++}
    for(let j=0,h=g;j<3;j++,h=rot(h)){for(let i=0;i<3;i++)ok(h[(h.indexOf(g[i])+1)%3]===g[(i+1)%3]);succ++}
  }
  ok(q===51840&&succ===51840);
  const graphs={
    A:{I:["012","014","013","012"],P:["012","023","013","012"],Q:["012","023","123","012"]},
    B:{I:["012","123","124","012"],P:["012","023","013","012"],Q:["012","123","013","012"]}
  };
  const expected={A:{I:"012",P:"021",Q:"102"},B:{I:"012",P:"021",Q:"210"}};
  const axes=x=>x.split("").map(Number);
  function hop(f,u,v,signs){
    const a=axes(u),b=axes(v),rm=a.filter(x=>!b.includes(x)),ins=b.filter(x=>!a.includes(x));
    ok(rm.length===1&&ins.length===1);
    return replace(f,rm[0],ins[0],signs[ins[0]]);
  }
  function loop(c,l,f,signs){const path=graphs[c][l];for(let i=0;i<3;i++)f=hop(f,path[i],path[i+1],signs);return f}
  const positive=Array(6).fill(1),counts={},three={},even={};
  let wordsChecked=0;
  for(const c of ["A","B"]){
    for(const a of "IPQ")ok(loop(c,a,["0+","1+","2+"],positive).map(ax).join("")===expected[c][a]);
    let words=[{w:"",f:["0+","1+","2+"]}],counter={};
    for(let k=0;k<=8;k++){
      const seen=new Set();
      for(const {w,f} of words){
        seen.add(f.join());
        let f2=["0+","1+","2+"];for(const a of w)f2=loop(c,a,f2,positive);
        ok(f2.join()===f.join());wordsChecked++;
        if(k===3&&["III","IIP","IIQ","IPQ","IQP","PQP"].includes(w))three[c+"_"+w]={frame:f.map(ax).join(""),orientation:orient(f),anchor:ax(f[0])};
      }
      counter[k]=seen.size;
      if(k<8)words=words.flatMap(({w,f})=>[...("IPQ")].map(a=>({w:w+a,f:loop(c,a,f,positive)})));
    }
    ok(JSON.stringify(Object.values(counter))===JSON.stringify([1,3,5,6,6,6,6,6,6]));counts[c]=counter;
    const example={};for(const w of ["PPQQ","PQPQ","QPQP"]){let f=["0+","1+","2+"];for(const a of w)f=loop(c,a,f,positive);example[w]=f}
    ok(new Set(Object.values(example).map(orient)).size===1);
    ok(new Set(Object.values(example).map(f=>f[0])).size===3);
    even[c]=Object.fromEntries(Object.entries(example).map(([w,f])=>[w,f.map(ax).join("")]));
  }
  ok(wordsChecked===19682);
  let covariance=0;
  for(const c of ["A","B"]){
    const edges=new Set();
    for(const path of Object.values(graphs[c]))for(let i=0;i<3;i++)edges.add(path[i]+":"+path[i+1]);
    ok(edges.size===7);
    for(const edge of edges){
      const [u,v]=edge.split(":"),a=axes(u),b=axes(v);
      for(let bits=0;bits<32;bits++){
        const signs=Array.from({length:6},(_,j)=>(bits&(1<<j))?1:-1);
        for(const p of S3){
          const f=p.map(i=>port(a[i],signs[a[i]])),g=hop(f,u,v,signs);
          for(const sigma of S6){
            const aa=a.map(x=>sigma[x]),bb=b.map(x=>sigma[x]);
            const rm=aa.find(x=>!bb.includes(x)),ins=bb.find(x=>!aa.includes(x));
            const h=replace(permFrame(f,sigma),rm,ins,signs[sigma.indexOf(ins)]);
            ok(h.join()===permFrame(g,sigma).join());covariance++;
          }
        }
      }
    }
  }
  ok(covariance===1935360);
  return {schema:"R747_C1_FRAME_CONNECTION_CHECK_V1",status:"PASS",source:"AUTHOR_SIDE_EXACT_CHECK",scope:"SIGNED_C1_CANDIDATE_OVERLAP_EDGE_LIFT_AND_ROOTED_BRC_LOOP_GRAMMAR",signed_source_states:160,oriented_C1_states:320,framed_states:960,sign_pattern_orbits:8,orbit_sizes:orbit,one_orbit_stabilizer_order:6,quotient_lift_tests:q,successor_cyclic_invariance_tests:succ,covariance_checks:covariance,rooted_word_checks:wordsChecked,distinct_end_frames_by_length:counts,generator_monodromies:expected,all_six_fixed_length_three_witnesses:three,orientation_only_counterexample_even_paths:even,native_event_permission:"NOT_TESTED",formal_source_claim:"NOT_ASSERTED",exactness:"INTEGER_PERMUTATION_AND_FINITE_EXHAUSTIVE_ENUMERATION"}
};
process.stdout.write(JSON.stringify(verify(),null,2)+'\n');
