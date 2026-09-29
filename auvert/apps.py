from django.apps import AppConfig

class AuvertConfig(AppConfig):
    name = 'auvert'
    verbose_name = "Genossenschaft auVert"

    def ready(self):
        from juntagrico.forms import RegisterMemberForm
        # juntagrico's agb_label() formats this via .format(organization=...),
        # i.e. with a NAMED argument, so the placeholder must be {organization}.
        # A bare positional {} raises IndexError on GET /signup/.
        RegisterMemberForm.text['accept_wo_docs'] = 'Hiermit beantrage ich meine Aufnahme in der {organization}.'
