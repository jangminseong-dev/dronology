import reflex as rx

class DronologyConfig(rx.Config):
    pass

config = DronologyConfig(
    app_name="dronology",
    api_url="nas.minstar.kr:8000"
)