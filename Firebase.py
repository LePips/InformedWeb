import string
import random
import sys
from os import listdir

import firebase_admin
from firebase_admin import credentials, firestore

from candidates.models import Candidate

class Firebase():
    __instance = None

    def __init__(self):
        if Firebase.__instance != None:
            raise Exception("Firebase is a singleton")
        else:
            Firebase.__instance = self

        cred = credentials.Certificate(getKeyFile())
        self.default_app = firebase_admin.initialize_app(cred)
        db = firestore.client()
        self.candidates_reference = db.collection(u'candidates')
        self.elections_reference = db.collection(u'elections')

    @staticmethod
    def instance():
        """ Static access method. """
        if Firebase.__instance == None:
            Firebase()
        return Firebase.__instance

    def get_candidates(self):
        candidates_ids_ref = self.candidates_reference.get()
        candidates = []
        for ref in candidates_ids_ref:
            candidate = self.get_candidate(ref.id)
            candidates.append(candidate)
        return candidates

    def get_election_ids(self):
        elections = self.elections_reference.get()
        ids = list(map(lambda x: x.id, elections))
        return ids

    def get_candidate(self, id):
        document_ref = self.candidates_reference.document(id)
        document = document_ref.get()
        dict = document_ref.get().to_dict()

        id = document_ref.id
        first = dict["first"]
        last = dict["last"]
        elections = dict.get("elections")
        image_url = dict.get("image_url")

        sections_ref = document_ref.collection(u'sections')
        sections = self.get_sections(sections_ref)

        candidate = Candidate(id=id,
                              first=first,
                              last=last,
                              elections=elections,
                              image_url=image_url,
                              sections=sections)
        return candidate

    def get_election(self, id):
        document_ref = self.elections_reference.document(id).get()
        election = document_ref.to_dict()
        return election

    def set_candidate(self, candidate):
        document_ref = self.candidates_reference.document(candidate.id)
        document_ref.set({
            u'first': candidate.first,
            u'last': candidate.last,
            u'elections': candidate.elections,
            u'image_url': candidate.image_url
        })

        sections_ref = document_ref.collection(u'sections')
        for section in candidate.sections:
            sections_ref.document(section.title).set({
                u'title': section.title,
                u'content': section.content
            })

    def get_sections(self, sections_ref):
        sections = []
        for section in sections_ref.get():
            sections.append(section.to_dict())

        return sections

    # def getUsersNames(self):
    #     ids = self.getUserIds()
    #     names = []
    #     for id in ids:
    #         document_ref = self.db.collection(u'users').document(u'{}'.format(id)).get()
    #         name = document_ref.to_dict()
    #         names.append(name)
    #     return names
    #
    # def createUser(self):
    #     collection_ref = self.db.collection(u'users').document(id_generator())
    #     collection_ref.set({
    #         u'first': "test",
    #         u'last': id_generator(),
    #         u'born': 2012
    #     })

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def getKeyFile():
    jsonFiles = []

    for f in listdir("./"):
        if f.endswith('.json'):
            jsonFiles.append(f)

    if len(jsonFiles) == 0:
        raise Exception("No Firebase key available")
    elif len(jsonFiles) > 1:
        raise Exception("Multiple json files in directory")

    return "./" + jsonFiles[0]
