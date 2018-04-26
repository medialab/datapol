# Extractions Google Trends

Origine : Google Trends

Critère de sélection : sélection de mots-clés manuelle

Temporalité de la collecte : Données du 1er janvier au 30 juin 2017

## Licence ODbL

[ODC Open Database License](http://vvlibri.org/en/licence/odbl-10/legalcode/official)

# Méthodologie

## Mots-clés

Google Trends est une source de données particulière dans la mesure où elle diffère énormément des sources de "production" de contenu comme Facebook ou Twitter. En effet, les données de Google Trends sont le reflet de l’usage d’un moteur de recherche.

Cela signifie que cibler des mots-clés sémantiques dans Google Trends peut très bien se révéler vide de sens dans la mesure où les gens ne cherchent pas des thèmes ou des concepts sur Google. Au contraire, les gens essaient d’y formuler une requête susceptible de délivrer des résultats répondant à leur interrogations et/ou besoins pratiques. Oublier ce fait mènera ainsi forcément à des contre-sens.

Afin de trouver des mots-clés pertinents, i.e. reflétant de réels usages d’internautes liés à l’élection présidentielle de 2017, nous avons procédé de la sorte (en testant évidemment les mots-clés dans Google Trends pour ne garder que ce qui marche/a du volume):

* Vagues d’entretiens très courts avec de multiples personnes. L’objectif de ces entretiens était de demander aux gens comment ils avaient pu utiliser Google durant les élections pour se renseigner ou répondre à des questions pratiques etc.

* Recherches d’articles de presse faisant le récapitulatif des thèmes, événements, fake news etc. de l’élection afin de s’en inspirer pour à notre tour tenter de formuler des requête Google susceptibles de répondre à des questions les concernant.

On notera plusieurs choses:

* En général, nous avons listé des mots-clés plutôt courts et abstrait car ceux-ci, grâce à la recommendation de Google Trends, peuvent s’étendre facilement à toutes leurs variations de formulation.

* L’accentuation des mots-clés EST importante.

* Le nombre des mots-clés (singulier, pluriel) EST important. Le mot-clé "retraite", par exemple renvoie des informations pratiques et administrative. Alors que “retraites” est un sujet politisé renvoyant plutôt vers des actualités.

## Dé-normalisation des valeurs

Google Trends ne fournit que des valeurs normalisée entre 0 et 100. Cela rend donc difficile la comparaison en volume de nombreuses requêtes. Or, l’outil nous laisse cependant la possibilité de comparer quelques mot-clés (5 maximum).

Il est donc possible de dé-normaliser les valeurs en employant la méthodologie suivante:

1. Il faut trouver une échelle de mot-clés plutôt stables dans le temps. Nous avons choisi l’échelle suivante: "chat", “lapin”, “renard”, “vipère”, “cyclohexane”.

2. Il faut récupérer les valeurs de nos mot-clés comparées à chacun des mots de l’échelle choisie. Ensuite, il convient de ne garder que la série temporelle comparée ayant la plus grande précision.

3. Une fois ceci fait, il devient possible de convertir les valeurs de la série choisie dans une unique unité (l’unité de "chat", ici) afin de dé-normaliser les valeurs et de rétablir la possibilité de dresser des comparaisons absolues.

## Volatilité des résultats

Il est bon de noter que l’API de Google Trends semble renvoyer des résultats très volatiles. C’est à dire qu’il n’y a aucune garantie, à paramètres égaux, qu’une requête renvoie les exactes mêmes informations. Egalement, certains des derniers jours peuvent manquer en fonction du mot de l’échelle choisi pour la comparaison avec le mot-clé courant.

# Données

* Keywords.csv - Liste des keywords reliés à l’élection.

* related_queries_network.gexf - Graphe des recherches liées (graphe dirigé)

* related_topics_network.gexf - Graphe des sujets liés (graphe non dirigé, tout les sujets associés à une même requête faites sur Google Trends sont liés entre eux)

* bipartite_network_nodetype.gexf - Graphe bipartite requêtes-sujets (graphe non dirigé, tout les sujets et requêtes associés à une même requête faites sur Google Trends sont liés entre eux)

* timeseries.csv - Series temporelles de tous les mots-clés normalisées en unité de chat.

# Code

Les scripts python servant à produire les graphes et à retraiter les données issues de l’API Google Trends sont disponibles sur le [repository Github](https://github.com/medialab/datapol/tree/master/scripts/google_trends).

