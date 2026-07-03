# forge/models/architecture.py

from dataclasses import dataclass

from dataclasses import field

from datetime import datetime

from typing import List

from models.module import Module


@dataclass

class Architecture:


    frontend: str


    backend: str


    database: str


    authentication: str


    cache: str


    modules: List[Module]


    deployment: str


    created_at: datetime = field(

        default_factory=datetime.now

    )


    def show(self):


        print()


        print("="*50)


        print(

            "SYSTEM ARCHITECTURE"

        )


        print("="*50)


        print(

            "\nFrontend:"

        )


        print(

            self.frontend

        )


        print(

            "\nBackend:"

        )


        print(

            self.backend

        )


        print(

            "\nDatabase:"

        )


        print(

            self.database

        )


        print(

            "\nAuthentication:"

        )


        print(

            self.authentication

        )


        print(

            "\nCache:"

        )


        print(

            self.cache

        )


        print(

            "\nModules:"

        )


        for module in self.modules:


            print()


            print(

                f"- {module.name}"

            )


            print(

                f"  {module.description}"

            )


        print(

            "\nDeployment:"

        )


        print(

            self.deployment

        )