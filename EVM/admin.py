from django.contrib import admin
from .models import vote_count,Messages,permission,Voting_details,LoggedInUser,Reply,Draft_Box

# Register your models here.
admin.site.register(vote_count)
admin.site.register(Messages)
admin.site.register(permission)
admin.site.register(Voting_details)
admin.site.register(LoggedInUser)
admin.site.register(Reply)
admin.site.register(Draft_Box)






