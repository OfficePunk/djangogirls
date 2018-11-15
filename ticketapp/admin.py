from django.contrib import admin
from .models import Cinema, FilmRoom, Ticket, Room, Place, Film, PlaceRoom

admin.site.register(Cinema)
admin.site.register(Film)
admin.site.register(Ticket)
admin.site.register(Room)
admin.site.register(Place)
admin.site.register(FilmRoom)
admin.site.register(PlaceRoom)