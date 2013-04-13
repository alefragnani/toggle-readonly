import sublime, sublime_plugin, os, stat

class ToggleReadonlyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
      myFile = self.view.file_name()
      fileAtt = os.stat(myFile)[0]

      if (not fileAtt & stat.S_IWRITE):
        sublime.status_message("Making "+myFile+" writable")
        os.chmod(myFile, stat.S_IWRITE)
      else:
        sublime.status_message("Making "+myFile+" not writable")
        os.chmod(myFile, stat.S_IREAD)          

    def is_enabled(self):
        return self.view.file_name() and len(self.view.file_name()) > 0
