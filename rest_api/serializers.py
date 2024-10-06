#study mart
from rest_framework import serializers
from .models import Student
#geekey
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField() # amra ai roll ke validate korbo. amra akn a jekono data insert korte parbo . kintu ami chaiteci je ami akta spacific data ba (200 teke 200) ar kom data insert korbo ai jnno amra ai field ke validate korbo
    city = serializers.CharField(max_length=100)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)

#partial update korlam ar ai jnno amara akn a PUT use korlam ar ai code partial ba data update ar jnno

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name',instance.name) #user jodi data provide kore take tahole akn a
        print(instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    #FIELD LAVEL VALIDATION:
    def validate_roll(self, value): #akn 7 no a line a roll a je value insert korbo sei data ta ai value ai self ar pase ai value te asbe
        if value >= 200:
            raise serializers.ValidationError('Seat Full') # amar akn a jodi 200 besi jon roll daiye takle seat full delhabe
        return value
    
    #object level validation start
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower()=='sadik' and ct.lower()!= 'dhaka':
            raise serializers.ValidationError('City Must be Dhaka')
        return data 
#object level validation end

    



