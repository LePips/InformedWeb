from django.db import models

# Create your models here.
class Election():
    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.title = kwargs["title"]
        self.category = kwargs["category"]
        self.cover_image_url = kwargs.get("cover_image_url")
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
