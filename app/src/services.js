'use strict';

/* Services */

angular.module('app.services', [])

	.factory('datasets', ['$http', function($http){
    var ns = {}     // namespace
    
    ns.datasets = [
      {
      	id: 'corpus-candidats-linkfluence',
        title: 'Corpus “Candidats présidentielle 2017” sur Linkfluence Radarly',
        licence: 'confidentiel',
        authors: 'Linkfluence : Guilhem Fouetillou',
        contact: 'benoit.tabutiaux@linkfluence.com'
      },{
      	id: 'extractions-corpus-linkfluence',
        title: 'Extractions du corpus Radarly Linkfluence',
        licence: 'confidentiel',
        authors: 'Linkfluence : Guilhem Fouetillou',
        contact: 'benoit.tabutiaux@linkfluence.com'
      },{
      	id: 'politoscope',
        title: 'Données Twitter de la campagne présidentielle 2017 ISC-PIF Politoscope.org',
        licence: 'confidentiel',
        authors: 'Institut des Systèmes Complexes de Paris Ile-de-France (ISC-PIF) sous la responsabilité de David Chavalarias. David Chavalarias (CNRS/EHESS, ISC-PIF/CAMS), responsable scientifique, data-mining & visualisations. Maziyar Panahi (CNRS, ISC-PIF) : responsable de l’infrastructure Big Data, chef de projet Multivac. Noé Gaumont (CNRS/EHESS, CAMS/ISC-PIF) : analyse des réseaux. Alexandre Delanoë (CNRS, ISC-PIF) : fouille de texte, chef de projet Gargantext.',
        contact: 'david.chavalarias@iscpif.fr'
      },{
      	id: 'sitotheque-bib',
        title: 'Sitothèque élections 2017 de la Bibliothèque de Sciences Po',
        licence: 'ODBL',
        authors: 'CEVIPOF : Diégo Antolinos-Basso, Odile Gaultier-Voituriez et Thierry Vedel (chercheur référent). Médialab : Audrey Baneyx, Mathieu Jacomy, Benjamin Ooghe-Tabanou. Bibliothèque : Laurent Bajon, Anita Beldiman-Moore, Anne L’Hôte, Zohra Mechri, Meryam Maizi, Cynthia Pedroja, Myriam Tazi',
        contact: 'cynthia.pedroja@sciencespo.fr',
        link: 'http://corpusweb.sciencespo.fr/#/en/election-presidentielle-2017/view/grid'
      },{
      	id: 'ideo-2017',
        title: 'Tweets des candidats à la présidentielle, par IDEO 2017',
        licence: 'CC-BY-SA',
        authors: 'Laboratoires producteurs : AGORA - Laboratoire AGORA (Cergy-Pontoise, France), ETIS - Equipes Traitement de l\'Information et Systèmes (Cergy-Pontoise, France). Soutien institutionnel : Fondation UCP (Cergy-Pontoise, France), CORLI - Consortium CORLI - Corpus, Langues, Interactions ',
        contact: 'julien.longhi@u-cergy.fr',
        link: 'https://www.ortolang.fr/market/corpora/corpus-presidentielle2017'
      },{
      	id: 'crawl-decodex',
        title: 'Catégories du Décodex (Le Monde et Sciences Po médialab)',
        licence: 'ODBL',
        authors: 'Décodex en lui-même : Les Décodeurs (Le Monde). Catégories additionnelles : Mathieu Jacomy (Sciences Po médialab)',
        contact: 'mathieu.jacomy@sciencespo.fr',
        link: 'http://www.lemonde.fr/verification/'
      },{
      	id: 'google-trends',
        title: 'Extractions Google Trends de la campagne électorale',
        licence: 'ODBL',
        authors: 'Données Trends : Google. Extraction et sélection : Sciences Po médialab',
        contact: 'medialab@sciencespo.fr'
      }
    ]

    ns.index = {}
    ns.datasets.forEach(function(d, i){
    	ns.index[d.id] = d
    	d.description = 'Loading description'
    	$http.get('data/datasets-descriptions/'+d.id+'.html')
    		.then(function(r){
    			d.description = r.data
    		}, function(){
    			console.error('Error loading description', d.id)
    		})
    })

    ns.get = function (id) {
      return ns.index[id.toLocaleLowerCase()]
    }

    ns.getAll = function(options) {
    	options = options || {}

    	if (options.sort && options.sort=='licence') {
    		var sortLicence = function(licence){
    			if (licence == 'confidentiel') {
    				return 'zzz'
    			} else return licence
    		}
    		return ns.datasets.sort(function(a, b){
    			if (a == b) return 0
    			if (sortLicence(a) < sortLicence(b)) return -1
    			return 1
    		})
    	} else return ns.datasets
    }

    return ns
  }])
