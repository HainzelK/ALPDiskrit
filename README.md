# Implementasi Teori Graf Menggunakan Python

## Deskripsi
Proyek ini adalah implementasi teori graf menggunakan **Python** dan library **NetworkX**. Proyek ini mencakup berbagai metode untuk mempelajari dan menganalisis graf, termasuk penambahan node, penambahan edge, visualisasi graf, dan analisis seperti jalur terpendek, koefisien clustering, dan diameter graf. 

Proyek ini dapat digunakan untuk memahami konsep dasar teori graf dan aplikasinya dalam analisis jaringan.

---

## Prasyarat
Pastikan Anda sudah menginstal library berikut sebelum menjalankan proyek ini:
- **NetworkX**: Untuk manipulasi graf.
- **Matplotlib**: Untuk visualisasi graf.

Anda dapat menginstalnya menggunakan perintah berikut:
```bash
pip install networkx matplotlib
```

---

## Fitur
Berikut adalah fitur utama yang tersedia dalam proyek ini:

1. **Penambahan Node**
   - Tambahkan node (titik) ke dalam graf.

2. **Penambahan Edge**
   - Tambahkan sisi (edge) yang menghubungkan dua node dengan bobot opsional.

3. **Visualisasi Graf**
   - Tampilkan graf secara visual untuk memahami struktur jaringan.

4. **Jalur Terpendek**
   - Temukan jalur terpendek antara dua node.

5. **Visualisasi Jalur Terpendek**
   - Tampilkan jalur terpendek secara visual pada graf.

6. **Cek Keterhubungan Graf**
   - Tentukan apakah graf terhubung sepenuhnya atau tidak.

7. **Derajat Node**
   - Hitung jumlah sisi (edge) yang terhubung ke node tertentu.

8. **Koefisien Clustering**
   - Hitung tingkat pengelompokan untuk setiap node.

9. **Jalur Terpendek Semua Pasangan**
   - Hitung semua jalur terpendek antara setiap pasangan node.

10. **Diameter Graf**
    - Tentukan diameter graf, yaitu jarak terpanjang antara dua node terdekat.

---

## Cara Penggunaan

### Membuat Objek Graf
```python
graph = Graf()
```

### Menambahkan Node
```python
graph.add_node(1)
graph.add_node(2)
```

### Menambahkan Edge
```python
graph.add_edge(1, 2, weight=4.5)
graph.add_edge(2, 3, weight=2.1)
```

### Visualisasi Graf
```python
graph.visualize_graph()
```

### Menemukan Jalur Terpendek
```python
graph.shortest_path(1, 3)
```

### Visualisasi Jalur Terpendek
```python
graph.visual_shortest_path(1, 3)
```

### Cek Keterhubungan Graf
```python
graph.is_connected()
```

### Hitung Derajat Node
```python
graph.degree_of_node(1)
```

### Koefisien Clustering
```python
graph.clustering_coefficient()
```

### Jalur Terpendek Semua Pasangan
```python
graph.all_pairs_shortest_path()
```

### Diameter Graf
```python
graph.diameter()
```

---

## Contoh Lengkap
Berikut adalah contoh implementasi lengkap:

```python
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
```
