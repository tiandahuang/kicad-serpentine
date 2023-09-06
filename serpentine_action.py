import pcbnew
import os
from .serpentine_wrapper import SerpentineWrapper

class SerpentineAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = 'serpentine 🐍 generator'
        self.category = 'routing tools'
        self.description = 'generate serpentine traces. support for adjusting angle and separately adjusting top/bottom traces.'
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')

    def Run(self):
        SerpentineWrapper()
