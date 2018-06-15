## Les circuits des fausses infos

<span class="contribs">Auteurs : Quentin Agren, Liliana Bounegru, Robert Bracciale, Dominique Cardon, David Chavalarias, Cheikh-Brahim El-Vaigh, Anne-Sophie Faivre Le Cadre, Maxime Ferrer, Guillaume Gravier, Jonathan Gray, Mathieu Jacomy, Antonio Martella, Mazyhar Panahi, Rosella Rega, Adrien Sénécat, Denis Teyssou, Tommaso Venturini.</span>

La circulation des fausses nouvelles (ou fakenews) lors de la campagne électorale française de 2017 est-elle virale ou structurelle ? Qui est responsable de la fabrication et de la circulation de ces fausses nouvelles ?

Dans les études récentes sur les « fake news », on rencontre deux interprétations sur leurs origines :

L’origine **VIRALE**, les fausses nouvelles arrivent par les amis ou une accumulation de reprise par des comptes à faible visibilité. Elles émergent des plateformes et leurs bulles de filtre.

L’origine **STRUCTURELLE**, les fausses nouvelles arrivent via des influenceurs, des comptes à forte visibilité. Les fausses nouvelles sont orchestrées « par le haut »,des comptes influents et des blanchisseurs de fausses infos.

Nous utilisons les données du <span info-dataset="crawl-decodex">Décodex</span> (qui codeclasse des sources d’informations par fiabilité) afin de détecter les comptes Twitter qui partagent les fausses nouvelles dans un corpus de tweets collectés pendant la campagne.

![](md/fakenews/image3.jpg)
_La place des utilisateurs dans la circulation de fausse nouvelles._

Les sources (liens URL) citées dans les tweets sont comparées à la base du <span info-dataset="crawl-decodex">Décodex</span> qui classe les sources d’information par fiabilité. En rouge, les cas de fausses nouvelles du répertoire <span info-dataset="crawl-decodex">Décodex</span> qui ont circulé sur Twitter. En gris, les comptes ayant retweeté plusieurs d’entre elles. Onconstate que certains comptes retweetent de nombreuses fausses nouvelles.

La classification du <span info-dataset="crawl-decodex">Décodex</span> comporte dans son échelle les sites « Peu fiable » ou « Très peu fiable », mais aussi « Parodique ». Nous nous intéressons à ces différentes qualités d’information en cherchant à identifier si leur circulation est équivalente sur les diverses plateformes. En affinant les catégories, c’est tout un spectre d’information qui est pris en compte allant du « bullshit » (l’aspect parodique ne fait aucun doute) aux fausses nouvelles qui jouent sur la limite entre information et fausse nouvelle.

![](md/fakenews/image2.jpg)
_Des fausses nouvelles colorées par fiabilité et positionnées en fonction des comptes qui les partagent._

Sur ce réseau sont représentées les fausses nouvelles et les sources (sites) qui les relayent (uniquement d’après le répertoire du <span info-dataset="crawl-decodex">Décodex</span>) : en rouge et bleu, sur la gauche, les informations catégorisées comme du « clickbait » (piège à clics), de la « satire » ou de la « parodie », en vert et indigo, sur la droite,  on observe les « fausses informations » et les contenus conspirationnistes.

Les univers de la « satire » et la « fausse information » communiquent peu et ne citent pas les mêmes sources, mais évoluent-ils sur les mêmes plateformes ?


L’intensité du grissuperposé au réseau signale les contenus ayant plus circulé sur Twitter. En faisant la même opération avec les fausses infos qui ont circulé sur Facebook, on constate que les contenus « satiriques » et « clickbait » sont plus représentés. Il y a une différence entre les plateformes, mais cela n’explique pas la différence entre les deux types de sources et de contenus.

![](md/fakenews/image1.jpg)

Dans une seconde exploration nous testons la fiabilité, à l’aide du <span info-dataset="crawl-decodex">Décodex</span>, des liens partagés par les communautés assemblées autour des candidats pendant la campagne sur Twitter. Le <span info-dataset="politoscope">Politoscope</span> qui est utilisé pour la définition des communautés sélectionne les profils qui font des retweets secs (sans ajouter de commentaires)  de personnalités politiques. Pour chacune deces communautés on représente le pourcentage de liens notés comme orientés, parodiques, fiables ou douteux.

![](md/fakenews/image4.jpg)
_Analyse de la fiabilité des liens partagés dans les communautés du <span info-dataset="politoscope">Politoscope</span>._

Les communautés partagent sur Twitter des URL assez hétérogènes et souvent de bonne qualité (en moyenne 97 % des URL sont de catégorie « fiable » ou « non répertorié »). Ont tout de même noter des variation sur les contenus douteux (en rose) et parodiques (en bleu). Par exemple,la communauté rassemblée autour de Marie Le Pen partage plus de 2,5 fois plus d’URL « douteuses » ou « orientées » que la moyenne.

Si l’on représente en réseau les comptes en fonction de retweets secs des candidats deux types de comptes peuvent être pris en compte : des comptes « engagés » (définis comme ceux dont les retweets ne vont qu’à un seul candidat) ou des comptes appartenants à la « la mer » (qui retweetent plusieurs candidats). Ces derniers forment l’étendue entre les îlots des candidats. Ils aident à polariser l’espace politique sans le définir entièrement.

![](md/fakenews/image6.jpg)
_Réseau des comptes des candidats et de ceux qui les retweetent pendant la campagne._

Les profils Twitter « engagés » auprès d’un candidat font-ils circuler des informations moins fiables que les autres, ceux qui retweetent plusieurs candidats ?

![](md/fakenews/image5.jpg)
_Pourcentage d’url partagés par catégories du <span info-dataset="crawl-decodex">Décodex</span>._

Si l’on compare les URL partagées par les profils « engagés » avec celles de la « mer » (c’est-à-dire avec le reste des comptesdu politoscope), on constate que les contenus de la « mer » sont plus parodiques, mais aussi légèrement plus fiables.
