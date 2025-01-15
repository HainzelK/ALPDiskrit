import networkx as nx
import matplotlib.pyplot as plt

class Graf:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node):
        """Menambahkan node ke dalam graf."""
        self.graph.add_node(node)
        print(f"Node {node} ditambahkan.")

    def add_edge(self, u, v, weight=None):
        """Menambahkan edge antara dua node."""
        self.graph.add_edge(u, v, weight=weight)
        print(f"Edge ditambahkan antara {u} dan {v} dengan bobot {weight}.")

    def visualize_graph(self):
        """Menampilkan graf secara visual."""
        pos = nx.spring_layout(self.graph)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=3000, font_size=12, font_weight='bold')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.title("Visualisasi Graf")
        plt.show()

    def shortest_path(self, source, target):
        """Menghitung jalur terpendek antara dua node."""
        try:
            path = nx.shortest_path(self.graph, source=source, target=target, weight='weight')
            print(f"Jalur terpendek dari {source} ke {target}: {path}")
            return path
        except nx.NetworkXNoPath:
            print(f"Tidak ada jalur dari {source} ke {target}.")
            return None

    def visual_shortest_path(self, source, target):
        """Menampilkan visualisasi jalur terpendek antara dua node."""
        try:
            path = self.shortest_path(source, target)
            if path:
                path_edges = list(zip(path, path[1:]))
                pos = nx.spring_layout(self.graph)
                nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=3000, font_size=12, font_weight='bold')
                nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges, edge_color='red', width=2)
                plt.title(f"Jalur Terpendek dari {source} ke {target}")
                plt.show()
        except Exception as e:
            print(f"Error: {e}")

    # Metode Tambahan

    def is_connected(self):
        """Memeriksa apakah graf terhubung atau tidak."""
        connected = nx.is_connected(self.graph)
        print(f"Apakah graf terhubung? {connected}")
        return connected

    def degree_of_node(self, node):
        """Menghitung derajat dari node tertentu."""
        if node in self.graph:
            degree = self.graph.degree[node]
            print(f"Derajat dari node {node}: {degree}")
            return degree
        else:
            print(f"Node {node} tidak ditemukan di dalam graf.")
            return None

    def clustering_coefficient(self):
        """Menghitung koefisien clustering untuk setiap node."""
        clustering = nx.clustering(self.graph)
        print("Koefisien clustering untuk setiap node:")
        for node, coef in clustering.items():
            print(f"Node {node}: {coef:.2f}")
        return clustering

    def all_pairs_shortest_path(self):
        """Menghitung jalur terpendek antara semua pasangan node."""
        paths = dict(nx.all_pairs_shortest_path(self.graph))
        print("Jalur terpendek antara semua pasangan node:")
        for source, targets in paths.items():
            for target, path in targets.items():
                print(f"{source} -> {target}: {path}")
        return paths

    def diameter(self):
        """Menghitung diameter graf (jarak terpanjang antara dua node terdekat)."""
        try:
            dia = nx.diameter(self.graph)
            print(f"Diameter graf: {dia}")
            return dia
        except nx.NetworkXError as e:
            print(f"Error: {e}")
            return None

# Contoh Penggunaan
if __name__ == "__main__":
    graph = Graf()

    # Menambah node
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)

    # Menambah edge
    graph.add_edge(1, 2, weight=4.5)
    graph.add_edge(1, 3, weight=3.2)
    graph.add_edge(2, 4, weight=2.7)
    graph.add_edge(3, 4, weight=1.8)
    graph.add_edge(1, 4, weight=6.7)
    graph.add_edge(3, 5, weight=2.7)

    # Visualisasi graf
    graph.visualize_graph()

    # Jalur terpendek
    graph.shortest_path(1, 5)

    # Visualisasi jalur terpendek
    graph.visual_shortest_path(1, 5)

    # Metode tambahan
    graph.is_connected()
    graph.degree_of_node(1)
    graph.clustering_coefficient()
    graph.all_pairs_shortest_path()
    graph.diameter()
