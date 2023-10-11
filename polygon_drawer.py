import tkinter as tk
from math import sqrt


class PolygonDrawer:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=600, height=600, bg="ivory")
        self.canvas.pack()
        self.points = []
        self.drawing = True

        self.canvas.create_polygon(0, 0, outline="black", width=3, fill="", tag="pgn")

        self.canvas.bind("<Button-1>", self.add_point)
        self.canvas.bind("<Motion>", self.show_live_polygon)

    def show_live_polygon(self, event):
        """
        Show the live polygone with current coordinates and mouse's position.
        """

        x, y = event.x, event.y

        if len(self.points) > 1 and self.drawing == True:
            polygon_points = self.points + [(x, y)]
            self.canvas.coords(
                "pgn", [coord for point in polygon_points for coord in point]
            )

    def add_point(self, event):
        """
        Add a new point to the list of points when user left click.
        """
        if self.drawing:
            x, y = event.x, event.y

            if (
                len(self.points) != 0
                and sqrt((x - self.points[0][0]) ** 2 + (y - self.points[0][1]) ** 2)
                < 20
            ):  # if the user has finished drawing the polygon
                self.drawing = False
                yellow_circle = self.canvas.find_withtag("yellow_circle")
                self.canvas.delete(yellow_circle)
                self.canvas.coords(
                    "pgn", [coord for point in self.points for coord in point]
                )

            else:
                self.points.append((x, y))
                if len(self.points) == 1:  # If it's the first point.
                    self.canvas.create_oval(
                        self.points[0][0] - 20,
                        self.points[0][1] - 20,
                        self.points[0][0] + 20,
                        self.points[0][1] + 20,
                        fill="#F6FF66",
                        width=0,
                        tag="yellow_circle",
                    )
                    self.canvas.tag_lower("yellow_circle")


def main():
    root = tk.Tk()
    root.title("Polygon Drawer")
    app = PolygonDrawer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
