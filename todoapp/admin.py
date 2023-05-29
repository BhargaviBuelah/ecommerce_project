from django.contrib import admin
from todoapp.models import Product

# Register your models here.
#sntax:admin.site.register(modelname)

#admin.site.register(Product)
#define custom filter
class MyPricefilter(admin.SimpleListFilter):

    title="Price"
    parameter_name="By Price"

    def lookups(self,request,Model_admin):

        return(('Greater','Price>5000'),('Lesser','Price<5000'))

    def queryset(self,request,queryset):

        
        if self.value()=="Greater":
            #q1=Q(price__gt=5000)
            #q2=Q(is_deleted='N')
            #return queryset.filter(q1 & q2)
            return queryset.filter(price__gt=5000)
        elif self.value()=="Lesser":
            return queryset.filter(price__lt=5000)
        else:
            return queryset.all()
 


class ProductAdmin(admin.ModelAdmin):

    list_display=['name','pdesc','price','cat','is_deleted']
    list_filter=['is_deleted','cat',MyPricefilter]

admin.site.register(Product,ProductAdmin)



