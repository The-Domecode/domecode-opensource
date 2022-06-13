class PageTitleMixin(object):

    def get_page_title(self, context):
        return getattr(self, "title", "Default Page Title")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_page_title(context)

        return context
