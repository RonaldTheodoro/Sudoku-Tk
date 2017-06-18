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

Help window
"""

from tkinter import Text, Toplevel
from tkinter.ttk import Style
from SudokuTkModules.constantes import set_icon, STYLE
from webbrowser import open as webOpen
#
#_ = lang.gettext


class Aide(Toplevel):
    def __init__(self, master, **options):
        
        Toplevel.__init__(self, master, **options)

        self.title(_("Sudoku-Tk Help"))
        self.transient(master)
        self.grab_set()
#        set_icon(self)

        self.geometry(self.master.geometry())
        txt = Text(self, wrap="word", font="Arial 10", tabs=("6"), padx=15, pady=15)
        txt.pack(fill="both", expand=True)

        txt.insert("end", _("Sudoku-Tk Help\n"), ("titre1"))
        txt.insert("end", _("Sudoku-Tk is a software written in python and using the Tcl/Tk graphical libraries. It enables you to play sudoku and can also solve sudoku puzzles."))
        txt.insert("end", _(" The puzzles can be loaded from files, entered by the user or generated by the software. I apologize for the slowness of the generation algorithm. It generates minimal puzzles, which means that if you remove any value from the puzzle it will not have a unique solution any more. See "))
        txt.insert("end", _("https://en.wikipedia.org/wiki/Sudoku"), ("link"))
        txt.insert("end", _(" for more information on sudoku.\n\n"))

        txt.insert("end", _("Starting a game\n"), ("titre2"))
        txt.insert("end", _("To start a game go to "))
        txt.insert("end", _("New -> Generate a puzzle"), ("it"))
        txt.insert("end", _(" or open an existing game / puzzle. You can also start from an empty grid."))
        txt.insert("end", _("You can find puzzles files in the "))
        txt.insert("end", "Sudoku-Tk/Puzzles", ("it"))
        txt.insert("end", _(" folder. The levels given are only indicative.\n\n"))

        txt.insert("end", _("Filling the grid\n"), ("titre2"))
        txt.insert("end", _("\t• Left mouse click in the cell to show the keypad to enter a value.\n"))
        txt.insert("end", _("\t• Right mouse click in the cell to show the keypad to enter a possibility.\n"), ("space"))
        txt.insert("end", _("If the keypad does not appear, check whether the game is on pause.\n"))
        txt.insert("end", _("The game can be saved at any time to continue it later. To open a saved game, go to "))
        txt.insert("end", _("Open -> Game"), ("it"))
        txt.insert("end", _(" and select the desired .sudoku file.\n\n"))

        txt.insert("end", _("Printing a puzzle\n"), ("titre2"))
        txt.insert("end", _("You cannot print directly a puzzle but you can export it as .png or .jpg in order to put several puzzles in a document editor of your choice and print them."))
        txt.insert("end", _("Only the values are printed (not the possibilities) and to save ink, there is no grey background for the initial values.\n\n"))

        txt.insert("end", _("Solving a puzzle\n"), ("titre2"))
        txt.insert("end", _("The "))
        txt.insert("end", _("Solve"), ("it"))
        txt.insert("end", _(" command in the menubar computes the solution of the current puzzle. First, it takes into account all the values in the grid, but if there is a mistake, the solution can be computed from the initial values only. In this case, the right value will be displayed in red in the cells that contained a wrong value."))

        txt.tag_configure("link", foreground="#0000ff", underline=1)
        txt.tag_bind("link", "<Button-1>",
                     lambda event: webOpen(_("https://en.wikipedia.org/wiki/Sudoku")))
        txt.tag_bind("link", "<Enter>",
                     lambda event: txt.config(cursor="hand1"))
        txt.tag_bind("link", "<Leave>", lambda event: txt.config(cursor=""))
        txt.tag_configure("it", font="Arial 10 italic")
        txt.tag_configure("space", spacing3=4)
        txt.tag_configure("titre1", font="Arial 14 bold", justify="center", spacing3=10)
        txt.tag_configure("titre2", font="Arial 11 bold", spacing3=4)
        txt.configure(state="disabled")

        self.protocol("WM_DELETE_WINDOW", self._quitter)
        self.resizable(0, 0)
        self.focus_set()
        self.wait_window(self)

    def _quitter(self):
        if self.master:
            self.master.focus_set()
        self.destroy()
