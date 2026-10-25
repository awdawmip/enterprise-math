"use strict";
function verify(){
  const MAX_DEPTH=15, WORD_DEPTH=8;
  const eq=(ok,msg)=>{if(!ok)throw Error("FAILED: "+msg)};
  const fac=[1n];for(let i=1;i<=16;i++)fac.push(fac[i-1]*BigInt(i));
  function W(a,b,c){if(Math.min(a,b,c)<0)return 0n;let ans=0n;
    for(let r=0;r<=Math.min(a,c);r++)
      ans+=fac[a+b+c-r]/(fac[r]*fac[a-r]*fac[b]*fac[c-r]);
    return ans;
  }
  const put=(m,k,v)=>m.set(k,(m.get(k)||0n)+v);
  const initial=q=>new Map([["0,0,0,"+q,1n]]);
  function step(states){const next=new Map();
    for(const [key,num] of states){const [a,b,c,q]=key.split(",").map(Number);
      put(next,[a+1,b,c,1].join(","),num);
      put(next,[a,b+1,c,0].join(","),num);
      put(next,[a,b,c+1,0].join(","),num*(q===1?2n:1n));
    }
    return next;
  }
  function endpoints(states){const map=new Map();
    for(const [key,num] of states){const k=key.split(",").slice(0,3).join(",");put(map,k,num)}
    return map;
  }
  let zero=initial(0),one=initial(1),entries=0;
  const H=[],D=[];
  for(let h=0;h<=MAX_DEPTH;h++){
    const a=endpoints(zero),b=endpoints(one);let total0=0n,total1=0n;
    for(let x=0;x<=h;x++)for(let y=0;y<=h-x;y++){
      const z=h-x-y,key=[x,y,z].join(","),p=a.get(key)||0n,q=b.get(key)||0n;
      eq(p===W(x,y,z),"closed form "+key+" depth "+h);
      eq(q-p===(z?W(x,y,z-1):0n),"future defect "+key+" depth "+h);
      eq(q>=p,"nonnegative "+key);total0+=p;total1+=q;entries++;
    }
    H.push(total0);D.push(total1-total0);
    if(h>0){eq(D[h]===H[h-1],"total defect "+h);
      eq(D[h]>=3n**BigInt(h-1),"exponential lower bound "+h);
      if(h>=3)eq(D[h]>3n**BigInt(h-1),"strict bound "+h);
    }else eq(D[h]===0n,"zero horizon");
    if(h>=2)eq(H[h]===3n*H[h-1]+H[h-2],"total recurrence "+h);
    zero=step(zero);one=step(one);
  }
  function enumerateLabels(word,start){
    let states=[start];
    for(const letter of word){const next=[];
      for(const q of states){if(letter==="A")next.push(1);
        else if(letter==="B")next.push(0);
        else if(q===1)next.push(0,0);
        else next.push(0);
      }states=next;
    }return BigInt(states.length);
  }
  function wordLaw(word,q){let occurrences=0;
    for(let i=1;i<word.length;i++)if(word[i-1]==="A"&&word[i]==="C")occurrences++;
    if(q===1&&word.startsWith("C"))occurrences++;
    return 2n**BigInt(occurrences);
  }
  let words=0,realizations=0n;
  function walk(prefix,n){if(prefix.length===n){
      for(const q of [0,1]){const val=enumerateLabels(prefix,q);
        eq(val===wordLaw(prefix,q),"word law "+prefix+"/"+q);
        words++;realizations+=val;
      }return;
    }for(const letter of ["A","B","C"])walk(prefix+letter,n);
  }
  for(let n=0;n<=WORD_DEPTH;n++)walk("",n);
  const hankel=[
    [enumerateLabels("AB",0),enumerateLabels("ABC",0)],
    [enumerateLabels("BA",0),enumerateLabels("BAC",0)]
  ];
  const det=hankel[0][0]*hankel[1][1]-hankel[0][1]*hankel[1][0];
  eq(det===1n,"rank-two Hankel");
  eq(H.slice(0,7).map(String).join(",")==="1,3,10,33,109,360,1189","H samples");
  eq(D.slice(0,7).map(String).join(",")==="0,1,3,10,33,109,360","D samples");
  return {status:"PASS",scope:"EC29 positive source-labelled BRC TEST model, not native heartbeat",
    exact_arithmetic:"JavaScript BigInt; two independent enumeration paths",
    depth_range:"0..15",word_depth_range:"0..8",
    endpoints_W_and_defect_verified:entries,word_start_state_pairs_verified:words,
    enumerated_labelled_realizations:realizations.toString(),
    H_first_7:H.slice(0,7).map(String),D_first_7:D.slice(0,7).map(String),
    hankel:hankel.map(r=>r.map(String)),hankel_determinant:String(det),hankel_rank:2,
    native_heartbeat_executed:false,independent_driver_review:false,
    proof_basis:"exact first-letter source-label bijection, finite-state transfer, Hankel rank"
  };
}
if(typeof module!=="undefined" && typeof require!=="undefined" && require.main===module)
  process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
