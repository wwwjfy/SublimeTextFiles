import sublime
import sublime_plugin


class GotoLast(sublime_plugin.WindowCommand):

    def run(self):
        views = self.window.views_in_group(self.window.active_group())
        self.window.focus_view(views[-1])
