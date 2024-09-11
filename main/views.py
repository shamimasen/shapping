from django.shortcuts import render

def show_main(request):
    context = {
        'nama' : 'Shalya Naura Lionita',
        'kelas' : 'PBP B',
        'name' : 'Liquid Blush',
        'price': 'Rp350.000,00',
        'description': 'Meet our new Liquid Blush with high quiality ingredients that will blow your mind!',
        'rating' : '4.7/5.0',
    }

    return render(request, "main.html", context)