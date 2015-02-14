import sublime
import sublime_plugin
import re

class CssUnminifyCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.view = self.window.active_view()
        input_region = sublime.Region(0, self.view.size())

        contents = self.view.substr(input_region)
        output = self.unminify(contents)

        if output:
            view = self.view
            output_region = input_region

            edit = view.begin_edit()
            view.replace(edit, output_region, output)
            view.end_edit(edit)

    def unminify(self, contents):
        unminified = re.sub("\{", " {\n\r\n\r\t", contents)
        unminified = re.sub("\}", "\n\r\n\r}\n\r\n\r", unminified)
        unminified = re.sub(";(?!base64)", ";\n\r\t", unminified)
        return unminified
