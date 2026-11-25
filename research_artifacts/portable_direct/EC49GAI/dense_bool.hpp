// Exact full-recovery observer, EC49GAH specialization, dense state order.
struct DenseBool {
 using U=uint32_t; using Q=vector<U>;
 size_t limit=8192; unordered_map<string,int> bank;
 uint64_t hits=0,misses=0,clears=0,products=0;
 static U full(int n){return (U(1)<<n)-1;}
 static U pack(U a,U b){U p=0,z=1;for(;b;b&=b-1,z<<=1)if(a&(b&-b))p|=z;return p;}
 static Q canon(Q q,int n){U f=full(n);for(U &a:q)a=min(a,f^a);sort(q.begin(),q.end());q.erase(unique(q.begin(),q.end()),q.end());if(!q.empty()&&!q[0])q.erase(q.begin());return q;}
 static Q restrictQ(const Q&q,U b){Q x;for(U a:q)x.push_back(pack(a,b));return canon(move(x),__builtin_popcount(b));}
 int solve(int n,const Q&q,int d){if(n<=1)return -2;if(d<=0||n>(1<<d))return -1;
 string key;key.push_back(char(n));key.push_back(char(d));for(U a:q){key.push_back(char(a&255));key.push_back(char(a>>8));}
 auto it=bank.find(key);if(it!=bank.end()){++hits;return it->second;}++misses;
 U f=full(n);int ans=-1;Q order=q;sort(order.begin(),order.end(),[&](U a,U b){return make_pair(abs(n-2*__builtin_popcount(a)),a)<make_pair(abs(n-2*__builtin_popcount(b)),b);});
 for(U a:order){int na=__builtin_popcount(a),nb=n-na;if(max(na,nb)>(1<<(d-1)))continue;++products;
 U b=f^a;if(na<nb){swap(a,b);swap(na,nb);}if(solve(na,restrictQ(q,a),d-1)!=-1&&solve(nb,restrictQ(q,b),d-1)!=-1){ans=min(a,b);break;}}
 if(limit){if(bank.size()>=limit){bank.clear();++clears;}bank.emplace(move(key),ans);}return ans;}
};
