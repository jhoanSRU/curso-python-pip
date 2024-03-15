import matplotlib.pyplot as plt

def bar_chart(name, labels, values):
    ax = plt.subplot()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{name}.png')
    plt.title(f'The artis is: {name}')
    plt.close()

#if __name__=='__main__':
   # bar_chart(labels, values) 