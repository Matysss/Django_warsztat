from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from django.views import View
from django.http import HttpResponse
from .models import ModelHall



class ShowAllRooms(View):
    def get(self, request, *args, **kwargs):
        rooms = ModelHall.objects.all()
        return render(request, 'show_all_rooms.html', context={"rooms": rooms})

    def post(self, request, *args, **kwargs):
        back = request.POST.get('back_button')
        if back == "Back":
            return HttpResponseRedirect('/')


class ReservationViews(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'reservation_view.html')

    def post(self, request, *args, **kwargs):
        add_room_view = request.POST.get('add_room')
        show_all_rooms = request.POST.get('show_all_rooms')
        if show_all_rooms == "Show all rooms":
            return HttpResponseRedirect('show_all_rooms/')
        elif add_room_view == "Add Room":
            return HttpResponseRedirect('add_room_view/')


class AddNewRoomView(View):
    def get(self, request):
        return render(request, 'add_room.html')

    def post(self, request):
        back_view = request.POST.get('page_button')
        name_room = request.POST.get('title_room')
        volume = request.POST.get('volume_room')
        available_projector = request.POST.get('avilable')
        volume_room = int(volume) if volume else 0
        print(available_projector)
        if back_view == "Back":
            return redirect("reservation-views")
        elif back_view == "Create Room":
            if not name_room:
                return render(request, "add_room.html", context={"error": "Nie podano nazwy sali"})
            if volume_room <= 0:
                return render(request, 'add_room.html', context={"error": "Sala nie moze miec 0 miejsc"})
            if ModelHall.objects.filter(name_room=name_room).exists():
                return render(request, 'add_room.html', context={"error": "Sala juz istnieje"})
            else:
                ModelHall.objects.create(
                    name_room=name_room,
                    capacity_room=volume_room,
                    projector_available=bool(available_projector),
                )
                return render(request, 'add_room.html', context={'message': "dodano sale"})


class DeleteRoomView(View):
    def get(self, request, *args, **kwargs):
        pass
        return render(request, 'reservation_view.html')

    def post(self, request, *args, **kwargs):
        pass
