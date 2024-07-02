from star_ray_pygame import View, WindowConfiguration
from star_ray_xml import XMLAmbient
from star_ray.event import (
    WindowCloseEvent,
    MouseButtonEvent,
    WindowFocusEvent,
    WindowMoveEvent,
    WindowResizeEvent,
)
from star_ray import Environment

from star_ray_pygame.avatar import Avatar

WIDTH, HEIGHT = 640, 480
NAMESPACES = {"svg": "http://www.w3.org/2000/svg"}

SVG = f"""
<svg x="100" y="100" width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <svg x="50" y="50" width="100" height="100">
        <rect id="myrect" x="0" y="0" width="100" height="200" fill="red"/>
        <circle id="mycircle" cx="50" cy="50" r="40" fill="yellow" stroke="black" stroke-width="2"/>
  </svg>  

  <g x="200" y="200" width="100" height="100">
        <rect id="myrect" x="0" y="0" width="100" height="200" fill="red"/>
        <circle id="mycircle" cx="50" cy="50" r="40" fill="yellow" stroke="black" stroke-width="2"/>
  </g>
</svg>"""

SVG = f"""<svg x="0" y="0" width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
    <rect id="myrect" x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="yellow"/>
    <rect id="myrect" x="-100" y="0" width="{WIDTH}" height="{HEIGHT}" fill="green"/>

    <rect id="myrect" x="0" y="0" width="100" height="100" fill="blue"/>
    <circle id="mycircle" cx="50" cy="50" r="40" fill="yellow" stroke="black" stroke-width="2"/>
</svg>"""

window_config = WindowConfiguration(
    width=WIDTH, height=HEIGHT, title="svg test", resizable=True, fullscreen=False
)

avatar = Avatar([], [], window_config=window_config)
ambient = XMLAmbient([avatar], xml=SVG, namespaces=NAMESPACES)
environment = Environment(ambient)
environment.run()

# running = True
# while running:
#     events = view.get_events()
#     # time.sleep(0.1)
#     for event in events:
#         if isinstance(event, WindowCloseEvent):
#             running = False
#         elif isinstance(event, MouseButtonEvent):
#             print(event)
#         elif isinstance(event, (WindowFocusEvent, WindowMoveEvent, WindowResizeEvent)):
#             print("window event:", event)
#             view.render()
#     view.render()