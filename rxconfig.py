import reflex as rx

class DronologyConfig(rx.Config):
    pass

config = DronologyConfig(
    app_name="dronology",
    api_url="http://dronology.kr:8000"
)