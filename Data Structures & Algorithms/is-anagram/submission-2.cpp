class Solution {
public:
    bool isAnagram(string s, string t) {
        std::map<char, int> s_occurence;
        std::map<char, int> t_occurence;
        if (s.length() != t.length()) return false;
        for (int i = 0; i < s.length(); i++) {
            if (s_occurence.find(s[i]) == s_occurence.end()) s_occurence[s[i]] = 0;
            else s_occurence[s[i]]++;
            if (t_occurence.find(t[i]) == t_occurence.end()) t_occurence[t[i]] = 0;
            else t_occurence[t[i]]++;
        }
        return s_occurence == t_occurence;
    }
};
