from rest_framework import serializers

from candidates.models import Candidate
from elections.models import Election

class SectionField(serializers.RelatedField):
    def to_representation(self, value):
        return { value.title: value.content }
        # return '%s: %s' % (value.title, value.content)

class CandidateSerializer(serializers.ModelSerializer):
    sections = SectionField(many=True, read_only=True)

    class Meta:
        model = Candidate
        fields = ('first', 'last', 'id', 'cover_image_url',
                  'image_urls', 'type', 'last_edited',
                  'elections', 'sections')

class ElectionSerializer(serializers.ModelSerializer):
    sections = SectionField(many=True, read_only=True)

    class Meta:
        model = Election
        fields = ('title', 'id', 'cover_image_url', 'image_urls', 'date',
                  'type', 'last_edited', 'candidates', 'sections')
