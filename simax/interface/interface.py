import pprint
from tkinter import *

from simax.seeding import seeder
from simax.world.world import World


def flatten_list(param):
    return [item for sublist in param for item in (sublist if hasattr(sublist, '__iter__') else [sublist])]


class Interface(object):

    def __init__(self):
        master = Tk()

        master.title("Simax v0.1 - Yotam Tanay")

        self.is_cycling = False
        self.master = master

        self.total_label_text = IntVar()
        self.total_label_text.set("Cycles: 0")
        self.total_label = Label(master, textvariable=self.total_label_text)


        self.label = Label(master, text="Simax (prototype)")

        self.reset_button = Button(master, text="Cycle", command=self.toggle_cycle)

        self.canvas = Canvas(master, width=800, height=500)

        self.action_list =Listbox(master)

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1)
        self.reset_button.grid(row=0, column=2, sticky=E)

        self.canvas.grid(row=2, column=0, columnspan=3, sticky=W + E)

        self.action_list.grid(row=3, column=0, columnspan=3, sticky=W+E)

        self.world = World(self.canvas)

    def start(self):
        for entity in flatten_list(seeder.seed_entities()):
            self.world.assign(entity)
        for infra in flatten_list(seeder.seed_topology()):
            self.world.topology.add_road(infra)
        pprint.pprint(self.world.topology.graph)
        self.world.prepare()
        self.master.mainloop()

    def cycle(self):
        print('cycling')
        self.world.draw_and_cycle()

    def toggle_cycle(self):
        if self.is_cycling:
            self.is_cycling = False
        else:
            self.is_cycling = True
            self.master.after(10, self.full_cycle)

    def full_cycle(self):

        self.world.draw_and_cycle()
        self.total_label_text.set("Cycle: {}".format(self.world.cycles))
        self.action_list.delete(0, END)
        for entity in self.world.entities:
            self.action_list.insert(END, entity)
        if self.is_cycling:
            self.master.after(10, self.full_cycle)

