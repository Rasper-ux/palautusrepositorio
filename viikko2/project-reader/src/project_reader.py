from urllib import request
from project import Project
import toml



class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        data = toml.loads(content)

        # Hakee projektin tiedot TOML-tiedoston rakenteesta
        name = data.get("tool", {}).get("poetry", {}).get("name", "Unknown")
        description = data.get("tool", {}).get("poetry", {}).get("description", "No description provided")
        license = data.get("tool", {}).get("poetry", {}).get("license", "No license specified")
        authors = data.get("tool", {}).get("poetry", {}).get("authors", [])

        # Hakee riippuvuudet ja kehitysaikaiset riippuvuudet
        dependencies = list(data.get("tool", {}).get("poetry", {}).get("dependencies", {}).keys())
        dev_dependencies = list(data.get("tool", {}).get("poetry", {}).get("group", {}).get("dev", {}).get("dependencies", {}).keys())

        # Luo ja palauttaa Project-olion
        return Project(name, description, license, authors, dependencies, dev_dependencies)