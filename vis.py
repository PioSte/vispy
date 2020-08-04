import matplotlib.pyplot as plt


class IndexTracker:
    def __init__(self, X, sliced_axis=2, axis_labels=['y','x','z']):
        self.fig, self.ax = plt.subplots(1, 1)

        self.axis_labels = axis_labels
        self.current_axis = int(sliced_axis)
        self.current_label = axis_labels[self.current_axis]

        self.X = X
        self.current_axis_size = self.X.shape[self.current_axis]
        
        self.ind = self.X.shape[self.current_axis]//2

        self.y_mouse_prev = None

        self.im = self.ax.imshow(self.X[:, :, self.ind])
        
        self.fig.colorbar(self.im, ax=self.ax)

        self.update()
        self.ax.set_title('Mouse drag up/down to select slice')

    def onmousemove(self, event):
        if event.x is not None and event.y is not None:
            if str(event.button) == 'MouseButton.LEFT':
                steps = int(round((event.y - self.y_mouse_prev) / 2))
                self.ind = (self.ind + steps) % self.current_axis_size
                self.update()
            self.y_mouse_prev = event.y
        else:
            self.y_mouse_prev = None

    def onrightmouseclick(self, event):
        if str(event.button) == 'MouseButton.RIGHT':
            self.current_axis = int(self.current_axis + 1)
            self.current_axis = self.current_axis % 3
            self.current_label = self.axis_labels[self.current_axis]
            self.current_axis_size = self.X.shape[self.current_axis]
            self.ind = self.ind % self.current_axis_size
            self.ax.clear()
            if self.current_axis == 0:
                self.im = self.ax.imshow(self.X[self.ind])
            elif self.current_axis == 1:
                self.im = self.ax.imshow(self.X[:, self.ind, :])
            else:
                self.im = self.ax.imshow(self.X[..., self.ind])
            self.update()

    def update(self):
        if self.current_axis == 0:
            self.im.set_data(self.X[self.ind])
        elif self.current_axis == 1:
            self.im.set_data(self.X[:, self.ind, :])
        else:
            self.im.set_data(self.X[..., self.ind])
        self.ax.set_title(self.current_label + ' = ' + str(self.ind) + ' / ' + str(self.current_axis_size))
        self.im.axes.figure.canvas.draw()


def vis(vol, sliced_axis=2, axis_labels=['y','x','z']):
    tracker = IndexTracker(vol, sliced_axis=2, axis_labels=['y', 'x', 'z'])
    tracker.fig.canvas.mpl_connect('motion_notify_event', tracker.onmousemove)
    tracker.fig.canvas.mpl_connect('button_press_event', tracker.onrightmouseclick)
    plt.show(block=True)


if __name__ == "__main__":
    test = 1