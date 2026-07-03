# forge/tools/file_writer_tool.py

from pathlib import Path


class FileWriterTool:

    def write(self, file):

        path = Path(file.path)

        path.parent.mkdir(

            parents=True,

            exist_ok=True

        )

        with open(

            path,

            "w",

            encoding="utf-8"

        ) as f:

            f.write(

                file.content

            )


    def write_many(

        self,

        files

    ):

        for file in files.values():

            self.write(file)