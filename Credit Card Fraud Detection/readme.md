Deteksi Penipuan Kartu Kredit dengan Machine Learning
Gambaran Umum Proyek
Proyek ini bertujuan untuk mengembangkan model machine learning yang mampu mendeteksi transaksi kartu kredit yang mencurigakan atau berpotensi penipuan. Model ini dapat membantu lembaga keuangan untuk mengurangi kerugian akibat penipuan dan meningkatkan keamanan transaksi pelanggan.

Dataset
Proyek ini menggunakan dataset transaksi kartu kredit yang berisi informasi seperti waktu transaksi, jumlah transaksi, dan berbagai fitur anonim yang dihasilkan dari Principal Component Analysis (PCA). Dataset ini sangat tidak seimbang, dengan transaksi penipuan hanya mewakili sebagian kecil dari total transaksi.

Metodologi
Analisis Data Eksplorasi (EDA): Memahami distribusi data, mengidentifikasi outlier, dan menganalisis hubungan antar fitur.
Pra-pemrosesan Data: Menangani nilai yang hilang, melakukan penskalaan fitur, dan mengatasi ketidakseimbangan kelas (misalnya, menggunakan teknik oversampling atau undersampling).
Pemilihan Fitur: Mengidentifikasi fitur-fitur yang paling relevan untuk pemodelan menggunakan teknik seperti analisis korelasi, Recursive Feature Elimination (RFE), atau SelectFromModel.
Pemodelan: Mengembangkan dan membandingkan beberapa model machine learning, seperti:
Logistic Regression
Random Forest
Support Vector Machines (SVM)
XGBoost
Evaluasi Model: Mengevaluasi performa model menggunakan metrik seperti precision, recall, F1-score, dan Area Under the Receiver Operating Characteristic Curve (AUROC).
Penyetelan Hyperparameter: Mengoptimalkan hyperparameter model untuk meningkatkan performa.
Hasil
Model terbaik yang dihasilkan mampu mendeteksi transaksi penipuan dengan tingkat akurasi dan recall yang tinggi. Model ini juga efektif dalam mengurangi false positive, yaitu transaksi sah yang salah diidentifikasi sebagai penipuan.

Kesimpulan
Proyek ini menunjukkan potensi machine learning dalam mendeteksi penipuan kartu kredit. Model yang dikembangkan dapat menjadi alat yang berharga bagi lembaga keuangan untuk meningkatkan keamanan transaksi dan melindungi pelanggan dari kerugian finansial.

Saran untuk Pengembangan Lebih Lanjut
Mencoba arsitektur model yang lebih kompleks, seperti deep learning.
Mengeksplorasi teknik pengurangan dimensi lain selain PCA.
Mengumpulkan lebih banyak data untuk meningkatkan performa model.
Mengembangkan sistem real-time untuk mendeteksi penipuan secara langsung.
Cara Menggunakan
Clone repositori ini.
Install dependencies yang diperlukan.
Jalankan notebook Jupyter yang disediakan untuk melihat analisis data, pemodelan, dan evaluasi.
Kontribusi
Kontribusi sangat diharapkan! Silakan ajukan pull request jika Anda memiliki saran atau perbaikan.