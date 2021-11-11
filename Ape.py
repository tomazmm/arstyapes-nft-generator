import json
import os
import sys
from PIL import Image


class Ape:
    RENDER_ORDER = ["background", "body", "outfit",
                    "head", "eye", "jewelry",
                    "mouth attributes", "accessories", "headwear"]

    def __init__(self, traits: dict):
        self._id = None
        self._traits = traits

    def render(self, _id):
        self._id = _id
        ape = None
        for trait in self.RENDER_ORDER:
            try:
                trait_img = Image.open(f'assets/{trait}/{self._traits[trait]}.png').convert('RGBA')
                if ape is None:
                    ape = trait_img
                else:
                    ape = Image.alpha_composite(ape, trait_img)
            except KeyError as e:
                continue

        rgb = ape.convert('RGBA')
        file_name = str("artsyape-" + str(_id)) + '.png'

        if not os.path.exists("generated"):
            os.mkdir('generated')
        rgb.save("./generated/" + file_name, optimize=True, quality=20)

        self._generate_json_metadata()

        # Count how many apes generated
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} ape generated.".format(_id))
        sys.stdout.flush()

    def _generate_json_metadata(self):
        if not os.path.exists("generated/metadata"):
            os.mkdir('generated/metadata')

        data = {
            "id": self._id,
            "traits": self._traits
        }
        with open(f"./generated/metadata/artsyape-{str(self._id)}.json", "w") as f:
            json.dump(data, f, indent=4)




class ZombieApe(Ape):
    RENDER_ORDER = ["background", "body", "outfit",
                    "head", "jewelry", "mouth attributes",
                    "accessories", "headwear"]


class AstronautApe(Ape):
    RENDER_ORDER = ["background", "body", "head",
                    "eye", "accessories", "outfit"]


class SquidgameApe(Ape):
    RENDER_ORDER = ["background", "outfit"]


class GasmaskApe(Ape):
    RENDER_ORDER = ["background", "body", "outfit", "head", "accessories", "headwear"]
