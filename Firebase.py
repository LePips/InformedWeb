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
        self.candidate_cache = {}
        self.election_cache = {}

    @staticmethod
    def instance():
        """ Static access method. """
        if Firebase.__instance == None:
            Firebase()
        return Firebase.__instance

    def get_candidate_ids(self):
        candidates = self.candidates_reference.get()
        ids = list(map(lambda x: x.id, candidates))
        return ids

    def get_election_ids(self):
        elections = self.elections_reference.get()
        ids = list(map(lambda x: x.id, elections))
        return ids

    def get_candidate(self, id):
        if id in self.candidate_cache:
            return self.candidate_cache[id]
        else:
            document_ref = self.candidates_reference.document(id).get()
            candidate_dict = document_ref.to_dict()
            first = candidate_dict["first"]
            last = candidate_dict["last"]
            id = document_ref.id
            candidate = Candidate(first, last, id)
            self.candidate_cache[id] = candidate
            return candidate

    def get_election(self, id):
        if id in self.election_cache:
            return self.election_cache[id]
        else:
            document_ref = self.elections_reference.document(id).get()
            election = document_ref.to_dict()
            self.election_cache[id] = election
            return election

    def set_candidate(self, candidate):
        document_ref = self.candidates_reference.document(candidate.id)
        document_ref.set({
            u'first': candidate.first,
            u'last': candidate.last,
            u'elections': []
        })
        self.candidate_cache[candidate.id] = candidate


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
        raise Exception("More Firebase key available")
    elif len(jsonFiles) > 1:
        raise Exception("Multiple json files in directory")

    return "./" + jsonFiles[0]
