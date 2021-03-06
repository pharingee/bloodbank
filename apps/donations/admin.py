from django.contrib import admin

from models import (
    Donor, Blood, BloodProduct, HospitalTest, NBGSTest, DonorConditionFormA,
    DonorConditionFormB, DonorConditionFormC, DonorConditionPreForm
)


admin.site.register(Donor)
admin.site.register(Blood)
admin.site.register(BloodProduct)
admin.site.register(HospitalTest)
admin.site.register(NBGSTest)
admin.site.register(DonorConditionPreForm)
admin.site.register(DonorConditionFormA)
admin.site.register(DonorConditionFormB)
admin.site.register(DonorConditionFormC)
