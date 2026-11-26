from pathlib import Path
s=Path('gaj_solver.cpp').read_text()
# Only change high-depth search. Adjacent-depth reuse of proved values.
needle='if(++calls>cap)throw 1;if(k<=4&&getenv("EM_DENSE"))'
assert s.count(needle)==1
s=s.replace(needle,'''if(getenv("EM_DEPTH")){
 auto hi=mem.find(Key{s,k+1});if(hi!=mem.end()&&hi->second==-1){++depthNo;return mem.emplace(key,-1).first->second;}
 if(k>1){auto lo=mem.find(Key{s,k-1});if(lo!=mem.end()&&lo->second!=-1){int proof=lo->second;++depthYes;return mem.emplace(key,proof).first->second;}}
 }if(++calls>cap)throw 1;if(k<=4&&getenv("EM_DENSE"))''')
s=s.replace('int cap,calls=0,envelopePrunes=0,satChecks=0,satPrunes=0;', 'int cap,calls=0,envelopePrunes=0,satChecks=0,satPrunes=0;uint64_t depthNo=0,depthYes=0,dups=0,knownNo=0;')
needle='struct O{long long score,bal;int q;S a,b;};vector<O> opts;'
assert s.count(needle)==1
s=s.replace(needle,'''struct O{long long score,bal;int q;S a,b;};vector<O> opts;
 struct PairKey{S a,b;bool operator==(const PairKey&o)const{return a==o.a&&b==o.b;}};
 struct PairHash{size_t operator()(const PairKey&x)const{size_t a=Hash{}(Key{x.a,0}),b=Hash{}(Key{x.b,0});return a^(b+0x9e3779b97f4a7c15ULL+(a<<6)+(a>>2));}};
 unordered_set<PairKey,PairHash> seen;
 bool dedup=getenv("EM_PAIR"),depth=getenv("EM_DEPTH");
 auto lessS=[](const S&a,const S&b){return tie(a.act,a.c)<tie(b.act,b.c);};
 auto no=[&](const S&t){auto it=mem.find(Key{t,k-1});if(it!=mem.end()&&it->second==-1)return true;if(depth){it=mem.find(Key{t,k});if(it!=mem.end()&&it->second==-1)return true;}return false;};''')
needle='long long score=max(ca,cb);opts.push_back'
assert s.count(needle)==1
s=s.replace(needle,'''if(dedup){if(no(a)||no(b)){++knownNo;continue;}PairKey pair=lessS(b,a)?PairKey{b,a}:PairKey{a,b};if(!seen.insert(move(pair)).second){++dups;continue;}}
 long long score=max(ca,cb);opts.push_back''')
# Replay can use a witnessed shorter budget, only on positive states. Exact keys always preferred.
needle='int q=mem.at(Key{s,rem});'
assert s.count(needle)==1
s=s.replace(needle,'''auto proof=mem.find(Key{s,rem});if(getenv("EM_DEPTH")){while(proof==mem.end()&&rem>0){--rem;proof=mem.find(Key{s,rem});}}assert(proof!=mem.end());int q=proof->second;assert(q!=-1);''')
s=s.replace('<<dense.products<<endl;', '<<dense.products<<","<<v.depthNo<<","<<v.depthYes<<","<<v.dups<<","<<v.knownNo<<endl;')
Path('gak_solver.cpp').write_text(s)
