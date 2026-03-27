import java.util.LinkedList;
import java.util.Queue;

// Author: Madison Lovett
// Date: March 27th, 2026

public class Graph {

    private String[] labels;
    private int[][] adjMatrix;
    private boolean directed;
    private int n;

    private String lastDFSOrder = null;
    private String lastDFSDeadEndOrder = null;
    private String lastBFSOrder = null;

    public Graph(String[] vertexLabels, boolean isDirected) {
        this.n = vertexLabels.length;
        this.labels = new String[n];
        System.arraycopy(vertexLabels, 0, this.labels, 0, n);
        this.directed = isDirected;
        this.adjMatrix = new int[n][n];
        this.lastDFSOrder = null;
        this.lastDFSDeadEndOrder = null;
        this.lastBFSOrder = null;
    }

    public boolean isDirected() {
        return directed;
    }

    public void addEdge(String u, String v) {
        int ui = indexOf(u);
        int vi = indexOf(v);
        if (ui == -1 || vi == -1) {
            return;
        }
        adjMatrix[ui][vi] = 1;
        if (!directed) {
            adjMatrix[vi][ui] = 1;
        }
    }

    public int size() {
        return n;
    }

    public String getLabel(int v) {
        return labels[v];
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(labels[i]).append(":");
            for (int j = 0; j < n; j++) {
                sb.append(" ").append(adjMatrix[i][j]);
            }
            if (i < n - 1) {
                sb.append("\n");
            }
        }
        return sb.toString();
    }

    // DFS from first vertex
    public void runDFS(boolean quiet) {
        boolean[] visited = new boolean[n];
        StringBuilder order = new StringBuilder();
        StringBuilder deadEndOrder = new StringBuilder();

        dfsHelper(0, visited, order, deadEndOrder, quiet);
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfsHelper(i, visited, order, deadEndOrder, quiet);
            }
        }

        lastDFSOrder = order.toString().trim();
        lastDFSDeadEndOrder = deadEndOrder.toString().trim();
    }

    // DFS from named vertex
    public void runDFS(String v, boolean quiet) {
        int start = indexOf(v);
        if (start == -1) {
            return;
        }

        boolean[] visited = new boolean[n];
        StringBuilder order = new StringBuilder();
        StringBuilder deadEndOrder = new StringBuilder();

        dfsHelper(start, visited, order, deadEndOrder, quiet);
        lastDFSOrder = order.toString().trim();
        lastDFSDeadEndOrder = deadEndOrder.toString().trim();
    }

    private void dfsHelper(int v, boolean[] visited, StringBuilder order,
                           StringBuilder deadEndOrder, boolean quiet) {
        visited[v] = true;
        order.append(labels[v]).append(" ");
        if (!quiet) {
            System.out.println("Visiting vertex " + labels[v]);
        }

        boolean isDeadEnd = true;
        for (int i = 0; i < n; i++) {
            if (adjMatrix[v][i] == 1 && !visited[i]) {
                isDeadEnd = false;
                dfsHelper(i, visited, order, deadEndOrder, quiet);
            }
        }

        if (isDeadEnd) {
            deadEndOrder.append(labels[v]).append(" ");
        }
    }

    // BFS from first vertex
    public void runBFS(boolean quiet) {
        boolean[] visited = new boolean[n];
        Queue<Integer> queue = new LinkedList<>();
        StringBuilder order = new StringBuilder();

        visited[0] = true;
        queue.add(0);
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            order.append(labels[curr]).append(" ");
            if (!quiet) {
                System.out.println("BFS visiting vertex " + labels[curr]);
            }

            for (int i = 0; i < n; i++) {
                if (adjMatrix[curr][i] == 1 && !visited[i]) {
                    visited[i] = true;
                    queue.add(i);
                }
            }
        }

        // disconnected components
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                queue.add(i);
                while (!queue.isEmpty()) {
                    int curr = queue.poll();
                    order.append(labels[curr]).append(" ");
                    if (!quiet) {
                        System.out.println("BFS visiting vertex " + labels[curr]);
                    }

                    for (int j = 0; j < n; j++) {
                        if (adjMatrix[curr][j] == 1 && !visited[j]) {
                            visited[j] = true;
                            queue.add(j);
                        }
                    }
                }
            }
        }

        lastBFSOrder = order.toString().trim();
    }

    // BFS from named vertex
    public void runBFS(String v, boolean quiet) {
        int start = indexOf(v);
        if (start == -1) {
            return;
        }

        boolean[] visited = new boolean[n];
        Queue<Integer> queue = new LinkedList<>();
        StringBuilder order = new StringBuilder();

        visited[start] = true;
        queue.add(start);
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            order.append(labels[curr]).append(" ");

            if (!quiet) {
                System.out.println("BFS visiting vertex " + labels[curr]);
            }

            for (int i = 0; i < n; i++) {
                if (adjMatrix[curr][i] == 1 && !visited[i]) {
                    visited[i] = true;
                    queue.add(i);
                }
            }
        }

        lastBFSOrder = order.toString().trim();
    }

    // various printouts
    public String getLastDFSOrder() {
        if (lastDFSOrder == null) {
            return "No DFS has been performed on this graph.";
        }
        return lastDFSOrder;
    }

    public String getLastDFSDeadEndOrder() {
        if (lastDFSDeadEndOrder == null) {
            return "No DFS has been performed on this graph.";
        }
        return lastDFSDeadEndOrder;
    }

    public String getLastBFSOrder() {
        if (lastBFSOrder == null) {
            return "No BFS has been performed on this graph.";
        }
        return lastBFSOrder;
    }

    private int indexOf(String label) {
        for (int i = 0; i < n; i++) {
            if (labels[i].equals(label)) {
                return i;
            }
        }
        return -1;
    }
}
