from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        printattava_materiaali = toml.loads(content)
        print(content)

        name = printattava_materiaali['tool']['poetry']['name']
        description = printattava_materiaali['tool']['poetry']['description']
        dependencies = list(printattava_materiaali['tool']['poetry']['dependencies'].keys())
        development_dependencies = list(printattava_materiaali['tool']['poetry'].get(['dev-dependencies'], {}).keys())
        license = printattava_materiaali['tool']['poetry'].get('license', '')
        authors = printattava_materiaali['tool']['poetry'].get('authors', [])

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, development_dependencies, license, authors)
