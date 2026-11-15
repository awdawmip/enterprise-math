"use strict";
const results=(function prefix802() {
  const assert=(x,msg)=>{if(!x)throw Error("ASSERT_FAIL "+msg);};
  const mon=(x,y)=>x+","+y;
  const weights=(b,c)=>{const A=[],B=[];for(let i=0;i<b;i++)for(let j=0;j<c;j++){A.push((i+2*j)%5-2);B.push((2*i-j+10)%5-2);}return [A,B];};
  function polyDP(K,b,c,row,col,W,mode="poly"){
    const E=b*c,R=row.slice(),S=col.slice(), memo=new Map();
    const stat={calls:0,hits:0,transitions:0,terms:0};
    function rec(k){
      stat.calls++;
      const key=k+"|"+R.join(",")+"|"+S.join(",");
      if(memo.has(key)){stat.hits++;return memo.get(key);}
      let ans;
      if(k===E){
        const good=R.every(x=>x===0)&&S.every(x=>x===0);
        ans=mode==="count"?(good?1n:0n):(good?new Map([[mon(0,0),1n]]):new Map());
      } else {
        const i=Math.floor(k/c),j=k%c,cap=Math.min(K[k],R[i],S[j]);
        ans=mode==="count"?0n:new Map();
        for(let t=0;t<=cap;t++){
          R[i]-=t;S[j]-=t;
          const child=rec(k+1);
          R[i]+=t;S[j]+=t;
          stat.transitions++;
          if(mode==="count")ans+=child;
          else{
            const dx=t*W[0][k],dy=t*W[1][k];
            for(const [exp,num] of child){
              const [x,y]=exp.split(",").map(Number),nk=mon(x+dx,y+dy);
              ans.set(nk,(ans.get(nk)||0n)+num);stat.terms++;
            }
          }
        }
      }
      memo.set(key,ans);return ans;
    }
    const value=rec(0);
    return {value,stat,states:memo.size};
  }
  function bruteFibers(K,b,c,W){
    const E=K.length, R=Array(b).fill(0),S=Array(c).fill(0),fibers=new Map();
    function rec(k,x,y){
      if(k===E){
        const id=R.join(",")+"|"+S.join(",");
        if(!fibers.has(id))fibers.set(id,{r:R.slice(),s:S.slice(),hist:new Map(),tables:0});
        const t=fibers.get(id),key=mon(x,y);
        t.hist.set(key,(t.hist.get(key)||0n)+1n);t.tables++;return;
      }
      const i=Math.floor(k/c),j=k%c;
      for(let t=0;t<=K[k];t++){
        R[i]+=t;S[j]+=t;
        rec(k+1,x+t*W[0][k],y+t*W[1][k]);
        R[i]-=t;S[j]-=t;
      }
    }
    rec(0,0,0);return fibers;
  }
  function samePoly(A,B){
    if(A.size!==B.size)return false;
    for(const [k,v] of A)if(B.get(k)!==v)return false;
    return true;
  }
  const coverage=[];
  let patterns=0,fibers=0,tables=0,polyTerms=0,dpStates=0,cacheHits=0,transitions=0;
  for(const [b,c,maxK] of [[2,2,2],[2,3,2],[3,3,1]]){
    const E=b*c,W=weights(b,c),K=Array(E).fill(0),stats={shape:b+"x"+c,max_capacity:maxK,patterns:0,fibers:0,tables:0,assertions:0};
    function patternsRec(k){
      if(k<E){for(let cap=0;cap<=maxK;cap++){K[k]=cap;patternsRec(k+1);}return;}
      stats.patterns++;patterns++;
      const groups=bruteFibers(K,b,c,W);
      for(const f of groups.values()){
        const d=polyDP(K,b,c,f.r,f.s,W);
        assert(samePoly(f.hist,d.value),"hist mismatch shape="+stats.shape+" K="+K+" margins="+f.r+"/"+f.s);
        let count=0n;for(const a of d.value.values())count+=a;
        assert(count===BigInt(f.tables),"count mismatch");
        stats.assertions+=2;stats.fibers++;fibers++;stats.tables+=f.tables;tables+=f.tables;
        polyTerms+=d.value.size;dpStates+=d.states;cacheHits+=d.stat.hits;transitions+=d.stat.transitions;
      }
    }
    patternsRec(0);coverage.push(stats);
  }
  assert(patterns===1322,"expected patterns 1322");
  assert(fibers===58421,"expected fibers 58421");
  assert(tables===67635,"expected tables 67635");
  const benchmark=[];
  for(const [b,c,k,v] of [[3,3,2,3],[4,4,1,2],[4,4,2,4],[5,5,1,2]]){
    const K=Array(b*c).fill(k),R=Array(b).fill(v),S=Array(c).fill(v),W=weights(b,c);
    const memo=polyDP(K,b,c,R,S,W,"count");
    let visits=0,found=0n;
    function direct(z){
      visits++;
      if(z===b*c){if(R.every(x=>x===0)&&S.every(x=>x===0))found++;return;}
      const i=Math.floor(z/c),j=z%c,lim=Math.min(k,R[i],S[j]);
      for(let t=0;t<=lim;t++){R[i]-=t;S[j]-=t;direct(z+1);R[i]+=t;S[j]+=t;}
    }
    direct(0);
    assert(found===memo.value,"large exact count");
    benchmark.push({shape:b+"x"+c,capacity:k,row_column_margin:v,named_tables:String(found),uncached_calls:visits,cached_unique_states:memo.states,cached_hits:memo.stat.hits,call_reduction:visits-memo.states});
  }
  // Two disjoint 2x2 blocks have a generating polynomial equal to the product of component polynomials.
  const K4=Array(16).fill(0);
  for(let i=0;i<4;i++)for(let j=0;j<4;j++)if(Math.floor(i/2)===Math.floor(j/2))K4[i*4+j]=1;
  const w4=weights(4,4),all=polyDP(K4,4,4,[1,1,1,1],[1,1,1,1],w4).value;
  function block(offset){
    let ka=[],wa=[[],[]];
    for(let i=0;i<2;i++)for(let j=0;j<2;j++){
      const idx=(i+offset)*4+j+offset;
      ka.push(K4[idx]);wa[0].push(w4[0][idx]);wa[1].push(w4[1][idx]);
    }
    return polyDP(ka,2,2,[1,1],[1,1],wa).value;
  }
  const p1=block(0),p2=block(2),product=new Map();
  for(const [ka,va] of p1)for(const [kb,vb] of p2){
    const [a,b]=ka.split(",").map(Number),[c,d]=kb.split(",").map(Number),k=mon(a+c,b+d);
    product.set(k,(product.get(k)||0n)+va*vb);
  }
  assert(samePoly(all,product),"block factorization");
  let total=0n;for(const v of all.values())total+=v;
  assert(total===4n,"component table count");
  // 2x2 with unit margins: unweighted count 2 but a named diagonal observation has values 0 and 1.
  const counter=polyDP([1,1,1,1],2,2,[1,1],[1,1],[[1,0,0,0],[0,0,0,0]]).value;
  assert(counter.size===2 && counter.get("0,0")===1n && counter.get("1,0")===1n,"prefix observer repair");
  const result={schema:"PREFIX802_EXACT_LAURENT_SUFFIX_DP_V1",source_science_pin:"f42f2906d77f24085c123f3ccfe9667d41caa96d",status:"ALL_CHECKS_PASS PREFIX802 LAURENT_SUFFIX_MEMO",
    coverage,totals:{capacity_patterns:patterns,margin_fibers:fibers,complete_named_tables:tables,exact_histogram_and_count_assertions:2*fibers,output_support_terms:polyTerms,memo_states_accumulated:dpStates,memo_cache_hits_accumulated:cacheHits,transition_scans:transitions},
    larger_cases:benchmark,component_factorization:{named_tables:String(total),support_terms:all.size,verified:true},prefix_observer_repair:{joint_observer_support:["0,0","1,0"],coefficients:["1","1"],verified:true},
    semantics:{arithmetic:"exact nonnegative BigInt coefficients and signed integer Laurent exponents",coverage:"All capacity assignments and all attainable margin fibers for the listed finite shapes; four additional individually specified dense/sparse cases",benchmark_metric:"Exact search calls/states; not elapsed time or general worst-case speedup"}};
  return result;
})();
console.log(JSON.stringify(results,null,2));
