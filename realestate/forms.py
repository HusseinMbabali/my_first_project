from django.forms import ModelForm

from realestate.models import Estate, Land, House, Customer, Payment, Title

class EstateForm(ModelForm):
    class Meta:
        model = Estate
        fields = '__all__'

class LandForm(ModelForm):
    class Meta:
        model = Land
        fields = '__all__'

class HouseForm(ModelForm):
    class Meta:
        model = House
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

class TitleForm(ModelForm):
    class Meta:
        model = Title
        fields = '__all__'
