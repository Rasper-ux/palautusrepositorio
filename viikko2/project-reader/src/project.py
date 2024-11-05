class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies


    def _stringify_dependencies(self, dependencies):
        # Tarkistetaan onko dependencies-lista tyhjä, ja tulostetaan jokainen riippuvuus omalle rivilleen
        return "\n".join(f"- {dep}" for dep in dependencies) if dependencies else "-"

    def _stringify_authors(self):
        # Tarkistetaan, onko authors-lista tyhjä, ja muodostetaan tulostettava merkkijono
        return "\n".join(f"- {author}" for author in self.authors) if self.authors else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors:\n{self._stringify_authors()}"
            f"\n\nDependencies:\n{self._stringify_dependencies(self.dependencies)}"
            f"\n\nDevelopment dependencies:\n{self._stringify_dependencies(self.dev_dependencies)}"
        )
