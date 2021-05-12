from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib import messages

from .models import Section


def create(request):
    label = request.POST.get('label')
    fullcode = request.POST.get('fullcode')

    *parent_code, code = fullcode.rsplit('.', 1)

    parent = Section.root() \
            if not parent_code else \
            Section.objects.get(fullcode=parent_code[0])

    if Section.objects.filter(fullcode=fullcode):
        messages.warning(request, f"Secção {fullcode} já existe")
    else:
        Section(
            label=label,
            code=int(code),
            fullcode=fullcode,
            parent=parent
        ).save()
        messages.success(request, f'Secção {fullcode} criada com sucesso')

    return redirect('section', parent.fullcode or '')


def update(request):
    label = request.POST.get('label')
    fullcode = request.POST.get('fullcode')
    try:
        section = Section.objects.get(fullcode=fullcode)
        section.label = label
        section.save()

        messages.success(request, f'Secção {fullcode} editada com sucesso')
        return redirect('section', fullcode)

    except Exception:
        messages.error("Alguma coisa deu errado. Tente novamente")
        return redirect('root')


def delete(request):
    fullcode = request.POST.get('fullcode')
    try:
        section = Section.objects.get(fullcode=fullcode)
        parent = section.parent
        if section.next:
            messages.warning(request, 'Não pode-se deletar secções que possuem sucessoras')
            return redirect('section', fullcode)
        else:
            section.delete()
            messages.success(request, f'Secção {fullcode} deletada com sucesso')
            return redirect('section', parent.fullcode)

    except Exception:
        messages.error("Alguma coisa deu errado. Tente novamente")
        return redirect('root')


class SectionListView(ListView):
    model = Section

    def get_context_data(self, **kwargs):
        context = super(SectionListView, self).get_context_data(**kwargs)
        context['relative'] = self.kwargs['relative'] \
                             if 'relative' in self.kwargs else \
                             Section.root()

        return context

    def get_queryset(self):
        relative = self.kwargs['relative'] if 'relative' in self.kwargs else Section.root()

        queryset = relative.parents | relative.queryset | relative.immediates
        return queryset.exclude(code=None).order_by('id')
