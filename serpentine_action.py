import pcbnew
import os
from .serpentine_wrapper import SerpentineWrapper

class SerpentineAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = 'name in kicad context menu'
        self.category = 'routing tools'
        self.description = 'descript'
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')

    def Run(self):
        SerpentineWrapper()
