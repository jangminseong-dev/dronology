import reflex as api
from .header import navbar

class State(api.State):
    pass


def index():
    return api.fragment(
        api.vstack(
            navbar(),
            api.heading("홈페이지 준비중입니다.", padding="30vh 10px 10px 10px"),
            api.text("이용에 불편을 드려 죄송합니다. 빠른 시일내에 홈페이지를 준비할 수 있도록 하겠습니다.")
        )
    )


# Add state and page to the app.
app = api.App()
app.add_page(index)
app.compile()
