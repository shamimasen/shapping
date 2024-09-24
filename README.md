**Nama : Shalya Naura Lionita**
**NPM : 2306245535**
**Kelas : B**
>**Shapping :** http://shalya-naura-shapping.pbp.cs.ui.ac.id/

## **Penjelasan Tugas**
<details>
<summary> <b> Tugas 2 : Implementasi Model-View-Template (MVT) pada Django <b> </summary>  


## **Implementasi Checklist Tugas**
* ### Membuat proyek Django baru:
1. Pertama saya membuat direktori baru dengan nama 'shapping' kemudian mengaktifkan virtual environmentnya.
2. Membuat berkas baru dengan nama requirement.txt untuk menyimpan dependencies yang diperlukan, yaitu :
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```

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

```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

3. Membuka berkas urls.py yang ada di dalam direktori proyek shapping lalu menambahkan fungsi include dan rute Url di dalam variabel urlpatterns seperti berikut :

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

4. Menjalankan proyek Django dengan perintah 'python manage.py runserver'.  


* ### Membuat model pada aplikasi main dengan nama Product yang memiliki atribut wajib name, price, dan description :
1. Membuka berkas models.py yang sudah ada pada direktori aplikasi main kemudian diisi dengan kode berikut:

```
from django.db import models

class MoodEntry(models.Model):
    mood = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5
```

2. Menjalankan perintah 'python manage.py makemigrations' untuk membuat migrasi model dan perintah 'python manage.py migrate' untuk menerapkan migrasi ke dalam basis data lokal.  


* ### Membuat sebuah fungsi pada views.py :
1. Membuka berkasi views.py yang terletak di dalam berkas aplikasi main kemudia menambahkan fungsi show_main di bawah impor yang sudah ada seperti berikut :

```
def show_main(request):
context = {
    'name' : 'Liquid Blush',
    'price': 'Rp350.000,00',
    'description': 'Meet our new Liquid Blush with high quiality ingredients that will blow your mind!',
    'rating' : '4.7/5.0',
}

return render(request, "main.html", context)  
```  


* ### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py :
1. Membuat berkas urls.py di dalam direktori main yang telah saya buat tadi
2. Mengisi urls.py dengan kode berikut :

```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

3. Membuka berkas urls.py yang ada di dalam direktori proyek shapping lalu menambahkan fungsi include dan rute Url di dalam variabel 
```
urlpatterns seperti berikut :

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
```

4. Menjalankan proyek Django dengan perintah 'python manage.py runserver'.  


* ### Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat :
1. Mengakses halaman pws (https://pbp.cs.ui.ac.id) kemudian login dengan data diri saya
2. DI home page PWS, saya membuat proyek baru dengan 'Create New Project' lalu membuat project name sebagai shapping.
3. Kembali ke VS Code, pada berkas settings.py di dalam direktori proyek shapping saya mengubah ALLOWED_HOSTS menjadi:

```
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "shalya-naura-shapping.pbp.cs.ui.ac.id"]
```

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

</details>

<details>
<summary> <b> Tugas 3 : Implementasi Form dan Data Delivery pada Django <b> </summary>

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

  

## **Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**
Method is_valid() pada form Django memiliki fungsi untuk memvalidasi data yang dikirimkan ke form, baik dari request (biasanya POST) maupun dari sumber lainnya. Method ini sangat penting karena memastikan bahwa data yang di-input oleh pengguna sudah sesuai dengan aturan dan batasan yang ditentukan pada form sebelum data tersebut digunakan atau disimpan ke database. Berikut ini beberapa fungsi "is_valid()" dalam Django :
1. Memeriksa Validasi Data : Method "is_valid()" akan memeriksa apakah data yang dikirimkan melalui form sesuai dengan semua aturan validasi yang didefinisikan di dalam form.
2. Mengisi Atribut "cleaned_data" : Jika form valid, method "is_valid()" akan mengisi atribut "cleaned_data," yang berisi data yang telah divalidasi dan difromat ulang sesuai dengan aturan yang telah ditetapkan.
3. Mengumpulkan Error Jika Tidak Valid : Jika data form tidak valid, method "is_valid()" akan mengisi atribut "errors," yang berisi detail kesalahan validasi yang terjadi.  


Berikut beberapa alasan mengapa kita membutuhkan "is_valid()" :
1. Mencegah Data yang Tidak Valid Untuk Masuk ke Database : Tanpa validasi, data yang tidak sesuai atau salah dapat masuk ke dalam databse, yang bisa menyebablan masalah seperti korupsi data, error aplikasi, atau hasil yang tidak diinginkan.
2. Keamanan Aplikasi : Dengan menggunakan validasi form, kita dapat melindungi aplikasi dari input yang berbahaya, seperti serangan, karena data yang tidak sesuai tidak akan diproses atau dimasukkan ke dalam sistem.
3. Memberikan Feedback kepada Pengguna : "is_valid()" membantu memberikan umpan balik langsung kepada pengguna jika mereka mengisi form dengan data yang tidak valid.  

Method "is_valid()" adalah komponen penting dalam sistem form Django yang membantu memastikan bahwa data yang dikirim oleh pengguna sesuai dengan aturan yang ditenntukan. Ini membantu melindungi aplikasi dari kesalahan input, menjaga integritas data, meningkatkan keamanan, dan memberikan umpan balik yang baik kepada pengguna.
  

## **csrf_token pada Django
CSRF token (Cross-Site Request Forgery token) adalah bagian penting dari keamanan dalam aplikasi Django, terutama saat menangani form yang mengirimkan data melalui metode POST. Ini adalah mekanisme yang melindungi aplikasi dari serangan CSRF, yang merupakan salah satu jenis serangan keamanan pada aplikasi web.  
  

* ### Mengapa Kita Membutuhkan "csrf_token" dalam Form Django?
1. Melindungi dari Serangan CSRF : Serangan CSRF terjadi ketika penyerang mencoba memanfaatkan sesi aktif pengguna untuk mengirimkan permintaan palsu ke server tanpa sepengetahuan pengguna. Jika aplikasi tidak dilindungi oleh CSRF token, penyerang dapat memalsukan permintaan atas nama pengguna yang sudah login dan memiliki sesi aktif.
2. Meningkatkan Keamanan Aplikasi : CSRF token memastikan bahwa setiap permintaan POST yang dikirimkan dari form web diverifikasi terlebih dahulu. Server memeriksa token pada setiap permintaan POST untuk memastikan bahwa itu berasal dari halaman atau situs yang sah, bukan dari sumber eksternal atau skrip jahat. Tanpa csrf_token, permintaan berbahaya bisa diterima dan diproses oleh server, yang bisa menimbulkan risiko keamanan serius.  

* ### Apa yang Terjaid Jika Tidak Menambahkan "csrf_token" pada Form?
1. Serangan CSEF dapat terjadi : Penyerang dapat mengeksploitasi sesi login aktif pengguna di aplikasi web. Dengan cara membuat halaman web yang berbahaya, penyerang bisa memaksa browser pengguna untuk melakukan permintaan POST ke server aplikasi tanpa disadari oleh pengguna.
2. Form Tidak Akan Diproses oleh Django : Secara default, Django akan menolak setiap permintaan POST tanpa CSRF token, dan menghasilkan kesalahan 403 Forbidden. Django memiliki mekanisme perlindungan otomatis yang akan memeriksa apakah setiap form POST mengandung token. Jika token tidak ada atau tidak valid, permintaan akan diblokir.  
  

* ### Bagaimana Penyerang Bisa Memanfaatkan Ketiadaan "csrf_token"?
Jika aplikasi web tidak menggunakan csrf_token, penyerang bisa melakukan serangan CSRF dengan langkah-langkah berikut :
1. Mengelabui Pengguna untuk Mengirim Permintaan Berbahaya : Penyerang dapat membuat situs web palsu atau menyisipkan link berbahaya di email, media sosial, atau pesan lainnya. Ketika pengguna yang login ke aplikasi membuka situs palsu atau mengklik link tersebut, situs tersebut akan mengirimkan permintaan POST ke server aplikasi menggunakan sesi pengguna yang sah.
2. Manipulasi Form di Latar Belakang : Dengan ketiadaan "csrf_token", penyerang dapat menyisipkan permintaan POST di latar belakang (melalui skrip tersembunyi) yang dikirim dari situs eksternal ke server aplikasi. Permintaan ini menggunakan sesi autentikasi pengguna yang aktif tanpa mereka sadari.  

"csrf_token" adalah komponen penting dalam keamanan form di Django yang melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Tanpa CSRF token, penyerang bisa memanfaatkan sesi pengguna yang sah untuk melakukan aksi tanpa izin, seperti mengubah data atau melakukan transaksi atas nama pengguna. Django menyediakan perlindungan bawaan ini agar aplikasi web aman dari serangan semacam ini.
  
    

## **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).  
  

* ### Membuat input form untuk menambahkan objek model pada app sebelumnya.
1. Membuat berkas baru di dalam direktori main dengan nama "forms.py" yang dapat menerima entry baru.
2. Menambahkan beberapa import berikut di dalam berkas views.py yang ada dalam direktori main :  

from django.shortcuts import render, redirect
from main.forms import EntryForm
from main.models import Entry

3. Membuat fungsi baru dengan nama create_entry yang mempunyai parameter request sehingga dapat menghasilkan form yang bisa menambahkan data entry secara otomatis ketika data di-submit dari form :

```
def create_entry(request):
    form = EntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_entry.html", context)
```

4. Mengubah fungsi show_main dalam berkas views.py menjadi seperti :

```
def show_main(request):
    entries = Entry.objects.all()

    context = {
        'nama' : 'Shalya Naura Lionita',
        'kelas' : 'PBP B',
        'entries': entries
    }

    return render(request, "main.html", context)
```

5. Mengimport fungsi create_entry pada berkas urls.py :

```
from main.views import show_main, create_entry
```

6. Menambahkan path URL ke dalam variabel urlpatterns pada urls.py untuk mengakses fungsi yang sudah di import sebelumnya :

```
urlpatterns = [
    ...
    path('create-entry', create_entry, name='create_entry'),
]
```

7. Membuat berkas HTML baru pada direktori main/templates dan diisi sebagai berikut :

```
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Mood Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Mood Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```

8. Menambahkan kode {% block content %} pada berkas main.html :

```
{% if not mood_entries %}
<p>Belum ada data untuk produk yang dijual</p>
{% else %}
<table>
  <tr>
    <th>Product Name</th>
    <th>Price</th>
    <th>Description</th>
    <th>Rating</th>
  </tr>

  {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini 
  {% endcomment %} 
  {% for mood_entry in mood_entries %}
  <tr>
    <td>{{mood_entry.product_name}}</td>
    <td>{{mood_entry.price}}</td>
    <td>{{mood_entry.description}}</td>
    <td>{{mood_entry.rating}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_mood_entry' %}">
  <button>Add New Product</button>
</a>
{% endblock content %}
```

9. Mengecek keberhasilan kode dengan menjalankan perintah "python manage.py runserver" dan membuka link http://localhost:8000/  

  

* ### Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
1. Menambahkan import pada berkas views.py pada direktori main seperti berikut :
from django.http import HttpResponse
from django.core import serializers

2. Membuat fungsi baru, yaitu show_xml, show_json, show_xml_by_id, dan show_json_by_id yang me-return fungsi berupa HttpResponse :

```
def show_xml(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")  
```


* ### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
1. Menambahkan import untuk fungsi yang telah dibuat di views.py ke dalam urls.py :

from main.views import show_main, create_mood_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

2. Menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang telah di import :

```
path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
```

3. Menjalankan proyek Django dengan perintah "python manage.py runserver" dan membuka 4 link, yaitu :
http://localhost:8000/xml/  
http://localhost:8000/json/  
http://localhost:8000/xml/[id]/  
http://localhost:8000/json/[id]/  

  
  
* ### Menjawab beberapa pertanyaan berikut pada README.md pada root folder.
1. Menjelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform.
2. Menjelaskan menurut saya yang lebih baik antara XML dan JSON beserta alasan mengapa JSON lebih populer dibandingkan XML.
3. Menjelaskan fungsi dari method "is_valis()" pada form di Django dan mengapa kita membutuhkannya.
4. Menjelaskan mengapa kita membutuhkan "csrf_token" saat membuat form di Django,  apa yang dapat terjadi jika tidak menambahkannya, serta bagaimana hal tersebut dapat dimanfaatkan oleh penyerang.
5. Menjelaskan bagaimana saya mengimplementasikan checklist dari Tugas 3 secara step-by-step di dalam README.md
6. Mengakses keempat URL di poin 2 menggunakan Postman, kemudian screenshot hasil akses, lalu mengunggah foto ke dalam berkas README.md
7. Melakukan add-commit-push ke GitHub.  

  
  
## **Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
![XML](images/xml.jpg)
![JSON](images/json.jpg)
![XML](images/xmlbyid.jpg)
![XML](images/jsonbyid.jpg)  

</details>

<details>
<summary> <b> Tugas 4 : Implementasi Autentikasi, Session, dan Cookies pada Django <b> </summary>  


## ** Apa Perbedaan Antara HttpResponseRedirect() dan redirect()?
1. **HttpResponseRedirect()** adalah kelas Django yang secara eksplisit mengembalikan objek respon yang diarahkan ke URL yang diberikan.
2. **redirect()** adalah shortcut yang digunakan untuk menghasilkan **HttpResponseRedirect()**. **redirect()** lebih sering digunakan karena lebih ringkas dan fleksibel, serta memungkinkan menerima objek model, nama view, atau URL secara langsung.  
  

## ** Jelaskan cara kerja penghubungan model Product dengan User!
Hubungan antara model Product dan User dapat dibuat menggunakan ForeignKey pada model Product yang merujuk ke model User. Dengan cara ini, setiap produk akan terkait dengan pengguna tertentu, sehingga pengguna yang login dapat mengelola produk miliknya sendiri.
```
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
```

## ** Apa perbedaan antara authentication dan authorization, dan apa yang dilakukan saat penggunna login?
1. Authentication adalah proses verifikasi identitas pengguna, seperti memastikan username dan password yang diberikan benar.
2. Authorization adalah proses yang terjadi setelah authentication, di mana sistem menentukan apa yang diizinkan atau tidak diizinkan dilakukan oleh pengguna yang sudah di-autentikasi.  
  

Saat pengguna login di Django, sistem melakukan authentication terlebih dahulu, dan jika berhasil, informasi pengguna disimpan dalam session. Django kemudian menggunakan session ini untuk mengelola otorisasi pengguna.

## ** Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login melalui session. Ketika pengguna login, Django membuat session ID yang disimpan sebagai cookie di browser. Setiap kali pengguna melakukan request, session ID ini dikirim kembali ke server, yang kemudian mengidentifikasi pengguna.  
  

Cookies juga digunakan untuk menyimpan data sementara seperti preferensi pengguna. Namun, tidak semua cookies aman karena mereka bisa diekspos jika tidak dikonfigurasi dengan baik. Secure cookies dan HttpOnly cookies lebih aman karena hanya bisa diakses melalui HTTPS atau tidak bisa diakses oleh JavaScript.  
  
  
## ** Jelaskan bagaimana cara mengimplementasikan checklist di atas secara step-by-step:  

* ### Mengimplementasikan fungsi registrasi, login, dan logout
**REGISTRASI**
1. Membuka file 'views.py' pada direktori main kemudian menambahkan import untuk 'UseCreatuinForm' dan 'massages' dari Django :
```
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```

2. Membuat fungsi view untuk register dengan menggunakan 'UserCreationForm' :
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

3. Menambahkan URL path di 'urls.py' untuk halaman registrasinya :
```
    path('register/', register, name='register'),
```  
  

**LOGIN**
1. Mmebuka file 'views.py' pada subdirektori main kemudian menambahkan import untuk menggunakan autentikasi bawaan Django :
```
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
```

2. Membuat fungsi 'login_user' yang akan menangani proses login :
```
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')  # Redirect ke halaman utama setelah login
    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'login.html', context)
```

3. Membuat file 'login.html' pada direktori main/templates kemudia mengisi dengan template login :
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}

  Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
</div>
{% endblock content %}
```

4. Menambahkan URL untuk halaman login di 'urls.py' :
```
from main.views import login_user

urlpatterns = [
    ...
    path('login/', login_user, name='login'),
]
```  
  
**LOGOUT**
1. Di dalam file 'views.py' pada subdirektori main, menambahkan lagi import untuk fungsi logout dari Django :
```
from django.contrib.auth import logout
```

2. Membuat fungsi 'logout_user' yang akan menangani proses logout :
```
def logout_user(request):
    logout(request)
    return redirect('main:login')  # Setelah logout, pengguna diarahkan ke halaman login
```

3. Menambahkan URL untuk logout di 'urls.py' :
```
from main.views import logout_user

urlpatterns = [
    ...
    path('logout/', logout_user, name='logout'),
]
```

4. Menambahkan tombol logout di 'main.html' untuk memungkinkan pengguna keluar dari aplikasi :
```
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```  
  

* ### Membuat dua akun pengguna dengan tiga dummy data



* ### Menghubungkan model Product dengan User
Untuk menghubungkan model Product dengan User, tambahkan field ForeignKey pada model Product:
```
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
```  

Dengan cara ini, setiap produk akan terkait dengan pengguna tertentu. on_delete=models.CASCADE memastikan bahwa ketika akun pengguna dihapus, semua produk yang dimiliki oleh pengguna tersebut juga akan terhapus.  
  

* ### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
1. Membuka file 'views.py' yang ada di subdirektori main kemudian menambahkan import :
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```  
2. Menambahkan cookie yang bernama last_login di dalam fungsi login_user :
```
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```  
3. Menambahkan potongan kode 'last_login' pada fungsi show_main :
```
'last_login': request.COOKIES['last_login'],
```  

4. Mengubah fungsi logout_user menjadi :
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```  

5. Menambahkan potongan kode ke dalam berkas 'main.html' untuk menampilkan last login :
```
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```  
  

## ** Menjawab pertanyaan README
Setelah semua fitur di atas diimplementasikan, perbarui file README.md untuk menjelaskan langkah-langkah implementasi tersebut dan jawaban dari beberapa pertanyaan yang diberikan.

</details>