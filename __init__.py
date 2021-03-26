bl_info = {
    "name": "IO CSV Colors Addon",
    "author": "Nezumi",
    "version": (0, 0, 1),
    "blender": (2, 92, 0),
    "location": "View3D > UI > Test Panel",
    "description": "",
    "warning": "",
    "wiki_url": "",
    "category": "Development",
    "support":"TESTING"
}
 
import sys
import importlib
import os

addon_path = os.path.dirname(os.path.realpath(__file__))
modulesNames = []
folders = ['operators', 'panels', 'properties', 'config']
for folder in folders:
    for mod in os.listdir(os.path.join(addon_path, folder)):
        if mod.endswith('.py'):
            modulesNames.append(f"{folder}.{mod[:-3]}")

modulesFullNames = {}
for currentModuleName in modulesNames:
    if 'DEBUG_MODE' in sys.argv:
        modulesFullNames[currentModuleName] = ('{}'.format(currentModuleName))
    else:
        modulesFullNames[currentModuleName] = ('{}.{}'.format(__name__, currentModuleName))
 
for currentModuleFullName in modulesFullNames.values():
    if currentModuleFullName in sys.modules:
        importlib.reload(sys.modules[currentModuleFullName])
    else:
        globals()[currentModuleFullName] = importlib.import_module(currentModuleFullName)
        setattr(globals()[currentModuleFullName], 'modulesNames', modulesFullNames)
 
def register():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'register'):
                sys.modules[currentModuleName].register()
 
def unregister():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'unregister'):
                sys.modules[currentModuleName].unregister()
 
if __name__ == "__main__":
    register()