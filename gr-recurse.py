import graphics as gr

alpha = 0.2

def draw_square(A, B, C, D, recurse=10):
    if recurse < 1:
        return
    for M, N in (A, B), (B, C), (C, D), (D, A):
        line = gr.Line(gr.Point(*M), gr.Point(*N))
        line.draw(window)
    A1 = (A[0] * (1 - alpha) + B[0] * alpha, A[1] * (1 - alpha) + B[1] * alpha)
    B1 = (B[0] * (1 - alpha) + C[0] * alpha, B[1] * (1 - alpha) + C[1] * alpha)
    C1 = (C[0] * (1 - alpha) + D[0] * alpha, C[1] * (1 - alpha) + D[1] * alpha)
    D1 = (D[0] * (1 - alpha) + A[0] * alpha, D[1] * (1 - alpha) + A[1] * alpha)
    draw_square(A1, B1, C1, D1, recurse - 1)

window = gr.GraphWin("project", 600, 600)

draw_square((100,100), (500,100), (500,500), (100,500), 100)

window.getMouse()
window.close()
