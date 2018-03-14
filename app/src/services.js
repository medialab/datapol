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
