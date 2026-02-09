import java.util.ArrayList;

/**
 * @author Madison Lovett
 * @student_id A01292253
 * @set V
 */
public class Lab2 {
    // get all palindromes of length n-2,
    // then wrap each one with the same letter on both sides.
    public ArrayList<String> generatePalindromeSequences(int n) {
        ArrayList<String> result = new ArrayList<>();
        char[] letters = {'A', 'B', 'C'};
        if (n == 1) {
            for (char c : letters) {
                result.add(String.valueOf(c));
            }
            return result;
        }
        if (n == 2) {
            for (char c : letters) {
                result.add("" + c + c);
            }
            return result;
        }

        ArrayList<String> smaller = generatePalindromeSequences(n - 2);
        for (char c : letters) {
            for (String s : smaller) {
                result.add(c + s + c);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Lab2 lab = new Lab2();
        for (int i = 1; i <= 20; i++) {
            ArrayList<String> seqs = lab.generatePalindromeSequences(i);
            System.out.println("Length " + i + " produces " + seqs.size() + " sequences.");
        }
        System.out.println("\nN=3: " + lab.generatePalindromeSequences(3));
        System.out.println("N=4: " + lab.generatePalindromeSequences(4));
        System.out.println("N=5: " + lab.generatePalindromeSequences(5));
    }
}
