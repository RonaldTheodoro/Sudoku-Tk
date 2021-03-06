#! /usr/bin/python3
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


Class for the virtual keyboard to enter numbers in the grid
"""

from tkinter import Toplevel
from tkinter.ttk import Style, Button
from SudokuTkModules.constantes import LOG
from numpy import array

class Clavier(Toplevel):    
    def __init__(self, parent, case, val_ou_pos, **options):
        Toplevel.__init__(self, parent, **options)
        self.type = val_ou_pos # clavier pour rentrer une valeur ou une possibilité
        self.overrideredirect(True)
        self.parent = parent
        self.case = case
        self.transient(self.parent)
        self.style = Style(self)
        self.style.configure("clavier.TButton", font="Arial 12")
        self.boutons = [[Button(self, text="1", width=2, style="clavier.TButton", command=lambda: self.entre_nb(1)),
                         Button(self, text="2", width=2, style="clavier.TButton", command=lambda: self.entre_nb(2)),
                         Button(self, text="3", width=2, style="clavier.TButton", command=lambda: self.entre_nb(3))],
                        [Button(self, text="4", width=2, style="clavier.TButton", command=lambda: self.entre_nb(4)),
                         Button(self, text="5", width=2, style="clavier.TButton", command=lambda: self.entre_nb(5)),
                         Button(self, text="6", width=2, style="clavier.TButton", command=lambda: self.entre_nb(6))],
                        [Button(self, text="7", width=2, style="clavier.TButton", command=lambda: self.entre_nb(7)),
                         Button(self, text="8", width=2, style="clavier.TButton", command=lambda: self.entre_nb(8)),
                         Button(self, text="9", width=2, style="clavier.TButton", command=lambda: self.entre_nb(9))]]
        for i in range(3):
            for j in range(3):
                self.boutons[i][j].grid(row=i, column=j)
        self.protocol("WM_DELETE_WINDOW", self.quitter)
        self.resizable(0, 0)
        self.attributes("-topmost",0)
        self.focus_set()
        self.lift()
        self.bind("<FocusOut>", self.focus_out)

    def focus_out(self, event):
        try:
            if not self.focus_get():
                self.quitter()
        except KeyError:
            # erreur déclenchée par la présence d'une tkMessagebox
            self.quitter()

    def entre_nb(self, val):
        i,j = self.case.get_i(), self.case.get_j()

        # données pour le log
        val_prec = self.case.get_val()
        pos_prec = array(self.case.get_possibilites(), dtype=str)
        coords = "%i\t%i;" % (i,j)
        undo_ch = "%i\t%s;" % (val_prec,"".join(pos_prec))
        modifs = ";"

        # modification de la case
        if self.type == "val":
            self.parent.modifie_nb_cases_remplies(self.case.edit_chiffre(val))
            if not self.parent.test_case(i,j):
                modifs = self.parent.update_grille(i,j)
            self.quitter()
        else:
            self.parent.modifie_nb_cases_remplies(self.case.edit_possibilite(val))
            self.parent.test_possibilite(i, j, val)

        # données pour le log
        pos = array(self.case.get_possibilites(), dtype=str)
        redo_ch = "%i\t%s\n" % (self.case.get_val(),"".join(pos))

        self.parent.log()
        with open(LOG, "a") as log:
            log.write(coords + undo_ch + modifs + redo_ch)
        self.parent.test_remplie()


    def quitter(self):
        if self.parent:
            self.parent.focus_set()
            self.parent.set_clavier(None)
        self.destroy()

    def set_case(self, case):
        self.case = case

