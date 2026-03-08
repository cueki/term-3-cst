// Madison Lovett, A01292253
// March 6th, 2026

public class HashSimulator {

    public int H1(String key, int tableSize) {
        int sum = 0;
        for (int i = 0; i < key.length(); i++) {
            sum += (key.charAt(i) - 'A' + 1);
        }
        return sum % tableSize;
    }

    public int H2(String key, int tableSize) {
        long sum = 0;
        long power = 1;
        for (int i = 0; i < key.length(); i++) {
            sum += (key.charAt(i) - 'A' + 1) * power;
            power *= 26;
        }
        return (int)(sum % tableSize);
    }

    // H3: Char pair hash inspired by n-gram...
    // Sums the products of adjacent character pairs to
    // capture the positional information that H1 misses.
    public int H3(String key, int tableSize) {
        int sum = 0;
        for (int i = 0; i < key.length() - 1; i++) {
            int a = key.charAt(i) - 'A' + 1;
            int b = key.charAt(i + 1) - 'A' + 1;
            sum += a * b;
        }
        return sum % tableSize;
    }

    public int[] runHashSimulation(String[] keys, int tableSize) {
        int[] results = new int[6];

        for (int h = 0; h < 3; h++) {
            String[] table = new String[tableSize];
            int collisions = 0;
            int probes = 0;

            for (String key : keys) {
                int hash;
                if (h == 0) hash = H1(key, tableSize);
                else if (h == 1) hash = H2(key, tableSize);
                else hash = H3(key, tableSize);

                if (table[hash] != null) {
                    collisions++;
                    int idx = hash;
                    do {
                        idx = (idx + 1) % tableSize;
                        probes++;
                    } while (table[idx] != null);
                    table[idx] = key;
                } else {
                    table[hash] = key;
                }
            }

            results[h * 2] = collisions;
            results[h * 2 + 1] = probes;
        }

        return results;
    }
}
