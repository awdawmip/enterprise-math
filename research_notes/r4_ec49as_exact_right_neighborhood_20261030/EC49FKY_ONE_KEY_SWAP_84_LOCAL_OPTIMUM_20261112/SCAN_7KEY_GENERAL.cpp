#include <bits/stdc++.h>
using namespace std;
const int INF=1e9;
struct Node{map<unsigned char,int> next;int labels=0;};
vector<Node> trie;
vector<int> local;
void addpath(const string& s,int label){int u=0;for(int j=2;j+1<(int)s.size();j+=2){int byte=stoi(s.substr(j,2),nullptr,16);auto it=trie[u].next.find(byte);if(it==trie[u].next.end()){int v=trie.size();trie[u].next[byte]=v;trie.push_back({});u=v;}else u=it->second;}auto it=find(local.begin(),local.end(),label);if(it==local.end())throw runtime_error("label missing");trie[u].labels|=1<<int(it-local.begin());}
unordered_map<int,int> visit(int u){unordered_map<int,int> dp;dp[0]=0;if(trie[u].labels)dp[trie[u].labels]=0;
 for(const auto &[ch,v]:trie[u].next){auto d=visit(v);unordered_map<int,int> next;next.reserve(dp.size()*min<size_t>(d.size(),8)+1);
 for(auto [a,ca]:dp)for(auto [b,cb]:d){int mask=a|b,c=ca+cb;auto it=next.find(mask);if(it==next.end()||c<it->second)next[mask]=c;}
 dp.swap(next);
 }
 for(auto &[m,c]:dp)if(m)c++;
 return dp;
}
vector<int> solve_root(int rt,const vector<pair<int,string>>& rows,const vector<int>& labs,int& node_n){
 trie.clear();trie.emplace_back();local=labs;
 for(auto [lab,s]:rows)if(stoi(s.substr(0,2),nullptr,16)==rt)addpath(s,lab);
 node_n=trie.size();auto d=visit(0);int n=local.size();vector<int> f(1<<n,INF);
 for(auto[m,c]:d)f[m]=c;
 for(int j=0;j<n;j++)for(int m=0;m<(1<<n);m++)if(!(m>>j&1))f[m]=min(f[m],f[m|(1<<j)]);
 return f;
}
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int N;cin>>N;
 for(int id=0;id<N;id++){
 int nw;cin>>nw;vector<pair<int,string>> rows;rows.reserve(nw);map<int,set<int>> sup;
 for(int j=0;j<nw;j++){int lab;string s;cin>>lab>>s;int rt=stoi(s.substr(0,2),nullptr,16);rows.emplace_back(lab,s);sup[rt].insert(lab);}
 vector<int> roots;vector<vector<int>> labsets;vector<vector<int>> cost;vector<vector<int>> positions(24);vector<int> nodecounts;
 for(const auto&[rt,labels]:sup){roots.push_back(rt);vector<int> L(labels.begin(),labels.end());labsets.push_back(L);int node_n;cost.push_back(solve_root(rt,rows,L,node_n));nodecounts.push_back(node_n);
 for(int j=0;j<(int)L.size();j++)positions[L[j]].push_back((int(roots.size())-1)<<16 |j);
 }
 int best=INF,ways=0;vector<int> acc(roots.size(),0);vector<int> best_acc;
 function<void(int)> dfs=[&](int lab){if(lab==24){int v=0;for(int k=0;k<(int)roots.size();k++)v+=cost[k][acc[k]];if(v<best){best=v;ways=1;best_acc=acc;}else if(v==best)ways++;return;}
  if(positions[lab].empty())throw runtime_error("not covered");
  for(int z:positions[lab]){int ri=z>>16,li=z&65535;acc[ri]|=1<<li;dfs(lab+1);acc[ri]&=~(1<<li);}
 };
 dfs(0);
 cout<<id<<" "<<best<<" "<<ways<<" "<<roots.size()<<" ";for(int k=0;k<(int)roots.size();k++)cout<<roots[k]<<":"<<cost[k].back()<<":"<<nodecounts[k]<<":"<<labsets[k].size()<<":"<<best_acc[k]<<",";cout<<"\n";
 }
}
