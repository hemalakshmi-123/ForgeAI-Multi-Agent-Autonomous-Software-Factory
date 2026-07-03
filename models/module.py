# forge/models/module.py

from dataclasses import dataclass


@dataclass
class Module:

    name: str

    description: str


    def show(self):

        print()

        print(

            f"Module: {self.name}"

        )

        print(

            f"Description: "

            f"{self.description}"

        )