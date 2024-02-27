from    plugins.plugin  \
        import  Plugin

class   PluginMaster:

    def __init__(self):
        self.plugins: Plugin = []
    
    def togglePlugin(self, _plugin):
        if _plugin in self.plugins:
            self.plugins.remove(_plugin)
        else:
            self.plugins.append(_plugin)
    
    def getPlugins(self):
        return self.plugins
    
    def start(self, frame):
        for plugin in self.plugins:
            frame = plugin.start(frame)
        return frame