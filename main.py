import pygame
pygame.init()
screen = pygame.display.set_mode((700, 1400))

black = (0, 0, 0)
line_width = 3
running = True
while running:
	screen.fill((255, 255, 255))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	#corner
	pygame.draw.line(screen, black, (350, 300), (350, 964), line_width)
	pygame.draw.line(screen, black, (350, 1006), (350, 1100), line_width)
	
	#roof
	pygame.draw.line(screen, black, (350, 300), (850, 50), line_width)
	pygame.draw.line(screen, black, (350, 300), (-250, 50), line_width)
	
	#floor
	pygame.draw.line(screen, black, (350, 1100), (356, 1101), line_width)
	pygame.draw.line(screen, black, (376, 1108), (850, 1350), line_width)
	
	pygame.draw.line(screen, black, (350, 1100), (260, 1138), line_width)
	pygame.draw.line(screen, black, (240, 1145), (-250, 1350), line_width)
	
	#window
	pygame.draw.polygon(screen, black, [(450, 500), (450, 800), (718, 934), (718, 366)], line_width)
	
	#lines in window
	pygame.draw.line(screen, black, (548, 450), (548, 849), line_width)
	pygame.draw.line(screen, black, (450, 650), (718, 650), line_width)
	
	#table top
	pygame.draw.polygon(screen, black, [(376, 981),  (250, 900), (-150, 1050), (-24, 1131)], line_width)
	pygame.draw.line(screen, black, (376, 996), (-24, 1146), line_width)
	
	#table legs
	pygame.draw.line(screen, black, (376, 981), (376, 1281), line_width)
	pygame.draw.line(screen, black, (366, 1000), (366, 1288), line_width)
	pygame.draw.line(screen, black, (356, 1004), (356, 1281), line_width)
	
	pygame.draw.line(screen, black, (376, 1281), (366, 1288), line_width)
	pygame.draw.line(screen, black, (366, 1288), (356, 1281), line_width)
	
	pygame.draw.line(screen, black, (250, 1045), (250, 1200), line_width)
	pygame.draw.line(screen, black, (260, 1040), (260, 1193), line_width)
	pygame.draw.line(screen, black, (240, 1049), (240, 1193), line_width)
	
	pygame.draw.line(screen, black, (250, 1200), (260, 1193), line_width)
	pygame.draw.line(screen, black, (250, 1200), (240, 1193), line_width)
	
	pygame.display.flip()
	
pygame.quit()
