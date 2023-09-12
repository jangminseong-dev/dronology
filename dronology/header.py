import reflex as api

def navbar():
    return api.box(
        api.hstack(
            api.image(src="/Typo.png", w="250px", padding="5px 5px 5px 50px"),
        ),
        position="fixed",
        bg="rgba(255,255,255, 0.9)",
        backdrop_filter="blur(10px)",
        padding_y=["0.8em", "0.8em", "0.5em"],
        border_bottom="1px solid #F4F3F6",
        width="100%",
    )