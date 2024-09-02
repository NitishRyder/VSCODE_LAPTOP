public class BruteForceAttack { 
    private static final char[] CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&* ()_+".toCharArray(); 
    private static final String TARGET_PASSWORD = "SRK"; 
    public static int totalAttempts = 1; 
    public static void main(String[] args) { 
        bruteForcePassword(); 
    } 
    public static void bruteForcePassword() { 
        for (int length = 1; ; length++) { 
            char[] attempt = new char[length]; 
            if (tryPassword(attempt, 0)) { 
                break; 
            } 
        } 
    } 
    public static boolean tryPassword(char[] attempt, int position) { 
        if (position == attempt.length) { 
            String guess = new String(attempt); 
            System.out.println("Trying: " + guess); 
 
            if (guess.equals(TARGET_PASSWORD)) { 
                System.out.println("Password found: " + guess); 
                System.out.println("No.of Attempts: "+totalAttempts); 
                return true; 
            } 
            totalAttempts = totalAttempts + 1; 
            return false; 
        } 
 
        for (char c : CHARACTERS) { 
            attempt[position] = c; 
            if (tryPassword(attempt, position + 1)) { 
                return true; 
            } 
        } 
        return false; 
    } 
} 