from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('titulo', '_autor')  # Colocado _autor para saber que é o autor modificado pela função abaixo

    # Não mostrar o campo autor, ou qualquer outro campo que eu colocar na lista
    exclude = ['autor', ]

    # função para pegar o nome completo do autor e apresentar na area administrativa
    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}'

    # função reescrita para apresentar somente os posts do autor logado
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(autor=request.user)

    # função reescrita para eu pegar o usuario que está logado e salvar como sendo autor post
    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)

