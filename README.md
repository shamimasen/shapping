**Nama : Shalya Naura Lionita**
**NPM : 2306245535**
**Kelas : B**
>**Shapping :** http://shalya-naura-shapping.pbp.cs.ui.ac.id/

## **Penjelasan Tugas**
<summary> <b> Tugas 2 : Implementasi Model-View-Template (MVT) pada Django <b> </summary>

## **Implementasi Checklist Tugas**
* ### Membuat proyek Django baru:
1. Pertama saya membuat direktori baru dengan nama 'shapping' kemudian mengaktifkan virtual environmentnya.
2. Membuat berkas baru dengan nama requirement.txt untuk menyimpan dependencies yang diperlukan, yaitu :
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
3. Melakukan instalasi terhadap dependenciesnya dengan menjalankan perintah 'pip install -r requirements.txt'
4. Terakhir membuat proyek Django bernama 'shapping' dengan menjalankan perintah 'django-admin startproject mental_health_tracker .'

* ### Membuat aplikasi dengan nama main pada proyek Shapping:
1. Membuka terminal di dalam direktori Shapping kemudian menjalankan perintah 'python manage.py startapp main' agar membuat direktori baru bernama main di dalam direktori utama Shappiing.
2. Setelah terbentuk direktori baru bernama main, direktori main tersebut akan berisi struktur awal untuk membuat aplikasi.
3. Mmebuka berkas settings.py di dalam direktori proyek Shapping (bukan direktori utama) kemudian menambahkan 'main' di dalam daftar aplikasi yang dapat diakses pada variabel INSTALLED_APPS.
4. aplikasi main berhasil dibuat dan didaftarkan.

* ### Membuat routing pada proyek agar dapat menjalankan aplikasi main:
1. Membuat berkas urls.py di dalam direktori main yang telah saya buat tadi
2. Mengisi urls.py dengan kode berikut :

    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]

3. Membuka berkas urls.py yang ada di dalam direktori proyek shapping lalu menambahkan fungsi include dan rute Url di dalam variabel urlpatterns seperti berikut :

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]

4. Menjalankan proyek Django dengan perintah 'python manage.py runserver'.

* ### Membuat model pada aplikasi main dengan nama Product yang memiliki atribut wajib name, price, dan description :
1. Membuka berkas models.py yang sudah ada pada direktori aplikasi main kemudian diisi dengan kode berikut:
    
    from django.db import models

    class MoodEntry(models.Model):
        mood = models.CharField(max_length=255)
        time = models.DateField(auto_now_add=True)
        feelings = models.TextField()
        mood_intensity = models.IntegerField()

        @property
        def is_mood_strong(self):
            return self.mood_intensity > 5

2. Menjalankan perintah 'python manage.py makemigrations' untuk membuat migrasi model dan perintah 'python manage.py migrate' untuk menerapkan migrasi ke dalam basis data lokal.

* ### Membuat sebuah fungsi pada views.py :
1. Membuka berkasi views.py yang terletak di dalam berkas aplikasi main kemudia menambahkan fungsi show_main di bawah impor yang sudah ada seperti berikut :

    def show_main(request):
    context = {
        'name' : 'Liquid Blush',
        'price': 'Rp350.000,00',
        'description': 'Meet our new Liquid Blush with high quiality ingredients that will blow your mind!',
        'rating' : '4.7/5.0',
    }

    return render(request, "main.html", context)

* ### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py :
1. Membuat berkas urls.py di dalam direktori main yang telah saya buat tadi
2. Mengisi urls.py dengan kode berikut :

    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]

3. Membuka berkas urls.py yang ada di dalam direktori proyek shapping lalu menambahkan fungsi include dan rute Url di dalam variabel urlpatterns seperti berikut :

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]

4. Menjalankan proyek Django dengan perintah 'python manage.py runserver'.

* ### Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat :
1. Mengakses halaman pws (https://pbp.cs.ui.ac.id) kemudian login dengan data diri saya
2. DI home page PWS, saya membuat proyek baru dengan 'Create New Project' lalu membuat project name sebagai shapping.
3. Kembali ke VS Code, pada berkas settings.py di dalam direktori proyek shapping saya mengubah ALLOWED_HOSTS menjadi:

    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "shalya-naura-shapping.pbp.cs.ui.ac.id"]

4. Melakukan perintah git add, commit, dan push untuk menyimpan perubahan ke repositori GitHub yang telah saya buat sebelumnya.
5. Menjalankan perintah yang ada di informasi Project Command setelah saya membuat project baru di PWS di dalam terminal direktori utama shapping saya.
6. Saat melakukan perintah push ke dalam PWS saya, saya memasukkan username dan password yang saya terima saat saya membuat project di PWS.
7. Menjalankan perintah 'git branch -M main' untuk merubah branch utama saya menjadi main
8. Terakhir saya menunggu di site bar situs PWS saya hingga project saya menjadi success.

* ### Membuat sebuah README.md :
1. Membuat berkas baru README.md
2. Masukkan link aplikasi PWS saya yang sudah di-deploy
3. Menjawab pertanyaan yang disediakan


## **Bagan Request Client ke web aplikasi berbasis Django**
![Bagan](images/bagan.jpg)
Pada aplikasi berbasis Django, alur dimulai ketika client mengirimkan request HTTP ke server. Request ini diterima oleh urls.py, yang bertugas memetakan URL ke fungsi tertentu di views.py. Di views.py, logika aplikasi diproses, dan jika diperlukan data dari database, views.py akan berinteraksi dengan models.py untuk mengambil atau memanipulasi data. Setelah data diperoleh, views.py mengirimkan data tersebut ke template (mengubah HTTP ke bentuk halaman HTML) yang akan di-render menjadi halaman web. views.py kemudian akan mengambil data yang diperlukan models.py lalu menampilkannya menggunakan template.



## **Menjelaskan Fungsi git dalam pengembangan perangkat lunak**
Git adalah alat versi kontrol yang digunakan dalam pengembangan perangkat lunak untuk:
1. Melacak Perubahan Kode: Mencatat setiap perubahan yang dilakukan pada kode, memungkinkan pengembang untuk melihat riwayat perubahan.
2. Kolaborasi Tim: Memungkinkan beberapa pengembang bekerja pada proyek yang sama tanpa konflik melalui fitur branching.
3. Branching dan Merging: Pengembang dapat membuat branch untuk fitur baru atau perbaikan, lalu menggabungkannya ke kode utama setelah diuji.
4. Pemulihan Versi: Memungkinkan rollback ke versi kode sebelumnya jika terjadi kesalahan.
5, Review Kode: Kode dapat direview melalui pull request sebelum digabungkan ke branch utama.



## **Mengapa framework Django dijadikaan pemulaan pembelajaran pengembangan perangkat lunak?**
Django dipilih untuk pemula karena:
1. Struktur MVT yang jelas memudahkan pemahaman.
2. Fitur bawaan lengkap (otentikasi, keamanan, manajemen database) mempercepat pengembangan.
3. ORM sederhana mempermudah interaksi dengan database tanpa perlu SQL.
4. Keamanan bawaan melindungi dari ancaman umum seperti CSRF dan SQL injection.
5. Dokumentasi lengkap dan komunitas besar mendukung pembelajaran.

Django memungkinkan pemula memahami konsep dasar pengembangan web dengan cepat dan efektif.



## **Mengapa model pada Django disebut sebagai ORM?**
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena model ini menghubungkan antara objek Python dan tabel dalam database. Dengan ORM, pengembang dapat berinteraksi dengan database menggunakan objek Python alih-alih menulis query SQL langsung.

ORM secara otomatis menerjemahkan operasi seperti Create, Read, Update, Delete (CRUD) ke dalam perintah SQL yang dieksekusi di database, sehingga pengembang hanya perlu bekerja dengan objek Python untuk mengelola data. Ini membuat pengelolaan database lebih sederhana dan lebih aman.



## **Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
Data delivery diperlukan dalam pengimplementasian sebuha platform karena platform modern sering kali mengandalkan transfer data yang efisien, aman, dan tepat waktu untuk menyediakan layanan kepada pengguna. Beberapa alasan mengapa data delivery sengatlah penting :
1. Ketersediaan dan Kecepatan Akses Informasi : Data delivery memastikan pengguna dapat mengakses informasi yang mereka butuhkan dengan cepat dan tepat.
2. Sinkronisasi Data antar Komponen : Data delivery membantu menyinkronkan data di antara komponen-komponen tersebut sehingga sistem bekerja secara konsisten dan terkoordinasi.
3. User Experience yang Lebih Baik : Pengiriman data yang cepat dan handal memastikan pengguna tidak mengalami lag atau kesalahan saat mengakses platform.

Masih ada banyak lagi alasan mengapa memerlukan data delivery dalam pengimplementasian sebuah platform seperti real-time data processing, keamanan dan privasi data, Optimasi kinerja sistem, dan lain sebagainya. Maka dari itu, data delivery menjadi hal yang sangat penting dalam pengoperasian platform modern. Dengan pengiriman data yang tepat dan efisien, platform dapat memberikan layanan yang lebih cepat, lebih aman, dan lebih dapat diandalkan, yang pada akhirnya menignkatkan pengalaman pengguna dan efisiensi operasional.



## **Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**
Menurut saya, JSON lebih baik jika dibandingkan dengan XML. Secara umum, JSON memang lebih disukai dan populer dibandingkan XML, terutama dalam pengembangan aplikasi web modern. Ada beberapa alasan yang dapat mendukung pernyataan saya mengenai popularitas JSON dibandingkan dengan XML :
1. Format yang Lebih Ringkas dan Mudah Dibaca : JSON memiliki format yang lebih sederhana, ringkas, dan mudah dibaca karena JSON menggunakan tanda kurung kurawal "{}" untuk objek dan tanda kurung siku "[]" untuk array. XML, di sisi lain, menggunakan tag pembuka dan penutup "(<tag>...</tag>)", yang cenderung membuat file panjang dan sulit dibaca.
2. Kinerja yang Lebih Baik : Karena JSON lebih ringan dan ringkas dibandingkan XML, pengiriman data JSON melalui jaringan memerlukan lebih sedikit bandwith dan labih cepat.
3. Lebih Mudah Diprodes oleh Banyak Bahasa Pemrograman : JSON lebih mudah diproses oleh banyak bahasa pemrograman modern, seperti Python, Ruby, JavaScript, dan PHP memiliki dukungan asli untuk bekerja dengan JSON.

Berdasarkan alasan-alasan tersebut, menurut saya, JSON lebih baik dalam hal kinerja, kemudahan integrasi, dan kesederhanaan, sehingga lebih cocok untuk aplikasi web dan mobile modern. Meskipun terkadang XML masih perlu digunakan untuk hal-hal tertentu, JSON tetap lebih populer dan nyaman digunakan karena kesederhanaan, efisiensi, dan kemampuannya untuk bekerja lebih baik dengan bahasa pemrograman modern dan arsitektur web.