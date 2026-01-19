from rest_framework.serializers import ModelSerializer;
from produtos.models.evaluation import Evaluation;

class EvaluationSerializer(ModelSerializer):
    class Meta:
        model = Evaluation;
        fields = '__all__';