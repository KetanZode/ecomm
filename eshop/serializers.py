from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    pname = serializers.CharField()
    pdesc = serializers.CharField()
    pslug = serializers.CharField()    
    pprice = serializers.CharField()
    pimg = serializers.CharField()
    pcat = serializers.CharField()

 
class CategorySerializer(serializers.Serializer):
    cname = serializers.CharField()
    cimg = serializers.CharField()


    