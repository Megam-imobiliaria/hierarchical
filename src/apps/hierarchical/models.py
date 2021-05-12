from django.db import models


class Section(models.Model):
    label = models.CharField(max_length=100)
    code = models.IntegerField(null=True)
    fullcode = models.CharField(max_length=50, null=True)
    parent = models.ForeignKey('Section', on_delete=models.CASCADE, null=True)

    @classmethod
    def root(cls):
        if not hasattr(cls, '_root'):
            try:
                cls._root = Section.objects.get(code=None)
            except:
                cls._root = Section(code=None, fullcode='', label='System Location', parent=None)
                cls._root.save()
        return cls._root

    def __str__(self):
        return self.label

    @property
    def isroot(self):
        return self.parent is None

    @property
    def hierarchy(self) -> list:
        return [] if self.isroot else self.parent.hierarchy + [self.code]

    @property
    def parents(self):
        parents = [] if self.isroot else self.parent.parents | self.queryset
        return Section.objects.filter(id__in=[section.id for section in parents])

    @property
    def immediates(self):
        return self.section_set.all().order_by('code')

    @property
    def queryset(self):
        return Section.objects.filter(id=self.id)

    @property
    def level(self) -> int:
        return len(self.hierarchy)

    @property
    def isodd(self):
        return self.level % 2 == 0

    @property
    def bump(self) -> str:
        """fullcode of next immediate"""
        bump = 1
        if self.immediates:
            bump = self.immediates.last().code + 1

        return '.'.join([
            str(i) for i in self.hierarchy + [bump]])

    def relative(self, adjacency):
        try:
            return Section.objects.get(code=self.code + adjacency, parent=self.parent)
        except:
            return None

    @property
    def previous(self):
        return self.relative(-1)

    @property
    def next(self):
        return self.relative(+1)
