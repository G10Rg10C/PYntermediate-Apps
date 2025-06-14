import pygame
import random

# Inizializzazione di pygame
pygame.init()

# Costanti
LARGHEZZA, ALTEZZA = 400, 400
DIMENSIONE_BLOCCO = 20
NERO, VERDE, ROSSO, BIANCO, GRIGIO = (0, 0, 0), (0, 255, 0), (255, 0, 0), (255, 255, 255), (100, 100, 100)

# Creazione finestra
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Funzione per generare una posizione casuale sulla griglia
def posizione_casuale():
    return (random.randint(0, (LARGHEZZA // DIMENSIONE_BLOCCO) - 1) * DIMENSIONE_BLOCCO,
            random.randint(0, (ALTEZZA // DIMENSIONE_BLOCCO) - 1) * DIMENSIONE_BLOCCO)

def mostra_pulsante():
    pulsante_rect = pygame.Rect(LARGHEZZA // 2 - 50, ALTEZZA // 2, 100, 40)
    pygame.draw.rect(schermo, BIANCO, pulsante_rect)
    testo_render = font.render("ARISE", True, NERO)
    schermo.blit(testo_render, (LARGHEZZA // 2 - 40, ALTEZZA // 2 + 10))
    pygame.display.flip()
    return pulsante_rect

def gioco():
    serpente = [(200, 200)]
    direzione = (DIMENSIONE_BLOCCO, 0)
    mela = posizione_casuale()
    game_over = False
    
    while True:
        while game_over:
            schermo.fill(NERO)
            pulsante_rect = mostra_pulsante()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and pulsante_rect.collidepoint(event.pos):
                    gioco()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direzione != (0, DIMENSIONE_BLOCCO):
                    direzione = (0, -DIMENSIONE_BLOCCO)
                elif event.key == pygame.K_DOWN and direzione != (0, -DIMENSIONE_BLOCCO):
                    direzione = (0, DIMENSIONE_BLOCCO)
                elif event.key == pygame.K_LEFT and direzione != (DIMENSIONE_BLOCCO, 0):
                    direzione = (-DIMENSIONE_BLOCCO, 0)
                elif event.key == pygame.K_RIGHT and direzione != (-DIMENSIONE_BLOCCO, 0):
                    direzione = (DIMENSIONE_BLOCCO, 0)
        
        # Movimento del serpente
        nuova_testa = (serpente[0][0] + direzione[0], serpente[0][1] + direzione[1])
        
        # Controllo collisioni
        if (nuova_testa in serpente or
            nuova_testa[0] < 0 or nuova_testa[0] >= LARGHEZZA or
            nuova_testa[1] < 0 or nuova_testa[1] >= ALTEZZA):
            game_over = True
        
        serpente.insert(0, nuova_testa)
        
        if nuova_testa == mela:
            mela = posizione_casuale()
        else:
            serpente.pop()
        
        # Disegna lo schermo
        schermo.fill(NERO)
        pygame.draw.rect(schermo, ROSSO, (*mela, DIMENSIONE_BLOCCO, DIMENSIONE_BLOCCO))
        for segmento in serpente:
            pygame.draw.rect(schermo, VERDE, (*segmento, DIMENSIONE_BLOCCO, DIMENSIONE_BLOCCO))
        
        pygame.display.flip()
        clock.tick(7)

# Avvio del gioco
gioco()
