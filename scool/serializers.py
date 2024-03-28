from rest_framework import serializers
from .models import Course, Person

class CourseSerializer(serializers.ModelSerializer):
    # скрытоое поле будет в базу добавлять id пользователя который добавил запись
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Course
        fields = ['id','name', 'course_num', 'description', 'user']



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'




# from rest_framework.renderers import JSONRenderer

# class Course:
#     def __init__(self, name, descr) -> None:
#         self.name = name
#         self.desc = descr


# class CourseSerialezer(serializers.Serializer):
#     name = serializers.CharField(max_lenhth=255)
#     descr = serializers.CharField()



# model = Course('dsdsdsd','dsdsd')    
# model_sr = CourseSerialezer(model)
# json = JSONRenderer().render(model_sr.data)


