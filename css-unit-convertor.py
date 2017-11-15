import sublime
import sublime_plugin
import re
import time
import os

SETTINGS = {}
lastCompletion = {"needFix": False, "value": None, "region": None}

def plugin_loaded():
    init_settings()

def init_settings():
    get_settings()
    sublime.load_settings('css-unit-convertor.sublime-settings').add_on_change('get_settings', get_settings)

def get_settings():
    settings = sublime.load_settings('css-unit-convertor.sublime-settings')
    SETTINGS['number'] = settings.get('number', 100)
    SETTINGS['operator'] = settings.get('operator', '/')
    SETTINGS['max_fraction_length'] = settings.get('max_fraction_length', 8)
    SETTINGS['from_unit'] = settings.get('from_unit', 'px')
    SETTINGS['to_unit'] = settings.get('to_unit', 'rem')
    SETTINGS['available_file_types'] = settings.get('available_file_types', ['.css', '.less', '.sass', '.scss', '.html', '.php'])

def get_setting(view, key):
    return view.settings().get(key, SETTINGS[key]);

class CssUnitConvertorCommand(sublime_plugin.EventListener):
    def on_text_command(self, view, name, args):
        # if name == 'commit_completion':
        if name == 'insert_dimensions':
            view.run_command('replace_unit')
        return None

    def on_query_completions(self, view, prefix, locations):
        # print('css unit convertion start {0}, {1}'.format(prefix, locations))

        number = get_setting(view, 'number')
        operator = get_setting(view, 'operator')
        max_fraction_length = get_setting(view, 'max_fraction_length')
        from_unit = get_setting(view, 'from_unit')
        to_unit = get_setting(view, 'to_unit')
        available_file_types = get_setting(view, 'available_file_types')

        # only works on specific file types
        fileName, fileExtension = os.path.splitext(view.file_name())
        if not fileExtension.lower() in available_file_types:
            return []

        # reset completion match
        lastCompletion["needFix"] = False
        location = locations[0]
        snippets = []

        # get from_unit match
        match = re.compile("([\d.]+)" + from_unit).match(prefix)
        if match:
            lineLocation = view.line(location)
            line = view.substr(sublime.Region(lineLocation.a, location))
            value = match.group(1)
            
            # fix: values like `0.5px`
            segmentStart = line.rfind(" ", 0, location)
            if segmentStart == -1:
                segmentStart = 0
            segmentStr = line[segmentStart:location]

            segment = re.compile("([\d.])+" + value).search(segmentStr)
            if segment:
                value = segment.group(0)
                start = lineLocation.a + segmentStart + 0 + segment.start(0)
                lastCompletion["needFix"] = True
            else:
                start = location

            operations = {
                '+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y,
                '/': lambda x, y: x / y,
                '%': lambda x, y: x % y,
                '**': lambda x, y: x ** y,
                '//': lambda x, y: x // y
            }

            to_value = round(operations[operator](float(value), number), max_fraction_length)
            to_value = int(to_value) if to_value == int(to_value) else to_value

            # save them for replace fix
            lastCompletion["value"] = str(to_value) + to_unit
            lastCompletion["region"] = sublime.Region(start, location)

            # set completion snippet
            snippets += [(value + from_unit + ' -> ' + to_unit + '(' + operator + str(number) + ')', str(to_value) + to_unit)]

        # print("css unit convertion: {0}".format(snippets))
        return snippets

class ReplaceUnitCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        needFix = lastCompletion["needFix"]
        if needFix == True:
            value = lastCompletion["value"]
            region = lastCompletion["region"]
            self.view.replace(edit, region, value)
            self.view.end_edit(edit)