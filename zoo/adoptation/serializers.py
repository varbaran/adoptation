from .models import Animal,Adopter, Dog, Cat
from rest_framework import serializers


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    adopted = serializers.SerializerMethodField('get_adopted')
    adopter = serializers.PrimaryKeyRelatedField(queryset=Adopter.objects.all())
    type = serializers.SerializerMethodField('get_type')

    # def get_fields(self):
    #     result = super().get_fields()
    #     # Rename `type_` to `type`
    #     type_ = result.pop('type_')
    #     result['type'] = type_
    #     return result

    def get_adopted(self, animal):
        return animal.adopter != None

    def get_type(self,animal):
        if isinstance(animal, Dog):
            return "dog"
        elif isinstance(animal, Cat):
            return "cat"
        return "invalid"

    def validate(self, data):
        # print(data)
        super(AnimalSerializer, self).validate(data)
        if isinstance(self.instance, Dog):
            old_type = 'dog'
        elif isinstance(self.instance, Cat):
            old_type = 'cat'
        else:
            old_type = 'invalid'
        type = self.initial_data.get('type', old_type)
        if type not in ['dog', 'cat'] or (type != old_type and old_type != 'invalid'):
            raise serializers.ValidationError('Invalid type')
        data['type'] = type
        return data

    def create(self, validated_data):
        type = validated_data.pop('type')
        if type == 'cat':
            return Cat.objects.create(**validated_data)
        else:
            return Dog.objects.create(**validated_data)

    class Meta:
        model = Animal
        fields = ['url' , 'name', 'age', 'adopted','type', 'adopter']

class AdopterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adopter
        fields = ['url', 'id','name', 'ssn']
        extra_kwargs = {
            'url': {'view_name': 'adopter-detail', 'lookup_field': 'ssn'}
        }

