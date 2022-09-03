stopwords = ['a', 'ante', 'após', 'até', 'com', 'contra', 'de', 'desde','em', 'entre', 
            'sob', 'sobre', 'trás', 'a', 'algo', 'algum', 'alguma', 'algumas', 'alguns',
            'aquelas', 'aquele', 'aqueles', 'aquilo', 'as', 'cada', 'certa', 'certas',
            'certo', 'certos', 'cuja', 'cujas', 'cujo', 'cujos', 'ela', 'elas', 'ele',
            'eles', 'essa', 'essas', 'esse', 'esses', 'esta', 'estas', 'este', 'estes',
            'eu', 'isso', 'isto', 'lhe', 'lhes', 'me', 'meu', 'meus', 'mim', 'minha',
            'minhas', 'muita', 'muitas', 'muito', 'muitos', 'nada', 'nenhum', 'nenhuma',
            'nenhumas', 'nenhuns', 'ninguem', 'nossa', 'nossas', 'nosso', 'nossos', 'nos',
            'o', 'os', 'outra', 'outras', 'outrem', 'outro', 'outros', 'pouca', 'poucas',
            'pouco', 'poucos', 'quais', 'quaisquer', 'qual', 'qualquer', 'quanta', 'quantas',
            'quanto', 'quantos', 'se', 'seu', 'seus', 'si', 'sua', 'suas', 'si', 'tanta', 'tantas',
            'tanto', 'tantos', 'te', 'teu', 'teus', 'ti', 'toda', 'todas', 'todo', 'todos', 'tu',
            'tua', 'tuas', 'tudo', 'vos', 'vossa', 'vossas', 'vosso', 'vossos', 'varia', 'várias',
            'varios', 'vos', 'voto', 'srs', 'mas', 'minha', 'tao', 'portanto', 'sou', 'do',
            'no', 'na', 'que', 'se', 'os', 'ao', 'aos', 'um', 'uma', 'para', 'perante', 
            'deputado', 'sr', 'presidente', 'pelo', 'pela', 'meu', 'alguem', 'aquela',
            'dos', 'eu', 'como', 'das', 'nome', 'as', 'sua', 'esse', 'por', 'sem',
            'este', 'seu', 'nas', 'deu', 'esta', 'tem', 'tambem', 'sra', 'pelas',
            'nos', 'mais', 'nesta', 'foi', 'me', 'meus', 'ha', 'aqui', 'ano','da',
            'vou', 'ter', 'tenho', 'sras', 'sao', 'neste', 'nós', 'nem', 'ser',
            'esta', 'nossa', 'isso', 'já', 'muito', 'mim', 'fazer', 'aquele',
            'as', 'você', 'digo', 'vai', 'estamos', 'pelos', 'porque', 'minas',
            'gerais', 'paulo', 'vamos', 'ele', 'ela', 'quem', 'rio', 'janeiro',
            'sul', 'paraná', 'quando', 'bem', 'ano', 'anos', 'deste', 'quero',
            'desta', 'dia', 'estao', 'todo', 'grande', 'toda', 'essa', 'seus',
            'pernambuco', 'dias', 'tudo', 'maioria', 'santa', 'catarina', 'bahia',
            'favor', 'hoje', 'querem', 'minhas', 'regiao', 'votando',
            'cada', 'para', 'so', 'exa', 'mato', 'grosso', 'goias', 'querida',
            'querido', 'muita', 'todas', 'sempre', 'nosso', 'todos', 'deputados',
            'casa', 'dizer', 'melhor', 'votar', 'fim', 'mineiro', 'primeiro',
            'temos', 'deste', 'sera', 'envolve', 'esses', 'estes', 'estas',
            'destas', 'aquela', 'naquela', 'menos', 'queremos', 'precisa', 'forma',
            'tenha', 'ainda', 'maior', 'possam', 'sendo', 'tenham', 'milhoes', 'apenas',
            'relaçao', 'ranking', 'índice', 'estar', 'unico', 'media', 'quadro',
            'escolha', 'apesar', 'preciso', 'principalmente','proximo', 'importante',
            'deve', 'cado', 'alto', 'ciente', 'meio', 'sejam', 'assim', 'piores',
            'medio', 'vezes', 'maiores', 'enquanto', 'gasta', 'aumentar', 'mesma', 'segundo',
            'acima', 'foram', 'atraves', 'alem', 'disso', 'pode', 'houve', 'caso'
            'serão', 'terá', 'terão', 'bilhões', 'milhares', 'política', 'dele','nunca'
            'eleicoes2022','eleicoes 2022','candidato','RT','devem','pesquisa','detalhes',
            'acontece','apreensao','casa','faltam','todos','materiais','voce','ju','via','dias',
            'houve','por','de','dar','pois','em','um','da','ser','aqui','vou','dos','ter','nao',
            'ao','sou','seu','a','n','se','esse','uma','mais','ele','fazendo','você','pode','essa',
            'e','mas','segue','pra','isso','vez','para','muito','pelo','pela','são', 'na','vamos',
            'https','t','co','c','New','eu','seis','retweets','ano','pessoa','likes','vai','que',
            'ou','anos','7dias','tirou','sobre','tem','q','0','o','e','os','assim','so','mesmo',
            'ta','pro','votar','nesta','as','pessoas','vc','caso','imoveis','news','b','proposta',
            'desgastar','exclusivo','nossa','politicamente','boker','visitando','ontem','esteve',
            'amor','cresce','eleicoes','dia','eleicoe','ampliarmos','vote','contra','congresso',
            'fala','evento','foi','bancada','acorda','uol','presidente','fazer','felipe','comprovar',
            'demorou','diferente','juntou','rio','adquiri','bahia','coragem','levar','equipe','meses',
            'rdctvdigital','peço','refez','francisco','ate','entao','tentou','esta','como','resultado',
            'abandonada','transposição','estava','durante','concluir','ai','historia','depois','ai','sofre'
           ]