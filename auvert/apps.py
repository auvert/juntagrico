from django.apps import AppConfig

class AuvertConfig(AppConfig):
    name = 'auvert'
    verbose_name = "Genossenschaft auVert"

    def ready(self):
        from django.conf import settings
        from juntagrico.config import Config
        from juntagrico.forms import RegisterMemberForm
        # juntagrico's agb_label() formats these via .format()/format_html() with
        # NAMED arguments, so the placeholders must be {organization}/{documents}.
        # A bare positional {} raises IndexError on GET /signup/.
        RegisterMemberForm.text['accept_wo_docs'] = 'Hiermit beantrage ich meine Aufnahme in der {organization}.'
        # Only the bylaws go into {documents}; the business regulations get their
        # own consent sentence. format_html() escapes only the arguments, so the
        # literal link below is rendered as HTML.
        RegisterMemberForm.documents = [('Statuten', Config.bylaws)]
        RegisterMemberForm.text['accept_with_docs'] = (
            'Hiermit beantrage ich meine Aufnahme in der {organization} ({documents}). '
            'Ich habe das <a target="_blank" href="' + settings.BUSINESS_REGULATIONS + '">Betriebsreglement</a> '
            'gelesen und bin damit einverstanden.'
        )
