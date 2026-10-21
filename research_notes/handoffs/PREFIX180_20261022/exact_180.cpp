#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <functional>
#include <numeric>
#include <unordered_set>
#include <vector>
using namespace std;
using P=array<int,4>;using B=uint64_t;
int pc(B x){return __builtin_popcountll(x);} P add(P x,P y){for(int i=0;i<4;i++)x[i]+=y[i];return x;}
int sup(P p){int z=0;for(int v:p)z+=v!=0;return z;}
vector<P> simplex(int n){vector<P>o;for(int a=0;a<=n;a++)for(int b=0;b<=n-a;b++)for(int c=0;c<=n-a-b;c++)o.push_back({a,b,c,n-a-b-c});return o;}
int key(P x){return ((x[0]*17+x[1])*17+x[2])*17+x[3];}
vector<P> X3,X4,R,ALL; vector<array<int,9>> qq; vector<vector<B>> options; vector<P> T;
void setup(){auto X=simplex(8);ALL=simplex(16);for(P p:X){if(sup(p)<=2){if(p!=P{4,4,0,0})R.push_back(p);}else if(sup(p)==3)X3.push_back(p);else X4.push_back(p);}if(X3.size()!=84||X4.size()!=35||R.size()!=45||ALL.size()!=969)abort();}
void prepare(const array<int,9>&q){vector<P>U=R;for(int j:q)U.push_back(X3[j]);static int tid[83521];static bool covered[83521];fill(tid,tid+83521,-1);fill(covered,covered+83521,false);
 for(int i=0;i<54;i++)for(int j=i;j<54;j++)covered[key(add(U[i],U[j]))]=true;
 T.clear();options.clear();for(P p:ALL)if(!covered[key(p)]){tid[key(p)]=T.size();T.push_back(p);}options.resize(T.size());
 for(int j=0;j<35;j++)for(P u:U){int ti=tid[key(add(u,X4[j]))];if(ti>=0)options[ti].push_back(B(1)<<j);}
 for(int j=0;j<35;j++)for(int k=j;k<35;k++){int ti=tid[key(add(X4[j],X4[k]))];if(ti>=0)options[ti].push_back((B(1)<<j)|(B(1)<<k));}
 for(auto &o:options){sort(o.begin(),o.end());o.erase(unique(o.begin(),o.end()),o.end());}
}
struct Solver {int K;unsigned long long nodes=0, limit;bool timed=false; B sol=0;unordered_set<B>bad;
 bool go(B chosen){nodes++; if(nodes>limit){timed=true;return false;}int left=K-pc(chosen);if(left<0)return false;if(bad.count(chosen))return false;int best_n=100000;vector<B> best_opts;vector<B> need_masks;need_masks.reserve(T.size());
 for(auto &o:options){bool done=false;B nm=0;vector<B>poss;
  for(B p:o){B a=p&~chosen;if(!a){done=true;break;}if(pc(a)<=left){poss.push_back(a);nm|=a;}}
  if(done)continue;
  if(poss.empty()){bad.insert(chosen);return false;}
  need_masks.push_back(nm);if((int)poss.size()<best_n){best_n=poss.size();best_opts=move(poss);}
 }
 if(best_n==100000){sol=chosen;return true;}
 sort(need_masks.begin(),need_masks.end(),[](B a,B b){return pc(a)<pc(b);});B used=0;int packing=0;for(B m:need_masks)if(!(used&m)){packing++;used|=m;if(packing>left){bad.insert(chosen);return false;}}
 sort(best_opts.begin(),best_opts.end(),[](B a,B b){int pa=pc(a),pb=pc(b);return pa==pb?a<b:pa<pb;});best_opts.erase(unique(best_opts.begin(),best_opts.end()),best_opts.end());
 for(B b:best_opts){if(go(chosen|b))return true;if(timed)return false;}bad.insert(chosen);return false;}
};
int main(int argc,char**argv){if(argc<5){cerr<<"USAGE bin prefix count K limit_nodes [start]\n";return 2;}setup();string file=argv[1];int count=atoi(argv[2]),K=atoi(argv[3]);unsigned long long limit=stoull(argv[4]);int start=argc>5?atoi(argv[5]):0;ifstream f(file,ios::binary);if(!f)return 2;int sz=file.find("prefix165")!=string::npos?29:27;vector<unsigned char>b(sz);int i=0,tested=0;while(f.read((char*)b.data(),sz)){if(i++<start)continue;array<int,9>q;for(int j=0;j<9;j++)q[j]=b[j];prepare(q);Solver s;s.K=K;s.limit=limit;bool got=s.go(0);cout<<file<<" row="<<i-1<<" Q=";for(int j:q)cout<<j<<",";cout<<" base_uncovered="<<T.size()<<" K="<<K<<" answer="<<(got?"YES":s.timed?"UNKNOWN":"NO")<<" nodes="<<s.nodes<<" W=";if(got)for(int j=0;j<35;j++)if((s.sol>>j)&1)cout<<j<<",";cout<<"\n"<<flush;tested++;if(got||tested>=count)break;}
}
