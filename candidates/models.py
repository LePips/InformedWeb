from django.db import models


class Candidate():
    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.first = kwargs["first"]
        self.last = kwargs["last"]
        self.elections = kwargs.get("elections")
        self.image_url = kwargs.get("image_url")
        self.sections = []

        sections_dict = kwargs.get("sections")
        if sections_dict is not None:
            for section_dict in sections_dict:
                section = Section(section_dict)
                self.sections.append(section)

class Section():
    def __init__(self, section_dict):
        self.title = section_dict["title"]
        self.content = section_dict["content"]
