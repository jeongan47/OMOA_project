from django.contrib import admin
from ranking.models import Netflix_movieRank, Netflix_tvRank, Amazon_movieRank, Amazon_tvRank, Disney_Rank, Wavve_movieRank, Wavve_tvRank
# Register your models here.

admin.site.register(Netflix_movieRank)
admin.site.register(Netflix_tvRank)
admin.site.register(Amazon_movieRank)
admin.site.register(Amazon_tvRank)
admin.site.register(Disney_Rank)
admin.site.register(Wavve_movieRank)
admin.site.register(Wavve_tvRank)