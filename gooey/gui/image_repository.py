'''
Collection of the image paths.

The module is meant to act as a singleton, hence the globals() abuse.

Image credit: kidcomic.net
'''
import os
from functools import partial
import warnings

from gooey.gui.util.freeze import getResourcePath
from gooey.util.functional import merge

filenames = {
    'programIcon': 'program_icon.png',
    'successIcon': 'success_icon.png',
    'runningIcon': 'running_icon.png',
    'loadingIcon': 'loading_icon.gif',
    'configIcon': 'config_icon.png',
    'errorIcon': 'error_icon.png'
}


def loadImages(targetDir):
    return {'images': merge(resolvePaths(getResourcePath('images'), filenames),
                            resolvePaths(getImageDirectory(targetDir),
                                         filenames))}


def getImageDirectory(targetDir):
    return getResourcePath('images') \
           if targetDir == '::gooey/default' \
           else targetDir


def resolvePaths(dirname, filenames):
    # Find candidate file paths
    filePaths = {}
    for f in sorted(os.listdir(dirname)):
        name, ext = os.path.splitext(f)
        if name in filePaths:
            warnings.warn('Multiple {} images found, using last found '
                          'extension ({})'.format(name, ext))
        filePaths[name] = os.path.join(dirname, f)

    # Build image dict
    return {key: filePaths[os.path.splitext(name)[0]]
            for key, name in filenames.items() if
            os.path.splitext(name)[0] in filePaths}
