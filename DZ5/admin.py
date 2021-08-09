from django.contrib import admin
from models import (
    Row,
    RowSession,
    Player,
    PersonalFrame,
    PersonalThrow
)

class PersonalThrowInLine(admin.TabularInline):
    model = PersonalThrow


class PersonalFrameInLine(admin.TabularInline):
    model = PersonalFrame


class PlayerInLine(admin.TabularInline):
    model = Player


class RowSessionInLine(admin.TabularInline):
    model = RowSession


@admin.register(Row)
class RowAdmin(admin.ModelAdmin):
    inlines = [
        RowSessionInLine
    ]


@admin.register(RowSession)
class RowSessionAdmin(admin.ModelAdmin):
    inlines = [
        PlayerInLine
    ]

    readonly_fields = [
        "display_username"
    ]

    list_display = [
        "display_username",
        "date"
    ]


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    inlines = [
        PersonalFrameInLine
    ]


@admin.register(PersonalFrame)
class PersonalFrameAdmin(admin.ModelAdmin):
    inlines = [
        PersonalThrowInLine
    ]
    readonly_fields = ["frame_sum"]

    fields = [
        "name",
        "frame_sum"
    ]

    list_display = [
        "name",
        "frame_sum"
    ]



@admin.register(PersonalThrow)
class PersonalThrowAdmin(admin.ModelAdmin):
    pass
