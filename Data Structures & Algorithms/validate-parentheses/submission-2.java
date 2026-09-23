class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> valid = new HashMap<>();
        valid.put('(',')');
        valid.put('[',']');
        valid.put('{','}');
        Deque<Character> stack = new ArrayDeque<>();

        for(int i=0; i<s.length();i++){
            char cur = s.charAt(i);
            if(valid.containsKey(cur)){
                stack.push(cur);
            } else {
                if(stack.isEmpty()){
                    return false;
                }
                char pop = stack.pop();
                if(valid.get(pop)!=cur){
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
