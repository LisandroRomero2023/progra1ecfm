import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def swap(A,i,j):
    if i != j:
        A[i], A[j] = A[j], A[i]

def bubblesort(A):
    if len(A) == 1:
        return
    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            yield A

def mergesort(A, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)
    yield A

def merge(A, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        A[start + i] = sorted_val
        yield A

def quicksort(A, start, end):
    if start >= end:
        return
    pivot = A[end]
    pivotIdx = start
    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, end, pivotIdx)
    yield A

    yield from quicksort(A, start, pivotIdx - 1)
    yield from quicksort(A, pivotIdx + 1, end)


class Simulador():
    def __init__(self, lista, sort, title=None):
        self.lista= lista
        self.sort = sort
        self.speedofSort=500
        self.title=title
    
    def update_fig(self, A, rects, i, *args, **kwargs):
            for rect, val in zip(rects, A):
                rect.set_height(val)

            i[0] += 1
            noOfOperations.set_text("No. of operations:"+str(i[0]))
            # timeTaken.set_text("Time taken:"+str(time.time()-start_time)[:4]+"sec")
            time_elapsed=(time.time()-start_time)
            time_elapsed=float("{0:.2f}".format(time_elapsed))
            time_elapsed=str(time_elapsed)
            timeTaken.set_text("Time taken:"+time_elapsed+" sec")
    
    def getLista(self, *args, **kwargs):
        return self.lista
    
    def getSort(self, *args, **kwargs):
        return self.sort
    
    def preparacion(self, *args, **kwargs):
        A = self.lista
        N = len(self.lista)
        if self.sort == "1":
            generator = bubblesort(A)

        elif self.sort == "2":
            generator = mergesort(A, 0, N - 1)

        elif self.sort == "3":
            generator = quicksort(A, 0, N - 1)

        ####################################################
        ######## SETTING UP MATPLOTLIB SUBPLOT #############
        fig, self.ax = plt.subplots()
        self.ax.set_title(self.title)
        self.bar_rects = self.ax.bar(range(len(A)), A, align="edge")

        self.ax.set_xlim(0, N)
        self.ax.set_ylim(0, int(1.07 * N))


        ####################################################
        ################ SETTING UP LABELS #################
        self.noOfOperations = self.ax.text(0.02, 0.95, "", transform=self.ax.transAxes)
        self.timeTaken = self.ax.text(0.02, 0.91, "", transform=self.ax.transAxes)
        self.interval= self.ax.text(0.02, 0.87, "Interval duration:"+str(self.speedofSort)+"ms", transform=self.ax.transAxes)

        self.i = [0]
        self.start_time=time.time()
        
        generator = bubblesort(self.lista)
        
        anim = animation.FuncAnimation(fig, func=self.update_fig,
            fargs=(self.bar_rects, self.i), frames=generator, interval=self.speedofSort,
            repeat=False)
        plt.show()
