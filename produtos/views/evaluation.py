from rest_framework.viewsets import ModelViewSet;
from produtos.models.evaluation import Evaluation;
from produtos.serializers.evaluation import EvaluationSerializer;

class EvaluationViewSet(ModelViewSet):
    queryset = Evaluation.objects.all();
    serializer_class = EvaluationSerializer;