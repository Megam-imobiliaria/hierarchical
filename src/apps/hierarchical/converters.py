from django.contrib import messages
from .models import Section


class SectionConverter:
    regex = '.*'

    def to_python(self, fullcode):
        if not fullcode:
            return Section.root()

        try:
            return Section.objects.filter(fullcode=fullcode).first()
        except Exception:
            messages.error("Algo deu errado! Tente novamente mais tarde")
            return Section.root()

    def to_url(self, fullcode):
        return fullcode
