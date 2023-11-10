from django import forms
from . models import Branch,District,Customer


class CustForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields= "__all__"
        widgets={ 'Date_of_birth':forms.DateInput(
            attrs={'type':'date','placeholder':'yyyy-mm-dd(DOB)','class':'form-control'}
        )}
        # Date_of_birth=forms.DateField(



    def __init__(self,  *args, **kwargs):
        super().__init__(*args,**kwargs)
        # if request_change:
        #     request_change=False
        # else:
        self.fields['Branch'].queryset=Branch.objects.none()

        if 'District' in self.data:
            try:
                district_id=int(self.data.get('District'))
                self.fields['Branch'].queryset=Branch.objects.filter(District_id=district_id).order_by('Name')
            except (ValueError,TypeError):
                pass
        # elif self.instance.pk:
        #     self.fields['Branch'].queryset=self.instance.District.Branch_set.order_by('Name')


