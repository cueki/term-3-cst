import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * @author Madison Lovett
 * @student_id A01292253
 * @set V
 *
 * Takes a benefit matrix where row X, column Y represents the benefit of
 * assigning person X to job Y, this class attempts to find the assignment that
 * maximizes total benefit by evaluating all possible permutations.
 *
 * This is very slow... on my 9950x3d:
 * real    0m0.448s
 * user    0m2.405s
 * sys     0m0.462s
 */
public class JobAssignmentFinder {

    private int[][] benefitMatrix;
    private int n;
    private ArrayList<Integer> maxAssignment;
    private int maxTotalValue;
    private boolean dataLoaded;

    public JobAssignmentFinder() {
        this.n = -1;
        this.benefitMatrix = null;
        this.maxAssignment = null;
        this.maxTotalValue = 0;
        this.dataLoaded = false;
    }

    /**
     * Reads a data file and inits the benefit matrix.
     * @param filename the path to the data file
     */
    public void readDataFile(String filename) {
        try {
            // oh java it is SO GREAT TO BE BACK LADIES AND GENTLEMEN!!
            Scanner scanner = new Scanner(new File(filename)); // D:
            n = scanner.nextInt();
            benefitMatrix = new int[n][n];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    benefitMatrix[i][j] = scanner.nextInt();
                }
            }
            scanner.close();
            dataLoaded = true;
            maxAssignment = null;
            maxTotalValue = 0;

        } catch (FileNotFoundException e) {
            dataLoaded = false;
            n = -1;
        }
    }

    /**
     * @return N (or -1 if no file has been loaded)
     */
    public int getInputSize() {
        if (!dataLoaded) {
            return -1;
        }
        return n;
    }

    /**
     * @return the benefit matrix as a 2D array
     */
    public int[][] getBenefitMatrix() {
        return benefitMatrix;
    }

    /**
     * A string representation of the benefit matrix.
     * @return A formatted string showing the matrix
     */
    public String benefitMatrixToString() {
        if (!dataLoaded || benefitMatrix == null) {
            return "No data.";
        }

        StringBuilder sb = new StringBuilder();
        sb.append("Benefit Matrix (").append(n).append("x").append(n).append("):\n");

        int maxWidth = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int width = String.valueOf(benefitMatrix[i][j]).length();
                if (width > maxWidth) {
                    maxWidth = width;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            sb.append("[");
            for (int j = 0; j < n; j++) {
                sb.append(String.format("%" + maxWidth + "d", benefitMatrix[i][j]));
                if (j < n - 1) {
                    sb.append(" ");
                }
            } sb.append("]\n");
        }

        return sb.toString();
    }

    /**
     * @return the optimal job assignment
     */
    public ArrayList<Integer> getMaxAssignment() {
        if (maxAssignment != null) {
            return maxAssignment;
        }

        findMaxAssignment();
        return maxAssignment;
    }

    /**
     * @return the total benefit value of the optimal assignment
     */
    public int getMaxAssignmentTotalValue() {
        if (maxAssignment == null) {
            findMaxAssignment();
        }
        return maxTotalValue;
    }

    /**
     * @param person the person index
     * @param job the job index
     * @return the benefit value for assigning the person to the job
     */
    public int getBenefit(int person, int job) {
        return benefitMatrix[person][job];
    }

    /**
     * Generates all permutations and evaluates each one.
     */
    private void findMaxAssignment() {
        ArrayList<ArrayList<Integer>> allPermutations = getPermutations(n);
        maxTotalValue = Integer.MIN_VALUE;
        maxAssignment = null;

        for (ArrayList<Integer> perm : allPermutations) {
            int totalValue = calculateTotalValue(perm);
            if (totalValue > maxTotalValue) {
                maxTotalValue = totalValue;
                maxAssignment = perm;
            }
        }
    }

    /**
     * Calculates the total benefit value for a given assignment.
     * @param assignment The job assignment permutation
     * @return The sum of benefits for this assignment
     */
    private int calculateTotalValue(ArrayList<Integer> assignment) {
        int total = 0;
        for (int person = 0; person < n; person++) {
            int job = assignment.get(person);
            total += benefitMatrix[person][job];
        }
        return total;
    }

    // From perms.java onwards

    /**
     * Recursive decrease-and-conquer algorithm to generate a list of all
     * permutations of the numbers 0..N-1. This follows the "decrease by 1" pattern
     * of decrease and conquer algorithms.
     *
     * This method returns an ArrayList of ArrayLists. One permutation is an
     * ArrayList containing 0,1,2,...,N-1 in some order. The final result is an
     * ArrayList containing N! of those permutations.
     *
     * @param N
     * @return
     */
    private ArrayList<ArrayList<Integer>> getPermutations(int N) {
        ArrayList<ArrayList<Integer>> results = new ArrayList<ArrayList<Integer>>();

        /**
         * This isn't a "base case", it's a "null case". This function does not call
         * itself with an argument of zero, but we can't prevent another caller from
         * doing so. It's a weird result, though. The list of permutations has one
         * permutation, but the one permutation is empty (0 elements).
         */
        if (N == 0) {
            ArrayList<Integer> emptyList = new ArrayList<Integer>();
            results.add(emptyList);

        } else if (N == 1) {
            /**
             * Now THIS is the base case. Create an ArrayList with a single integer, and add
             * it to the results list.
             */
            ArrayList<Integer> singleton = new ArrayList<Integer>();
            singleton.add(0);
            results.add(singleton);

        } else {
            /**
             * And: the main part. First a recursive call (this is a decrease and conquer
             * algorithm) to get all the permutations of length N-1.
             */
            ArrayList<ArrayList<Integer>> smallList = getPermutations(N - 1);

            /**
             * Iterate over the list of smaller permutations and insert the value 'N-1' into
             * every permutation in every possible position, adding each new permutation to
             * the big list of permutations.
             */
            for (ArrayList<Integer> perm : smallList) {

                /**
                 * Add 'N-1' -- the biggest number in the new permutation -- at each of the
                 * positions from 0..N-1.
                 */
                for (int i = 0; i < perm.size(); i++) {
                    @SuppressWarnings("unchecked")
                    ArrayList<Integer> newPerm = (ArrayList<Integer>) perm.clone();
                    newPerm.add(i, N - 1);
                    results.add(newPerm);
                }

                /**
                 * Add 'N-1' at the end (i.e. at position "size").
                 */
                @SuppressWarnings("unchecked")
                ArrayList<Integer> newPerm = (ArrayList<Integer>) perm.clone();
                newPerm.add(N - 1);
                results.add(newPerm);

            }

        }

        /**
         * Nothing left to do except:
         */
        return results;
    }
}
