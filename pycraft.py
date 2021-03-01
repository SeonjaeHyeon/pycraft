from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=load_texture('assets/skybox.jpg'),
            scale=500,
            double_sided=True
        )


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), init=True):
        rand = False if init else random.random() < 0.5
        rand2 = random.randint(0, 1)

        block_list = ['stone.png', 'bricks.png']

        super().__init__(
            parent=scene,
            position=position,
            model=('assets/stone' if rand else 'assets/block'),
            origin_y=.5,
            texture=load_texture((f'assets/{block_list[rand2]}' if rand else 'assets/grass_block')),
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            scale=.5,
            highlight_color=color.white
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                destroy(self)

            if key == 'right mouse down':
                Voxel(position=self.position + mouse.normal, init=False)


Sky()

for z in range(30):
    for x in range(30):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()
app.run()
