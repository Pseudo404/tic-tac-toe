import pygame

pygame.init()
taille = 600
case = taille // 3
screen = pygame.display.set_mode((taille, taille))
pygame.display.set_caption("Tic Tac Toe")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

grille = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

joueur = "X"
gagnant = None
cases_gagnantes = []

score_X = 0
score_O = 0

def reset():
    global grille, joueur, gagnant, cases_gagnantes
    grille = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    joueur = "X"
    gagnant = None
    cases_gagnantes = []

def grille_pleine():
    for ligne in grille:
        for case in ligne:
            if case is None:
                return False
    return True

def verifier_victoire():
    global cases_gagnantes

    lignes = []

    for i in range(3):
        lignes.append([(i, 0), (i, 1), (i, 2)])
        lignes.append([(0, i), (1, i), (2, i)])

    lignes.append([(0, 0), (1, 1), (2, 2)])
    lignes.append([(0, 2), (1, 1), (2, 0)])

    for ligne in lignes:
        a, b, c = ligne
        v1 = grille[a[0]][a[1]]
        v2 = grille[b[0]][b[1]]
        v3 = grille[c[0]][c[1]]

        if v1 is not None and v1 == v2 and v2 == v3:
            cases_gagnantes = ligne
            return v1

    return None

def dessiner_grille():
    screen.fill((255, 255, 255))

    for i in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (i * case, 0), (i * case, taille), 6)
        pygame.draw.line(screen, (0, 0, 0), (0, i * case), (taille, i * case), 6)

def dessiner_symboles():
    marge = case // 5

    for y in range(3):
        for x in range(3):
            valeur = grille[y][x]
            px = x * case
            py = y * case

            if valeur == "X":
                pygame.draw.line(screen, (255, 0, 0),
                                 (px + marge, py + marge),
                                 (px + case - marge, py + case - marge), 8)
                pygame.draw.line(screen, (255, 0, 0),
                                 (px + marge, py + case - marge),
                                 (px + case - marge, py + marge), 8)

            if valeur == "O":
                pygame.draw.circle(screen, (0, 0, 255),
                                   (px + case // 2, py + case // 2),
                                   case // 2 - marge, 8)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if gagnant is None:
                mx, my = event.pos
                x = mx // case
                y = my // case

                if grille[y][x] is None:
                    grille[y][x] = joueur
                    gagnant = verifier_victoire()

                    if gagnant == "X":
                        score_X += 1
                    elif gagnant == "O":
                        score_O += 1
                    else:
                        if grille_pleine():
                            gagnant = "NUL"
                        else:
                            joueur = "O" if joueur == "X" else "X"

    dessiner_grille()
    dessiner_symboles()

    if gagnant is None:
        texte = f"Tour de {joueur}"
    elif gagnant == "NUL":
        texte = "Match nul ! (R pour rejouer)"
    else:
        texte = f"{gagnant} a gagné ! (R pour rejouer)"

    txt = font.render(texte, True, (0, 0, 0))
    screen.blit(txt, (10, taille - 35))

    score = font.render(f"X: {score_X}   O: {score_O}", True, (0, 0, 0))
    screen.blit(score, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
