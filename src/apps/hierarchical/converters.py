from .models import Section


class SectionConverter:
    regex = '.*'

    def to_python(self, fullcode):
        if not fullcode:
            return Section.root()
        return Section.objects.get(fullcode=fullcode)

    def to_url(self, fullcode):
        return fullcode
