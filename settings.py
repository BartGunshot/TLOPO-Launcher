from pathlib import Path
from launcherglobals import FILEPATHS


class Settings:

    def __init__(self, ver='live'):
        self.settingspath = Path(Path.cwd(), FILEPATHS.get(ver))
        self.settingsdict = {}

    def read(self):
        try:
            # p_working_options seems to be reliably created after first run
            with open(Path(self.settingspath, 'p_working_options.txt'), 'r') as f:
                for line in f:
                    # Cleanup the messy new line garbage and the spaces present on all but 1 entry lol?
                    line = line.replace('\n', '').replace(' ', '')
                    nextline = next(f).replace('\n', '')
                    self.settingsdict[line] = nextline
        except FileNotFoundError:
            pass
        return self.settingsdict

    def write(self):
        try:
            # 3 settings files, just overwrite each
            for filealias in ['game_options.txt', 'last_working_options.txt', 'p_working_options.txt']:
                with open(Path(self.settingspath, filealias), 'w') as f:
                    for key, value in self.settingsdict.items():
                        # Write back the two lines, each header has a space following
                        f.write(key + ' \n')
                        f.write(value + '\n')
        except FileNotFoundError:
            pass
