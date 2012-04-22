#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk


class Spawn(object):
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect('delete_event', self.spawn)
        self.window.connect('destroy', self.spawn)
        self.window.set_border_width(10)

        self.button = gtk.Button('Spawn!')
        self.button.connect('clicked', self.spawn)

        self.window.add(self.button)
        self.button.show()
        self.window.show()

    def spawn(self, widget, data=None):
        spawn = Spawn()
        spawn.main()
        return True

    def main(self):
        gtk.main()


if __name__ == '__main__':
    spawn = Spawn()
    spawn.main()
