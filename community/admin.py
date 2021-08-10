from django.contrib import admin
from .models import Community
from .models import Expert
from .models import ExpertRe
from .models import Reply

# Register your models here.
admin.site.register(Community)
admin.site.register(Expert)
admin.site.register(ExpertRe)
admin.site.register(Reply)