#Analisis 1

hasilnya setelah mengubah hero1.hp menjadi 500 maka output dari hp akan berubah menjadi 500

#Analisis 3

ketika saya meniadakan super().__init__(name, hp, attack_power) maka akan terjadi error disebabkan kode tsb merupakan warisan dari class hero.

peran super adalah memanggilkan attribute dari class induk

#Analisis 4
1. Nilai Hp dan tidak error dikarenakan menggunakan Name Mangling dengan tujuan menghindari penamaan dengan subkelas dan kita tidak boleh sembarangan menggunakan teknik ini karena ia bersifat private yang tidak boleh diakses secara langsung

2. Nilai hp akan berubah menjadi -100, tujuan dari keberadaan Setter ialah untuk melindungi suatu objek dari data yang tidak valid

#Analisis 5
1. "Can't instantiate abstract class Hero without an implementation for abstract method 'attack' " ini berarti bahwa class Hero telah melanggar kontrak dari kelas abstract yang dimana method attack tidak didefinisikan yang dimana kelas abstract adalah cetak biru dari subclassnya(Hero dan Monster) konsekuensi nya akan terjadi Error

2. karena ia bukanlah subclass melainkan abstract class, Abstarct class(Games) dijadikan sebagai cetak biru untuk subclass.

# Analisis 6

1. program berjalan lancar, keuntungan ia tidak perlu mendeklarasikan method yang banyak cukup dengan mengikuti parent class

2. memunculkan method yang ada di dalam parent class, karena untuk memaksimalkan override dan menjalankan polimorfisme secara efektif.konsep dasar dari polimorfisme ialah  penggunaan satu antarmuka tunggal untuk merepresentasikan tindakan yang sama pada objek yang berbeda. 