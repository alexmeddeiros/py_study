def votacao():
	candidato_a = 0
	candidato_b = 0
	candidato_c = 0
	voto_nulo = 0
	voto_branco = 0
	
	for eleitor in range(16):
		voto = input('Digite seu voto: ')
		
		if voto == '1':
			candidato_a += 1
		elif voto == '2':
			candidato_b += 1
		elif voto == '3':
			candidato_c += 1
		elif voto == '4':
			voto_nulo += 1
		elif voto == '5':
			voto_branco += 1
		else:
			print('valor inválido')

	print('O candidato A teve %s votos' % candidato_a)
	print('O candidato B teve %s votos' % candidato_b)
	print('O candidato C teve %s votos' % candidato_c)
	print('Votos nulos %s' % voto_nulo)
	print('Votos Em branco %s' % voto_branco)
	print('A porcentagem de votos nulos foi de %s' %((voto_nulo * 100) / 15))
	print('A porcentagem de votos brancos foi de %s' %((voto_nulo * 100) / 15))


votacao()
