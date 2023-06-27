class Solution {
    public boolean isPalindrome(int x) {
        String str = String.valueOf(x);
        String rts = "";
        for (int i = str.length()-1; i >= 0; i--) {
            rts = rts + str.charAt(i);
        }
        if (str.equals(rts)) {
            return true;
        }
        else {
            return false;
        }
    }
}