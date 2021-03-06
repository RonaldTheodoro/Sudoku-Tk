# ! /usr/bin/python
# -*- coding:Utf-8 -*-
"""
Sudoku-Tk - Sudoku games and puzzle solver
Copyright 2016 Juliette Monsel <j_4321@protonmail.com>

Sudoku-Tk is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Sudoku-Tk is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Window displaying the information about the software
"""

from tkinter import Text, Toplevel
from tkinter.ttk import Button, Label, Style
from SudokuTkModules.constantes import set_icon, ICONE_48, VERSION, open_image
from webbrowser import open as webOpen


class About(Toplevel):
    """ Toplevel de l'application principale donnant les informations à
        propos du logiciel """
    def __init__(self, master, **options):
        Toplevel.__init__(self, master, **options)

        self.title(_("About Sudoku-Tk"))
        self.transient(master)
        self.grab_set()
#        set_icon(self)
        self.image = open_image(ICONE_48)
        Label(self, image=self.image).grid(row=0, columnspan=2, pady=10)

        Label(self,
                  text=_("Sudoku-Tk %(version)s")
                  % ({"version": VERSION})).grid(row=1, columnspan=2)
        Label(self, text=_("Sudoku games and puzzle solver")).grid(row=2, columnspan=2, padx=10)
        Label(self, text="Copyright (C) Juliette Monsel 2016").grid(row=3, columnspan=2)
        Label(self, text="j_4321@protonmail.com").grid(row=4, columnspan=2)
        Button(self, text=_("License"), command=self._license).grid(row=5, column=0, pady=(20, 10), padx=(10,4))
        Button(self, text=_("Close"), command=self._quitter).grid(row=5, column=1, pady=(20, 10), padx=(4,10))

        self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self._quitter)
        self.resizable(0, 0)
        self.initial_focus.focus_set()
        self.wait_window(self)

    def _quitter(self):
        
        if self.master:
            self.master.focus_set()
        self.destroy()

    def _license(self):
        
        def close():
            self.focus_set()
            fen.destroy()

        fen = Toplevel(self)
        fen.title(_("License"))
        fen.transient(self)
        fen.protocol("WM_DELETE_WINDOW", close)
        fen.resizable(0, 0)
        fen.grab_set()
#        set_icon(fen)
        texte = Text(fen, width=50, height=18)
        texte.pack()
        texte.insert("end",
                     _("Sudoku-Tk is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.\n\n"))
        texte.insert("end",
                     _("Sudoku-Tk is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.\n\n"))
        texte.insert("end",
                     _("You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/."))

        i = int(texte.index("5.end").split(".")[1])
        texte.tag_add("link", "5.%i" % (i - 29), "5.%i" % (i - 1))
        texte.tag_configure("link", foreground="#0000ff", underline=1)
        texte.tag_bind("link", "<Button - 1>",
                       lambda event: webOpen("http://www.gnu.org/licenses/"))
        texte.tag_bind("link", "<Enter>",
                       lambda event: texte.config(cursor="hand1"))
        texte.tag_bind("link",
                       "<Leave>", lambda event: texte.config(cursor=""))
        texte.configure(state="disabled", wrap="word")

        b_close = Button(fen, text=_("Close"), command=close)
        b_close.pack(side="bottom")
        b_close.focus_set()
        fen.wait_window(fen)
