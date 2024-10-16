from nicegui import ui
import tinytuya

lamp = tinytuya.BulbDevice(
    "bf55cfaca2dd52af980iov",
    "192.168.0.195",
    "?s1W`~jvobw8#vr_",
    version=3.3
)


def main():
    ui.label("Smart Pears 🍐").classes("text-3xl text-bold")
    ui.button("Turn on", on_click=turn_on)
    ui.button("Turn off", on_click=turn_off)
    with ui.button(icon="colorize"):
        ui.color_picker(on_pick=change_color)


def turn_on():
    lamp.turn_on()
    ui.notify("Turned on")


def turn_off():
    lamp.turn_off()
    ui.notify("Turned off")


def change_color(e):
    print(e.color)
    c = e.color[1:]
    r = int(c[0:2], 16)
    g = int(c[2:4], 16)
    b = int(c[4:6], 16)
    lamp.set_colour(r, g, b)
    ui.notify(f"Color changed: {r}, {g}, {b}")


if __name__ in {"__main__", "__mp_main__"}:
    main()
    ui.run(title="Smart Pears 🍐", favicon='🍐')
