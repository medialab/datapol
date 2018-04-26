## Comparaison et circulation des idéologies : comment mesurer l’utilisation et l’efficacité des idéologies dans la campagne présidentielle ?

<span class="contribs">Julien Longhi, Claudia Marinica, Abdulhafiz Alkhouli, Clément Plancq, Axel Meunier, Agata Brilli, Zakarya Després, Friederike Richter, Emmanuelle Coniquet, Paige Camerino – Adil Ouafssou, Audrey Baneyx, Mamy Rakotondravohitra, Amalia Nikolaidi, Mathieu Ouagazzal, Boris Borzic, Mathias Quoy, Savinien de Rivet, Abdelouafi El Otmani</span>
### L’idéologie dans le discours

Afin d’identifier dans ce corpus les messages idéologiques, nous avons testé deux approches. La première s’intéresse aux idéologies dans le discours, la seconde à l’univers politique des candidats.
Avant d’entrer plus en détail il nous faut définir comment se caractérise une idéologie. Le choix est fait de prendre une définition venue de la linguistique et de l’analyse du discours qui nous dit que l’idéologie est :

|                                                 |                                                  |
| ----------------------------------------------- | ------------------------------------------------ |
| **Atemporelle**                                 | **Intemporelle**                                 |
| Est vraie hors de son contexte spatio-temporel. | Est vraie de tout temps.                         |
| &nbsp;                                          | &nbsp;                                           |
| **Polylectale**                                 | **Autotélique**                                  |
| S’énonce diversement, mais simplement.          | Se réfère à elle-même et impose sa propre norme. |
|                                                 |                                                  |


Pour mener cette exploration, nous disposons du corpus **#Idéo2017** qui représentent les discours des candidats et des sympathisants. Le corpus #Idéo2017 contient 44 979 tweets des 11 candidats du 1er nov. 2016 jusqu’au soir de l’élection avec un focus sur la période 18/03/2017 au 18/04/2017.

Nous testons 2 méthodes pour détecter dans les messages partagés sur Twitter les messages idéologiques.

![exemple de tweets idéologiques](md/ideologies/exemple-tweet-ideo.jpg)
*exemple de tweets idéologiques*

Une première méthode s’appuie sur des règles(pronoms, connecteurs, verbes, etc.) qui une fois traduite en code informatique permette une détection automatisée de 2612 tweets idéologiques.

La seconde méthode par apprentissage se base sur une annotation manuelle de 600 tweets par 9 annotateurs qui permet une classification automatique (Naive Bayes) de l’ensemble du corpus et permet la détection de 2737 tweets idéologiques.

![](md/ideologies/image10.jpg)
_comparaison entre les deux méthodes de détection des messages idéologiques_

Les résultats de ces deux méthodes ne coïncident pas pour environ ⅓ des résultats il nous faudrait plus de temps pour affiner les résultats, mais nous disposons d’un corpus exploitable.

En comparant la quantité de tweets classés comme idéologique au nombre de tweets total, nous pouvons suivre l’évolution de la proportion de tweets idéologiques et les rapprocher d’événement marquant tout au long de la campagne.

![](md/ideologies/image2.jpg)
_évolution de la proportion de tweets idéologiques entre le 18 mars et le 18 avril 2017_

Le 24 mars 2017, on peut noter une forte augmentation des messages idéologique pour Jean Luc Mélenchon qui coïncide avec la parution d’un sondage ou il est annoncé comme étant le quatrième homme. Sur twitter, la communauté se mobilise pour valoriser le candidat en utilisant des messages que nous avons détectés idéologiques.

![](md/ideologies/exemple-tweet-ideo-24-03-17.jpg)
_exemple de tweets classé comme idéologique le 24 mars_

Le 20 mars 2017, Jacques Cheminade est invité de l’émission Bourdin Direct. Cette exposition médiatique fait bondir la part des messages idéologique le concernant.

![](md/ideologies/image4.jpg)
_Le 20 mars 2017, Jacques Cheminade est invité de l’émission Bourdin Direct._

![](md/ideologies/image3.jpg)
_exemple de tweets classé comme idéologique le 20 mars_

### Les univers politiques des candidats

À l’aide du logiciel d’analyse de langage « iramuteq », on extrait des messages postés par les candidats des classes de mots. Ces classes sont ensuite titrées manuellement pour obtenir des thématiques.

![](md/ideologies/image8.jpg)
_Exemple de transformation d’une classe reconnue par l’analyse du langage en thématique._

Ces thématiques sont ensuite qualifiées sur une échelle allant de la grande « charge émotionnelle » (chaud) à la « neutralité » (froid).

![](md/ideologies/image5.jpg)
_Représentation de la place occupée par les thématiques dans le discours des candidats sur lequel est projeté le type de discours utilisé._

On peut ensuite comparer comment un mot est utilisé pour parler de différents thèmes.

Ici l’utilisation du mot « chômage » par parler de « défense de la France », « politique intérieure » ou « menaces intérieures » en fonction des candidats avec des charges émotionnelles variées.

![](md/ideologies/image11.jpg)

ou encore l’utilisation du mot « femme »

![](md/ideologies/image12.jpg)

### conclusion

Nous avons pu à l’aide de ces deux approches montrer comment les discours se teintent d’idéologies en fonction des moments de la campagne, mais aussi de l’univers politique des candidats.

Le travail réalisé contribue à la fois à légitimer le recours aux tweets politiques pour mener des analyses politiques (pas seulement pour leur facilité d’accès, mais aussi leur qualité comme genre du discours politique), et à proposer une méthodologie quali-quantitative basées sur ces “data” politiques.

Surtout, à partir d’un questionnement linguistique et textuel, nous avons cherché à caractériser les idéologies et les univers politiques des différents candidats, en nous focalisant sur la matérialité des discours. Cette recherche propose donc une analyse pluridisciplinaire de la communication de ces candidats qui met en évidence, par le prisme linguistique et politique, leurs spécificités idéologiques.
