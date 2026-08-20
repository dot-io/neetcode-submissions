#include <stack>

class Solution {
public:
    bool isValid(string s) {
        std::stack<char> parenth_stack;
        for (char c : s) {

            switch (c) {
                case '(': case '{': case '[':
                    parenth_stack.push(c);
                    break;

                case ')':
                    if (parenth_stack.empty() ||parenth_stack.top() != '('){
                        return false;
                    } else {
                        parenth_stack.pop();
                    }
                    break;

                case ']':
                    if (parenth_stack.empty() || parenth_stack.top() != '['){
                        return false;
                    } else {
                        parenth_stack.pop();
                    }
                    break;

                case '}':
                    if (parenth_stack.empty() || parenth_stack.top() != '{'){
                        return false;
                    } else {
                        parenth_stack.pop();
                    }
                    break;
            }
        }
        if (parenth_stack.size() != 0) return false;
        return true;
    }
};
