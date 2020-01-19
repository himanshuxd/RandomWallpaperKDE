#!/usr/bin/env python3
import dbus
import os, random
import argparse
import string

def setwall(folderpath):
    wpath = folderpath + random.choice(os.listdir(folderpath))
    jscript = """
    var allDesktops = desktops();
    print (allDesktops);
    for (i=0;i<allDesktops.length;i++) {
        d = allDesktops[i];
        d.wallpaperPlugin = "%s";
        d.currentConfigGroup = Array("Wallpaper", "%s", "General");
        d.writeConfig("Image", "file://%s")
    }
    """
    bus = dbus.SessionBus()
    plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
    plugin = 'org.kde.image'
    plasma.evaluateScript(jscript % (plugin, plugin, wpath))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Set KDE wallpaper randomly from a folder')
    parser.add_argument('folder', help='Wallpaper folder path')
    args = parser.parse_args()
    setwall(args.folder)
